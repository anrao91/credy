from django.db import models

class Bank(models.Model):
	"""
		Comment
	"""
	code = models.CharField(max_length=64, unique=True, db_index=True)
	name = models.CharField(max_length=256)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name


class Branch(models.Model):
	"""
		Comment here to describe this model.
	"""
	bank = models.ForeignKey(Bank)
	ifsc = models.CharField(max_length=32, unique=True, db_index=True)
	name = models.CharField(max_length=256, null=True, blank=True)
	contact = models.CharField(max_length=15, null=True, blank=True)
	address = models.TextField(max_length=512, null=True, blank=True)
	city = models.CharField(max_length=64, null=True, blank=True)
	district = models.CharField(max_length=64, null=True, blank=True)
	state = models.CharField(max_length=64, null=True, blank=True)

	class Meta:
		ordering = ('ifsc',)

	def __str__(self):
		return self.name