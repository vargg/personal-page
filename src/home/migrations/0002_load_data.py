# ruff: noqa: RUF012
from django.db import migrations

from ._init_data import create_page


class Migration(migrations.Migration):

    dependencies = [("home", "0001_initial")]

    operations = [
        migrations.RunPython(create_page, None, atomic=False)
    ]
