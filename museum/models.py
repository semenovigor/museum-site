from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Purpose(models.Model):
    namePurpose = models.CharField("Название Цели", max_length=100)

    def __str__(self):
        return self.namePurpose


class Event(models.Model):
    title = models.CharField("Название организации", max_length=200, default="")
    start_time = models.DateTimeField("Начало экскурсии")
    end_time = models.DateTimeField("Конец экскурсии")
    userscount = models.IntegerField("Количество участников")
    purpose = models.ForeignKey(Purpose, null=True, on_delete=models.SET_NULL)
    description = models.TextField(default="somthing")
    FIO = models.TextField("ФИО ответственного", default="")
    phone = models.IntegerField("контактный телефон", default="")
    mail = models.EmailField("Электронная почта", default="")

    def __str__(self):
        return self.title


class Category(models.Model):
    nameCategory = models.CharField("Название категории", max_length=100)

    def __str__(self):
        return self.nameCategory


class NewManager(models.Manager):
    def Excursions(self):
        return self.filter(category_id=1).order_by('-date')[:4]

    def Graduates(self):
        return self.filter(category_id=2).order_by('-date')[:4]

    def Maecenases(self):
        return self.filter(category_id=3).order_by('-date')[:4]

    def Veterans(self):
        return self.filter(category_id=4).order_by('-date')[:4]

    def NewsSortByDate(self):
        return self.order_by('-date')

    def ExcursionsCategory(self):
        return self.filter(category_id=1).order_by('-date')

    def GraduatesCategory(self):
        return self.filter(category_id=2).order_by('-date')

    def VeteransCategory(self):
        return self.filter(category_id=3).order_by('-date')

    def MaecenasesCategory(self):
        return self.filter(category_id=4).order_by('-date')

    def MuseumNal(self):
        return self.filter(category_id=5).order_by('-date')


class Guest(models.Model):
    titleFIO = models.TextField("Имя Фамилия Отчество почётного гостя")
    imageGuest = models.ImageField("Фото почётного гостя", upload_to='media/%Y/%m/%d/')
    descriptionText = RichTextField("Отзыв Гостя", default=" ")
    descriptionGuest = models.ImageField("Отзыв гостя", upload_to='media/%Y/%m/%d/')
    dateReview = models.DateField("Дата Отзыва")

    def __str__(self):
        return self.titleFIO

    class Meta:
        verbose_name = "Почётный гость"
        verbose_name_plural = "Почётные гости"


class New(models.Model):
    objects = NewManager()
    title = models.TextField("Название новости")
    text = RichTextField("Описание Новости")
    date = models.DateTimeField("Дата Публикации")
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class NewImage(models.Model):
    image = models.ImageField("Картинка", upload_to='media/%Y/%m/%d/', blank=True)
    new = models.ForeignKey(New, null=True, on_delete=models.SET_NULL, verbose_name="Новость")

    class Meta:
        verbose_name = "Картинки для новости"
        verbose_name_plural = "Картинки для новости"


class Review(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField()
    text = models.TextField("Текст", max_length=10000)
    date_review = models.DateTimeField("Дата отзыва", auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Application(models.Model):
    name = models.CharField("Организация", max_length=100)
    phone = models.IntegerField("Телефон")
    email = models.EmailField()
    count_users = models.IntegerField("Количество Участников")
    date_application = models.DateField("Дата экскурсии")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class Watermark(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    image = models.ImageField(upload_to='watermarks', verbose_name="image")
    is_active = models.BooleanField(default=True, blank=True, verbose_name="is active")

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
