from django.db import models

class SocialMediaAccount(models.Model):
	social_media = models.charField(default=None, max_length=255)
	social_account = models.charField(default=None, max_length=255)
	def __str__(self):
		return self.social_account

	class Meta:
		pass