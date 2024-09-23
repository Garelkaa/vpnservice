from django.urls import path
from . import views

app_name = 'vpn'

urlpatterns = [
    path('<str:site_name>/<path:path>/',views.ProxyView.as_view(), name='proxy_view'),

]