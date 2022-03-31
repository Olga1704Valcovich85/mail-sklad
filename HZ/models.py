from django.db import models

# Create your models here.
class Autorization(models.Model):
    login = models.CharField(max_length = 30)
    password = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return str(self.login)

class user1(models.Model):
    user_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=15, null=True)
    otdel = models.CharField(max_length = 50, null=True)
    mail = models.EmailField()
    def __str__(self):
        return  str(self.last_name)+' ' + str(self.otdel)

class own_production(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'мужчина'),
        (FEMALE, 'женщина'),
    ]
    name = models.CharField(max_length = 30, blank = False)
    articul = models.IntegerField()
    kod = models.CharField(max_length = 30, blank = False)
    kolichestvo = models.IntegerField()
    color = models.CharField(max_length = 30, blank = False)
    size = models.IntegerField()
    gender = models.CharField(max_length = 1, choices=GENDERS, default=FEMALE)
    user_name = models.OneToOneField(user1, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.name)+ " " + str(self.articul)+ " " )

class Articl(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full = models.TextField('Статья')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return f'Раздел: {self.title}'














