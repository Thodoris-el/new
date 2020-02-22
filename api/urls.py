from django.urls import include, path
from rest_framework import routers
from api import views

#router = routers.DefaultRouter()
#router.register(r'users',views.UserViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('api/users/',views.user_list),
    path('api/users/<int:pk>/',views.user_detail),
    path('api/actualtotalloads/',views.actualtotalload_list),
    path('api/aggregatedgenerationpertypes/',views.aggregatedgenerationpertype_list),


    path('api/actualtotalloads/<str:areaname>/<str:resolutioncode>/<str:date>/<str:info>/',views.actual),
    #path('api/actualtotalloads/<str:areaname>/<str:resolutioncode>/<int:year>/<int:month>/<str:format>/',views.actualtotalload_detail1),
    #path('api/actualtotalloads/<str:areaname>/<str:resolutioncode>/<int:year>/<str:format',views.actualtotalload_detail),

    path('api/import',views.upload),

    path('api/aggregatedgenerationpertypes/<str:areaname>/<str:productiontype>/<str:resolutioncode>/<str:date>/<str:info>/',views.aggre),
    #path('api/aggregatedgenerationpertypes/<str:areaname>/<str:productiontype>/<str:resolutioncode>/<int:year>/<int:month>/',views.aggregatedgenerationpertype_detail1),
    #path('api/aggregatedgenerationpertypes/<str:areaname>/<str:productiontype>/<str:resolutioncode>/<int:year>/',views.aggregatedgenerationpertype_detail),

    path('api/dayaheadtotalloadforecast/<str:areaname>/<str:resolutioncode>/<str:date>/<str:info>/',views.dayahead),
    #path('api/dayaheadtotalloadforecast/<str:areaname>/<str:resolutioncode>/<int:year>/<int:month>/',views.dayaheadtotalloadforecast_detail1),
    #path('api/dayaheadtotalloadforecast/<str:areaname>/<str:resolutioncode>/<int:year>/',views.dayaheadtotalloadforecast_detail),

    path('api/actualvsforecast/<str:areaname>/<str:resolutioncode>/<str:date>/<str:info>/',views.actualvs),
    #path('api/actualvsforecast/<str:areaname>/<str:resolutioncode>/<int:year>/<int:month>/',views.actualvsforecast_detail1),
    #path('api/actualvsforecast/<str:areaname>/<str:resolutioncode>/<int:year>/',views.actualvsforecast_detail),

    path('api/healthcheck',views.process_request)
]
