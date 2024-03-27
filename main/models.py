from django.db import models

# Create your models here.
class ingredient(models.Model):
  name = models.CharField(max_length=20, help_text="Enter ingredient", blank=False)
  quantity = models.DecimalField(max_digits=5, decimal_places=1)
  
  def __str__(self):
    return self.name + " ("+ str(self.quantity)"+)"
  
class  recipe(models.Model):
  title = models.CharField(max_length=30, help_text='Enter the recipe title')
  description = models.TextField(help_text='Write a brief about the recipe',blank=True)
  date = models.DateField(auto_now_add=True)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #this is who made it
  image = models.ImageField(upload_to= 'images/', blank=True)
  ingredients = models.ManyToManyField