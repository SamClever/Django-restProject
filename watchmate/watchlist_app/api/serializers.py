
from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review  # Ensure the correct model is imported

       
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model =Review
        fields  = '__all__'
     
      
class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many= True , read_only = True)
    class Meta:
        model = WatchList  # Specify the model to serialize
        fields = '__all__'  # This includes all fields from the Movie model
        # fields = ['id', 'name', 'description']# This includes only the specified fields from the Movie model
        # exclude = ['name']  # This excludes the specified fields from the Movie model
   
   
   
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model =  StreamPlatform # Specify the model to serialize
        fields = '__all__'
     
   
   
   
   
   
    
    # def get_len_name(self,object):
    #     return len(object.name)
    
    # def create(self, validated_data):
    #  return Movie.objects.create(**validated_data)
 
    # def update(self,instance,validated_data):
    #     # instance.name =validated_data.get('name',instance.name)
    #     instance.name =validated_data.get('name',instance.name)
    #     instance.description= validated_data.get('description',instance.description)
    #     instance.active=validated_data.get('active',instance.active)
    #     instance.save()
    #     return instance
    
    # # validation field level
    
    # # def validate_name(self, value):
    # #     if len(value) < 2:
    # #         raise serializers.ValidationError('Name is too short! Must be at least 2 characters.')
    # #     return value
    