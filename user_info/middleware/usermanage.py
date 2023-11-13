from django.utils.timezone import now
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.conf import settings
import datetime


class TokenRefreshMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        refresh_token_cookie = request.COOKIES.get('refresh.myblog')

        if refresh_token_cookie:
            try:
                refresh_token = RefreshToken(refresh_token_cookie)

                expiration_time = refresh_token.payload['exp']
                expiration_time = datetime.datetime.fromtimestamp(expiration_time, datetime.timezone.utc)

                lifetime_remaining = (expiration_time - now()).total_seconds()

                if lifetime_remaining < 3600:
                    new_tokens = RefreshToken.for_access_token(refresh_token)

                    expiration_refresh = now() + settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
                    expiration_access = now() + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']

                    response.set_cookie('refresh.myblog', str(new_tokens), expires=expiration_refresh, httponly=True,
                                        secure=True, samesite='Lax')
                    response.set_cookie('access.myblog', str(new_tokens.access_token), expires=expiration_access,
                                        httponly=True, secure=True, samesite='Lax')
            except TokenError:
                # Handle token error (e.g., token is invalid or expired), you can also log the error here
                response.delete_cookie('refresh.myblog')
                response.delete_cookie('access.myblog')

        return response
