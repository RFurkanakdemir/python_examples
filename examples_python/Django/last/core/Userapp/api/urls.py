from django.urls import path,include
from Userapp.api import views as api_views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns = [
    path('register/',api_views.UserRegisterAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('login/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('change_password/',api_views.ChangePasswordAPIView.as_view(),name='change-password'),
    path('password_reset/', api_views.PasswordResetAPIView.as_view() ,name='password-reset-request'),
    path(
        "password_reset/<str:encoded_pk>/<str:token>/",
        api_views.ResetPasswordLinkAPIView.as_view(),
        name="reset-password",
    )

]
   