from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = "Ads"

urlpatterns = [
	path("", views.HomeView, name="home"),
    path("form/", views.AdView, name="form"),
    path("<int:ad_id>/", views.AdDetailView, name="addetail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)