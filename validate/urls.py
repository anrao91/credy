from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^bank_details/', TemplateView.as_view(template_name='bank_details.html')),
	url(r'^get_banks/', views.ListBankView.as_view()),
	url(r'^get_branch/(?P<ifsc>[^/]+)/$', views.RetreiveBranchView.as_view()),
	url(r'^get_ifsc/', views.ListIFSCView.as_view()),
	url(r'^upload/', views.DecryptDocumentView.as_view()),

]