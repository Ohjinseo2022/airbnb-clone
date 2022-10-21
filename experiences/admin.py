from django.contrib import admin
from .models import Experiences, Perk

# Register your models here.


@admin.register(Experiences)
class ExperiencesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "start",
        "end",
        "created_at",
    )

    list_filter = ("category",)


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "details",
        "explanation",
    )
