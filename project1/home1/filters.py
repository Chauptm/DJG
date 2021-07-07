import django_filters
from .models import Product
# class IsOwnerFilterBackend(filters.BaseFilterBackend):
#     def filter_queryset(self, request, queryset, view):
#         return queryset.filter(owner=request.user)

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    # id_owner= django_filters.CharFilter(field_name='owner', source)

    class Meta:
        model = Product
        fields = ['name']