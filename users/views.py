from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = CreateUserSerializer(data=request.data, context={'request': request})
        

        if serializer.is_valid():
            password = serializer.validated_data['password']

            # Create the user first
            user = serializer.save()

            # Set up the password after
            user.set_password(password)

            user.save()

            return Response({
                'status': 'Success',
                'message': 'User {} created successfully!',
            })
        else:
            return Response({
                "status": "Failure",
                'message': 'Invalid data!',
                'details': serializer.errors,
            })

class ProviderListView(generics.ListAPIView):
    queryset = User.objects.filter(is_provider=True)
    serializer_class = UserSerializer

class ServiceProviderProfileViewSet(viewsets.ModelViewSet):
    queryset = ServiceProviderProfile.objects.all()
    serializer_class = ServiceProviderSerializer


@api_view(http_method_names=['POST'])
def turn_to_provider(request, pk):
    # Get the user by pk
    try:
        user = User.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({
            'status': 'failure',
            'message': 'User with id = {} does not exist!'.format(pk)
        })
    
    # if user is already a provider, do nothing
    if user.is_provider:
        res = {
            'status': 'failure',
            'message': 'User {} was already a provider!'.format(user.username),
        }
        return Response(res)

    # Turn the user to a provider
    user.is_provider = True

    # Create and attach a Service Provider Profile to the user
    sp_profile = ServiceProviderProfile()
    sp_profile.user = user

    # Save all the changes
    sp_profile.save()
    user.save()

    # Notify the success of operation
    res = {
        'status': 'success',
        'message': 'User {} is now a provider!'.format(user.username),
    }

    return Response(res)


@api_view(http_method_names=['POST', 'PUT'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    as_provider = False
    if 'as_provider' in request.data.keys() and request.data['as_provider'] in [True, 'True', 'true', 'TRUE']:
        as_provider = True

    # Find the user by his username
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return Response({
            'status': 'failure',
            'message': 'User does not exist!',
        })
    
    # Check the password
    authenticated = user.check_password(password)

    if not authenticated:
        return Response({
            'status': 'failure',
            'message': 'User credentials incorrect!',
        })
    else:
        if not as_provider or as_provider and user.is_provider:
            return Response({
                'status': 'success',
                'message': 'User {} is authenticated'.format(username),
                'data': UserSerializer(user, context={'request': request}).data,
                
            })
        else:
            return Response({
            'status': 'failure',
            'message': 'User is not a provider!',
        })
