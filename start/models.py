from __future__ import unicode_literals

from django.db import models

class Movie(models.Model):
	title = models.CharField(max_length=200, default="")
	year = models.CharField(max_length=200, default="")
	director = models.CharField(max_length=200, default="")
	average_rating = models.DecimalField(max_digits=3, decimal_places=2)
	plot_description = models.CharField(max_length=1000, default="")
	#photo

	def __str__(self):
		return self.title
