from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('',views.home,name='home'),
   path('login/',views.login_user,name='login'),
   path('logout/',views.logout_user,name='logout'),
   path('register/',views.register_user,name='register'),
   path('records/',views.records,name='records'),
   path('records/<int:pk>', views.customer_records, name='record'),
   path('delete/<int:pk>', views.delete, name='delete'),
   path('add_record/',views.add_record,name='add_record'),
   path('update_record/<int:pk>', views.update_record, name='update_record'),
   
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
