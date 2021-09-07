from django.urls import path
from . import views


urlpatterns = [

    path('login_user', views.login_user, name='login_user'),
    path('', views.login_user, name='login_user'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    # path('', views.taskAdd, name='task'),
    path('task', views.taskAdd, name='task'),
    path('list/', views.taskList, name='list'),
    path('<int:id>/', views.taskUpdate, name='update'),
    path('delete/<int:id>', views.taskDelete, name='delete')
]
