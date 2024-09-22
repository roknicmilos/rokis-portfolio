from urllib.parse import urljoin

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.handlers.wsgi import WSGIRequest
from django.db import models


def create_sample_image() -> SimpleUploadedFile:
    """
    Creates a simple representation of an in memory image (JPG) file
    """
    tiny_1x1_px_jpeg_image_data = (
        b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00"
        b"\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07"
        b"\x07\t\x08\x0a\x0a\t\x08\t\t\n\x0c\x14\x0d\n\x0b\x13\x0b\t"
        b"\t\x12\x11\x12\x14\x12\x0c\x0e\x17\x16\x18\x18\x17\x16\x1a"
        b'\x1d%\x1f\x1a\x1b#\x1c\x16\x17 \x1e("Qq2br\x15&B\xb8\xa1'
        b"\xcb\x82\xe2\xff\xc0\x00\x0b\x08\x00\x01\x00\x01\x01\x01"
        b"\x11\x00\xff\xc4\x00\x14\x00\x01\x00\x00\x06\x01\x01\x05"
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x05"
        b"\x03\x02\x06\x01\x00\xff\xda\x00\x08\x01\x01\x00\x00?\x00"
        b"\xf7+0~\xff\xd9"
    )
    return SimpleUploadedFile(
        name="sample_image.jpg",
        content=tiny_1x1_px_jpeg_image_data,
        content_type="image/jpg",
    )


def create_media_absolute_url(
    request: WSGIRequest, file_field: models.FileField
) -> str:
    file_url = urljoin(settings.MEDIA_URL, file_field.name)
    return request.build_absolute_uri(file_url)
