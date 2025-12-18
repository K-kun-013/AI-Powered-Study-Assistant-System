from django.urls import path
from .views import UserRegistrationView, UserLoginView, RoleBasedView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('role-based/', RoleBasedView.as_view(), name='role-based-view'),
]