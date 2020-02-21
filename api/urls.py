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


    path('api/actualtotalloads/<str:areaname>/<str:resolutioncode>/<int:year>/<int:month>/<int:day>/',views.actualtotalload_detail2),
    path('api/actualtotalloads/<str:areaname>/<str:resolutioncode>/<int:year>/<int:month>/',views.actualtotalload_detail1),
    path('api/actualtotalloads/<str:areaname>/<str:resolutioncode>/<int:year>/',views.actualtotalload_detail),

    path('api/import',views.upload),

    path('api/aggregatedgenerationpertypes/<str:areaname>/<str:productiontype>/<str:resolutioncode>/<int:year>/<int:month>/<int:day>/',views.aggregatedgenerationpertype_detail2),
    path('api/aggregatedgenerationpertypes/<str:areaname>/<str:productiontype>/<str:resolutioncode>/<int:year>/<int:month>/',views.aggregatedgenerationpertype_detail1),
    path('api/aggregatedgenerationpertypes/<str:areaname>/<str:productiontype>/<str:resolutioncode>/<int:year>/',views.aggregatedgenerationpertype_detail),

    path('api/dayaheadtotalloadforecast/<str:areaname>/<str:resolutioncode>/<int:year>/<int:month>/<int:day>/',views.dayaheadtotalloadforecast_detail2),
    path('api/dayaheadtotalloadforecast/<str:areaname>/<str:resolutioncode>/<int:year>/<int:month>/',views.dayaheadtotalloadforecast_detail1),
    path('api/dayaheadtotalloadforecast/<str:areaname>/<str:resolutioncode>/<int:year>/',views.dayaheadtotalloadforecast_detail),

    path('api/actualvsforecast/<str:areaname>/<str:resolutioncode>/<int:year>/<int:month>/<int:day>/',views.actualvsforecast_detail2),
    path('api/actualvsforecast/<str:areaname>/<str:resolutioncode>/<int:year>/<int:month>/',views.actualvsforecast_detail1),
    path('api/actualvsforecast/<str:areaname>/<str:resolutioncode>/<int:year>/',views.actualvsforecast_detail),

    path('api/healthcheck',views.process_request)
]
