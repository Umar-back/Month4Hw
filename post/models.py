from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=333)

class Product(models.Model):
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(
        'post.Category',
        blank=True,
        related_name='products'
    )
    product_reviews = models.ManyToManyField(
        'post.Review',
        blank=True,
        related_name='product_reviews'
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

class Review(models.Model):
    product = models.ForeignKey(
        'post.Product',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review #{self.id} for {self.product.title}"
