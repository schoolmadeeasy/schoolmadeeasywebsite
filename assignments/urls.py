from django.urls import path
from . import views

urlpatterns = [
    path('view/<int:pk>/', views.AssignmentView.as_view(), name='view_assignment'),

    path('view/all/', views.AllAssignmentsView.as_view(), name='all_assignments'),

    path('search/', views.SearchView.as_view(), name='search'),
]