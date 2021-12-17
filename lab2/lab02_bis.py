from lab02 import parse_file, TermNotFoundError

f = '/home/guest_04/Desktop/SP1_Lab2/dat_ex01_anisole_IR.jdx'
try:
	data = parse_file(f, search = 'XYDATA')[1:]
	minx = float(parse_file(f, search = 'MINX')[0])
	maxx = float(parse_file(f, search = 'MAXX')[0])
	npoints = float(parse_file(f, search = 'NPOINTS')[0])
	delta = float(parse_file(f, search = 'DELTAX')[0])

except TermNotFoundError:
	print('error')

#xsteps = len(data[0]) -1
#xvals = [float(x[0].split(' ')[0]) for x in data]


#diff_x = []
#for i, x in enumerate(xvals[1:]):
#	diff_x.append(xvals[i]-xvals[i+1])
#print(mean(diff_x)
delta_comp = (maxx-minx)/npoints
print(delta_comp- delta)
