from django.db import models

# 'Task' model to be serialized into JSON data
class Task(models.Model):
	# Title of a todo item
	title = models.CharField(max_length=200)
	# Todo is complete or incomplete
	completed = models.BooleanField(default=False, blank=True, null=True)

	def __str__(self):
		return self.title
