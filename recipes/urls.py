from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.prihlaseni, name="prihlaseni"),
    path('register/', views.registrace, name="registrace"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),

    path('novy/', views.recipe_add, name="recipe_add"),
    path('details/', views.recipe_list, name="recipe_list"),
    path('recipe/<int:pk>', views.details, name="details"),

    path('addcat/', views.add_cat, name="add_cat"),
    path('catlist/', views.cat_list, name="cat_list"),
    path('catdetails/<int:pk>/', views.cat_details, name="cat_details"),
]
