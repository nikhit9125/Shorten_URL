from django.db import models

class URL(models.Model):
    original_url=models.URLField(unique=True)

    short_url=models.CharField(max_length=10,unique=True)

    created_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.original_url
    