from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .serializers import ProfileSerializer, PinSerializer
from rest_framework.decorators import api_view, permission_classes
from .throttling import PinRateThrottle
import logging

logger = logging.getLogger(__name__)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)

    def patch(self, request):
        serializer = ProfileSerializer(request.user.profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PinCreateView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [PinRateThrottle]

    def post(self, request):
        serializer = PinSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pin = serializer.validated_data['pin']
        request.user.profile.pin_code_hash = make_password(pin)
        request.user.profile.save()
        return Response({'detail': 'PIN code set successfully'})


class PinVerifyView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [PinRateThrottle]

    def post(self, request):
        serializer = PinSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pin = serializer.validated_data['pin']
        valid = check_password(pin, request.user.profile.pin_code_hash or '')
        logger.info(f"PIN verification attempt for user {request.user.username}: {'success' if valid else 'failure'}")
        return Response({'valid': valid})

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_profile(request):
    user = request.user
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)