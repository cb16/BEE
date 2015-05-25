from django.db import models
from bee.settings import MEDIA_ROOT

# Create your models here.
GENDER_CHOICES = (
	('F', 'Feminino'),
	('M', 'Masculino'),
	('A', 'Anônimo'),
)

SEXUAL_ORIENTATION_CHOICES = (
	('HT', 'Heterossexual'),
	('H', 'Homossexual'),
	('B', 'Bissexual'),
	('T', 'Transexual'),
	('P', 'Pansexual'),
)

class Badge(models.Model):
	name = models.CharField(verbose_name="nome", max_length = 100, unique=True)
	description = models.CharField(verbose_name="descrição", max_length = 300)
	icon = models.ImageField(upload_to = MEDIA_ROOT) #ver width, height e upload to

class Tag(models.Model):
	title = models.CharField(verbose_name = "titulo", max_length=30, unique=True)

class Person(models.Model):
	name = models.CharField(verbose_name = "nome", max_length = 100)
	nickname = models.CharField(verbose_name = "nome visível", max_length = 100, unique = True)
	birth_date = models.DateField(verbose_name = "data de nascimento")
	gender = models.CharField(verbose_name = "gênero", max_length=1, choices = GENDER_CHOICES, default = 'A')
	sexuality = models.CharField(verbose_name = "opção sexual", max_length=2, choices=SEXUAL_ORIENTATION_CHOICES)
	picture = models.ImageField() #ver width, height e upload to
	email = models.EmailField(unique = True)
	anonymous = models.BooleanField(default = True)
	badges = models.ManyToManyField(Badge, related_name = "have_author")

class Post(models.Model):
	text = models.TextField(verbose_name = "texto", max_length=1000)
	likes = models.PositiveIntegerField(verbose_name="curtidas")
	tags = models.ManyToManyField(Tag)
	date_hour = models.DateTimeField(verbose_name = "data e hora de criação")
	author = models.ForeignKey(Person, related_name = "have_author_post")
	post_likes = models.ManyToManyField(Person, related_name = "likes_person_post")
	post_reports = models.ManyToManyField(Person, related_name = "reports_person_post")

class Comment(models.Model):
	text = models.TextField(verbose_name = "comentário", max_length=400)
	author = models.ForeignKey(Person, related_name = "have_author_comment")
	post = models.ForeignKey(Post, related_name = "have_post")
	comment_likes = models.ManyToManyField(Person, related_name = "likes_person_comment")
	comment_reports = models.ManyToManyField(Person, related_name = "reports_person_comment")
	date_hour = models.DateTimeField(verbose_name="data e hora da criação")
	