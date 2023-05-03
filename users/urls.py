from django.urls import path, include

from users.views import login, registration

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),      # .../users/login/
    path('registration/', registration, name='registration'),
]