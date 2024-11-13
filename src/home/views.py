from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from .models import Page


def _make_context_for_page(page: Page) -> dict:
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


def index(request):
    page = Page.objects.filter(is_active=True).first()
    if not page:
        return render(request, "404.html")

    return render(
        request, "index.html", context=_make_context_for_page(page),
    )


@user_passes_test(lambda user: user.is_superuser)
def preview(request, pk):
    page = Page.objects.filter(pk=pk).first()
    if not page:
        return render(request, "404.html")

    return render(
        request, "index.html", context=_make_context_for_page(page)
    )
