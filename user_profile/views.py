from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view, permission_classes

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

    def post(self, request):
        pin = request.data.get('pin')
        if not pin or len(pin) < 4:
            return Response({'error': 'PIN must be at least 4 digits'}, status=400)

        request.user.profile.pin_code_hash = make_password(pin)
        request.user.profile.save()
        return Response({'detail': 'PIN code set successfully'})


class PinVerifyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pin = request.data.get('pin')
        if not pin:
            return Response({'error': 'PIN is required'}, status=400)

        valid = check_password(pin, request.user.profile.pin_code_hash or '')
        return Response({'valid': valid})

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_profile(request):
    user = request.user
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)