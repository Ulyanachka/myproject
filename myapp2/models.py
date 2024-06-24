# from django.db import models


# class Client(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     address = models.TextField()
#     registration_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField()
#     added_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Order(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     order_date = models.DateField(auto_now_add=True)

#     def calculate_total_amount(self):
#         total = sum(product.price *
#                     product.quantity for product in self.products.all())
#         self.total_amount = total
#         self.save()

#     def __str__(self):
#         return f"Order {self.id} by {self.client.name}"

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return f'Title is {self.title}'
    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'