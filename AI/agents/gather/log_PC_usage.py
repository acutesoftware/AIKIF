# log_usage.py  written by Duncan Murray 13/1/2014

from win32gui import GetWindowText, GetForegroundWindow
import sys
import time
sys.path.append('S://duncan//C//user//dev//src//python//aspytk')
import lib_file as fle
fname = 'T:\\user\\AIKIF\\pc_usage.txt'

def main():
	lstRaw = []
	prevText = ''
	startTime = fle.TodayAsString()
	tot_seconds = 1
	try:
		while True:
			txt = GetWindowText(GetForegroundWindow())
			#print(txt)
			#fle.AppendToFile(fname, fle.TodayAsString() + ' ' + txt + '\n')
			if txt == prevText:
				tot_seconds = tot_seconds + 1
			else:
				lstRaw.append(startTime + ',' + format(tot_seconds, "03d") + ',' + txt)
				prevText = txt
				tot_seconds = 1
				startTime = fle.TodayAsString()
			time.sleep(1)
			if fle.TodayAsString()[-3:] == ':00':
				lstRaw.append(startTime + ',' + format(tot_seconds, "03d") + ',' + txt)
				print('Recording data')
				tot_seconds = 1
				startTime = fle.TodayAsString()
				record(lstRaw)
				lstRaw = []

	except KeyboardInterrupt:	
		print("logging halted")
		lstRaw.append(startTime + ',' + format(tot_seconds, "03d") + ',' + txt)   # save the latest record
		record(lstRaw)

	
def record(lst):
	with open(fname, "a") as f:
		for txt in lst:
			f.write(txt + '\n')
	tot_seconds = 1
		
if __name__ == '__main__':
	main()
	
	
