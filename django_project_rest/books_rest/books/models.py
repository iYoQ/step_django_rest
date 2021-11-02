from django.db import models
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save

class AuthorsManager(models.Manager):
    def create_author(self, name, surename, fathername, city, birthday):
        return self.create(name=name.capitalize(), surename=surename.capitalize(), fathername=fathername.capitalize(), city=city.capitalize(), birthday=birthday)


class BooksManager(models.Manager):
    def create_book(self, name, write_date, description, pages, image, author_relative, publishing_relative):
        return self.create(name=name.capitalize(), write_date=write_date, description=description, pages=pages, image=image, author_relative=author_relative, publishing_relative=publishing_relative)



class ShopManager(models.Manager):
    def update_shop(self, name, address, phone, assortiment):
        return self.update(name=name, address=address, phone=phone, assortiment=assortiment)


class Authors(models.Model):
    name = models.CharField(max_length=250)
    surename = models.CharField(max_length=250)
    fathername = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True)
    birthday = models.DateField()

    objects = AuthorsManager()

    def __str__(self):
        return f'{self.name} {self.surename}'
    
    class Meta:
        verbose_name = 'Authors'
        verbose_name_plural = 'Authors'
        ordering = ['name']


class Publishings(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Publishings'
        verbose_name_plural = 'Publishings'


class Books(models.Model):
    name = models.CharField(max_length=250)
    write_date = models.DateField()
    description = models.CharField(max_length=4000)
    pages = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='books/%y/%m/%d', null=True, blank=True)
    author_relative = models.ForeignKey(Authors, on_delete=models.PROTECT, verbose_name='author', null=True)
    publishing_relative = models.ForeignKey(Publishings, on_delete=models.PROTECT, verbose_name='publishing', null=True, blank=True)

    objects = BooksManager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Books'
        verbose_name_plural = 'Books'
        ordering = ['name']


class Review(models.Model):
    nickname = models.CharField(max_length=250)
    review = models.CharField(max_length=3000)
    book_id = models.ForeignKey(Books, on_delete=models.PROTECT, verbose_name='book', null=True)

    def __str__(self):
        return f'{self.nickname}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Review'
        ordering = ['nickname']


class Shop(models.Model):
    name = models.CharField(max_length=250, verbose_name='Name of shop')
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=16)
    assortiment = models.ManyToManyField(Books, related_name='Assortiment_of_books', null=True, blank=True)

    objects = ShopManager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
        ordering = ['name']


class StatData(models.Model):
    save_books = models.IntegerField(verbose_name='Count of books')
    save_date = models.DateField(auto_now_add=True, verbose_name='Date save of stats')
    save_books_name = models.CharField(max_length=1500, verbose_name='List of books for day', blank=True, null=True)

    def __str__(self):
        return f'{self.save_date}'


    class Meta:
        verbose_name = 'Statistic for day'
        verbose_name_plural = 'Statistic for day'


@receiver(pre_save, sender=Books)
def save_book(sender, **kwargs):
    date_now = datetime.now().date()
    queryset = StatData.objects.filter(save_date=date_now)

    if queryset.exists():
        for item in queryset:
            item.save_books += 1
            item.save()
    else:
        StatData.objects.create(save_books=1, save_date=date_now)

@receiver(pre_delete, sender=Books)
def delete_book(sender, **kwargs):
    date_now = datetime.now().date()
    queryset = StatData.objects.filter(save_date=date_now)

    if queryset.exists():
        for item in queryset:
            item.save_books -= 1
            item.save()
    else:
        StatData.objects.create(save_books=-1, save_date=date_now)