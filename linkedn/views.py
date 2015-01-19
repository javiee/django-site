import oauth2 as oauth
import urlparse   
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Import project
from linkedn.models import Profile
print settings.LINKEDN_KEY, settings.LINKEDN_SECRET
consumer = oauth.Consumer(settings.LINKEDN_KEY, settings.LINKEDN_SECRET)
client = oauth.Client(consumer)

request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
authorize_url = 'https://api.linkedin.com/uas/oauth/authorize'

def index(request):
    return HttpResponse("LINKEDN index page")

def linkedn_login(request):
    #request token from linkdn
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
        print content
        raise Exception("Invalid response")
    access_token = dict(urlparse.parse_qsl(content))
# is it neccarry this line?
    context = {'access_token': access_toke}
    return render(request, 'linkedn/index.html',context

"""
    try:
        user = User.objects.get(pk=access_token['screen_name'])
    except User.DoesNotExist:
        user = User.objects.create_user(access_token['screen_name'], access_token['oauth_token_secret'])
        profile = Profile()
        profile.user = user 
        profile.auth_token = access_token['oauth_token']
        profile.auth_sercret = access_token['oauth_token_secret']
        profile.save()

        user = authenticate(username=access_token['screen_name'],
        password=access_token['oauth_token_secret'])
        login(request, user)
"""   





