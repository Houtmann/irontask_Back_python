from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from irontask_back.serializers.serializer import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


class BenevoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Benevole.objects.all()
    serializer_class = BenevoleSerializer

    def post(self, request, pk):
        benevole= get_object_or_404(Benevole, pk=pk)
        serializer = BenevoleSerializer(benevole, data=request.data)
        serializer.save()
        return Response({'serializer': serializer, 'benevole': benevole})




