from django.db import models


class Publishings(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Publishings'
        verbose_name_plural = 'Publishings'


class Authors(models.Model):
    name = models.CharField(max_length=250)
    surename = models.CharField(max_length=250)
    fathername = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True)
    birthday = models.DateField()

    def __str__(self):
        return f'{self.name} {self.surename}'
    
    class Meta:
        verbose_name = 'Authors'
        verbose_name_plural = 'Authors'
        ordering = ['name']


class Books(models.Model):
    name = models.CharField(max_length=250)
    write_date = models.DateField()
    description = models.CharField(max_length=4000)
    pages = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='books/%y/%m/%d', null=True, blank=True)
    author_relative = models.ForeignKey(Authors, on_delete=models.PROTECT, verbose_name='author', null=True)
    publishing_relative = models.ForeignKey(Publishings, on_delete=models.PROTECT, verbose_name='publishing', null=True, blank=True)

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
    adress = models.CharField(max_length=1000)
    phone = models.CharField(max_length=16)
    assortiment = models.ManyToManyField(Books, related_name='Assortiment_of_books', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
        ordering = ['name']