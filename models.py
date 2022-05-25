from django.db import models

# Create your models here.
class covidinfo(models.Model):
	village = models.CharField(max_length=30)
	tehsil = models.CharField(max_length=30)
	confirmed = models.IntegerField()
	active = models.IntegerField()
	recovered = models.IntegerField(default="0")
	deceased = models.IntegerField(default="0")

	def __str__(self):
		return self.village+" "+self.tehsil+" "+str(self.confirmed)+" "+str(self.active)+" "+str(self.recovered)+" "+str(self.deceased)

class bascoinfo(models.Model):
	btcase = models.IntegerField()
	bonactive = models.IntegerField()
	brecovered = models.IntegerField()
	bdeceased = models.IntegerField()

	def __str__(self):
		return str(self.btcase)+" "+str(self.bonactive)+" "+str(self.brecovered)+" "+str(self.bdeceased)

class udaicoinfo(models.Model):
	utcase = models.IntegerField()
	uonactive = models.IntegerField()
	urecovered = models.IntegerField()
	udeceased = models.IntegerField()

	def __str__(self):
		return str(self.utcase)+" "+str(self.uonactive)+" "+str(self.urecovered)+" "+str(self.udeceased)

class dcoinfo(models.Model):
	dtcase = models.IntegerField()
	donactive = models.IntegerField()
	drecovered = models.IntegerField()
	ddeceased = models.IntegerField()

	def __str__(self):
		return str(self.dtcase)+" "+str(self.donactive)+" "+str(self.drecovered)+" "+str(self.ddeceased)