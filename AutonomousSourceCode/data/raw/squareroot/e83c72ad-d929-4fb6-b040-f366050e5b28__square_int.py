#-----------------------------------------------------------------------------------
#! /usr/bin/env python
# --------------------------------------------------------
# SQUARE ROOT CALCULATOR USING INTERVALL-SPLITTING
#
# description:
#	simple s_root approximation function _square_root(param1)
#	usage: int.py => enter positive number
#
# options: 
# 	return_param_1 = number of needed steps
#  	return_param_2 = final result of square root
#
# (c) fred
# --------------------------------------------------------
# settings [don't change unless you are babo]
steps = 1000 # number of max loop_steps
debug = 5   # max number of lines for debugging output

# app_description
print   '[-----------------------------]\n'+ \
	'|-- SQUARE ROOT  CALCULATOR --|\n'+ \
	'|-----------------------------|\n'+ \
	'|--  using intervall-split  --|\n'+ \
	'[-----------------------------]'

# normal input
num = raw_input('[*] Please insert number: ')

# func_for_calculation using black magic c0de :)
def _square_root(num):

	# lazy error_checking for failheads
	try: num = float(num)
	except ValueError: 
		print '[!] Value has to be a number'
		return -1
	if(num<=0): 
		print '[!] Value has to be positive'; 
		return -2

	print '[-] Calculating square root of: '+str(num)

	#set start_intervall limits [0,num]
	_I_o = num; 	# upper limit
	_I_u = 0; 	# lower limit
	print '[-] Lower limit: '+str(_I_u)+' Upper limit: '+str(_I_o)
	if(int(debug)>0): print '[-] Debug-information:'

	#black magic :>
	for i in range(0, steps): 

		_I_t = (_I_o+_I_u)/2 	 # define intervall-split
		if i<debug:              # print temp value, temp intervall and square
			print '['+str(i+1)+'] value: '+str(_I_t) \
			+'\tIntervall: ['+str(_I_u)+','+str(_I_o)+']'
		# check by type_cast to str char_by_char for len(_x_) cause no
		# external routines were allowed such as substr(), find() etc..
		# accuracy max 10^-10 due to length of [float]
		if(str(_I_t*_I_t)==str(num)):  break
		elif(_I_t*_I_t>num): _I_o=_I_t # change upper intervall limit
		elif(_I_t*_I_t<num): _I_u=_I_t # change lower intervall limit

	print '[.] .......................'
	if(i==steps-1):
		print '[!] '+str(steps-1)+' steps are reached: cant guarantee full accuracy'
		
	res1 = str(i+1)		# final number of steps
	res2 = str(_I_t)	# final result
	print '['+res1+'] Found square root with accuracy of 10^-10: ['+res2+']' # output
	return(res1,res2)	# return the shit to _main_ if needed (addr of call func)

# simple call root_function, usage of return[0],return[1] possible as well
_square_root(num)

# EOF 12.2013
