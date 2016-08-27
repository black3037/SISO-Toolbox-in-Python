import re
import numpy as np
import matplotlib.pyplot as plt
import cmath
import sys
from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import subprocess


def tf(numerator,denominator):

	num = numerator
	den = denominator

	# Get the size of the numerator & denominator
	len_n = len(num)
	len_d = len(den)
	# Numerator - Constant
	if len_n == 1:
		a = str(num[0])
		top = a

	# Numerator - 1st Order
	if len_n == 2:
		if num[0] == 0:
			a = str(num[1])
			top = a
		elif num[0] > 0:
			a = str(num[0])
			b = str(num[1])
			top = a + 's' + ' ' + '+' + ' ' + b

	# Numerator - 2nd Order 
	if len_n == 3:
		if (num[0] == 0 and num[1] == 0):
			a = str(num[2])
			top = a
		
		elif num[0] == 0:
			a = str(num[1])
			b = str(num[2])
			top = a + 's' + ' ' + '+' + ' ' + b

		elif (num[1] == 0 and num[0] > 0 and num[2] > 0):
			a = str(num[0])
			b = str(num[2])
			top = a + u'\u00B2' + ' ' + '+' + ' ' + b

		elif (num[0] > 0 and num[1] == 0 and num[2] == 0):
			a = str(num[0])
			top = a + u'\u00B2'
			
		elif num[0] == 0 or num[1] == 0:
			a = str(num[2])
			top = a


		else :
			a = str(num[0])
			b = str(num[1])
			if num[2] == 0:
				top = a + u'\u00B2' + ' ' + '+' + ' ' + b + 's'
			else:
				c = str(num[2])
				top = a + u'\u00B2' + ' ' + '+' + ' ' + b + 's' + ' ' + '+' + ' ' + c

	# Numerator - 3nd Order 
	if len_n == 4:
		if (num[0] == 0 and num[1] == 0 and num[2] ==0):
			a = str(num[3])
			top = a
		
		elif (num[0] == 0 and num[1] == 0 and num[2] > 0 and num[3] > 0):
			a = str(num[2])
			b = str(num[3])
			top = a + 's' + ' ' + '+' + ' ' + b

		elif num[0] == 0:
			a = str(num[1])
			b = str(num[2])
			c = str(num[3])
			top = a + u'\u00B2' + ' ' + '+' + ' ' + b + 's' + ' ' + '+' + ' ' + c

		elif (num[1] == 0 and num[0] > 0 and num[2] > 0 and num[3] > 0):
			a = str(num[0])
			b = str(num[2])
			c = str(num[3])
			top = a + u'\u00B3' + ' ' + '+' + ' ' + b + 's' + ' ' + '+' + ' ' + c

		elif (num[0] > 0 and num[1] == 0 and num[2] == 0 and num[3] > 0):
			a = str(num[0])
			b = str(num[3])
			top = a + u'\u00B3' + ' ' + '+' + ' ' + b
			
		elif (num[0] > 0 and num[1] == 0 and num[2] == 0 and num[3] == 0):
			a = str(num[0])
			top = a + u'\u00B3'

		else :
			a = str(num[0])
			b = str(num[1])
			c = str(num[2])
			d = str(num[3])
			top = a + u'\u00B3' + ' ' + '+' + ' ' + b + u'\u00B2' + ' ' + '+' + ' ' + c + 's' + ' ' + '+' + '' + d

	if len_n > 4:
		return "The degree of the polynomial is to high, please restrict your transfer function to a 3rd or lower order system"

	# Denominator - Constant
	if len_d == 1:
		a = str(den[0])
		bottom = a

	# Denominator - 1st Order
	if len_d == 2:
		if den[0] == 0:
			d = str(den[1])
			top = d
		elif den[0] > 0:
			d = str(den[0])
			e = str(den[1])
			bottom = d + 's' + ' ' + '+' + ' ' + e
		else:
			d = str(den[0])
			e = str(den[1])
			bottom = d + 's' + ' ' + '+' + ' ' + e

	# Denominator - 2nd Order
	if len_d == 3:
		if (den[0] == 0 and den[1] == 0):
			d = str(den[2])
			bottom = d
		
		elif den[0] == 0:
			d = str(den[1])
			e = str(den[2])
			bottom = d + 's' + ' ' + '+' + ' ' + e

		elif (den[1] == 0 and den[0] > 0 and den[2] > 0):
			d = str(den[0])
			e = str(den[2])
			bottom = d + u'\u00B2' + ' ' + '+' + ' ' + e

		elif (den[0] > 0 and den[1] == 0 and den[2] == 0):
			d = str(den[0])
			bottom = d + u'\u00B2'
			
		elif den[0] == 0 or den[1] == 0:
			d = str(den[2])
			bottom = d

		else :
			d = str(den[0])
			e = str(den[1])
			if den[2] == 0:
				bottom = d + 's' + u'\u00B2' + ' ' + '+' + ' ' + e + 's'
			else:
				f = str(den[2])
				bottom = d + 's' + u'\u00B2' + ' ' + '+' + ' ' + e + 's' + ' ' + '+' + ' ' + f


	# Denominator - 3nd Order 
	if len_d == 4:
		if (den[0] == 0 and den[1] == 0 and den[2] ==0):
			a = str(den[3])
			bottom = a
		
		elif (den[0] == 0 and den[1] == 0 and den[2] > 0 and den[3] > 0):
			a = str(den[2])
			b = str(den[3])
			bottom = a + 's' + ' ' + '+' + ' ' + b

		elif den[0] == 0:
			a = str(den[1])
			b = str(den[2])
			c = str(den[3])
			bottom = a + u'\u00B2' + ' ' + '+' + ' ' + b + 's' + ' ' + '+' + ' ' + c

		elif (den[1] == 0 and den[0] > 0 and den[2] > 0 and den[3] > 0):
			a = str(den[0])
			b = str(den[2])
			c = str(den[3])
			bottom = a + u'\u00B3' + ' ' + '+' + ' ' + b + 's' + ' ' + '+' + ' ' + c

		elif (den[0] > 0 and den[1] == 0 and den[2] == 0 and den[3] > 0):
			a = str(den[0])
			b = str(den[3])
			bottom = a + u'\u00B3' + ' ' + '+' + ' ' + b
			
		elif (den[0] > 0 and den[1] == 0 and den[2] == 0 and den[3] == 0):
			a = str(den[0])
			bottom = a + u'\u00B3'

		else :
			a = str(den[0])
			b = str(den[1])
			c = str(den[2])
			d = str(den[3])
			bottom = a + u'\u00B3' + ' ' + '+' + ' ' + b + u'\u00B2' + ' ' + '+' + ' ' + c + 's' + ' ' + '+' + ' ' + d

	if len_d > 4:
		return "The degree of the polynomial is to high, please restrict your transfer function to a 3rd or lower order system"

	result = top + '\n' + '-------------' + '\n' + bottom
	return result

def zpk(zeros,poles,gain):
	
	len_z = len(zeros)
	len_p = len(poles)
	gain = str(gain)
	zeros_list = []
	poles_list = []
	for i in zeros:
		if i > 0:
			sign = '-'
		elif i < 0:
			i = abs(i)
			sign = '+'

		zero = str(i)
		factor = '(' + ' ' + 's' + ' ' + sign + ' ' + zero + ' ' + ')'
		zeros_list.append(factor)

	for j in poles:
		if j > 0:
			p_sign = '-'
		elif j < 0:
			j = abs(j)
			p_sign = '+'

		pole = str(j)
		p_factor = '(' + ' ' + 's' + ' ' + p_sign + ' ' + pole + ' ' + ')'
		poles_list.append(p_factor)

		top = str()
		for k in zeros_list:
			top = top + str(k)

		bottom = str()
		for l in poles_list:
			bottom = bottom + str(l)


	return gain + ' ' + top + '\n' + '-------------' + '\n' + bottom

# This currently only works for 2nd order systems, more works needs to be done for higher Order systems.
def tf2ss(T):
	T1,T2=T.split('-------------',1)
	b = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", T1)
	a = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", T2)
	b_list = map(float,b)
	a_float_list = map(float,a)
	a_list = []

	for i in a_float_list[1:]:
		a_list.append(i)
	A = np.array([])
	size = len(a_list)
	A = np.zeros((size,size))

	if size == 2:
		for i in range(size):
			A[0,i] = 1.0
			A[i,0] = 0.0
			A[1,i-1] = a_list[1]
			A[1,i] = a_list[0]

	if size == 3:
		A[0,1] = 1.0
		A[1,2] = 1.0
		A[2,0] = a_list[2]
		A[2,1] = a_list[1]
		A[2,2] = a_list[0]


	B = np.zeros((size))
	B[size-1] = 1.0

	size_a = len(a_list)
	size_b = len(b_list)
	D = b_list[0]
	b0 = b_list[0]
	C = []
	for i in a_list:
		for j in b_list:
			C.append(j - i*b0)
         
	return A, D, C

def step(T):
	T1,T2=T.split('-------------',1)
	b = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", T1)
	a = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", T2)
	a_float_list = map(float,a)
	b_float_list = map(float,b)
	a_list = []
	b_list = []
	for i in a_float_list:
		a_list.append(i)

	for j in b_float_list:
		b_list.append(j)



	# 1st Order System
	if len(a_list) == 2:
		if abs(a_list[0]) > 0:
			a_list[1] = a_list[1]/a_list[0]
			p = float(a_list[1])

		else:
			p = float(a_list[1])

		t = np.linspace(0,1,1000)
		y = 1 - np.exp(-p*t)

	# 2nd Order System
	elif (len(a_list) == 3 and len(b_list) == 1):
		if abs(a_list[0]) > 0:
			a_list[1] = a_list[1]/a_list[0]
			a_list[2] = a_list[2]/a_list[0]
			wn = np.sqrt(a_list[2])
			zeta = a_list[1]/(2*wn)
			wd = wn*np.sqrt(1-zeta**2 + 0j)
			theta = np.arccos(zeta + 0j)
		else:
			wn = np.sqrt(a_list[2])
			zeta = a_list[1]/(2*wn)
			wd = wn*np.sqrt(1-zeta**2 + 0j)
			theta = np.arccos(zeta + 0j)

		t = np.linspace(0,(4.6/(zeta*wn))+2,1000)
		y = np.real(1.0 - (np.exp(-zeta*wn*t + 0j)/np.sqrt(1-zeta**2 + 0j))*np.sin(wd*t + theta + 0j))

	elif (len(a_list) == 3 and len(b_list) == 2):
		if abs(a_list[0]) > 0:
			a_list[1] = a_list[1]/a_list[0]
			a_list[2] = a_list[2]/a_list[0]
			wn = np.sqrt(a_list[2])
			zeta = a_list[1]/(2*wn)
			wd = wn*np.sqrt(1-zeta**2 + 0j)
			theta = np.arccos(zeta + 0j)
		else:
			wn = np.sqrt(a_list[2])
			zeta = a_list[1]/(2*wn)
			wd = wn*np.sqrt(1-zeta**2 + 0j)
			theta = np.arccos(zeta + 0j)
		if (abs(b_list[0]) > 1.0):
			a = b_list[1]/b_list[0]
		else:
			a = b_list[1]

		t = np.linspace(0,(4.6/(zeta*wn))+2,1000)
		
		y = np.real(1.0-(np.cos(np.sqrt(-zeta**2 + 1 + 0j)*t*wn))*np.exp(-t*zeta*wn + 0j) + ((np.sin(np.sqrt(-zeta**2 + 1 + 0j)*t*wn))*np.exp(-t*zeta*wn + 0j)*(-zeta*a + wn))/(np.sqrt(-zeta**2 + 1 + 0j)*a))


	x = np.linspace(1,1,1000)
	plt.plot(t,y,'k-')
	plt.plot(t,x,'k--')
	#plt.fill(t,y, 'red', alpha=0.4)
	if (len(a_list) == 3):
		plt.fill_between(t,y,1.0,color='b',alpha=0.5)
	else:
		pass
	
	plt.title('Step Response',fontsize=15,weight='bold')
	plt.xlabel('time (sec)',fontsize=12,weight='bold')
	plt.ylabel('Amplitude',fontsize=12,weight='bold')
	plt.grid()

	return plt.show()

def pzmap(T):
	T1,T2=T.split('-------------',1)
	b = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", T1)
	a = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", T2)
	a_float_list = map(float,a)
	b_float_list = map(float,b)
	a_list = []
	b_list = []
	for i in a_float_list:
		a_list.append(i)

	for j in b_float_list:
		b_list.append(j)	

	poles = np.roots(a_list)
	zeros = np.roots(b_list)
	points = np.concatenate((poles,zeros))

	marker="--"
	plt.plot(poles.real, poles.imag,'x',color='black',markersize=8,mew=2)
	plt.plot(zeros.real, zeros.imag ,'o', color='red',markersize=8)
	plt.axhline(linewidth=1, color='black', linestyle='--')
	plt.margins(y=.5, x=.5)
	plt.title('Pole-Zero Map',fontsize=15,weight='bold')
	plt.xlabel('Re',fontsize=12,weight='bold')
	plt.ylabel('Im',fontsize=12,weight='bold')
	plt.grid()
	
	return plt.show()

#Not fully implemented.
def PID(T,OS,Ts,Tr):
	T1,T2=T.split('-------------',1)
	b = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", T1)
	a = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", T2)
	a_float_list = map(float,a)
	b_float_list = map(float,b)
	a_list = []
	b_list = []
	for i in a_float_list:
		a_list.append(i)

	for j in b_float_list:
		b_list.append(j)

	if abs(a_list[0]) > 0:
		a_list[1] = a_list[1]/a_list[0]
		a_list[2] = a_list[2]/a_list[0]
		wn = np.sqrt(a_list[2])
		zeta = a_list[1]/(2*wn)
		wd = wn*np.sqrt(1-zeta**2 + 0j)
		theta = np.arccos(zeta + 0j)
	else:
		wn = np.sqrt(a_list[2])
		zeta = a_list[1]/(2*wn)
		wd = wn*np.sqrt(1-zeta**2 + 0j)
		theta = np.arccos(zeta + 0j)

	t = np.linspace(0,(4.6/(zeta*wn))+2,1000)

	Ki = 33.66
	Kd = 1.025
	Kp = 11.7499


	y = Ki - ((Ki - Kd*wn**2)*(np.cosh(t*wn*(zeta**2 - 1 + 0j)**(1/2)) - (np.sinh(t*wn*(zeta**2 - 1 + 0j)**(1/2))*(wn*zeta + (Kp*wn**2 - 2*Ki*wn*zeta)/(Ki - Kd*wn**2)))/(wn*(zeta**2 - 1)**(1/2))))/np.exp(t*wn*zeta + 0j)

	plt.plot(t,y,'k-')
	return plt.show()

def tfchar(T):
	T1,T2=T.split('-------------',1)
	a = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", T2)
	a_float_list = map(float,a)
	a_list = []
	for i in a_float_list:
		a_list.append(i)

	if len(a_list) == 2:
		return 'NaN or inf'
	elif len(a_list) > 2:
		if abs(a_list[0]) > 0:
			a_list[1] = a_list[1]/a_list[0]
			a_list[2] = a_list[2]/a_list[0]
			wn = np.sqrt(a_list[2])
			zeta = a_list[1]/(2*wn)
		else:
			wn = np.sqrt(a_list[2])
			zeta = a_list[1]/(2*wn)
	
	Ts = 4.0/(zeta*wn)
		
	OS = np.real(np.exp((-np.pi*zeta)/(np.sqrt(1-zeta**2 + 0j)))*100)
	OS = float(OS)
	return OS,Ts

def sisotool(*argv):


	return subprocess.call("python sisotool.py", shell=True)














