from django.conf.urls import url
from .views import (
					UploadImageAPIView,
					
                    )


urlpatterns = [
    url(r'^upload/$', UploadImageAPIView.as_view(), name="img-api"),
]