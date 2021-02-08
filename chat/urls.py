from django.urls import path,include
from django.conf.urls import url
# from .views import SignUpView,LogInView
from . import views


urlpatterns = [
    path ('' ,views.index, name= 'index'),
    path ('<str:room_name>/',views.room, name = 'room'),
    # path('register/', views.signup, name='signup'),
    # path('account/', include('django.contrib.auth.urls')),
]