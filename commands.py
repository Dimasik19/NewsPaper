# Создать двух пользователей (с помощью метода User.objects.create_user).
from django.contrib.auth.models import User
>>> user1 = User.objects.create_user("Bonny", "bonny@gmail.com", "bonnypassword")
>>> user1.save()

>>> user2 = User.objects.create_user("Clide", "clide@gmail.com", "clidepassword")
>>> user2.save()

# Создать два объекта модели Author, связанные с пользователями.
>>> Author.object.create (user = user1)
>>> Author.object.create (user = user2)

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



# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
