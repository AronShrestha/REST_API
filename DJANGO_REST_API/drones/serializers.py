from rest_framework import serializers
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition
import drones.views


class DroneCategorySerializers(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
        many=True,
        read_only = True,
        view_name = 'drone-detail'
    )
    class Meta:
        model = DroneCategory
        fields=(
            'url','pk','name','drones'
        )

class DroneSerializers(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(
        queryset = DroneCategory.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Drone
        fields =(
            'url',
            'name',
            'drone_category',
            'manufacturing_date',
            'has_it_completed',
            'inserted_timestamp'
        )

class CompetitionSerializers(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializers()
    class Meta:
        fields =(
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'drone'
        )

class PilotSeriazliers(serializers.HyperlinkedModelSerializer):
    Competition = CompetitionSerializers(many = True, read_only =True)
    gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES)
    gender_description = serializers.CharField(
        source =  'get_gender_display',
        read_olny =True
    )
    class Meta :
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'races_count',
            'inserted_timestamp',
            'competitions'
        )

class PilotCompetitionSerializer(serializers.ModelSerializer):
    pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(),slug_field='name')
    drone = serializers.SlugRelatedField(quryset = Drone.objects.all(),slug_field='name')
    class Meta:
        model = Competition
        fields=(
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'pilot',
            'drone'
        )
