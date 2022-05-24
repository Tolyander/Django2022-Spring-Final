from rest_framework.response import Response
from rest_framework import views
from .serializers import UserRegistrationSerializer


class LoginView(views.APIView):

    def post(self,request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
