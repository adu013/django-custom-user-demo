from django.conf.urls import url
from .views import register, login_view, logout_view


urlpatterns = [
    url(r'^register/$', register),
    url(r'^login/$', login_view),
    url(r'^logout/$', logout_view),
]
