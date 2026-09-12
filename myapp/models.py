from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    b_date = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    author =models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.title
    

    
    
    
    

