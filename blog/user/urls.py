from django.urls import path
from . import views
urlpatterns=[ 
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('single/<int:id>/',views.single, name='single'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('register/',views.register, name='register')
]