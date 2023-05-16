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

class Category(models.Model):
    breaking = 'BR'
    weather = 'WE'
    social = 'SO'
    business = 'BU'
    other = 'OT'
    
    TYPES = [
        (breaking, 'Срочное'),
        (weather, 'Погода'),
        (social, 'Общество'),
        (business, 'Бизнес'),
        (other, 'Другое')
    ]
    
    cat_name = models.CharField(choices=TYPES, default = other, unique = True)
    
class PostCategory (models.Model):
    PostCat_id = models.ForeignKey(Post, on_delete = models.CASCADE)
    PostCat_id = models.ForeignKey(Category, on_delete = models.CASCADE)
    
class Comment (models.Model):
    Comm_id = models.ForeignKey(Post, on_delete = models.CASCADE)
    Comm_id = models.ForeignKey(User, on_delete = models.SET_DEFAULT, default = 'удаленный пользователь')
    
    text = model.TextField ()
    date_of_publ = model.DateTimeField (auto_now_add = True)
    rating = models.IntegerField()
