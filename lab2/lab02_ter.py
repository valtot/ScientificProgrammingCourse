from lab02 import parse_file, TermNotFoundError

f = '/home/guest_04/Desktop/SP1_Lab2/dat_ex01_anisole_IR.jdx'
try:
	data = parse_file(f, search = 'XYDATA')[1:]data = parse_file(f, search = 'XYDATA')[1:]
except TermNotFoundError():
