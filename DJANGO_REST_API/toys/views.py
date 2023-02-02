import imp
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from toys.models import Toy,Bio
from toys.serializers import ToySerializer,BioSerializer


# class JSONResponse(HttpResponse):
#     """
#     This class was overridden for using JSONResponse to be used in different view decleared below
#     """
#     def __init__(self,data ,**kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse,self).__init__(content,**kwargs)



# @csrf_exempt
# def name_list(request):
#     if request.method == 'GET':
#         name = Bio.objects.all()
#         name_searializer = BioSerializer(name,many=True)
  
#         print("Now data")
#         print(JSONResponse(name_searializer.data))
#         return JSONResponse(name_searializer.data)
#     elif request.method == "POST":
#         name_data = JSONParser().parse(request)
#         name_searializer = BioSerializer(data=name_data)
#         if name_searializer.is_valid():
#             name_searializer.save()
#             return JSONResponse(name_searializer.data,status=status.HTTP_201_CREATED)
#         return JSONResponse(name_searializer.error,status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# def toy_list(request):
#     if request.method == 'GET':
#         toys = Toy.objects.all()
#         toy_serializer = ToySerializer(toys,many=True)
#         print(JSONResponse(toy_serializer.data))
#         return JSONResponse(toy_serializer.data)
#     elif request.method == 'POST':                         
#         toy_data = JSONParser().parse(request)
#         toy_serializer = ToySerializer(data=toy_data)
#         if toy_serializer.is_valid():
#             toy_serializer.save()
#             return JSONResponse(toy_serializer.data,status=status.HTTP_201_CREATED)
        
#         return JSONResponse(toy_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# def toy_detail(request,pk): 
#     try:
#         toy = Toy.objects.get(pk=pk)
#     except Toy.DoesNotExist:
#         return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         toy_serializer = ToySerializer(toy)
#         return JSONResponse(toy_serializer.data)
    
#     elif request.method == 'PUT':
#         toy_data = JSONParser().parse(request)
#         toy_serializer = ToySerializer(toy,data =toy_data) #update(self,instance, validated_data)
#         if toy_serializer.is_valid:
#             toy_serializer.save()
#             return JSONResponse(toy_serializer.data)
#         else:
#             return JSONResponse(toy_serializer.errors,status=status.HTTP_204_NO_CONTENT)
    
#     elif request.method == 'DELETE':
#         toy.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)



#below is more generic way of implementing views that not ony works with json data but also other format data and specify explicitly which view support what types of request
@api_view(['GET','POST'])#changed part for @api_view
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toy_serializer = ToySerializer(toys,many=True)
        print(Response(toy_serializer.data))
        return Response(toy_serializer.data)#changed part for @api_view
    elif request.method == 'POST':                         
        
        toy_serializer = ToySerializer(data=request.data)#changed part for @api_view
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(toy_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def toy_detail(request,pk): 
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return Response(toy_serializer.data)
    
    elif request.method == 'PUT':
       
        toy_serializer = ToySerializer(toy,data=request.data) #update(self,instance, validated_data)
        if toy_serializer.is_valid:
            toy_serializer.save()
            return Response(toy_serializer.data)#changed part for @api_view
        else:
            return Response(toy_serializer.errors,status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'DELETE':
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)