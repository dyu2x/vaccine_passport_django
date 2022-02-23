from django.urls import path
from passports import views as passports_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', passports_views.index, name='home'),
    path('', passports_views.index.as_view(), name='home'),
    path('api/passports/', passports_views.passport_list),
    path('api/passports/<int:pk>/', passports_views.passport_detail),
    path('api/passports/published/', passports_views.passport_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
