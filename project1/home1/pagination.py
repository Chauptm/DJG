from rest_framework import pagination

class PaginationSet(pagination.BasePagination):
    page_size = 1
    def paginate_queryset(self, queryset, request, view):
        return super().paginate_queryset(queryset, request, view=view)
    def get_paginated_response(self, data):
        return super().get_paginated_response(data)