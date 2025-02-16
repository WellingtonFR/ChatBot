from django.shortcuts import render
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView

class CustomGoogleLoginView(OAuth2LoginView):
    adapter_class = GoogleOAuth2Adapter

def google_login_view(request):
    return render(request, "account/login_google.html")
