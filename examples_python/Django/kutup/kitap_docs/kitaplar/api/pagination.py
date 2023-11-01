from rest_framework.pagination import PageNumberPagination

class SmallPagination(PageNumberPagination):
    page_size=5


class LargePAgination(PageNumberPagination):
    page_size=20