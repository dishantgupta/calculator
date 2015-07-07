import csv
from data import subject, applied, core, humanities
from data import credit_4, credit_2, credit_3, credit_1, credit_8
from data import data, back


def category(code):
	code = int(code)
	if code in applied:
		return 'applied'
	elif code in core:
		return 'core'
	elif code in humanities:
		return 'humanities'

def credits(code):
	code = int(code)
	if code in credit_2:
		return 2
	elif code in credit_3:
		return 3
	elif code in credit_4:
		return 4
	elif code in credit_1:
		return 1
	elif code in credit_8:
		return 8

def initialize():
	"""
	loads the subject names, credits and 
	category against the subject codes
	"""
	i = 1
	while (i < 9):
		data['semester' + str(i)] = []
		code = 1
		while (True):
			try: 
				sub_code = str(100*i + code)
				data['semester' + str(i)].append({
						'name': subject[sub_code],
						'credits': credits(sub_code),
						'marks': 0,
						'category': category(sub_code)
					})
				code = code + 1
			except KeyError:
				break
		i = i + 1
	return data

def input_marks():
	marks = []
	with open('/home/delhivery/calculator/calc/sample.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			marks.append(row[1])
	i = 1
	index = 0
	while (i < 9):
		data['semester' + str(i)] = []
		code = 1
		while (True):
			try: 
				sub_code = str(100*i + code)
				data['semester' + str(i)].append({
						'name': subject[sub_code],
						'credits': credits(sub_code),
						'marks': marks[index],
						'category': category(sub_code)
					})
				code = code + 1
				index = index + 1
			except KeyError:
				break
		i = i + 1

def marks_obtained(semester):
	"""
	obt: marks obtained in semester
	total: total marks for semester

	returns:
	percentage or marks obtained
	"""
	obt = 0
	sem = data['semester' + str(semester)]
	for sub in sem:
		if (sub['marks'] > 40):	# not including the back-waale subjects
			obt = obt + (sub['credits'] * int(sub['marks']))
		else: 
			back = back + 1
	return obt

def total_credits(semester):
	total = 0
	sem = data['semester' + str(semester)]
	for sub in sem:
		total = total + sub['credits']
	return total

def percentage(sem):
	"""
	function to return the marks otained or percentage till the passed sem.
	
	args:
	sem: semester till the percentage needs to be calculated.
	returns:
	percentage or marks obtained in smesters
	"""
	obt = 0
	tot = 0
	i = 1
	while (i <= sem):
		obt = obt + marks_obtained(i)
		tot = tot + total_credits(i)
		i = i + 1
	return obt/tot

def drop_subjects():
	
	applied_sub = {'category': 'applied', 'marks': 100, 'name': '', 'credits': ''}
	core_sub = {'category': 'core', 'marks': 100, 'name': '', 'credits': ''}
	humanities_sub = {'category': 'humanities', 'marks': 100, 'name': '', 'credits': ''}
	i = 1
	while(i <= 8):
		sem = data['semester'+str(i)]
		for sub in sem:
			if sub['category'] == 'applied':
				if (int(sub['marks']) < applied_sub['marks']):
					applied_sub = sub
			elif sub['category'] == 'core':
				if (int(sub['marks']) < core_sub['marks']):
					core_sub = sub
			elif sub['category'] == 'humanities':
				if (int(sub['marks']) < humanities_sub['marks']):
					humanities_sub = sub
		i = i + 1
	print applied_sub, core_sub, humanities_sub
	