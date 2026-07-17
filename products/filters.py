import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    sizes = django_filters.CharFilter(method="filter_sizes")
    gender = django_filters.CharFilter(method="filter_gender")

    class Meta:
        model = Product
        fields = ["gender"]

    def filter_sizes(self, queryset, name, value):
        sizes = [size.strip().lower() for size in value.split(",")]
        return queryset.filter(sizes__contains=sizes)

    def filter_gender(self, queryset, name, value):
        return queryset.filter(gender__iexact=value)
