import numpy as np
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
from astropy import wcs
from astropy.wcs import WCS
from astropy.io import fits
import sys
import math
import os
import glob
import sys
from sortedcontainers import SortedDict
import datetime as dt
import imageio
import os
from PIL import Image
from matplotlib.colors import LogNorm
from astropy.nddata.utils import Cutout2D
from astropy import units as u
import datetime as dt 
import glob

path = '/home/swebb/oz100/archive_NOAO_data/data_drop'


for filename in os.listdir(path): 
	if filename.endswith('.fits'): 
		print(filename)
		hdulist = fits.open(path + '/'+ filename)
		head = hdulist[0].header
		field = head['OBJECT']
		date = dt.datetime.strptime(head['DATE'], '%Y-%m-%dT%H:%M:%S')
		year = date.strftime('%Y')
		month = date.strftime('%m')
		print(month)
		
		move_path_field = '/home/swebb/oz100/archive_NOAO_data/'+ year+'/' + month + '/' + field +  '/'
		move_path_year = '/home/swebb/oz100/archive_NOAO_data/'+ year+ '/ '
		move_path_month = '/home/swebb/oz100/archive_NOAO_data/'+ year+ '/ ' + month + '/' 
	
		if not os.path.exists(move_path_year): 
			 os.makedirs(move_path_year, 0o755)
		else: 
			pass 
			
		if not os.path.exists(move_path_month): 
			 os.makedirs(move_path_month, 0o755)
		else: 
			pass 
				
			
		if not os.path.exists(move_path_field): 
			 os.makedirs(move_path_field, 0o755)
		else: 
			pass 
		
		os.rename(path + '/'+ filename, move_path_field + '/' + filename)
		
#hdulist= fits.open()
#hrd = hdulist[0].header
#field = hrd['OBJECT']
#date = dt.datetime.strptime(hrd['DATE'], '%Y-%m-%dT%H:%M:%S') 
#print(date) 
		
