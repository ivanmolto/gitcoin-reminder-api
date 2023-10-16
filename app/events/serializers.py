from django.contrib.auth.models import User
from rest_framework import serializers
from events.models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Event
        fields = ['url', 'id', 'owner', 'event_name', 'cta_text',
                  'bot_name', 'event_date']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(many=True,
                                                 view_name='event-detail',
                                                 read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'events']
