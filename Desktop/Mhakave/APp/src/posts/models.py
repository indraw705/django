from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User
import registration.backends.default
# Create your models here.


def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)




class Post(models.Model):
	user = models.ForeignKey(User,default=1)
	title = models.CharField(max_length=140)
	image = models.ImageField(upload_to = upload_location,
		null=True,
		blank=True, 
		height_field="height_field", 
		width_field = "width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})


	class Meta:
		ordering = ["-timestamp" , "-updated" ]




# def create_slug(instance, new_slug=None):
# 	slug = slugify(instance.title)
# 	if new_slug is not None:
# 		print isEnglish(slug)
# 		if (isEnglish(slug) != True):
# 		 	slug = "news_"+str(instance.pk)
# 		slug = new_slug
# 	qs = Post.objects.filter(slug=slug).order_by("-id")
# 	exists = qs.exists()
# 	if exists:
# 		new_slug = "%s_%s" %(slug, qs.first().id)
# 		return create_slug(instance, new_slug=new_slug)
# 	return slug




# def pre_save_post_receiver(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = create_slug(instance)


# pre_save.connect(pre_save_post_receiver, sender=Post)


