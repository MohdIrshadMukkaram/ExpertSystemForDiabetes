from django.db import models
from django import forms
from djchoices import ChoiceItem, DjangoChoices
from django.utils import timezone
from datetime import datetime
from .fields import ListTextWidget
from django.contrib.auth.models import User
from django.urls import reverse



INTEGER_CHOICES_1= [tuple([x,x]) for x in range(40,200)]
INTEGER_CHOICES_2= [tuple([x,x]) for x in range(100,350)]
INTEGER_CHOICES_3= [tuple([x,x]) for x in range(0,50)]



class prescription_form(models.Model):
	
	class medicine_choices(DjangoChoices):
		glycomet = ChoiceItem('glycomet', 'glycomet')
		glychipage = ChoiceItem('glychipage', 'glychipage')
		gluconorm = ChoiceItem('gluconorm', 'gluconorm')
		amryl = ChoiceItem('amryl', 'amryl')
		glimistar = ChoiceItem('glimistar', 'glimistar')
		glim = ChoiceItem('glim', 'glim')
		KGlim  = ChoiceItem(' K-Glim', ' K-Glim')
		Voglimac = ChoiceItem('Voglimac GM', 'Voglimac GM')
		Vogli = ChoiceItem('Vogli GM1', 'Vogli GM1')
		Vogli2 = ChoiceItem(' Vogli GM2', ' Vogli GM2')
		Daonilm = ChoiceItem('Daonil-m', 'Daonil-m')
		Bieuglicon = ChoiceItem('Bi-euglicon', 'Bi-euglicon')
		GlykindM  = ChoiceItem('Glykind-M', 'Glykind-M')
		glicM  = ChoiceItem('glic-M', 'glic-M')
		glychomadegp1 = ChoiceItem('glychomade-gp1', 'glychomade-gp1')
		glychomadegp2 = ChoiceItem('glychomade-gp2', 'glychomade-gp2')
		glychomadegp3 = ChoiceItem('glychomade-gp3', 'glychomade-gp3')
		acarbose = ChoiceItem('acarbose', 'acarbose')
		miglitol = ChoiceItem('miglitol', 'miglitol')
		metforminalogliptin = ChoiceItem('metformin-alogliptin', 'metformin-alogliptin')
		metformincanagliflozin = ChoiceItem('metformin-canagliflozin', 'metformin-canagliflozin')
		metformindapagliflozin = ChoiceItem('metformin-dapagliflozin', 'metformin-dapagliflozin')
		metforminempagliflozin = ChoiceItem('metformin-empagliflozin', 'metformin-empagliflozin')
		metforminglipizide = ChoiceItem('metformin-glipizide', 'metformin-glipizide')
		metforminglyburide = ChoiceItem('metformin-glyburide', 'metformin-glyburide')
		metforminlinagliptin = ChoiceItem('metformin-linagliptin', 'metformin-linagliptin')
		metforminpioglitazone = ChoiceItem('metformin-pioglitazone', 'metformin-pioglitazone')
		metforminrosiglitazone = ChoiceItem('metformin-rosiglitazone', 'metformin-rosiglitazone')
		metforminsaxagliptin = ChoiceItem('metformin-saxagliptin', 'metformin-saxagliptin')
		metforminsitagliptin = ChoiceItem('metformin-sitagliptin', 'metformin-sitagliptin')
		alogliptin = ChoiceItem('alogliptin', 'alogliptin')
		alogliptinmetformin = ChoiceItem('alogliptin-metformin', 'alogliptin-metformin')
		linagliptin = ChoiceItem('linagliptin', 'linagliptin')
		linagliptinempagliflozin = ChoiceItem('linagliptin-empagliflozin', 'linagliptin-empagliflozin')
		saxagliptin = ChoiceItem('saxagliptin', 'saxagliptin')
		saxagliptinmetformin = ChoiceItem('saxagliptin-metformin', 'saxagliptin-metformin')
		sitagliptin = ChoiceItem('sitagliptin', 'sitagliptin')
		sitagliptinmetformin = ChoiceItem('sitagliptin-metformin', 'sitagliptin-metformin')
		nateglinide = ChoiceItem('nateglinide', 'nateglinide')
		repaglinide = ChoiceItem('repaglinide', 'repaglinide')
		repaglinidemetformin = ChoiceItem('repaglinide-metformin', 'repaglinide-metformin')
		glimepiride = ChoiceItem('glimepiride', 'glimepiride')
		glimepiridepioglitazone = ChoiceItem('glimepiride-pioglitazone', 'glimepiride-pioglitazone') 
		gliclazide = ChoiceItem('gliclazide', 'gliclazide')
		glipizide = ChoiceItem('glipizide', 'glipizide')
		glipizidemetformin = ChoiceItem('glipizide-metformin', 'glipizide-metformin')
		glyburide = ChoiceItem('glyburide', 'glyburide')




	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default=datetime.now())
	fasting = models.IntegerField(default=40, choices=INTEGER_CHOICES_1)
	posting = models.IntegerField(default=100, choices=INTEGER_CHOICES_2)
	diabetic_exp = models.IntegerField(default=0,choices=INTEGER_CHOICES_3)
	medicine_taken = models.CharField(choices=medicine_choices.choices,default=medicine_choices.glycomet,max_length=50)
	
	


	
	def __str__(self):
		return self.medicine_taken

	def get_absolute_url(self):
		return reverse("blog-result",kwargs={"username":self.author})

	class Meta:
		db_table = 'Prescription Form'

class Medicine(models.Model):
	class medicine_classes(DjangoChoices):
		class1 = ChoiceItem('class1', 'class1')
		class2 = ChoiceItem('class2', 'class2')
		class3 = ChoiceItem('class3', 'class3')

	medicine = models.CharField(max_length = 50)
	date = models.DateTimeField(default=timezone.now)
	medicine_class  = models.CharField(choices=medicine_classes.choices,default=medicine_classes.class1,max_length=8)
	

	def __str__(self):
		return self.medicine
	
	



	



