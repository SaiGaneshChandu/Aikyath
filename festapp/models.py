from django.db import models

class LoginRecord(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name