from django.db import models

class Product(models.Model):
    # ... другие поля модели ...
    photo = models.ImageField(upload_to='product_photos/')
