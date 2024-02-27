from django.db import models

# Create your models here.
class Candidates(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='candidates/')
    job_title = models.CharField(max_length=50)
    


    def __str__(self):
        return self.name


