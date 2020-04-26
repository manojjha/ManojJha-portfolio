from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.email, name='contacts'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    