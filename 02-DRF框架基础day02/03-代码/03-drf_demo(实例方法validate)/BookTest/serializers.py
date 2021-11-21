
from rest_framework import serializers
from datetime import date

class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期')
    bread = serializers.IntegerField(label='阅读量', required=False, min_value=0, max_value=999999)
    bcomment = serializers.IntegerField(label='评论量', required=False, min_value=0, max_value=999999)
    image = serializers.ImageField(label='图片', required=False)


    # 终极校验函数*****
    def validate(self, attrs):
        # 功能：针对所有字段进行自定义校验
        # 参数：attrs —— 字典类型，记录了经过前序校验之后的所有字段的值： {"btitle": "精通django", "bpub_date": date(1999, 8, 7)......}
        # 返回值：一定要返回经过当前校验之后的所有字段值 —— 返回值即是最终的"有效数据"

        btitle = attrs.get('btitle')
        print('书名：', btitle)
        bpub_date = attrs.get('bpub_date')
        print('出版日期：', bpub_date)

        if 'django' not in btitle:
            raise serializers.ValidationError('这不是一本关于django的书')

        # 约定，出版日期必须大于/晚于date(2017,1,1)
        if bpub_date <= date(2017, 1, 1): # 2017年1月1日:
            raise serializers.ValidationError('出版日期必须晚于2017年1月1日')

        # 返回最终的有效数据
        return attrs








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