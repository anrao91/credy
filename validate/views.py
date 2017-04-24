
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import Bank, Branch
from .serializer import BankSerializer, BranchSerializer, DocumentSerializer, ListBankSerializer, IfscSerializer
from PyPDF2 import PdfFileReader


class ListBankView(generics.ListAPIView):
	'''
		Lists all bank names with code
	'''
	allowed_methods = ('GET', 'OPTIONS')
	queryset = Bank.objects.all()
	serializer_class = ListBankSerializer

	def get(self, request, *args, **kwargs):
		return super(ListBankView, self).get(request, *args, **kwargs)


class ListIFSCView(generics.ListAPIView):
	"""
		Lists all branches for a given bank. 
		GET: name = bank_name
	"""

	allowed_methods = ('GET', 'OPTIONS')
	queryset = Branch.objects.all()
	serializer_class = IfscSerializer

	def get_queryset(self):
		return super(ListIFSCView, self).get_queryset().filter(
			bank = Bank.objects.get(name = self.request.GET.get('name')))


	def get(self, request, *args, **kwargs):
		return super(ListIFSCView, self).get(request, *args, **kwargs)


class RetreiveBranchView(generics.RetrieveAPIView):
	"""
		Retrieves branch details for a given ifsc code
	"""
	queryset = Branch.objects.all()
	serializer_class = BranchSerializer
	lookup_field = 'ifsc'


class DecryptDocumentView(generics.GenericAPIView):
	"""
		Tries to decrypt the given document - preferably pdf with the user given password
	"""
	allowed_methods = ('POST', 'OPTIONS')
	serializer_class = DocumentSerializer

	def post(self, request):
		file_obj = request.FILES.get('file')
		password = request.POST.get('password')
		result = False
		try:
			file_pointer = PdfFileReader(file_obj, "rb")
			if file_pointer.isEncrypted:
				status_code=status.HTTP_200_OK
				if file_pointer.decrypt(password):
					result = True	
			else:
				result = 'File not encrypted'
		except Exception as e:
			status_code = status.HTTP_400_BAD_REQUEST

		return Response(data = {'decrypted':result}, status=status_code)







































# import json
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from .models import Bank, Branch
# from django.core import serializers

# def get_ifsc_codes(request):
# 	code = request.GET.get('code')
# 	ifsc_codes = Branch.objects.filter(bank__code=code)
# 	ifsc_codes = ifsc_codes.values('ifsc', 'name')
# 	return HttpResponse(ifsc_codes)


# def get_branch_details(request):
# 	ifsc = request.GET.get('ifsc')
# 	branch = {}
# 	if ifsc:
# 		branch = get_object_or_404(Branch, ifsc=ifsc)
# 	return HttpResponse(serializers.serialize('json', [ branch, ]))