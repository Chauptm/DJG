from django.db.models import fields
import django_filters
from rest_framework.fields import CharField
from .models import Author, Book, Publisher, Store
from django.contrib.auth.models import User
from django.db.models import Q 
# class IsOwnerFilterBackend(filters.BaseFilterBackend):
#     def filter_queryset(self, request, queryset, view):
#         return queryset.filter(owner=request.user)

# GENDER_CHOICES = tuple(
#     Book.objects.filter(group__id='id').values_list('id', 'price'))

# class BookFilter(django_filters.FilterSet):
#     c_name_icontains = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
#     c_id_max= django_filters.NumberFilter(field_name='id', lookup_expr='lte')
#     c_id_min= django_filters.NumberFilter(field_name='id', lookup_expr='gte')
#     gender= django_filters.MultipleChoiceFilter(choice= GENDER_CHOICES, method= 'filter_id')

#     def filter_id(self,qs, name, value):
#         result = qs.filter(Q(attribute_values__attribute__name='id',
#                          attribute_values__value_option__in=value))

#         return result

#     class Meta:
#         model = Book
#         fields = ['c_name_icontains','name', 'c_id_max', 'c_id_min', 'gender']


class CustomFilterList(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            values = [v for v in value.split(',')]
            return qs.filter(**{'%s__%s' % (self.field_name, self.lookup_expr): values})
        return qs

class PublisherFilter(django_filters.FilterSet):

    c_name_icontains = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    c_id_max= django_filters.NumberFilter(field_name='id', lookup_expr='lte')
    c_id_min= django_filters.NumberFilter(field_name='id', lookup_expr='gte')
    id_list= CustomFilterList(field_name= 'id', lookup_expr="in")
    class Meta:
        model = Publisher
        fields = ['c_name_icontains','name', 'c_id_max', 'c_id_min', 'id_list']

    # def id_filter(self, queryset, name, value):
    #     value_list = value.split(u',') 
    #     return queryset.filter(**{name+"__in": value_list})
