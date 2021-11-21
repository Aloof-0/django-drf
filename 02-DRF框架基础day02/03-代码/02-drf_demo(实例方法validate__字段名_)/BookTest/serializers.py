
from rest_framework import serializers


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    # read_only=True表明该字段只参与序列化，不参与反序列化
    id = serializers.IntegerField(label='ID', read_only=True)
    # write_only=True表明该字段只参与反序列化，不参与序列化
    # btitle = serializers.CharField(label='名称', max_length=20, write_only=True)

    btitle = serializers.CharField(label='名称', max_length=20)

    bpub_date = serializers.DateField(label='发布日期')
    bread = serializers.IntegerField(label='阅读量', required=False, min_value=0, max_value=999999)
    bcomment = serializers.IntegerField(label='评论量', required=False, min_value=0, max_value=999999)
    image = serializers.ImageField(label='图片', required=False)


    # 自定义一个特殊名称的实例方法，来针对btitle字段进行单独校验
    # 方法名称固定格式：validate_<字段名>
    def validate_btitle(self, value):
        # 功能：针对btitle单独校验
        # 参数：value —— 当前字段经过前序校验的值
        # 返回值：经过当前校验之后的有效值
        if 'django' not in value:
            raise serializers.ValidationError('这不是一本关于django的书')

        # 一定要返回经过当前校验之后的有效值
        return value










class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    # ChoiceField类型其本质就是整数 —— 带有可选项整数(枚举整数)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)