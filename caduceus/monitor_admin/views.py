from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, UpdateView, 
    ListView, DetailView)

from django.urls import reverse

from monitor_admin.models import Project, Request

class ProjectListView(LoginRequiredMixin, ListView):

    model = Project

    def get_queryset(self):

        return Project.objects.filter(owner=self.request.user).all()

class ProjectCreateView(LoginRequiredMixin, CreateView):

    model = Project
    fields = ['name', 'owner', 'django_project_name']

    def get_queryset(self):

        return Project.objects.filter(owner=self.request.user).all()

    def get_context_data(self, **kwargs):
        '''
        Adds the current user's ID to the form data.
        '''
        data = super(ProjectCreateView, self).get_context_data(**kwargs)
        data['owner_id'] = self.request.user.id
        return data

    def get_form(self, *args, **kwargs):

        form = super(ProjectCreateView, self).get_form(*args, **kwargs)
        form.fields['owner'].widget = forms.widgets.HiddenInput()
        return form

    def get_initial(self):

        initial = super(ProjectCreateView, self).get_initial()
        initial['owner'] = self.request.user
        return initial

class ProjectUpdateView(LoginRequiredMixin, UpdateView):

    model = Project
    fields = ['name', 'django_project_name']

    def get_queryset(self):

        return Project.objects.filter(owner=self.request.user).all()

    def get_context_data(self, **kwargs):
        '''
        Adds the current user's ID to the form data.
        '''
        data = super(ProjectUpdateView, self).get_context_data(**kwargs)
        data['owner_id'] = self.request.user.id
        return data

class ProjectDeleteView(LoginRequiredMixin, DeleteView):

    model = Project

    def get_queryset(self):

        return Project.objects.filter(owner=self.request.user).all()

    def get_success_url(self):

        return reverse('project-list')

class ProjectDetailView(LoginRequiredMixin, DetailView):

    model = Project
    fields = ['name', 'project_id', 'owner']
    
    def get_queryset(self):

        return Project.objects.filter(owner=self.request.user).all()

    def get_context_data(self, **kwargs):

        project = self.get_object()
        data = super(ProjectDetailView, self).get_context_data(**kwargs)
        data['requests'] = project.requests.all()
        return data