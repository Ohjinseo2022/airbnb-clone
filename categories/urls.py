from django.urls import path
from . import views

urlpatterns = [
    # CategoryViewSet 사용시 action을 명시해주면 자동으로 처리해줌
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:pk>",
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
