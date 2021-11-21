
from rest_framework import serializers


def check(value):
    # 功能： 针对btitle字段，自定义一个校验函数
    # 参数：一定有一个参数value，是当前字段经过前序校验的值 —— "静态django"
    # 返回值：无

    if "django" not in value:
        # 说明校验失败 —— 抛出ValidationError异常来通知上层调用者校验失败
        raise serializers.ValidationError('这不是一本关于djangod的书')


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    # read_only=True表明该字段只参与序列化，不参与反序列化
    id = serializers.IntegerField(label='ID', read_only=True)
    # write_only=True表明该字段只参与反序列化，不参与序列化
    # btitle = serializers.CharField(label='名称', max_length=20, write_only=True)

    # validators用于指定针对当前字段的多个校验函数
    btitle = serializers.CharField(label='名称', max_length=20, validators=[check])

    bpub_date = serializers.DateField(label='发布日期')
    bread = serializers.IntegerField(label='阅读量', required=False, min_value=0, max_value=999999)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)












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