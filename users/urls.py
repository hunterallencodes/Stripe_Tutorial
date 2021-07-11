from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    inactive_subscription,
    landing_page,
    profile,
    MembersAreaView,
    RegisterView,
)


app_name = 'users'


urlpatterns = [
    path('', landing_page, name="landing-page"),
    path('accounts/login/', LoginView.as_view(template_name="users/login.html"), name="login"),
    path('accounts/logout/', LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('accounts/members/', MembersAreaView.as_view(), name="members"),
    path('accounts/register/', RegisterView.as_view(), name="register"),
    path('accounts/subscribe/', inactive_subscription, name="subscribe"),
    path('accounts/profile/', profile, name="profile"),
]