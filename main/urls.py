from django.urls import path
from main import views
urlpatterns = [
    path('',views.index,name='index'),
    path('project',views.project,name='project'),
    path('language',views.language,name='language'),
]