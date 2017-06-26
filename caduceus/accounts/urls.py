from django.conf.urls import url

from accounts.views import LoginView, LogoutView

urlpatterns = [
    url(r'^auth/login/$', LoginView.as_view(), name='account-login'),
    url(r'^auth/logout/$', LogoutView.as_view(), name='account-logout'),
]