from django.urls import path
from . import views
# from home.views import extbuilding



urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('system_overview/', views.system_overview, name='system_overview'),
     path('system_overview/ground-floor/', views.ground_floor, name='ground_floor'),
        path('system_overview/ground-floor/gf_pnumatical', views.gf_pnumatical, name='gf_pnumatical'),
        path('system_overview/ground-floor/gf_hydraulic', views.gf_hydraulic, name='gf_hydraulic'),
        path('system_overview/ground-floor/gf_cooling', views.gf_cooling, name='gf_cooling'),
        path('system_overview/ground-floor/gf_maintenance', views.gf_maintenance, name='gf_maintenance'),

     path('system_overview/7m/', views.seven_m, name='7m'),
        path('system_overview/7m/7m_system/', views.seven_system, name='7m_system'),
        path('system_overview/7m/7m_maintenance/', views.seven_maintenance, name='7m_maintenance'),
        
     path('system_overview/11m/', views.eleven_m, name='11m'),
        path('system_overview/11m/11m_system/', views.eleven_system, name='11m_system'),
        path('system_overview/11m/11m_maintenance/', views.eleven_maintenance, name='11m_maintenance'),

     path('system_overview/dome/', views.dome, name='dome'),
        path('system_overview/dome/dome_system/', views.dome_system, name='dome_system'),
        path('system_overview/dome/dome_maintenance/', views.dome_maintenance, name='dome_maintenance'),

     path('system_overview/ext_building/', views.ext_building, name='extbuilding'),
        path('system_overview/ext_building/building_system', views.building_system, name='building_system'),
        path('system_overview/ext_building/building_maintenance', views.building_maintenance, name='building_maintenance'),


    path('maintenance_schedule/', views.maintenance_schedule, name='maintenance_schedule'),
    path('maintenance_data_entry/', views.maintenance_data_entry, name='maintenance_data_entry'),
    path('help_support/', views.help_support, name='help_support')
]
