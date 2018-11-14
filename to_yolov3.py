import os, glob, re
import tqdm

lists = glob.glob(os.path.join('*.xml'))


def new_metrics(imwid, imhei,xmin,ymin,xmax,ymax):
	width = xmax - xmin
	height = ymax - ymin
	cx = (0.5 * width)/imwid
	cy = (0.5 * height)/imhei
	width /= imwid
	height /= imhei
	return  cx, cy, width, height



for afile in tqdm.tqdm(lists):
	name_checker = 0
	nfile = afile[:-3] + 'txt'
	with open(afile) as pfile:
		lines = pfile.readlines()
	new = open(nfile,'w')
	for j,line in enumerate(lines):
		if re.search('width',line):
			imwid = int(re.search('\d\d\d',line).group())

		if re.search('height',line):
			imhei = int(re.search('\d\d\d',line).group())

		if re.search('<object>',line):
			theclass = int(re.search('\d',lines[j+1]).group())  -1

		if re.search('xmin',line):
			xmin = int(re.search('\d\d?\d?',line).group())

		if  re.search('ymin',line):
			ymin = int(re.search('\d\d?\d?',line).group())

		if re.search('xmax',line):
			xmax = int(re.search('\d\d?\d?',line).group())

		if re.search('ymax',line):
			ymax = int(re.search('\d\d?\d?',line).group())
			cx, cy, width, height = new_metrics(imwid,imhei,xmin,ymin,xmax,ymax)
			new.write(str(theclass)+' '+str(cx)+' '+str(cy)+' '+str(width)+' '+str(height)+'\n')
	new.close()


