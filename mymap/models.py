from django.db import models
from django.conf import settings # setting에 있는 값을 가져올 수 있다.
# Create your models here.

class Stamp(models.Model):
    oname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.oname
    
class Oreum(models.Model):
    oname = models.CharField(max_length=300)
    oplace = models.CharField(max_length=300)
    ocontent = models.CharField(max_length=300, null=True)
    ourl = models.CharField(max_length=300)
    oparking = models.CharField(max_length=10, null=True)
    otoilet = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.oname