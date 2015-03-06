import oauth2 as oauth
import urlparse  
import json
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required  
from django.contrib.admin.views.decorators import staff_member_required

#Import project
from linkedn.models import Profile, Education, Positions, Certifications

#ouath configuration
consumer = oauth.Consumer(settings.LINKEDN_KEY, settings.LINKEDN_SECRET)
client = oauth.Client(consumer)
request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
authorize_url = 'https://api.linkedin.com/uas/oauth/authorize'

@staff_member_required
def index(request):
    return HttpResponse("LINKEDN index page")

@staff_member_required
def linkedn_login(request):
    #request token from linkedn
    resp, content = client.request(request_token_url, "POST")
    if resp['status'] != '200':
        raise Exception("Invalid response, status is %s"%resp['status'])
    #store the token in a session
    request.session['request_token'] = dict(urlparse.parse_qsl(content))
    url = "%s?oauth_token=%s" % (authorize_url, request.session['request_token']['oauth_token'])
    return HttpResponseRedirect(url)

def linkedn_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def linkedn_authenticated(request):
    token = oauth.Token( request.session['request_token']['oauth_token'], request.session['request_token']['oauth_token_secret'])
    token.set_verifier(request.GET.get('oauth_verifier'))
    client = oauth.Client(consumer, token)
    resp, content = client.request(access_token_url, "POST")
    if resp['status'] != '200':
        raise Exception("Invalid response")
    access_token = dict(urlparse.parse_qsl(content))
    url = "https://api.linkedin.com/v1/people/~:(id,first-name,last-name,educations,certifications,three-current-positions,three-past-positions)?format=json"     
    token_user = oauth.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
    client = oauth.Client(consumer, token_user)
    if resp ['status'] != '200':
        raise Exception("Invalid response")
    resp, content = client.request(url)

    #storing the JSON into the dabases
    content = json.loads(content)

    #Profile model
    #profile = Profile(first_name = content['firstName'], 
    #        last_name = content['lastName'],
    #        user = request.user)
    #profile.save()

    #Education model
    content_educ = content['educations']['values']
    for value in content_educ:
        education = Education(school_name = value['schoolName'],
                user = request.user,
                field_study = value['fieldOfStudy'],
                degree = value['degree'],
                start_date = value['startDate']['year'] ,
                end_date = value['endDate']['year'])
        education.save()

    #Positions model
    content_pos = [content['threeCurrentPositions']['values'],
    content['threePastPositions']['values']]
    for list in content_pos:
        for value in list:
                positions = Positions(title = value['title'],
                        company = value['company']['name'],
                        user = request.user,
                        summary = value['summary'],
                        is_current = value['isCurrent'],
                        start_date_year = value['startDate']['year'],
                        start_date_month = value['startDate']['month'],
                        end_date_year = value['startDate']['year'],
                        end_date_month = value['startDate']['month']) 
                positions.save()

    #Certifications model
    content_crt = content['certifications']['values']
    for value in content_crt:
        certifications = Certifications(name = value['name'],
                user = request.user)
        certifications.save()
    

    return HttpResponseRedirect('/admin/')

