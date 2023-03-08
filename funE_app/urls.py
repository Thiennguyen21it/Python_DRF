from django.urls import path
from funE_app.views import UserViewSet
from .views import SignupView
from  rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet,)

urlpatterns = router.urls
# urlpatterns = [
#      path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
#      # path('users/', UserList.as_view(), name='user-list'),
#      path('signup/', SignupView.as_view(), name='signup'),
#      # path('user/',GetAllUserApi.as_view()),
#      # path('user/<str:pk>',GetAllUserApi.as_view()),
# ]