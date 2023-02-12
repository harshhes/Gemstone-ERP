import re
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from django.core.validators import EmailValidator
from django.core.mail import send_mail
from django.contrib.auth import login
from .models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .custom_permissions import *
from rest_framework import viewsets

# generate JWT token after login
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

#authenticate user via email
def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
        print(user)
    except User.DoesNotExist:
        return None
    if user.check_password(password):
        return user


class RegisterUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, format=None):

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email') 
            password = serializer.data.get('password') 

            user = authenticate_user(email=email, password=password)
            
            if user is not None:
                token = get_tokens_for_user(user)
                login(request,user)
                return Response({'msg': 'Login Success!', "user_token": token}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non-field errors':{'email or password is not valid!!'}}}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InviteUserViaEmailView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = InviteUserViaEmailSerializer
    permission_classes = [IsAccountAdmin, IsBusinessOwner]

    def post(self, request, format=None, *args, **kwargs):
        email = request.data.get('email')
        if email is None:
            return Response({'non-field errors': "Please enter email"})

        if User.objects.filter(email=email).exists():
            return Response({'non-field errors': "Please enter unique email, this email is already taken"})

        if not (re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',email)):
            return Response({"ValidationError":f"{email} is not a Valid Email"})

        username = email[:email.index('@')] #extract username from the email
        host = 'http://localhost:8000/register-via-invite'

        try:
            send_mail(
"Invitation Mail to Join Gemstone",
f'''Hey, {username}\nWe are delighted to have you on board with us, This is your invitation mail to join our organisation.\nYou can create a account through the following link:
{host}
Regards
Gemstone
''',
                'harshhes007@gmail.com',
                [email],
                fail_silently=True,
                )
            return Response(
                {"msg":f"Email sent succussfully to {email}, Please check your mail and register ASAP"})
        
        except Exception as e:
            raise ValueError('Something Went Wrong!!')
        

class RegisterInviteUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterInviteUserSerializer



class PurchaseOrderView(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsPurchaseManager]


class PurchaseMemoView(viewsets.ModelViewSet):
    queryset = PurchaseMemo.objects.all()
    serializer_class = PurchaseMemoSerializer
    permission_classes = [IsSalesManager]


class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAccountAdmin]