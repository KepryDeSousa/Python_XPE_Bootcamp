from django.urls import path
from .views import index
# incluindo nossos codigos


urlpatterns = {
    path("",index, name="index"),
}
