from django.urls import path
from classroom.views import index, resources, add_resource

urlpatterns = [
    path("", index, name="classroom"),
    path("resources/", resources, name="resources"),
    path("addresource/", add_resource, name="add_resource"),
]