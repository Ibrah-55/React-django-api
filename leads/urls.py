from django.urls import path, include
from. import views
urlpatterns = [
    path('api/lead/', views.LeadListCreate.as_view())
]
