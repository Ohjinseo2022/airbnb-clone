from rest_framework.views import APIView
from django.db import transaction
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from .models import Amenity, Room
from categories.models import Category
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

    # create room!
    def post(self, request):
        if request.user.is_authenticated:  ##로그인정보가있으면 owner 정보를 가지고있다면 ? 밑에 코드를 실행하라
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                category_pk = request.data.get("category")
                if not category_pk:  # 카테고리_pk 의 값이 없으면 오류출력
                    raise ParseError("Category is required")  # 데이터를 잘못 전던했을떄 보여주는 에러
                try:
                    category = Category.objects.get(
                        pk=category_pk
                    )  # 있다면 카테고리 번호를 가지는 값을 변수에 담아주고
                    if (
                        category.kind == Category.CategoryKindChoices.EXPERIENCES
                    ):  # 카테고리 정보가 EXPERIENCES에 포함된 카테고리라면 잘못된정보라고 에러띄울예정
                        raise ParseError("The category kind should be 'rooms")
                except Category.DoesNotExist:
                    raise ParseError("Category not found")
                    # 모두가 작동하거나 모두가 작동자체를 않기를 원함 ! -> pk 가 과도하게 많이 소비되는것을 막는다 . 코드세트를 만들어서 그세트안에 하나라도 실패하면 모든것을 없던일로 만들 필요가있습니당 그걸 위해 Transection 을 사용할거임! 원래 기존 장고프레임워크는 코드가 실행되면 DB에 바로 적용된다는 단점이있음 그걸 없던일로 되돌리는 역할을함 !

                    # transaction.atomic 을 사용하면 코드들이 정상적으로 작동하는지 확인후 작동하게됨
                    # 변경사항들을 리스트로 저장하게되고 나중에 db 반영한다는거임

                    # 기존에는 amenity생성시 오류 발생을하면 이미 생성된 방을 없애는 과정이 한번더 들어감
                    # 하지만 이건 방자체를 생성하지 않기떄문에 과정하나가 사라짐
                try:
                    with transaction.atomic():
                        room = serializer.save(
                            owner=request.user,
                            category=category,  # 카테고리의 정보를 명시해줌
                        )  ## save() 메서드안에 .create()가 포함되어있음
                        amenity_list = request.data.get("amenity")
                        for amenity_pk in amenity_list:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenity.add(amenity)
                        serializer = RoomDetailSerializer(room)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("amenity not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)

    def put(self, request, pk):
        room = self.get_object(pk)
        if not request.user.is_authenticated:  # 로그인이 됐는지 확인
            raise NotAuthenticated
        if room.owner != request.user:  # 유저 정보가 일치하는지 확인
            raise PermissionDenied  ## 권한 거부

        serializer = RoomDetailSerializer(
            room,
            data=request.data,
            partial=True,  # partial => 부분적 업데이트 허용 !
        )
        if serializer.is_valid():  # serializer 에 값이 있으면
            updated_perk = serializer.save()  # 업데이트 값 저장
            return Response(
                RoomDetailSerializer(updated_perk).data,
            )  # 업데이트 값 전달
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        room = self.get_object(pk)
        if not request.user.is_authenticated:  # 로그인이 됐는지 확인
            raise NotAuthenticated
        if room.owner != request.user:  # 유저 정보가 일치하는지 확인
            raise PermissionDenied  ## 권한 거부
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)
