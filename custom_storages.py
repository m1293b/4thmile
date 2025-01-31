from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class CustomStaticStorage(S3Boto3Storage):
    location = settings.AWS_STATIC_LOCATION

class CustomMediacStorage(S3Boto3Storage):
    location = settings.AWS_MEDIA_LOCATION