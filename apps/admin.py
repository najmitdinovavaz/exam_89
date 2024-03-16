from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from apps.models import Category, Product
from apps.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", 'password', "email")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", 'photo', 'phone_number')}),
        (
            _("Permissions"),
            {
                'fields': (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def custom_image(self, obj: User):
        return mark_safe('<img src="{}"/>'.format(obj.photo.url))

    custom_image.short_description = "Image"


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass

@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    search_fields = 'name' , 'description'
