
# serializers模块，是drf框架定义关于序列化器内容
from rest_framework import serializers

class HeroInfoSimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    hname = serializers.CharField()


# 针对BookInfo模型类对象，定义一个序列化器，这个序列化器专门用来操作BookInfo对象数据的
# (1)、明确操作的目标数据 —— 模型类
# (2)、继承自Serializer
# (3)、定义和模型类"同名"类属性，类型一一对应的形式，来确定参与序列化的模型类属性
# (4)、只要模型类中存在的属性，哪怕是隐藏的都可以在序列化器中定义出来
# (5)、针对一个模型类，可以定义多个序列化器实现不同的序列化业务需求
class BookInfoSerializer(serializers.Serializer):
    # read_only=True表明该字段只参与序列化，不参与反序列化
    id = serializers.IntegerField(read_only=True, label='主键值')
    btitle = serializers.CharField(required=True, max_length=20, label='书名')
    bpub_date = serializers.DateField(required=True, label='出版日期')

    bread = serializers.IntegerField(required=False, default=0, label='阅读量')
    bcomment = serializers.IntegerField(required=False, default=0, label='评论量')
    is_delete = serializers.BooleanField(required=False, default=False, label='逻辑删除')
    image = serializers.ImageField(required=False, allow_null=True, label='图片')

    # 隐藏的关联字段heros —— 记录关联的从表HeroInfo多个对象
    # (1)、序列化为关联对象的主键值，read_only=True表明此属性/字段只参与序列化操作
    # heros = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # (2)、序列化为关联对象的__str__方法返回的结果
    # heros = serializers.StringRelatedField(many=True)
    # (3)、使用自定义的关联对象模型类序列化器进行序列化
    # heros = HeroInfoSimpleSerializer(many=True)


# 针对HeroInfo模型类定义序列化器
class HeroInfoSerializer(serializers.Serializer):
    # 主键隐藏属性
    id = serializers.IntegerField()
    # 固有属性
    hname = serializers.CharField()
    hgender = serializers.IntegerField()
    hcomment = serializers.CharField()
    is_delete = serializers.BooleanField()
    # 关联属性/字段
    # (1)、序列化为关联对象的主键值，read_only=True表明此属性/字段只参与序列化操作
    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)
    # (2)、序列化为关联对象的__str__方法返回的结果
    # hbook = serializers.StringRelatedField()
    # (3)、使用自定义的关联对象模型类序列化器进行序列化
    # hbook = BookInfoSerializer()











