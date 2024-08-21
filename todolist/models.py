from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField("заголовок",max_length=200)
    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "задачи"
