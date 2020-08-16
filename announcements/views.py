from django.shortcuts import render
from announcements.forms import AnnouncementForm
from announcements.models import Announcements
from decouple import config
from authapp.models import UserProfile
from qna.models import ClassRoom
from twilio.rest import Client

# Create your views here.


def create(request):
    form = AnnouncementForm()
    return render(request, 'announcements/create.html', {'form': form})


def index(request):
    history = Announcements.objects.all()
    return render(request, 'announcements/index.html', {'history': history})


def send(request):
    if request.method == "POST":
        client = Client(config('TWILIO_ACCOUNTS_SID'), config('TWILIO_AUTH_TOKEN'))
        body = request.POST['body']
        classroom = ClassRoom.objects.get(name=request.POST['classroom'])
        students_feature = UserProfile.objects.filter(classroom=classroom).filter(isTeacher=False).filter(
            isFeaturePhone=True)
        students_whatsapp = UserProfile.objects.filter(classroom=classroom).filter(isTeacher=False).filter(
            isFeaturePhone=False)
        link = ""
        try:
            link = request.POST['link']
        except:
            pass

        try:
            for user in students_feature:
                message = client.messages.create(body=body + "   " + link, from_="+12058585073", to="+91" + user.phone)

                a = Announcements(class_id=classroom,
                                  title=request.POST['title'],
                                  link=request.POST['link'],
                                  body=request.POST['body'])
                a.save()
                print(message.sid)
        except:
            print("Some error occured")
