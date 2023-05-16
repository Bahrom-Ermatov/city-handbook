from django.urls import path, include
from rest_framework import routers
from city_handbook_app.views import EstablishmentViewSet, EstablishmentByCategory, EstablishmentByCity, EstablishSearchByAddress, EstablishSearchByName

router = routers.DefaultRouter()
router.register("establishments", EstablishmentViewSet, "establishments")

urlpatterns = [
    path('', include(router.urls)),
    path('by_category/<int:category_id>', EstablishmentByCategory.as_view()),
    path('by_city/<int:city_id>', EstablishmentByCity.as_view()),    
    path('search_by_address/<str:address>/', EstablishSearchByAddress.as_view()),
    path('search_by_name/<str:name>/', EstablishSearchByName.as_view()),
]


