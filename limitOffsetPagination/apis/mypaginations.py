from rest_framework.pagination import LimitOffsetPagination


class MyPageNumberPagination(LimitOffsetPagination):
    default_limit = 4
    limit_query_param = 'mylimit' #change the limit to mylimit
    offset_query_param = 'myoffset' #change the offset to myoffset
    max_limit = 8