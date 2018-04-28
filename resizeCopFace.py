
# -*- coding: utf-8 -*-      
import os  
import argparse
import cv2
def file_name(file_dir):   
	L=[]   
	for root, dirs, files in os.walk(file_dir):
		for file in files:  
	   		if os.path.splitext(file)[1] == '.jpg':  
	   			L.append(file)  
                        if os.path.splitext(file)[1] == '.txt':
                                L.append(file[0:-4])
			if os.path.splitext(file)[1] == '.png':
                                L.append(file)
                        if os.path.splitext(file)[1] == '.jpeg':
                                L.append(file)
	return L 


def parse_args():
  parser = argparse.ArgumentParser(
    description='Generate filelist.txt  ->  ****.jpg 0'
    )
  parser.add_argument(
    '--srcdir', dest='srcdir', default=None, type=str
    )
  parser.add_argument(
    '--dstdir', dest='dstdir', default=None, type=str
    )
  return parser.parse_args()

args = parse_args()

if __name__ == '__main__':
  print args
  imglist=file_name(args.srcdir)
  for imgname in imglist:
     srcimg=args.srcdir+'/'+imgname
     print srcimg
     image = cv2.imread(srcimg)
     resizeimg=cv2.resize(image,(256,256),interpolation=cv2.INTER_CUBIC)
     dstimg=args.dstdir+'/'+imgname
     cv2.imwrite(dstimg,resizeimg) 
