from django.urls import include, path

urlpatterns = [
    path('', include('main.urls')),
    path('user/', include('users.urls')),
    path('vpn/', include('vpn.urls'))
]
