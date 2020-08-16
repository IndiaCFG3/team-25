from django.urls import path
from classroom.views import index 

urlpatterns = [
    path("", index, name="classroom"),
    # path("resources/", resources, name="resources")
]