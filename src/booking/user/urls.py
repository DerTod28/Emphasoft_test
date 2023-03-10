from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from booking.user.views import CurrentUserView, RegisterView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', RegisterView.as_view(), name='auth_signup'),
    path('me/', CurrentUserView.as_view(), name='current_user')
]
