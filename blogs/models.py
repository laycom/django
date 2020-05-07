from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    avatar = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Blog(models.Model):
    title = models.CharField(max_length=200)
    blog_text = models.TextField()
    pub_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title



