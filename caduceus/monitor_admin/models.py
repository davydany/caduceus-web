from django.db import models

from core.models import BaseClass

class Project(BaseClass):

    name = models.CharField(max_length=25)


class Request(BaseClass):

    uuid = models.CharField(max_length=36)
    request_stats = models.TextField()

