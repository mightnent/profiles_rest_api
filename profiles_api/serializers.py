from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """serialize a user profile obj"""
    class Meta:
        model = models.UserProfile
        #fields is to create access for our model
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'} #this will make the typing of pw into astricks
            }
        }

    #this is to override the default create, so password is hashed
    def create(self,validated_data):
        """create a new user with pw hash"""
        #so i'm assuming objects refer to UPM in userprofiles
        user = models.UserProfile.UPM.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user

    #this is to override the default update, so password is hashed
    def update(self,instance,validated_data):
        if 'password' in validated_data:
            #pop it out and hash it
            password = validated_data.pop('password')
            instance.set_password(password)

        #if you dont super, then it becomes recurssion. lol
        return super().update(instance,validated_data)

class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}
        #id and created on is auto read only