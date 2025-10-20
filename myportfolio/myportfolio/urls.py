from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from portfolio.views import contact_form_submit
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit-contact/', contact_form_submit, name='submit-contact'),
    path('', include('portfolio.urls')),  # ✅ This handles all portfolio routes including homepage
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
