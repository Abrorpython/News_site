from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return "Категория %s - %s" % (self.id, self.name)


class News(models.Model):
    title = models.TextField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to='news_image', null=True)
    text = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.id, self.title)
