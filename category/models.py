from django.db import models

class Category(models.Model):

	id =  models.AutoField(primary_key=True)
	title = models.CharField(max_length=120,null=True,blank=False)
	slug = models.CharField(max_length=120,null=True,blank=False)
	description = models.TextField()
	tags = models.TextField() 


	def __unicode__(self): return self.title


	class Meta:
		db_table = 'category'
