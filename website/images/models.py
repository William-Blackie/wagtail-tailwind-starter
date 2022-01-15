from django.conf import settings
from django.db import models
from wagtail.api import APIField
from wagtail.images.models import AbstractImage, AbstractRendition, Image


class CustomImage(AbstractImage):
    alt = models.CharField(max_length=255, blank=True)

    admin_form_fields = Image.admin_form_fields + ("alt",)


class Rendition(AbstractRendition):
    image = models.ForeignKey(
        "CustomImage", related_name="renditions", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)
