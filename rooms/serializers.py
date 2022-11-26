from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
        )
        # depth = 1  ## 관계성이 설정된 모든 정보를 보이게 자동으로 설정해주는 친구 ->> 단 커스터마이징이 불가능함


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"


class RoomDetailSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        depth = 1
