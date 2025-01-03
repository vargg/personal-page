# Generated by Django 5.1.3 on 2024-11-22 16:33

import sortedm2m.fields
from django.db import migrations
from sortedm2m.operations import AlterSortedManyToManyField


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_aboutme_description_asset_description_and_more'),
    ]

    operations = [
        AlterSortedManyToManyField(
            model_name='contacts',
            name='details_list',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='home.contactdetail', verbose_name='список данных'),
        ),
        AlterSortedManyToManyField(
            model_name='contacts',
            name='link_list',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='home.contactlink', verbose_name='список ссылок'),
        ),
        AlterSortedManyToManyField(
            model_name='portfolio',
            name='items',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, related_name='+', to='home.asset', verbose_name='Примеры'),
        ),
        AlterSortedManyToManyField(
            model_name='serviceblock',
            name='items',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='home.serviceitem', verbose_name='строки'),
        ),
        AlterSortedManyToManyField(
            model_name='services',
            name='items',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='home.serviceblock', verbose_name='блоки'),
        ),
    ]
