from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.managers import CustomUserManager, Roles


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model with required email field, bio field, role
    """
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        null=True
    )
    role = models.CharField(
        max_length=16,
        choices=Roles.choices,
        default='user'
    )
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField(_('description'), max_length=255, null=True)
    first_name = models.CharField(_('first name'), max_length=30, null=True)
    last_name = models.CharField(_('last name'), max_length=30, null=True)
    password = models.CharField(
        _('password'),
        max_length=128,
        null=True,
        blank=True,
        default=''
    )
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_superuser(self):
        return self.role == Roles.ADMIN

    @property
    def is_staff(self):
        return self.role == Roles.MODERATOR or self.role == Roles.ADMIN

    def __str__(self):
        return f'{self.email}, {self.role}'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['username']


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name[:40]

    class Meta:
        ordering = ['slug']


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name[:40]

    class Meta:
        ordering = ['slug']


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(datetime.now().year)],
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='titles'
    )
    genre = models.ManyToManyField(Genre, related_name='titles')
    description = models.TextField(
        max_length=200,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name[:40]


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='reviews'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['pub_date']
        unique_together = ['author', 'title']

    def __str__(self):
        return f'Review for {self.title} from {self.author}'


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.text[:40]
