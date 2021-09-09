
from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve
from django.conf.urls import url

app_name='blog'

urlpatterns = [
    path('accounts/',include('accounts.urls')),
    path('articles/',include('articles.urls')),
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('',views.homepage,name='homepage')

]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)