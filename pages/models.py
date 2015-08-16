from django.db import models

class Contact(models.Model):

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=125,null=True,blank=False)
	email = models.CharField(max_length=125,null=True,blank=False)
	message = models.TextField()
	insert_date=models.DateTimeField(auto_now_add=True,auto_now=False)
	

	def __unicode__(self): return self.name

	class Meta:

		db_table = "contact"




