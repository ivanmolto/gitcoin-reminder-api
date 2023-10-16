from django.contrib.auth.models import User
from rest_framework import serializers
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Event
        fields = ['id', 'owner', 'event_name', 'cta_text',
                  'bot_name',
                  'event_date']


class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Event.objects.all()
                                                )

    class Meta:
        model = User
        fields = ['id', 'username', 'events']
