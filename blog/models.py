from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.



class Technology(models.Model):
    name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"



class Portfolio(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        description=models.TextField()
    )

    image = models.ImageField(upload_to='portfolio_images/')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    technologies = models.ManyToManyField(Technology, related_name="portfolios")

    class Meta:
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return self.title
