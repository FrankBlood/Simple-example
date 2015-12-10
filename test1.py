import os
import time

source=[r'E:\GitHub\hello-world\test1',r'E:\GitHub\hello-world\test2']
target_dir=r'E:\GitHub\backup'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command="zip -qr '%s' %s" %(target,''.join(source))

if os.system(zip_command)==0:
	print('Successful backup to',target)
else:
	print('Backup FAILED')
	print(''.join(source))