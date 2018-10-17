import os 
import sys 


# ----------------- Path to unzip -------------------

path = '/home/swebb/oz100/archive_NOAO_data/data_drop/'

# ----------------- UnZip all files in path ---------

for filename in os.listdir(path): 
	if filename.endswith('.fz'): 
		unzip = 'funpack ' + str(path + filename)
		print(unzip)
		os.system(unzip)
		
