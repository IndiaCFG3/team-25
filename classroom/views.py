from django.shortcuts import render, HttpResponseRedirect
from classroom.models import Course, Chapter, Resource
from classroom.forms import ResourceForm

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "classroom/classpage.html")
    course_name = request.POST['course_name']
    chapter_name = request.POST['chapter_name']

    course = Course.objects.get_or_create(name=course_name)
    Chapter.objects.create(course=course[0], name=chapter_name)

    chapters = Chapter.objects.filter(course=course[0])
    context = {}
    context['course'] = course[0]
    context['chapter'] = chapters
    return render(request, "classroom/classpage.html", context)


def resources(request):
    resources = Resource.objects.all()
    return render(request, "classroom/resources.html", {'resources': resources})

def add_resource(request):
    form = ResourceForm()
    if request.method == "GET":
        return render(request, "classroom/addresource.html", {'form' : form})
    form = ResourceForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/classpage/resources/")
     
