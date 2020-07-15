from django import forms
from django.contrib.auth.models import User
from .Neural import inputs_to_network

answer_1 = 0
answer_2 = 0

def result(answer1,answer2):
	if(60 <= answer1 and answer1 <= 120 and 110 <= answer2 and answer2 <= 200):
		return inputs_to_network(1)
	elif(40 <= answer1 and answer1 <= 60 and 110 > answer2):
		return inputs_to_network(2)
	elif(40 <= answer1 and answer1 <= 60 and 110 <= answer2 and answer2 <= 200):
		return inputs_to_network(3)
	elif(60 <= answer1 and answer1 <= 120 and 110 > answer2):
		return inputs_to_network(6)
	elif(60 <= answer1 and answer1 <= 120 and 200 <= answer2 and answer2 <= 300):
		return inputs_to_network(7)
	elif(60 <= answer1 and answer1 <= 120 and answer2 > 300):
		return inputs_to_network(8)
	elif(120 <= answer1 and answer1 <= 180 and 110 > answer2):
		return inputs_to_network(9)
	elif(120 <= answer1 and answer1 <= 180 and 110 <= answer2 and answer2 <= 200):
		return inputs_to_network(10)
	elif(120 <= answer1 and answer1 <= 180 and 200 <= answer2 and answer2 <= 300):
		return inputs_to_network(11)
	elif(120 <= answer1 and answer1 <= 180 and answer2 > 300):
		return inputs_to_network(12)
	elif(180 <= answer1  and 110 <= answer2 and answer2 <= 200):
		return inputs_to_network(13)
	elif(180 <= answer1  and 200 <= answer2 and answer2 <= 300):
		return inputs_to_network(14)
	elif(180 <= answer1  and answer2 > 300):
		return 'refer doctor'
	else:
		return "Invalid"

