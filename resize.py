import os
from PIL import Image

spath='./source'
tpath='./target'
sfilenames = os.listdir(spath)

for sfilename in sfilenames:
	sname=os.path.join(spath,sfilename)
	tname=os.path.join(tpath,sfilename)
	simg = Image.open(sname)
	timg = simg.resize((864, 480),Image.ANTIALIAS)
	timg.save(tname,'jpeg')        
	# print(simg.size)
	# print(timg.size)