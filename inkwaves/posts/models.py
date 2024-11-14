from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Title', max_length=50, default='Untitled')
    announcement = models.CharField('Announcement', max_length=250, default='')
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/posts/{self.id}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
