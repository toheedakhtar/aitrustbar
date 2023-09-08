from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Score(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=50, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])  # The default score is 50

    def increment(self, user):
        if self.score >= 100:
            self.score = 100
            self.voter = user
            self.save()
        else:
            # self.voter = self.voter
            self.score += 1
            self.voter = user
            self.save() 

    def decrement(self, user):
        if self.score <= 0:
            self.score = 0
            self.voter = user
            self.save()
        else:
            # self.voter = self.voter
            self.score -= 1
            self.voter = user
            self.save() 


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    slug = models.CharField(max_length=130)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 