import typing as t
from dataclasses import dataclass
from pathlib import Path

import dataclass_settings as ds


@dataclass
class MessageForwarder:
    worker_timeout: t.Annotated[int, ds.Env("WORKER_TIMEOUT")] = 30
    request_timeout: t.Annotated[int, ds.Env("REQUEST_TIMEOUT")] = 3
    batch_size: t.Annotated[int, ds.Env("BATCH_SIZE")] = 10
    api_token: t.Annotated[str, ds.Env("API_TOKEN")] = ""
    chat_id: t.Annotated[int, ds.Env("CHAT_ID")] = 0


@dataclass
class Database:
    host: t.Annotated[str, ds.Env("DB_HOST")] = ""
    port: t.Annotated[int, ds.Env("DB_PORT")] = 0
    db_name: t.Annotated[str, ds.Env("DB_NAME")] = ""
    username: t.Annotated[str, ds.Env("DB_USER")] = ""
    password: t.Annotated[str, ds.Env("DB_PASSWORD")] = ""


@dataclass
class EnvSettings:
    db: Database
    message_forwarder: MessageForwarder

    debug: bool = True
    secret_key: t.Annotated[str, ds.Env("SECRET_KEY")] = ""
    allowed_hosts: t.Annotated[str, ds.Env("ALLOWED_HOSTS")] = ""

    csrf_trusted_origins: t.Annotated[str, ds.Env("CSRF_TRUSTED_ORIGINS")] = ""

    db_root: t.Annotated[str, ds.Env("DB_ROOT")] = ""
    static_root: t.Annotated[str, ds.Env("STATIC_ROOT")] = ""
    media_root: t.Annotated[str, ds.Env("MEDIA_ROOT")] = ""


ENV_SETTINGS: EnvSettings = ds.load_settings(
    EnvSettings, nested_delimiter="__"
)

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = (
    ENV_SETTINGS.secret_key
    or "django-insecure-a%3n=nw*e37eoc00dy+q2psi==#9jy0)##4s%l=#^&1sf=(#_)"
)

DEBUG = ENV_SETTINGS.debug

ALLOWED_HOSTS: list[str] = (
    ENV_SETTINGS.allowed_hosts.split(",") if ENV_SETTINGS.allowed_hosts else []
)
CSRF_TRUSTED_ORIGINS = (
    ENV_SETTINGS.csrf_trusted_origins.split(",")
    if ENV_SETTINGS.csrf_trusted_origins
    else []
)


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_bootstrap5",
    "fontawesomefree",
    "home",
    "sortedm2m",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "conf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "conf.wsgi.application"

if ENV_SETTINGS.db.host:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": ENV_SETTINGS.db.db_name,
            "USER": ENV_SETTINGS.db.username,
            "PASSWORD": ENV_SETTINGS.db.password,
            "HOST": ENV_SETTINGS.db.host,
            "PORT": ENV_SETTINGS.db.port,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": (
                ENV_SETTINGS.db_root
                or BASE_DIR.joinpath("..", "files", "db.sqlite3")
            ),
        }
    }

AUTH_PASSWORD_VALIDATORS = []
for validation in (
    "UserAttributeSimilarityValidator",
    "MinimumLengthValidator",
    "CommonPasswordValidator",
    "NumericPasswordValidator",
):
    AUTH_PASSWORD_VALIDATORS.append(
        {"NAME": "django.contrib.auth.password_validation." + validation}
    )

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
MEDIA_URL = "media/"

STATIC_ROOT = (
    ENV_SETTINGS.static_root
    or BASE_DIR.joinpath("..", "files", "static")
)
MEDIA_ROOT = (
    ENV_SETTINGS.media_root
    or BASE_DIR.joinpath("..", "files", "media")
)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
