from rest_framework import serializers
from city_handbook_app.models import Establishment, EstCategory, City

class EstablishmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Establishment
        fields = "__all__"

class EstCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = EstCategory
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = "__all__"

class EstabRetrieveSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source="category.name")
    city_name = serializers.CharField(source="city.name")
    class Meta:
        model = Establishment
        fields = ("name", "description", "address", "contacts", "category_name", "city_name")




