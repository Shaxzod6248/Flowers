from django.db import models
from django.core.exceptions import ValidationError
import os
from users.models import Profile


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Flower(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='flower_images', null=True)
    title = models.CharField(max_length=300, null=True)
    describe = models.TextField(blank=True, null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


class Order_detail(models.Model):
    product = models.ForeignKey(Flower, on_delete=models.CASCADE)
    total = models.IntegerField()
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.product