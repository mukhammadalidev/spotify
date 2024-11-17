from django.urls import path

from users.views import LoginAPIView,RegisterAPIView,ProfileAPIView,LogoutAPIView

urlpatterns=[
    path('login/',LoginAPIView.as_view(),name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]