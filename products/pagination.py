from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

import math


class ProductPagination(LimitOffsetPagination):
    default_limit = 9
    max_limit = 100

    def get_paginated_response(self, data):
        count = self.count
        limit = self.limit or self.default_limit

        pages = math.ceil(count / limit)

        return Response(
            {
                "count": count,
                "pages": pages,
                "products": data,
            }
        )
