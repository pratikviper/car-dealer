from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from payment.views import payment_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
    # path('socialaccounts/', include('allauth.urls')),
    path('contacts/', include('contacts.urls')),
    path('payment/', payment_view, name='payment_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
