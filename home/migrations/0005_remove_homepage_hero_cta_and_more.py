# Generated by Django 5.0.6 on 2024-07-16 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_hero_cta_homepage_hero_cta_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='hero_cta',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='hero_cta_link',
        ),
    ]
