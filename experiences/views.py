from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Perk
from .serializers import PerkSerializer


class Perks(APIView):
    # read
    def get(self, request):
        all_perks = Perk.objects.all()  # perks의 모든 오브젝트를 다불러옴
        serializer = PerkSerializer(
            all_perks, many=True
        )  # 불러온정보를 PerkSerializer 로 형식에 맞춰 번역
        return Response(serializer.data)  # 정보를 보여줭

    # create 함수
    def post(self, request):
        serializer = PerkSerializer(data=request.data)  # reques.data 로 정보를 받아오고
        if serializer.is_valid():  ## serializer 에 값이 있으면
            perk = serializer.save()  # 받은정보를 저장
            return Response(
                PerkSerializer(perk).data
            )  # PerkSerializer 형식에 맞춰서 data를 변형 하고 post 로 전달해줌
        else:  # 값이 없으면 에러메세지 출력
            return Response(serializer.error_messages)


class PerkDetail(APIView):
    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)  # pk번호에 맞는 데이터 가져오기
        except Perk.DoesNotExist:  # 값이 없다면 못찾겠다는 메세지 출력
            raise NotFound

    def get(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk)
        return Response(serializer.data)

    # update 함수
    def put(self, request, pk):
        perk = self.get_object(pk)  # 내가
        serializer = PerkSerializer(
            perk,
            data=request.data,
            partial=True,  # partial => 부분적 업데이트 허용 !
        )
        if serializer.is_valid():  # serializer 에 값이 있으면
            updated_perk = serializer.save()  # 업데이트 값 저장
            return Response(
                PerkSerializer(updated_perk).data,
            )  # 업데이트 값 전당
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete()
        return Response(status=HTTP_204_NO_CONTENT)


## 1 URL, 2 view , 3 serializer, 4 method
