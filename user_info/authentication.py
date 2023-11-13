from django.utils.timezone import now
from datetime import timedelta
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add extra responses here
        data['username'] = self.user.username

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh') and response.data.get('access'):
            # Extract tokens
            refresh_token = response.data.pop('refresh')
            access_token = response.data.pop('access')

            # Calculate expiration time for the cookies (5 days for this example)
            expiration = now() + timedelta(days=5)

            # Set tokens in HttpOnly cookies
            response.set_cookie('refresh.myblog', refresh_token,
                                expires=expiration, httponly=True, secure=True, samesite='Lax')
            response.set_cookie('access.myblog', access_token,
                                expires=expiration, httponly=True, secure=True, samesite='Lax')

        return super().finalize_response(request, response, *args, **kwargs)
