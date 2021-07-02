from rest_framework import pagination

# class PaginationSet(pagination.LimitOffsetPagination):
#     default_limit=2
#     limit_query_param='limit'
#     offset_query_param='offset'
#     max_limit=3
# class PaginationSet(pagination.PageNumberPagination):
#     page_size=2
#     page_query_param='page'
#     page_size_query_param='record'
#     max_page_size=3
#     last_page_strings='end'
class PaginationSet(pagination.CursorPagination):
        page_size=2
        ordering= 'date'
        cursor_query_param='cursor'
    
class PaginationSetUser(pagination.CursorPagination):
        page_size=2
        ordering= 'date_joined'
        cursor_query_param='cursor'