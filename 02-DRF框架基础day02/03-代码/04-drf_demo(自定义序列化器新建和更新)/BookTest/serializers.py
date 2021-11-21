from rest_framework import serializers
from .models import *


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期')
    bread = serializers.IntegerField(label='阅读量', required=False, min_value=0)
    bcomment = serializers.IntegerField(label='评论量', required=False, min_value=0)
    image = serializers.ImageField(label='图片', required=False)

    # 新键
    def create(self, validated_data):
        """
        功能：根据有效数据，来新建模型类对象保存数据 —— 新建/保存数据
        :param validated_data: 有效数据
        :return: 新建的模型类对象
        """
        instance = BookInfo.objects.create(**validated_data)
        return instance

    # 更新
    def update(self, instance, validated_data):
        """
        功能：根据有效数据，来更新模型类对象保存数据 —— 更新数据
        :param instance: 被更新的模型类对象(BookInfo)
        :param validated_data: 用于更新的有效数据
        :return: 更新之后的模型类对象
        """
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.is_delete = validated_data.get('is_delete', instance.is_delete)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        return instance


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    # id主键隐藏字段(自增)，一定只参与序列化，所以设置read_only=True
    id = serializers.IntegerField(label='ID', read_only=True)
    # 固有字段（均为常规普通类型）
    hname = serializers.CharField(label='名字', max_length=20)
    # ChoiceField类型其本质就是整数 —— 带有可选项整数(枚举整数)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    is_delete = serializers.BooleanField(label='逻辑删除', default=False)
    # 外间关联字段，代表一个关联的主表模型类(BookInfo)对象
    # 外间关联字段设置为PrimaryKeyRelatedField —— 在序列化的时候把对象序列化为主键值，在反序列化的时候把主键值反序列化为对象
    hbook = serializers.PrimaryKeyRelatedField(queryset=BookInfo.objects.all())

    # 新键
    def create(self, validated_data):
        return HeroInfo.objects.create(**validated_data)

    # 更新
    def update(self, instance, validated_data):
        instance.hname = validated_data.get('hname', instance.hname)
        instance.hgender = validated_data.get('hgender', instance.hgender)
        instance.hcomment = validated_data.get('hcomment', instance.hcomment)
        instance.is_delete = validated_data.get('is_delete', instance.is_delete)
        instance.hbook = validated_data.get('hbook', instance.hbook)
        instance.save()
        return instance
