# Generated by Django 5.0.7 on 2024-07-23 21:20

import wagtail.contrib.table_block.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_tablepage_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablepage',
            name='table',
            field=wagtail.fields.StreamField([('table', wagtail.contrib.table_block.blocks.TableBlock())], blank=True, null=True),
        ),
    ]
