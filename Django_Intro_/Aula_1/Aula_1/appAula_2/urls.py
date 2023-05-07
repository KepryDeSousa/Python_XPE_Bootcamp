from django.urls import path 

# incluindo nossos codigos
from .views import index

urlpatterns = {
    path("",index, name="index"),
}
