from curses import meta
from rest_framework import serializers
from toys.models import Toy,Bio

# class ToySerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     name= serializers.CharField(max_length=150)
#     description = serializers.CharField(max_length=250)
#     release_date = serializers.BooleanField(required=False)

#     def create(self,validated_data):
#         return Toy.objects.create(**validated_data)

#     def update(self,instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.releasedate = validated_data.get('release_date',instance.release_date)
#         instance.toy_category = validated_data.get('toy_category',instance.toy_category)
#         instance.was_included_in_home = validated_data.get('was_included_in_home',instance.was_included_in_home)
#         instance.save()
#         return instance

#The above method is old and traditional that we have to write redundancy i.e repat information of model so we will 
# Now, we will take advantage of model serializers to simplify code and to avoid repeating
# information that is already included in the model. We will create a new version of the
# existing ToySerializer class that will inherit from the
# rest_framework.serializers.ModelSerializer superclass instead of inheriting from
# the rest_framework.serializers.ModelSerializer superclass.
# The ModelSerializer class automatically populates a set of default fields and default
# validators by retrieving metadata from the related model class that we must specify. In
# addition, the ModelSerializer class provides default implementations for the create
# and update methods. In this case, we will take advantage of these default implementations
# because they will be suitable to provide our necessary create and update methods.

class  ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields=(
            'id',
            'name',
            'description',
            'release_date',
            "toy_category",
            "was_included_in_home",
        )
class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields=('name','hobby')