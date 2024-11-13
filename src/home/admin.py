from django.contrib import admin

from . import models


class BaseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    list_display_links = ("id", "name")
    search_fields = ("name",)


class AssetAdmin(BaseAdmin):
    list_display = ("id", "name", "tag", "created_at","updated_at")
    list_filter = ("tag",)


class StartScreenAdmin(BaseAdmin):
    pass


class PromoAdmin(BaseAdmin):
    pass


class ServiceItemAdmin(BaseAdmin):
    pass


class ServiceBlockAdmin(BaseAdmin):
    filter_horizontal = ("items",)


class ServicesAdmin(BaseAdmin):
    filter_horizontal = ("items",)


class PortfolioAdmin(BaseAdmin):
    filter_horizontal = ("items",)


class AboutMeAdmin(BaseAdmin):
    pass


class ContactLinkAdmin(BaseAdmin):
    pass


class ContactDetailAdmin(BaseAdmin):
    pass


class ContactsAdmin(BaseAdmin):
    filter_horizontal = ("details_list", "link_list")


class FooterAdmin(BaseAdmin):
    pass


class PageAdmin(BaseAdmin):
    list_display = ("id", "name", "is_active", "created_at","updated_at")


admin.site.register(models.Asset, AssetAdmin)
admin.site.register(models.StartScreen, StartScreenAdmin)
admin.site.register(models.Promo, PromoAdmin)
admin.site.register(models.ServiceItem, ServiceItemAdmin)
admin.site.register(models.ServiceBlock, ServiceBlockAdmin)
admin.site.register(models.Services, ServicesAdmin)
admin.site.register(models.Portfolio, PortfolioAdmin)
admin.site.register(models.AboutMe, AboutMeAdmin)
admin.site.register(models.ContactDetail, ContactDetailAdmin)
admin.site.register(models.ContactLink, ContactLinkAdmin)
admin.site.register(models.Contacts, ContactsAdmin)
admin.site.register(models.Footer, FooterAdmin)
admin.site.register(models.Page, PageAdmin)
