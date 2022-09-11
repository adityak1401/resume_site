from django.db import models

# Create your models here.
class Personal(models.Model):
    name = models.CharField(default = 'Aditya Kanodia', max_length = 20 )
    position = models.CharField(default = '', max_length = 25)
    img = models.ImageField(default = 'images/img.webp', upload_to='images')

    zipcode = models.IntegerField(default= 100000)
    address = models.TextField(default= '')
    phone = models.CharField(max_length = 15, default='')
    email = models.EmailField(default='adityakanodia08@gmail.com')

    github = models.URLField(default = '')
    linkedin = models.URLField(default = '')
    twitter = models.URLField(default = '')

    def __str__(self):
        return self.name