# This view allows users of our API to see a list of all of the url routes/patterns


from django.shortcuts import render
from django.http import JsonResponse

# From documentation tutorial
from rest_framework.decorators import api_view
# Allows us to use the 'Response' decorator/method per the docs
# Decorator is used from documentation because we are using function based views at this time. The decorator created an API view.
# This will give our view access to the methods that DRF gives us
from rest_framework.response import Response
# Importing serializer from 'serializers.py'
from .serializers import TaskSerializer

from .models import Task


# Each view is passed thru files 'urls.py - api' > 'urls.py - appUpdo'


# View that returns a response that displays api url routes for api user reference
# Here is the decorator from the docs, using only 'GET' method to keep this page read-only
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		# List of all of our views for the api
		'List':'task-list/',
		'Detail View':'task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	# 'Response' returns a 'DRF' type response (replacing 'JsonResponse')
	return Response(api_urls)

# List view of all tasks
# Query DB, serialize data and return it in api response
@api_view(['GET'])
def taskList(request):
	# Query 'Task' model to retrieve all task objects
	tasks = Task.objects.all()
	# Set specific serializer to be used and pass in all task objects
	# 'many=True' will change to 'many=Fasle' at a later time so that, in the future, we only serialize one task object at a time.
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

# Detailed view of individual tasks
@api_view(['GET'])
def taskDetail(request, pk):
	# Retrieve one task with '.get'; pass in pk (the id of whichever task we ask for)
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
	# Models forms usually use something like 'request.post', but Django allows us to us '.data' because this is an api view (using the decorator)
	# 'request.data' sends us a Json object as per the docs
	serializer = TaskSerializer(data=request.data)

	# Save to DB like you would save any form
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item successfully deleted!')
