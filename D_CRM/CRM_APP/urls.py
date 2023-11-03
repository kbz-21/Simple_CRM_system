
from django.urls import path
from . import views

urlpatterns = [
      path('', views.landing_page_view, name='landing'),  
      path('home/', views.home, name='home'),
      
      path('login/', views.login_user, name='login'),
      path('import/',views.importExcel, name='push_excel'),
      path('logout/',views.logout_user, name='logout'),
      path('register/',views.register_user, name='register'),
      path('record/<int:pk>',views.customer_record, name='record'),
      path('add_record/',views.add_record, name='add_record'),
      path('update_record/<int:pk>',views.update_request, name='update_record'),
      path('export_excel', views.export_excel, name="export-excel"),
    #   path('searchStudent/',views.searchRecord, name='searchStudent'),
      # path('home/', views.searchRecord, name='home'),

]
