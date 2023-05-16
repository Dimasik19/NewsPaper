from django.db import models

class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    rating = models.IntegerField(default = 0)
    
    def update_rating(self):
        rating_post_author = self.Post_set.all().aggregate(Sum('rating'))
        rating_comm_author = self.Comment_set.all().aggregate(Sum('rating'))
        rating_comm_post_author = self.Post_set.Comment_set.all().aggregate(Sum('rating'))
        
        self.rating = (rating_post_author *3 + rating_comm_author + rating_comm_post_author)
        self.save()

class Post(models.Model):
    post = models.OneToOneField (Author, on_delete = models.CASCADE, primary_key = True)
    post_cat = models.ManyToManyField(Category, through = 'PostCategory')
    
    type_is_news = models.BooleanField (default = False)
    date_of_publ = model.DateTimeField (auto_now_add = True)
    title = models.CharField (max_length = 64)
    text = model.TextField ()
    rating = models.IntegerField()
    
    def like(self):
        self.rating +=1
        self.save()
        
    def dislike(self):
        self.rating -=1
        self.save()
        
    def preview(self):
        return self.text([0:124] + '...'])

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
    comm_post = models.ForeignKey(Post, on_delete = models.CASCADE)
    comm_user = models.ForeignKey(User, on_delete = models.SET_DEFAULT, default = 'удаленный пользователь')
    
    text = model.TextField ()
    date_of_publ = model.DateTimeField (auto_now_add = True)
    rating = models.IntegerField()
    
    def like(self):
        self.rating +=1
        self.save()
        
    def dislike(self):
        self.rating -=1
        self.save()
