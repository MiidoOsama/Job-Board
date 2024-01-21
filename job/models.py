from django.db import models
from django.utils.text import slugify

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),

)
def image_upload (instance , filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)



class Job (models.Model):
    title = models.CharField(max_length=50)
    #location
    job_type = models.CharField(max_length=50 , choices = JOB_TYPE)
    content = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default = 0)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(null = True , blank =True)
    

    def save(self, *args, **kwargs):
        # Generate a slug from the title if one is not provided
            self.slug = slugify(self.title)

            super().save(*args, **kwargs)

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=25)
    


    def __str__(self):
        return self.name

class Apply(models.Model):
    job = models.ForeignKey(Job , verbose_name=("apply_now"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=1000)





    def __str__(self):
        return self.name



