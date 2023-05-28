from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/',views.RegistrationAPIView.as_view()),
    path('login/', views.AuthorizateView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('wedding/get', views.WeddingListCreateAPIVew.as_view(), name='wedding'),
    path('wedding/post', views.WeddingPostNews.as_view(), name='wedding'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)