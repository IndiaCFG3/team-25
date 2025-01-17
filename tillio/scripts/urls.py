import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djtwilio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Here we add our Twilio URLs
    url(r'^sms/$', 'djtwilio.views.sms'),
    url(r'^ring/$', 'djtwilio.views.ring'),
)




# # -*- coding: utf-8 -*-
# from django_twilio.decorators import twilio_view
# from twilio.twiml.messaging_response import MessagingResponse

# @twilio_view
# def sms(request):
#     r = Response()
#     r.message('Hello from your Django app!')
#     return r