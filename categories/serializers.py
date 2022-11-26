from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    # ModelSerializer 활용시 serializers에서 수동으로 설정하던 create update를 알아서 설정해줌 모델설정을 상속받아와서 하는 방식
    class Meta:
        model = Category
        # 보여줄 필드 설정
        fields = ("name", "kind")
        # exclude = () 안에 들어가는 필드를 제외하고 다보여줌
        # fields = "__all__"  # 모든 필드를 다보고싶을떄

    # serializers 사용방식
    # pk = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(
    #     required=True,
    #     max_length=50,
    # )
    # kind = serializers.ChoiceField(
    #     choices=Category.CategoryKindChoices.choices,
    # )
    # created_at = serializers.DateTimeField(read_only=True)

    # def create(self, validated_data):
    #     return Category.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.kind = validated_data.get("kind", instance.kind)
    #     instance.save()
    #     return instance
