"""
URL configuration for giro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from album import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('player',views.PlayerListView.as_view(), name='player-list'),
    path('player/<int:pk>/detail/', views.PlayerDetailView.as_view(), name='player-detail'),
    path('team',views.TeamListView.as_view(), name='team-list'),
    path('team/<int:pk>/detail/', views.TeamDetailView.as_view(), name='team-detail'),

     # Update
    path('player/<int:pk>/update/',views.PlayerUpdate.as_view(),name='player-update'), 
    #Create
    path('player/create/', views.PlayerCreate.as_view(), name='player-create'),
    #Delete
    path('player/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player-delete'),

    # Update
    path('team/<int:pk>/update/',views.TeamUpdate.as_view(),name='team-update'), 
    #Create
    path('team/create/', views.TeamCreate.as_view(), name='team-create'),
    #Delete
    path('team/<int:pk>/delete/', views.TeamDelete.as_view(), name='team-delete'),
]
