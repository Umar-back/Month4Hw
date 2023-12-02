from django.db import models

class Hashtag(models.Model):
    title = models.CharField(max_length=333)



class Product(models.Model):
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    hashtag = models.ManyToManyField(
        'post.Hashtag',
        blank=True,
        null=True,
        related_name='products'
    )
    def __str__(self) -> str:
        return f"{self.id} {self.title}"

class Comment(models.Model):
    product = models.ForeignKey(
        'post.Product',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)