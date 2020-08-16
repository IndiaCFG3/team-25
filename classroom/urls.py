from django.urls import path
from classroom.views import index, resources 

urlpatterns = [
    path("", index, name="classroom"),
    path("resources/", resources, name="resources")
]