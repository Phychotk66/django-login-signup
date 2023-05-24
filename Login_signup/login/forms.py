from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class Signup(UserCreationForm):
   class Meta:
      model = User
      fields =['username', 'first_name', 'last_name', 'email',]

#Update profile
class EditUserProfileForm(UserChangeForm):
   password = None
   class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email',]
      labels ={'email': 'Email'}

class EditAdminProfileForm(UserChangeForm):
  password = None
  class Meta:
   model = User
   fields =  ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
   labels = {'email': 'Email'}