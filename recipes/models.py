from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    Recipe_Author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Recipe_Title = models.CharField(max_length=60)
    Recipe_Ingredients = models.TextField()
    Recipe_Description = models.TextField()
    Recipe_Info = models.TextField()
    Recipe_Cat = models.ForeignKey('recipes.Cat', on_delete=models.CASCADE)
    Recipe_Img = models.ImageField(upload_to='../media', blank=True)
    Recipe_Date = models.DateTimeField(default=timezone.now)
    Recipe_note = models.TextField(blank=True)

    def __str__(self):
        return self.Recipe_Title


class Cat(models.Model):
    Cat_Name = models.CharField(max_length=60, unique=True)
    Cat_Description = models.TextField(blank=True)

    def __str__(self):
        return self.Cat_Name


class Prispevek(models.Model):
    tvurce = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nazev = models.CharField(max_length=200)
    text = models.TextField()
    datum_vytvoreni = models.DateTimeField(
            default=timezone.now)
    datum_publikace = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.datum_publikace = timezone.now()
        self.save()

    def __str__(self):
        return self.nazev
