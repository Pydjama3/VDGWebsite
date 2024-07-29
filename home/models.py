import wagtail.fields
from django.db import models
from wagtail.blocks import StreamBlock, RichTextBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.blocks import ImageChooserBlock

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField

from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from VDGWebsite.blocks import VDGTableBlock

# Email: vdgrimpe@gmail.com


class HomePage(Page):
    main_img = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Hero image",
    )

    subtitle = models.CharField(
        blank=True,
        max_length=255,
        help_text="Sous-titre de la page"
    )

    body = RichTextField(blank=True)

    news = models.IntegerField(default=3)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("main_img"),
                FieldPanel("subtitle"),
            ],
            heading="En-tête",
        ),
        MultiFieldPanel([
            FieldPanel('news'),
            FieldPanel('body')
            ],
            heading="Contenu"
        )
    ]

class ContentPage(Page):
    main_img = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Hero image",
    )

    subtitle = models.CharField(
        blank=True,
        max_length=255,
        help_text="Sous-titre de la page"
    )

    # body = RichTextField(blank=True)

    # body = StreamField(
    #     [
    #         ("text", RichTextBlock())
    #     ],
    #     blank=True,
    #     null=True
    # )

    body = StreamField(
        [
            ("text", RichTextBlock()),
            ("table", TableBlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("main_img"),
                FieldPanel("subtitle"),
            ],
            heading="En-tête",
        ),
        FieldPanel("body")
    ]


class FormsPage(Page):
    main_img = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Hero image",
    )

    subtitle = models.CharField(
        blank=True,
        max_length=255,
        help_text="Sous-titre de la page"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("main_img"),
                FieldPanel("subtitle"),
            ],
            heading="En-tête",
        ),
    ]


class GalleryPage(Page):
    main_img = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Hero image",
    )

    subtitle = models.CharField(
        blank=True,
        max_length=255,
        help_text="Sous-titre de la page"
    )

    gallery = StreamField(
        [
            ("image", ImageChooserBlock())
        ],
        default={}
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("main_img"),
                FieldPanel("subtitle"),
            ],
            heading="En-tête",
        ),
        FieldPanel("gallery")
    ]
