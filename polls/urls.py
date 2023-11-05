from django.urls import path

from . import views

app_name = 'polls' # this is the namespace for the app
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # "" is the root path, "index" is the name of the view
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
]