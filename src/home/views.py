import typing as t

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import Page

INDEX_TEMPLATE = "index.html"


def _render_index_template(
    request: HttpRequest, context: dict
) -> HttpResponse:
    return render(request, INDEX_TEMPLATE, context=context)


def _make_context_for_page(page: Page) -> dict[str, t.Any]:
    return {
        "page": page,
        "start_screen": page.start_screen,
        "promo": page.promo,
        "services": page.services,
        "about_me": page.about_me,
        "portfolio": page.portfolio,
        "contacts": page.contacts,
        "footer": page.footer,
    }


def _get_first_page(filter_kwargs: dict) -> Page | None:
    selected = (
        "icon",
        "shortcut_icon",
        "logo",
        "start_screen",
        "start_screen__logo",
        "start_screen__bg_pattern",
        "promo",
        "services",
        "portfolio",
        "about_me",
        "about_me__avatar",
        "about_me__bg_image",
        "contacts",
        "footer",
        "footer__logo",
        "footer__bg_pattern",
    )
    excluded_fields = ("id", "note", "created_at", "updated_at")
    defered = []
    for head in selected:
        defered.extend(f"{head}__{tail}" for tail in excluded_fields)

    return Page.objects.filter(**filter_kwargs).select_related(
        *selected
    ).prefetch_related(
        "services__items__image",
        "services__items__items",
        "portfolio__items",
        "contacts__details_list",
        "contacts__link_list",
    ).defer(
        *excluded_fields,
        *defered,
        "is_active",
    ).first()


def index(request: HttpRequest) -> HttpResponse:
    page = _get_first_page({"is_active": True})
    if not page:
        return HttpResponseNotFound()

    return _render_index_template(request, _make_context_for_page(page))


@user_passes_test(lambda user: user.is_superuser)
def preview(request: HttpRequest, pk: int) -> HttpResponse:
    page = _get_first_page({"pk": pk})
    if not page:
        return HttpResponseNotFound()

    return _render_index_template(request, _make_context_for_page(page))
