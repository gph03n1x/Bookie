from django.db import models
from django.contrib.auth.models import User

REVIEW = (
    ("positive", "Positive"),
    ("negative", "Negative"),
)


class Book(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    issued_date = models.DateField()
    description = models.TextField(default="")
    hidden = models.BooleanField(default=False)
    price = models.FloatField(default=0.0)
    ISBN = models.CharField(max_length=256)
    pages = models.IntegerField(default=0)
    positive_votes = models.IntegerField(default=0)
    negative_votes = models.IntegerField(default=0)
    cover_image = models.ImageField()




class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    comment = models.TextField(default="")
    would_recommend = models.BooleanField(default=True)

    class Meta:
        unique_together = (("user", "book"),)


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    payed_order = models.BooleanField(default=False)
