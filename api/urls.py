from django.conf.urls import url
from .views import Register, HelloWorld, MyTokenObtainPairView

urlpatterns = [
    url(r'^api/token$', MyTokenObtainPairView.as_view()),
    url(r'^register$', Register.as_view()),
    url(r'^hello$', HelloWorld.as_view())
]