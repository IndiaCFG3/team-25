from django.shortcuts import render
from classroom.models import Course, Chapter
# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request,"classroom/classpage.html")
    course_name = request.POST['course_name']
    chapter_name = request.POST['chapter_name']

    course = Course.objects.get_or_create(name=course_name)
    Chapter.objects.create(course=course[0], name=chapter_name)

    chapters = Chapter.objects.filter(course=course[0])
    context = {}
    context['course'] = course[0]
    context['chapter'] = chapters
    return render(request,"classroom/classpage.html", context)


# def resources(index):
