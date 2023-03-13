from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404, handler400, handler403, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('menu/', include('menu.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('faqs/', include('faqs.urls')),
    path('locations/', include('location.urls')),
    path('contact/', include('contact.urls')),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'burger_bar.views.handler400'
handler403 = 'burger_bar.views.handler403'
handler404 = 'burger_bar.views.handler404'
handler500 = 'burger_bar.views.handler500'
