from django.db import models

class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    
    rating = models.IntegerField()

class Post(models.Model):
    post = models.OneToOneField (Author, on_delete = models.CASCADE, primary_key = True)
    post_cat = models.ManyToManyField(Category)
    
    type_is_news = models.BooleanField (default = False)
    date_of_publ = model.DateTimeField (auto_now_add = True)
    title = models.CharField (max_length = 64)
    text = model.TextField ()
    rating = models.IntegerField()   
