from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloApiViewset,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet) #basename only if you dont have a queryset

urlpatterns = [
    path('hello-view/',views.HelloApi.as_view()),
    path('',include(router.urls))
]
