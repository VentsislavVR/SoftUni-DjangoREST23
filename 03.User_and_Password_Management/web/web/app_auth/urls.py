from django.urls import path

from web.app_auth.views import RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('register/', LoginUserView.as_view(), name='login_user'),
    path('register/', LogoutUserView.as_view(), name='logout_user')
)
