from django.db import models
from django.contrib.auth.models import User
from rest_framework.views import APIView
# Create your models here.

class SentMail(APIView):
    user_id = models.ForeignKey(User,)