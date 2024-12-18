from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_countries import countries

from .exceptions import NotYourProfile, ProfileNotFound
from .models import Profile
from .serializers import ProfileSerializer, UpdateProfileSerializer


class GetProfileAPIVIew(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user_profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UpdateProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        try:
            Profile.objects.get(user_username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound
        
        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile
        
        data = request.data
        serializer = UpdateProfileSerializer(
            instance=request.user, data=data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)