from django.db import models

class Posts(models.Model):

	id = models.AutoField(primary_key=True)
	cid = models.IntegerField()
	title = models.CharField(max_length=125,null=True,blank=False)
	slug = models.CharField(max_length=125,null=True,blank=False)
	description = models.TextField()
	tags = models.TextField()
	publish_date=models.DateTimeField(auto_now_add=True,auto_now=False)
	update_date=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self): return self.title

	class Meta:

		db_table = "posts"




