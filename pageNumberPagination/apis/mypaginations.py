from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'records'
    page_query_param = 'p'    
    max_page_size = 7
    last_page_strings = 'end'

