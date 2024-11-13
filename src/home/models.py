# ruff: noqa: D105, D106
from django.db import models


class BaseModel(models.Model):
    name = models.CharField("название", max_length=64)
    note = models.CharField("примечание", max_length=128, default="", blank=True)

    created_at = models.DateTimeField("создано", auto_now_add=True)
    updated_at = models.DateTimeField("изменено", auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-id",)

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}: "
            f"'{self.name}' ({self.updated_at.date().strftime('%d.%m.%Y')})"
        )


class Asset(BaseModel):
    file = models.FileField("файл")
    tag = models.CharField("тэг", max_length=32, default=" ", blank=True)

    class Meta:
        verbose_name = "ассет"
        verbose_name_plural = "ассеты"

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}: "
            f"'{self.name} - {self.tag}' ({self.updated_at.date()})"
        )


class StartScreen(BaseModel):
    logo = models.ForeignKey(
        Asset, verbose_name="лого", on_delete=models.RESTRICT, related_name="+"
    )
    bg_pattern = models.ForeignKey(
        Asset,
        verbose_name="паттерн",
        on_delete=models.RESTRICT,
        related_name="+",
    )
    primary_text = models.CharField("основной текст", max_length=255)
    secondary_text = models.CharField("дополнительный текст", max_length=255)

    class Meta:
        verbose_name = "стартовый экран"
        verbose_name_plural = "стартовые экраны"


class Promo(BaseModel):
    text = models.CharField("текст", max_length=255)

    class Meta:
        verbose_name = "промо блок"
        verbose_name_plural = "промо блоки"


class ServiceItem(BaseModel):
    icon = models.CharField("fa-иконка", max_length=64)
    description = models.CharField("описание", max_length=255)

    class Meta:
        verbose_name = "услуги: строка"
        verbose_name_plural = "услуги: строки"


class ServiceBlock(BaseModel):
    class PositionChoice(models.TextChoices):
        LEFT = "L", "Left"
        RIGHT = "R", "Right"

    description = models.CharField("описание", max_length=255, default="")
    image = models.ForeignKey(
        Asset,
        verbose_name="изображение",
        on_delete=models.RESTRICT,
        related_name="+",
    )
    image_position = models.CharField(
        "расположение изображения",
        max_length=1,
        choices=PositionChoice,
        default=PositionChoice.LEFT,
    )
    items = models.ManyToManyField(ServiceItem, verbose_name="строки")

    class Meta:
        verbose_name = "услуги: блок"
        verbose_name_plural = "услуги: блоки"


class Services(BaseModel):
    items = models.ManyToManyField(ServiceBlock, verbose_name="блоки")

    class Meta:
        verbose_name = "услуги"
        verbose_name_plural = "услуги"


class Portfolio(BaseModel):
    description = models.CharField("описание", max_length=255, default="")
    items = models.ManyToManyField(Asset, verbose_name="Примеры", related_name="+")

    class Meta:
        verbose_name = "портфолио"
        verbose_name_plural = "портфолио"


class AboutMe(BaseModel):
    message = models.TextField()
    avatar = models.ForeignKey(
        Asset,
        verbose_name="аватар",
        on_delete=models.RESTRICT,
        related_name="+",
    )
    bg_image = models.ForeignKey(
        Asset,
        verbose_name="паттерн",
        on_delete=models.RESTRICT,
        related_name="+",
    )

    class Meta:
        verbose_name = "обо мне"
        verbose_name_plural = "обо мне"


class ContactDetail(BaseModel):
    icon = models.CharField("fa-иконка", max_length=64)
    detail = models.CharField("информация", max_length=512)

    class Meta:
        verbose_name = "контакты: данные"
        verbose_name_plural = "контакты: данные"


class ContactLink(BaseModel):
    icon = models.CharField("fa-иконка", max_length=64)
    url = models.URLField("ссылка")

    class Meta:
        verbose_name = "контакты: ссылка"
        verbose_name_plural = "контакты: ссылки"


class Contacts(BaseModel):
    details_list = models.ManyToManyField(
        ContactDetail, verbose_name="список данных"
    )
    link_list = models.ManyToManyField(
        ContactLink, verbose_name="список ссылок"
    )
    map_widget = models.CharField(
        "виджет карты", max_length=2048, default="", blank=True
    )

    class Meta:
        verbose_name = "контакты"
        verbose_name_plural = "контакты"


class Footer(BaseModel):
    logo = models.ForeignKey(
        Asset, verbose_name="лого", on_delete=models.RESTRICT, related_name="+"
    )
    bg_pattern = models.ForeignKey(
        Asset,
        verbose_name="паттерн",
        on_delete=models.RESTRICT,
        related_name="+",
    )
    copyright_text = models.CharField("копирайт", max_length=512)

    class Meta:
        verbose_name = "футер"
        verbose_name_plural = "футеры"


class Page(BaseModel):
    icon = models.ForeignKey(
        Asset,
        verbose_name="иконка (png)",
        on_delete=models.RESTRICT,
        related_name="+",
    )
    shortcut_icon = models.ForeignKey(
        Asset,
        verbose_name="иконка (ico)",
        on_delete=models.RESTRICT,
        related_name="+",
    )
    logo = models.ForeignKey(
        Asset,
        verbose_name="лого панели навигации",
        on_delete=models.RESTRICT,
        related_name="+",
    )
    title = models.CharField("название страницы", max_length=255)

    start_screen = models.ForeignKey(
        StartScreen, verbose_name="стартовый экран", on_delete=models.RESTRICT
    )
    promo = models.ForeignKey(
        Promo,
        verbose_name="промо блок",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    services = models.ForeignKey(
        Services, verbose_name="услуги", on_delete=models.RESTRICT
    )
    portfolio = models.ForeignKey(
        Portfolio, verbose_name="портфолио", on_delete=models.RESTRICT
    )
    about_me = models.ForeignKey(
        AboutMe, verbose_name="обо мне", on_delete=models.RESTRICT
    )
    contacts = models.ForeignKey(
        Contacts, verbose_name="контакты", on_delete=models.RESTRICT
    )
    footer = models.ForeignKey(
        Footer, verbose_name="футер", on_delete=models.RESTRICT
    )

    is_active = models.BooleanField("сделать активной", default=False)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.is_active:
            return

        queryset = Page.objects.filter(~models.Q(pk__in=(self.pk,)), is_active=True)
        queryset.update(is_active=False)
