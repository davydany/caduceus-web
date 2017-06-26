import json
import uuid
from django.db import models
from django.contrib.auth.models import User

from core.models import BaseClass
from django.urls import reverse


class Project(BaseClass):

    owner = models.ForeignKey(User)
    name = models.CharField(max_length=25, help_text='Name of your Project')
    django_project_name = models.CharField('Django Project Name',
        max_length=25, help_text='Name of your Django Project.')
    project_id = models.CharField(max_length=36, unique=True)

    def save(self, *args, **kwargs):
        '''
        Overrides 'save' in the Project model to generate a unique
        project_id.
        '''
        if not self.project_id:
            self.project_id = str(uuid.uuid4())

        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        '''
        Returns the resource url for this project.
        '''
        return reverse('project-detail', args=[self.id])

    def __str__(self):

        return self.name


class Request(BaseClass):
    """
    Request represents a HTTP request, and additional metrics
    collected by the monitors.
    """
    project = models.ForeignKey(
        Project, related_name='requests', on_delete=models.CASCADE)
    uuid = models.CharField(max_length=36, unique=True)
    request_stats = models.TextField()

    def __str__(self):

        return '%s - Request: %s' % (self.project.name, self.uuid)

    def metrics(self):
        '''
        Transforms the stats from JSON to a Python Dictionary.
        '''
        try:
            parsed = json.loads(self.request_stats)
            print("PARSED:", parsed)
            return parsed
        except ValueError:
            return False
