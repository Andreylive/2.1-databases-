from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    release_date = models.DateField(null=False)
    image = models.ImageField(upload_to='phones')
    lte_exists = models.BooleanField(null=False)
    slug = models.SlugField(max_length = 100)


    def __str__(self):
        return f'{self.name}, {self.price}, {self.price}'
