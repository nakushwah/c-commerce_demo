"""
Urls set for the Account's views
"""


from django.urls import path
from .views import Register, Home, UserLogin, UserLogout, VerifyEmail

urlpatterns = [
    path('home',
         Home.as_view(),
         name='home'
         ),
    path("Register/",
         Register.as_view(),
         name='Register'
         ),
    path("", UserLogin.as_view(),
         name='UserLogin'
         ),
    path("UserLogout/",
         UserLogout.as_view(),
         name='UserLogout'
         ),
    path("VerifyEmail/",
         VerifyEmail.as_view(),
         name='VerifyEmail'
         ),
]
