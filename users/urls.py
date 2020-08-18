from django.urls import path

from .views import SignupPageView, LogOutView


urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('logout_redirect/', LogOutView.as_view(), name='logout_redirect'),
]