from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import SmSerializer
from .models import Sm
from rest_framework.response import Response


class SmViewSet(viewsets.ModelViewSet):
    queryset = Sm.objects.all().order_by('name')
    serializer_class = SmSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Sm.objects.filter(status=False)


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