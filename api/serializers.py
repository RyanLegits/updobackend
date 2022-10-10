from rest_framework import serializers

# Using '.' because we are already in the same dir as 'models'
from .models import Task

# Arg comes directly from framework, we are serializing a model specifically
class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		# Serialize all fields from Task model
		fields = '__all__'
