from rest_framework import pagination
from rest_framework.response import Response

class PaginationSet(pagination.LimitOffsetPagination):
    page_size=2