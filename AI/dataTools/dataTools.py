# coding: utf-8
# dataTools.py   written by Duncan Murray 9/4/2014  (C) Acute Software
# data tools for AIKIF


def DataSet(fname):
	# defines a dataset
	print('dataset defined = ' + fname)
	

def main():
	print('data tools')
	testFile = 'test.csv'
	DataSet(testFile)
	AnalyseCSV(testFile)
	
def AnalyseCSV(fname):
	print('dataTools.py - AnalyseCSV("' + fname + '")')
	
	
if __name__ == '__main__':
    main()	
	

