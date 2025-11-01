from django.contrib import admin
from blog.models import Portfolio,Technology
from parler.admin import TranslatableAdmin

# Register your models here.



@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("id","name",)
    search_fields = ("name",)


@admin.register(Portfolio)
class PortfolioAdmin(TranslatableAdmin):
    list_display = ("title",  "created_at")
    search_fields = ("title", "description")
    list_filter = ("technologies",)
    filter_horizontal = ("technologies",)  # ManyToManyField uchun qulay tanlov