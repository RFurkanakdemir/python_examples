from rest_framework import serializers
from todotask.models import Task, Categorie
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class CatSerializer(serializers.ModelSerializer):
    
    
    # task_user = serializers.CharField()
    # if User.username != task_user:
    #     raise serializers.ValidationError({"password": "Password fields didn't match."})
    class Meta:
        model= Categorie
        fields='__all__'
        


class TaskSerializer(serializers.ModelSerializer):
    
    
    # task_user = serializers.CharField()
    # if User.username != task_user:
    #     raise serializers.ValidationError({"password": "Password fields didn't match."})
    class Meta:
        model=Task
        # fields='__all__'
        exclude = ['task_user']


   


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['id',"username","is_staff","is_active"]

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True}
        # }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        # cat=Categorie.objects.create(
        #     cat_title = 'default Cat'
        # )
        # cat.save()
        
        user.set_password(validated_data['password'])
        user.save()

        return user