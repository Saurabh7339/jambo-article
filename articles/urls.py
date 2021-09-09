from django.urls import path
from .import views

app_name='articles'

urlpatterns = [
    path('',views.articles_list,name="articles"),
    path('create',views.article_create,name="create"),
    path('<slug:slug>',views.article_detail,name="detail"),
    path('delete_article/<slug:slug>',views.delete_article,name="delete"),
    path('update_article/<slug:slug>',views.update_article,name="update")

]
