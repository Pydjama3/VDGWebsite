# Generated by Django 5.0.7 on 2024-07-23 21:09

import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_tablepage_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablepage',
            name='table',
            field=wagtail.fields.StreamField([('table', wagtail.blocks.StreamBlock([('table', wagtail.contrib.table_block.blocks.TableBlock(non_nullable=False))]))], blank=True),
        ),
    ]
