from django.contrib import admin

from . import models


class DK:
    created_at = "created_at"
    details_list = "details_list"
    id_ = "id"
    is_active = "is_active"
    items = "items"
    link_list = "link_list"
    name = "name"
    tag = "tag"
    updated_at = "updated_at"


class BaseAdmin(admin.ModelAdmin):
    list_display = (DK.id_, DK.name, DK.created_at, DK.updated_at)
    list_display_links = (DK.id_, DK.name)
    search_fields = (DK.name,)


@admin.register(models.Asset)
class AssetAdmin(BaseAdmin):
    list_display = (DK.id_, DK.name, DK.tag, DK.created_at, DK.updated_at)
    list_filter = (DK.tag,)


@admin.register(models.StartScreen)
class StartScreenAdmin(BaseAdmin):
    pass


@admin.register(models.Promo)
class PromoAdmin(BaseAdmin):
    pass


@admin.register(models.ServiceItem)
class ServiceItemAdmin(BaseAdmin):
    pass


@admin.register(models.ServiceBlock)
class ServiceBlockAdmin(BaseAdmin):
    filter_horizontal = (DK.items,)


@admin.register(models.Services)
class ServicesAdmin(BaseAdmin):
    filter_horizontal = (DK.items,)


@admin.register(models.Portfolio)
class PortfolioAdmin(BaseAdmin):
    filter_horizontal = (DK.items,)


@admin.register(models.AboutMe)
class AboutMeAdmin(BaseAdmin):
    pass


@admin.register(models.ContactLink)
class ContactLinkAdmin(BaseAdmin):
    pass


@admin.register(models.ContactDetail)
class ContactDetailAdmin(BaseAdmin):
    pass


@admin.register(models.Contacts)
class ContactsAdmin(BaseAdmin):
    filter_horizontal = (DK.details_list, DK.link_list)


@admin.register(models.Footer)
class FooterAdmin(BaseAdmin):
    pass


@admin.register(models.Page)
class PageAdmin(BaseAdmin):
    list_display = (
        DK.id_, DK.name, DK.is_active, DK.created_at, DK.updated_at
    )
