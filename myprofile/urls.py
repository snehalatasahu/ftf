from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('my-profile',views.index, name='my-profile')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)