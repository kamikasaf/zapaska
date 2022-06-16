from rest_framework import pagination

class ProductPagination(pagination.PageNumberPagination):
    page_size = 3
    page_query_param='page'
    max_page_size = 30
