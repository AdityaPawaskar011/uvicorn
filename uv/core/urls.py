from django.urls import path
from core.views import notificatin_view


urlpattern = [
    path("notification/",notificatin_view,name="notification_view")
]
