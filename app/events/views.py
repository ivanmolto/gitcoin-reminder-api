from django.contrib.auth.models import User
from events.models import Event
from events.serializers import EventSerializer, UserSerializer
from rest_framework import generics, permissions
from events.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from datetime import datetime, timedelta


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'events': reverse('event-list', request=request, format=format)
    })


class EventList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Optionally restricts the returned events to a given bot,
        by filtering agains a `bot_name` query parameter in the URL
        """
        queryset = Event.objects.all()
        botname = self.request.query_params.get('botname')
        if botname is not None:
            queryset = queryset.filter(
                event_end_date__gte=datetime.utcnow() + timedelta(minutes=10))
            queryset = queryset.filter(bot_name=botname)
        return queryset


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
