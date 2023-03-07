from django.urls import path
from funE_app.views import UserList
from .views import SignupView

urlpatterns = [
     path('users/', UserList.as_view(), name='user-list'),
     path('signup/', SignupView.as_view(), name='signup'),
     # path('user/',GetAllUserApi.as_view()),
     # path('user/<str:pk>',GetAllUserApi.as_view()),
]