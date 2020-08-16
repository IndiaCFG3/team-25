from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from announcements.models import Announcements
from quiz.models import Quiz


def announcement_response():
    ann = Announcements.objects.all().order_by("-id")
    message = "These are recent Announcements : \n"
    for a in ann :
        message = message + a.title + "\n" + a.body + a.link + "\n\n"

    return message

def quiz_response():
    quizzes = Quiz.objects.all().order_by("-id")
    message = "These are quizzes : \n"
    for a in quizzes :
        message = message + a.title 
    return message







# define home function
def home(request):

    # return a fulfillment message
    # fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.'}
    # return response
    # print(json.loads(request.body))
    
    return HttpResponse(quiz_response())

@csrf_exempt
def twilio(request):


    
    return HttpResponse("this is response for twilio webhook")

@csrf_exempt
def webhook(request):
    # build a request object
    req = json.loads(request.body)
    
    # get action from json
    action = req.get('queryResult').get('action')
    # return a fulfillment message
    fulfillmentText = {'fulfillmentText': announcement_response()}
    # return response
    return JsonResponse(fulfillmentText, safe=False)
