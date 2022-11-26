from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerilalizer
from categories.serializers import CategorySerializer


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
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(ModelSerializer):
    owner = TinyUserSerilalizer(
        read_only=True
    )  # owner 에 해당하는 부분은 TinyUserSerializer 양식에 맞춰서 보여줘라!
    amenity = AmenitySerializer(many=True)  # 안에 여러개의 정보가 포함되어 있기 떄문에 many=True 옵셥을 줘야함!
    category = CategorySerializer()

    class Meta:
        model = Room
        fields = "__all__"
