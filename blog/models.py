from django.db import models

# Create your models here.

class Category(models.Model):
        CATEGORY_CHOICES = (
                ('TECH', 'Technology'),
                ('SPORTS','Sports'),
                ('ENTERTAINMENT', 'Entertainment'),
                ('TRAVELLIFESTYLE', 'Travel,Lifestyle'),
                ('FOOD', 'Food & Tasty'),
                # Add more choices as needed
            )
        name = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

        def __str__(self):
            return self.name


class BlogList(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=50)
    content =  models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.title


