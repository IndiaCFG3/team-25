from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from announcements.models import Announcements
from quiz.models import Quiz
# import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

def announcement_response():
    ann = Announcements.objects.all().order_by("-id")
    message = "These are recent Announcements : \n"
    for a in ann :
        message = message + a.title + "\n" + a.body +"\n"+ a.link + "\n\n"
    return message

def quiz_response():
    quizzes = Quiz.objects.all().order_by("-id")
    message = "These are quizzes : \n"
    for a in quizzes :
        message = message + a.title 
    return message







# define home function
@csrf_exempt
def twilio(request):

    # return a fulfillment message
    resp = MessagingResponse()    # Add a text message
    msg = resp.message("Hello, you!")
    return HttpResponse(str(resp))

@csrf_exempt
def home(request):


    
    return HttpResponse("this is response for twilio webhook")

@csrf_exempt
def webhook(request):
    # build a request object
    req = json.loads(request.body)
    print(req["queryResult"]["intent"]["displayName"])
    # print(json.dumps(req, indent=4))
    # print(req)
    if req["queryResult"]["intent"]["displayName"] == "tests":
        message = quiz_response()
    elif req["queryResult"]["intent"]["displayName"] == "results":
        message = "results are not announced yet"
    elif req["queryResult"]["intent"]["displayName"] == "announcements":
        message = announcement_response()


    # get action from json
    action = req.get('queryResult').get('action')
    # return a fulfillment message
    fulfillmentText = {'fulfillmentText': message}
    # return response
    return JsonResponse(fulfillmentText, safe=False)
