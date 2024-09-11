from rest_framework.pagination import CursorPagination


class MyPageNumberPagination(CursorPagination):
    page_size = 6
    ordering = 'id'
    # cursor_query_param = 'c'

