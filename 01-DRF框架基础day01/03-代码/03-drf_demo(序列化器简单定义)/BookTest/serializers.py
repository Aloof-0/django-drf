
# serializers模块，是drf框架定义关于序列化器内容
from rest_framework import serializers

# 针对BookInfo模型类对象，定义一个序列化器，这个序列化器专门用来操作BookInfo对象数据的
# (1)、明确操作的目标数据 —— 模型类
# (2)、继承自Serializer
# (3)、定义和模型类"同名"类属性，类型一一对应的形式，来确定参与序列化的模型类属性
# (4)、只要模型类中存在的属性，哪怕是隐藏的都可以在序列化器中定义出来

class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    btitle = serializers.CharField()
    bpub_date = serializers.DateField()
    bread = serializers.IntegerField()
    bcomment = serializers.IntegerField()
    is_delete = serializers.BooleanField()
    image = serializers.ImageField()









