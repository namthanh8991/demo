from rest_framework.views import APIView
from .models import Person
from .serializer import Personserializer,PersonPortalserializers
from rest_framework.response import Response
class ListPersonview(APIView):
    def get(self,request, format= None):
        person = Person.objects.all()
        serializer = PersonPortalserializers(person, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = PersonPortalserializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def put(self,request,khoa_chinh):
        person = Person.objects.get(pk=khoa_chinh)
        serializer = PersonPortalserializers(person, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,khoa_chinh):
        person = Person.objects.get(pk=khoa_chinh)
        person.delete()
        return Response({'da xoa thanh cong'})







