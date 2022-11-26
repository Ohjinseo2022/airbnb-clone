from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Amenity, Room
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer


# /api/v1/rooms/amenites
# /api/v1/rooms/amenites/1


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(
            all_amenities,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(
                AmenitySerializer(amenity).data,
            )
        else:
            return Response(serializer.errors)


#     def get(self, request, pk):
#         serialilzer = CategorySerializer(self.get_object(pk))
#         return Response(serialilzer.data)
class AmentiyDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(
            serializer.data,
        )
        # 두가지 방법 가능
        # return Response(
        #     AmenitySerializer(
        #         self.get_object(pk).data,
        #     )
        # )

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serilaizer = AmenitySerializer(
            amenity,
            data=request.data,
            partial=True,
        )
        if serilaizer.is_valid():
            updated_amenity = serilaizer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serilaizer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()  ##Room 의 모든 오브젝틀르 뽑아옴
        serializer = RoomListSerializer(
            all_rooms, many=True
        )  # serializer 를 사용하여 형식에 맞게 번역처리
        return Response(serializer.data)  # serializer 에 담긴 data 를 전손


class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            return NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)
