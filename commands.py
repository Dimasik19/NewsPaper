# Создать двух пользователей (с помощью метода User.objects.create_user).
from django.contrib.auth.models import User
>>> User.objects.create_user("Bonny", "bonny@gmail.com", "bonnypassword")
>>> User.objects.create_user("Clide", "clide@gmail.com", "clidepassword")

# Создать два объекта модели Author, связанные с пользователями.
>>> Author.object.create (user="Bonny")
>>> Author.object.create (user="Clide")

# Добавить 4 категории в модель Category.
# Я применил ограниченный список в модели Category, если бы создавал объекты, то делал бы это так:
# >>> Category.object.create (cat_name = 'Срочное')
# >>> Category.object.create (cat_name = 'Погода')
# >>> Category.object.create (cat_name = 'Бизнес')
# >>> Category.object.create (cat_name = 'Другое')

# Добавить 2 статьи и 1 новость.
# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
>>> Post.object.create (post_cat = ('BR','WE'), title = "Ураган налетел...", text = "..." )   
>>> Post.object.create (post_cat = 'SO', title = "Школьники собрались...", text = "...")
>>> Post.object.create (post_cat = 'BU', type_is_news = True, title = "Про завод...", text = "...")

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
>>> Comment.object.create (comm_id = post, text = "Комментарий 1")
>>> Comment.object.create (text = "Комментарий 2")
>>> Comment.object.create (text = "Комментарий 3")
>>> Comment.object.create (text = "Комментарий 4")

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
# Обновить рейтинги пользователей.
>>> like(Comment.id[1])
>>> dislike(Comment.id[2])
>>> like(Post.id[0])
>>> dislike(Post.id[1])
>>> like(Post.id[2])
>>> like(Post.id[2])
>>> update_rating ()

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
>>> leader_auth = Author.objects.order_by("rating")
>>> print (leader_auth[0](user, rating))

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
>>> leader_post = Post.objects.order_by("rating")
>>> print (leader_post[0](date_of_publ, Author.user, rating, title) + preview(leader_post[0]))
>>> all_comments = Comments.objects_set.all(leader_post[0])
>>> print (all_comments)
