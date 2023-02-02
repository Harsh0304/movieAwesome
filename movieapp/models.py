from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
#create categories
class categories(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    def __str__(self):
        return self.title
#create Movie models

class Movies(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    added_date=models.DateTimeField()
    rating=models.CharField(max_length=10,default="")
    download=models.URLField(max_length=200,default="")
    cat=models.ForeignKey(categories,on_delete=models.CASCADE)

    def __str__(self):

        return self.title
