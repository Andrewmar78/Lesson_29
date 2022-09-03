from django.contrib import admin

from ads.models_old import Ad, Category, User, Location


admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(Location)

# @admin.register(Ad)
# class AdAdmin(admin.ModelAdmin):
#     list_display = ("name", "author", "price", "is_published")
#     search_fields = ("name", "description")
#     list_filter = ("is_published",)
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ("username", "first_name", "last_name",)
#     search_fields = ("username",)
#     list_filter = ("role",)
