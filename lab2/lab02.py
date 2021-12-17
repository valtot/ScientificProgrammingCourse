import os
import re
import sys



def parse_file(f, search: str = None):
	fDict = {}
	keys =[] 
	values = []
	with open(f) as fobj:
		for ind, el in enumerate(fobj):
			#print(type(el))
			if el.startswith("##"):
				keys.append(el.rstrip().lstrip('##').split('=')[0])
				if len(el.rstrip().lstrip('##').split('='))<2:
					values.append([''])
				else:
					values.append([el.rstrip().lstrip('##').split('=')[1]])
				#fDict = {el.lstrip('##').split('=')[0]: el.lstrip('##').split('=')[1]}

			
			elif not el.startswith("##"):
				values[-1].append(el.rstrip().lstrip('##').split('=')) 
	fDict = {key: val for key, val in zip(keys, values)}		 
	if search != None:
		try:	
			search_val = fDict[search.upper()]
			return search_val 
		except KeyError:
			raise TermNotFoundError()
			
			
	fDict = {key: val for key, val in zip(keys, values)}			
	return fDict
		

class TermNotFoundError(Exception):
	def __init__(self, msg = None):
		if msg == None:
			msg = 'Term not found in the selected file'
		super().__init__(msg)
		
if __name__ == '__main__':
 
	f = '/home/guest_04/Desktop/SP1_Lab2/dat_ex01_anisole_IR.jdx'
	try:
		print(parse_file(f, search = 'pippo'))
	except TermNotFoundError:
		print('error')
		
