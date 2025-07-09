from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, TaskViewSet, CommentViewSet, ProjectMemberViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)
router.register('comments', CommentViewSet)
router.register('project-members', ProjectMemberViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
