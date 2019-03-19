from django.conf.urls import url
from . import views


urlpatterns = [
    url('signup/', views.UserCreate.as_view(), name='create_account'),
    url('login/',views.Loginview.as_view(), name='login'),
    url('', views.HomeView.as_view(), name='home'),

]