from django.urls import path
from .views import PerkDetail, Perks

urlpatterns = [
    path(
        "perks/",
        Perks.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    )
]
