from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from authentication.models import User
from authentication.serializers import UserSerializer


@api_view(['post'])
@authentication_classes([])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    ok, data = User.login(request, username, password)

    if ok:
        serialized = UserSerializer(data)
        token = Token.objects.get_or_create(user=data)[0].key

        return Response({'user': serialized.data, 'token': token})
    else:
        return Response({
            'status': 'Unauthorized',
            'message': data,
        }, status=status.HTTP_401_UNAUTHORIZED)
