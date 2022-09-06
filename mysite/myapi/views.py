from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import SmSerializer
from .serializers import CollegeSerializer
from .serializers import MetaSerializer
from .serializers import DeviceSerializer
from .models import Sm
from .models import College
from .models import Meta
from .models import Device
from rest_framework.response import Response
from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from pyfcm import FCMNotification
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


class SmViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Sm.objects.all().order_by('name')
    serializer_class = SmSerializer

    def get_queryset(self):
        data = Sm.objects.filter(status=False)
        cities_sorted = list(data)
        data.update(status=True)
        return cities_sorted


class DeviceViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Device.objects.all().order_by('clinicid')
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return Device.objects.filter(status=True)


class CollegeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = College.objects.all().order_by(F('created_at').desc(nulls_last=True))
    serializer_class = CollegeSerializer

    def create(self, request, pk=None, company_pk=None, project_pk=None):
        is_many = True if isinstance(request.data, list) else False

        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        timestamp = self.request.GET.get('timestamp')
        return College.objects.filter(created_at__gt=timestamp)


class MetaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Meta.objects.all().order_by(F('timestamp').desc(nulls_last=True))
    serializer_class = MetaSerializer

    def create(self, request, pk=None, company_pk=None, project_pk=None):
        is_many = True if isinstance(request.data, list) else False

        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        clientid = self.request.GET.get('clientId')
        return Meta.objects.filter(client_id=clientid).order_by(F('timestamp').desc(nulls_last=True))[:1]


def hey(request):
    try:
        if request.method == 'POST':
            sm = Sm()
            data = request.POST.copy()
            sm.mobilenumber = data.get("mobilenumber")
            sm.message = data.get("message")
            sm.save()

            return render(request, 'status.html', {
                'num': data.get('mobilenumber'),
                'msg': data.get('message')
            })
        else:
            return render(request, 'sendsms.html')
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

@csrf_exempt 
def fcmPush(request):
    try:
        if request.method == 'POST':
            data = request.POST.copy()
            clinicid = data.get("clinicid")
            title = data.get("title")
            icon = "https://healthcare.quetap.ph/assets/images/components/QueTap_1500px.png"
            print("title" , title)
            message = data.get("message")
            print("message" , message)
            devices = Device.objects.values('device_id','created_document_timestamp').filter(clinicid=clinicid).latest('created_document_timestamp')
            print(devices)
            push_service = FCMNotification(api_key=settings.FCM_DJANGO_SETTINGS["FCM_SERVER_KEY"])
            registration_id = devices['device_id']
            data_message = { "Title" : title,"body" : message, "icon" : icon }
            result = push_service.single_device_data_message(registration_id=registration_id, data_message=data_message)
            print(result)
            return render(request, 'status.html', {
                'num': title,
                'msg': result
            })
        else:
            return render(request, 'sendsms.html')
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)