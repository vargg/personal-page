# ruff: noqa: ANN001, ANN202, N803, N806
import pathlib

from django.core.files import File

DEFAULT_FILES_DIR = pathlib.Path(__file__).parent.joinpath("files")


def _create_assets(AssetModel):
    pattern_file = DEFAULT_FILES_DIR.joinpath("bg_pattern.png")
    pattern = AssetModel.objects.create(
        name="bg-pattern",
        file=File(pattern_file.open("rb"), name=pattern_file.name),
    )

    image_file = DEFAULT_FILES_DIR.joinpath("image-placeholder.jpg")
    image = AssetModel.objects.create(
        name="image-placeholder",
        file=File(image_file.open("rb"), name=image_file.name),
    )

    logo_file = DEFAULT_FILES_DIR.joinpath("logo-placeholder.png")
    logo = AssetModel.objects.create(
        name="logo-placeholder",
        file=File(logo_file.open("rb"), name=logo_file.name),
    )

    icon_file = DEFAULT_FILES_DIR.joinpath("icon-placeholder.png")
    icon = AssetModel.objects.create(
        name="icon-placeholder.png",
        file=File(icon_file.open("rb"), name=icon_file.name),
    )

    return pattern, image, logo, icon


def _create_start_screen(StartScreenModel, logo, pattern):
    return StartScreenModel.objects.create(
        name="sample start screen",
        note="sample start screen note",
        logo=logo,
        bg_pattern=pattern,
        primary_text="sample primary text",
        secondary_text="sample secondary text",
    )


def _create_promo(PromoModel):
    return PromoModel.objects.create(
        name="sample promo",
        note="this is a sample promo note.",
        text="this is a sample promo text",
    )


def _create_service_items(ServiceItemModel):
    result = []

    for i, icon in enumerate(
        (
            "fa-solid fa-info",
            "fa-solid fa-asterisk",
            "fa-solid fa-star",
            "fa-solid fa-heart",
            "fa-solid fa-ruble-sign",
            "fa-solid fa-eye",
            "fa-solid fa-paw",
            "fa-solid fa-clover",
            "fa-solid fa-pencil",
            "fa-solid fa-feather",
        ),
        1
    ):
        result.append(
            ServiceItemModel.objects.create(
                name=f"service item {i}",
                note=f"this is service item {i} note",
                icon=icon,
                description=f"this is service item {i} description",
            )
        )

    return result


def _create_service_blocks(ServiceItemModel, ServiceBlockModel, image):
    items = _create_service_items(ServiceItemModel)

    main = ServiceBlockModel.objects.create(
        name="main services block",
        note="main services block note",
        description="main services block description",
        image_position="R",
        image=image,
    )
    main.items.set(items[:5])

    extra = ServiceBlockModel.objects.create(
        name="extra services block",
        note="extra services block note",
        description="extra services block description",
        image_position="L",
        image=image,
    )
    extra.items.set(items[5:])

    return main, extra


def _create_services(
    ServiceItemModel, ServiceBlockModel, ServicesModel, image
):
    services = ServicesModel.objects.create(name="sample services")
    services.items.set(
        _create_service_blocks(ServiceItemModel, ServiceBlockModel, image)
    )

    return services


def _create_portfolio(PortfolioModel, image):
    portfolio = PortfolioModel.objects.create(
        name="sample portfolio",
        note="sample portfolio note",
        description="sample portfolio description",
    )
    portfolio.items.set([image])
    return portfolio


def _create_about_me(AboutMeModel, avatar, pattern):
    return AboutMeModel.objects.create(
        name="sample about me",
        note="sample about me note",
        message="sample about me message",
        avatar=avatar,
        bg_image=pattern,
    )


def _create_contact_links(ContactLinkModel):
    return [
        ContactLinkModel.objects.create(
            name="tg link",
            icon="fa-brands fa-telegram",
            url="https://t.me/",
        ),
        ContactLinkModel.objects.create(
            name="tt link",
            icon="fa-brands fa-tiktok",
            url="https://tiktok.com/",
        ),
        ContactLinkModel.objects.create(
            name="inst link",
            icon="fa-brands fa-instagram",
            url="https://instagram.com/",
        ),
        ContactLinkModel.objects.create(
            name="youtube link",
            icon="fa-brands fa-youtube",
            url="https://youtube.com/",
        ),
        ContactLinkModel.objects.create(
            name="vk link",
            icon="fa-brands fa-vk",
            url="https://vk.com/",
        ),
    ]


def _create_contact_details(ContactDetailModel):
    return [
        ContactDetailModel.objects.create(
            name="tg:",
            icon="fa-brands fa-telegram-plane",
            detail="@tgaccount",
        ),
        ContactDetailModel.objects.create(
            name="email:",
            icon="fa-solid fa-envelope",
            detail="sample@email.no",
        ),
        ContactDetailModel.objects.create(
            name="phone:",
            icon="fa-solid fa-phone",
            detail="+71231231212",
        ),
        ContactDetailModel.objects.create(
            name="address:",
            icon="fa-solid fa-map-marker-alt",
            detail="sample address description <br> second line",
        ),
    ]


def _contacts(ContactDetailModel, ContactLinkModel, ContactsModel):
    contacts = ContactsModel.objects.create(
        name="sample contacts",
        note="sample contacts note",
    )
    contacts.details_list.set(_create_contact_details(ContactDetailModel))
    contacts.link_list.set(_create_contact_links(ContactLinkModel))
    return contacts


def _create_footer(FooterModel, logo, pattern):
    return FooterModel.objects.create(
        name="sample footer",
        note="sample footer note",
        logo=logo,
        bg_pattern=pattern,
        copyright_text="© sample company",
    )


def create_page(apps, _schema_editor) -> None:
    AssetModel = apps.get_model("home", "Asset")
    StartScreenModel = apps.get_model("home", "StartScreen")
    PromoModel = apps.get_model("home", "Promo")
    ServiceItemModel = apps.get_model("home", "ServiceItem")
    ServiceBlockModel = apps.get_model("home", "ServiceBlock")
    ServicesModel = apps.get_model("home", "Services")
    PortfolioModel = apps.get_model("home", "Portfolio")
    AboutMeModel = apps.get_model("home", "AboutMe")
    ContactDetailModel = apps.get_model("home", "ContactDetail")
    ContactLinkModel = apps.get_model("home", "ContactLink")
    ContactsModel = apps.get_model("home", "Contacts")
    FooterModel = apps.get_model("home", "Footer")
    PageModel = apps.get_model("home", "Page")

    pattern, image, logo, icon = _create_assets(AssetModel)

    PageModel.objects.create(
        name="sample page",
        note="sample page note",
        title="sample page title",
        logo=logo,
        icon=icon,
        start_screen=_create_start_screen(StartScreenModel, logo, pattern),
        promo=_create_promo(PromoModel),
        services=_create_services(
            ServiceItemModel, ServiceBlockModel, ServicesModel, image
        ),
        portfolio=_create_portfolio(PortfolioModel, image),
        about_me=_create_about_me(AboutMeModel, image, pattern),
        contacts=_contacts(
            ContactDetailModel, ContactLinkModel, ContactsModel
        ),
        footer=_create_footer(FooterModel, logo, pattern),
        is_active=True,
    )
