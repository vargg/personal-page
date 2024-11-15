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


def index(request: HttpRequest) -> HttpResponse:
    page = Page.objects.filter(is_active=True).first()
    if not page:
        return HttpResponseNotFound()

    return _render_index_template(request, _make_context_for_page(page))


@user_passes_test(lambda user: user.is_superuser)
def preview(request: HttpRequest, pk: int) -> HttpResponse:
    page = Page.objects.filter(pk=pk).first()
    if not page:
        return HttpResponseNotFound()

    return _render_index_template(request, _make_context_for_page(page))
