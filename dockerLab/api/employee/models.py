from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Employee(models.Model):
	def save(self, *args, **kwargs):
		super(Employee, self).save(*args, **kwargs)

	owner = models.ForeignKey('auth.User', related_name='employee')
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100, blank=True, default='')
	email = models.CharField(max_length=100, blank=True, default='')
	position = models.TextField()
	class Meta:
		ordering = ('created',)
