# Generated by Django 5.0.7 on 2024-07-25 13:48

import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_complexcontentpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complexcontentpage',
            name='body',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock())], default={}),
        ),
    ]
