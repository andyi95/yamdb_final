from django_filters import rest_framework as filters

from api.models import Title


class TitleFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    category = filters.CharFilter(
        field_name='category__slug',
        lookup_expr='exact'
    )
    genre = filters.CharFilter(field_name='genre__slug', lookup_expr='iexact')

    class Meta:
        model = Title
        fields = ['name', 'category', 'genre', 'year', ]