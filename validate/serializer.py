from rest_framework import serializers
from .models import Bank, Branch


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class ListBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('name',)


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class IfscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('ifsc', 'name',)

class DocumentSerializer(serializers.Serializer):
	file = serializers.FileField(required=True)
	password = serializers.CharField(max_length=32)
	class Meta:
		fields = ('file', 'password')