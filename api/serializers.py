from rest_framework import serializers

from api.models import Category, Comment, Genre, Review, Title, User


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        lookup_field = 'slug'
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        lookup_field = 'slug'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class TitleWriteSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug'
    )

    class Meta:
        fields = '__all__'
        model = Title


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['password']
        model = User


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()


class ReviewSerializer(serializers.ModelSerializer):
    # Увы, но без CurrentUserDefault при создании отзыва через Postman
    # мы получаем author=null, и, хотя тесты проходятся, хочется,
    # чтоб работало нормально
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True,
        slug_field='username'
    )

    def validate(self, attrs):
        if self.context['request'].method == 'POST':
            review_exists = Review.objects.filter(
                author=self.context['request'].user,
                title=self.context['view'].kwargs.get('title_id')
            ).exists()
            if review_exists:
                raise serializers.ValidationError(
                    'Пользователь уже оставлял отзыв на это произведение'
                )
        return attrs

    class Meta:
        read_only_fields = ['id', 'pub_date', ]
        exclude = ['title']
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='username'
    )

    class Meta:
        fields = ['id', 'text', 'author', 'pub_date']
        model = Comment
