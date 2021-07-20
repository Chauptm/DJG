from django.db.models import fields
import django_filters
from .models import Product
from django.contrib.auth.models import User
# class IsOwnerFilterBackend(filters.BaseFilterBackend):
#     def filter_queryset(self, request, queryset, view):
#         return queryset.filter(owner=request.user)

class ProductFilter(django_filters.FilterSet):
    c_name_icontains = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    c_id_max= django_filters.NumberFilter(field_name='id', lookup_expr='lte')
    c_id_min= django_filters.NumberFilter(field_name='id', lookup_expr='gte')
    class Meta:
        model = Product
        fields = ['c_name_icontains','name', 'c_id_max', 'c_id_min']

class UserFilter(django_filters.FilterSet):
    c_id_max= django_filters.NumberFilter(field_name='id', lookup_expr='lte')
    c_id_min= django_filters.NumberFilter(field_name='id', lookup_expr='gte')
    class Meta:
        model= User
        fields= ['c_id_max', 'c_id_min']