from django.urls import path
# Using this to import apiOverview
from . import views

# Creating url path for each view
urlpatterns = [
	# Create path for 'apiOverview' from 'views.py'
	path('', views.apiOverview, name="api-overview"),

	# Paths for other tasks views
	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),
	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),

]
