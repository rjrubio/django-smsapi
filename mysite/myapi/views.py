from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import SmSerializer
from .serializers import CollegeSerializer
from .serializers import MetaSerializer
from .models import Sm
from .models import College
from .models import Meta
from rest_framework.response import Response


class SmViewSet(viewsets.ModelViewSet):
    queryset = Sm.objects.all().order_by('name')
    serializer_class = SmSerializer

    def get_queryset(self):
        return Sm.objects.filter(status=False)


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all().order_by('created_at')
    serializer_class = CollegeSerializer

    def get_queryset(self):
        timestamp = self.request.GET.get('timestamp')
        return College.objects.filter(created_at__gt=timestamp)


class MetaViewSet(viewsets.ModelViewSet):
    queryset = Meta.objects.all().order_by('timestamp')
    serializer_class = MetaSerializer

    def get_queryset(self):
        clientid = self.request.GET.get('clientId')
        return Meta.objects.filter(client_id=clientid)


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