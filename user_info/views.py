# from django.contrib.auth.models import User
from .models import User, UserProfile
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from user_info.serializers import UserSerializer
from user_info.permissions import IsSelfOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly, IsSelfOrReadOnly]

        return super().get_permissions()

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()

            # Check if UserProfile already exists for the user
            if not UserProfile.objects.filter(user=user).exists():
                # Create a UserProfile instance for the new user
                UserProfile.objects.create(user=user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET /api/user/personal-info/ to allow the logged-in user to retrieve their information
    @action(detail=False, methods=['get'], url_path='personal-info')
    def retrieve_self(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

