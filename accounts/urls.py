from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    # apos fazer serilizer logout tira tokenblacklistview 
    # TokenBlacklistView,
    # e impor customtokenblack..
    )

from .views import CustomTokenBlackListView



app_name = "accounts"
urlpatterns = [
    path("login", TokenObtainPairView.as_view(), name="login"),
    path("refresh", TokenRefreshView.as_view(), name="refresh"),
    
    # altera e utiliza o custom
    # path("logout", TokenBlacklistView.as_view(), name="logout"),
    path("logout", CustomTokenBlackListView.as_view(), name="logout"),

    
]