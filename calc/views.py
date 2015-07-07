from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import csv
from utility import credits, category
from utility import initialize, marks_obtained
from utility import percentage, input_marks, drop_subjects
from data import subject, data


# loads the subject names, credits and category against the subject codes
def index(request):
	return HttpResponseRedirect('/home/')


def home(request):
	return HttpResponse(data)
# include back marks in percentage CHECKBOX
