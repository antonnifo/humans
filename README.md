# Humans [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)   

A Reusable Django authentication app for users to register, log in, edit their profile, and change or reset their password

## Installation & Setup
 You can clone the repo and use it as your project starter, or you can set up the human app only.
### Setting Up the Human app. 
Assuming you have a project setup and a virtual environment, follow the steps below. 
1. Install `social-auth-app-django` in your virtual environment.  
```
    pip install social-auth-app-django pillow
```

2. Register the **social-auth-app-django**, **human** & **pillow** app in installed apps.  
```
INSTALLED_APPS = [
                    #...
                    'human',  
                    'social_django',
      ] 
```
3. Configure the following fields in the settings.py according to your project.
```
            LOGIN_REDIRECT_URL = 'dashboard' 
            LOGIN_URL = 'login'
            LOGOUT_URL = 'logout'

            if DEBUG:
                EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
                #You can configure your SMTP server here also.
            else:
              #add your SMTP configuration
               pass


            AUTHENTICATION_BACKENDS = [
                'django.contrib.auth.backends.ModelBackend',
                'human.authentication.EmailAuthBackend',
                'social_core.backends.google.GoogleOAuth2',
                'social_core.backends.twitter.TwitterOAuth',
                'social_core.backends.facebook.FacebookOAuth2',
            ]
            #You don't have to setup the following if you are not setting up Facebook/Twitter/Gmail authentification
            SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'XXX' # Google Consumer Key
            SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'XXX' # Google Consumer Secret


            SOCIAL_AUTH_TWITTER_KEY = 'XXX' # Twitter API Key
            SOCIAL_AUTH_TWITTER_SECRET = 'XXX' # Twitter API Secret


            SOCIAL_AUTH_FACEBOOK_KEY = 'XXX' # Facebook App ID
            SOCIAL_AUTH_FACEBOOK_SECRET = 'XXX' # Facebook App Secret
``` 
4. Open the main urls.py file of your project and include the social_django and humans URL patterns as
   follows:  
   ```
             urlpatterns = [
                path('admin/', admin.site.urls),
                path('account/', include('human.urls')),
                path('social-auth/',
                          include('social_django.urls', namespace='social')),
                ]  
   ```             


5. Run migrations to sync Python Social Auth models and human models with your database.  
```
  python manage.py migrate 
```
## Available urls. 
```
      account/ login/ [name='login']
      account/ logout/ [name='logout']
      account/ password_change/ [name='password_change']
      account/ password_change/done/ [name='password_change_done']
      account/ password_reset/ [name='password_reset']
      account/ password_reset/done/ [name='password_reset_done']
      account/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
      account/ reset/done/ [name='password_reset_complete']
      account/ dashboard/ [name='dashboard']
      account/ register/ [name='register']
      account/ edit/ [name='edit']
      social-auth/^(?P<path>.*)$ 
```
