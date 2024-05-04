from django.urls import path, include
from . import views

urlpatterns = [

    #path('', include(router.urls)),
    path('<int:page>/',views.index, name = 'home'),
    path("",views.index, name = 'home'),
    path("create",views.create_todo, name = 'create-todo'),
    path('todo/<id>/', views.todo_detail, name='todo'),
    path('todo_delete/<id>/', views.todo_delete, name='todo-delete'),
    path('todo_edit/<id>/', views.todo_edit, name='todo-edit'),

    ]

    # Les filles d'Obala avec la malbouche, celles d'Okola avec la bagarre et enfin celles de Monatelé avec le kongossa. Ce sont les meilleures vraiment
    # onanadonald@yahoo.com


    