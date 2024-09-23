from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.UserView.as_view(), name='main'),
    path('update-data/', views.UpdateDataView.as_view(), name='update_data'),
    path('add-site/', views.AddSiteView.as_view(), name='add_site'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]