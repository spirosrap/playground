from datetime import datetime 
import os
startTime= datetime.now() 
os.system("python siever.py 10000000")
timeElapsed=datetime.now()-startTime
print('Time elpased (hh:mm:ss.ms) {}'.format(timeElapsed))