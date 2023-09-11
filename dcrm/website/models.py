from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.username}'

