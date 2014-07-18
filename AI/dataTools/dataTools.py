# -*- coding: utf-8 -*-
# dataTools.py		written by Duncan Murray  9/4/2014
# Module to manage and process datasets - basically a wrapper
# around existing lists, with added documentation and logging
# for AIKIF and commonly used functions for simple data processing
#
#
# Functions
#	Transform columns to new tables
#	Generate SQL for imports
# 	Import and convert CSV to XLS
#	uses (?replaces?) most of aspytk data.py
 
# Usage:
    # from AIKIF import dataTools as ds
    # ds = dat.DataSet(?C_COUNTRY.XLS?)   		  #existing table (your source file)
    # dsOutput = dat.DataSet(?FACT_FILE.XLS?)   #output table after processing
    # cols = ds.IntentifyColumns()   # returns a dict with detailed estimates of col types
    # mapping = ds.MapTo(dsOutput)
    # mapping.col(?country code?, ?FACT_COUNTRY_ID?)
    # mapping.col(?country name?, ?FACT_COUNTRY_DESC?)
    # countryRules = bus.DatasetRules(ds)	# define rules for this dataset
    # countryRules.Add(?China (excl Mongolia)?, ?China?)
    # countryRules.Add(?AUSTRALIA?, ?Australia?)

    # mapping.Process()	# does the work moving data from file 1 to file 2 with column mappings
    # countryRules.Apply(dsOutput)  # apply rules on which file you want 
    # dsOutput.Export()

import os
import sys
import csv
import string


try:
    import xlrd as xl        # NOTE - xlrd imports fine from python shell, but this line cant find it
except:
    print('you need to install xlrd')

fldr = '..//..//data//temp//'
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "data" + os.sep + "temp") 

print(root_folder)

def TEST():
    print('Data tools test...')
    url = 'http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&standard australian classification of countries, 2011, version 2.2.xls&1269.0&Data Cubes&EE21444EE8F2C99CCA257BF30012B66F&0&2011&01.10.2013&Latest'
    fname = fldr + 'test.xlsx'
    dl_fname = fldr + 'test-download.xlsx'
    #DownloadFile(url, dl_fname)
    #csv_from_excel(fname , os.getcwd())
    testFile = fldr + 'test.csv'
    CreateRandomCSVFile(testFile)
    GenerateSQL(testFile, 'MY_TABLE', testFile + '.SQL', headerRow=1)

    CreateRandomIndentedCSVFile(fldr + 'indented.csv')
#	ExtractTable(f, tmpFile, extractList[1]['colList'], 8, 1, 52, 9)
    AutoFillCSV(fldr + 'indented.csv', fldr + 'indented-fixed.csv', ['grouping', 'code', 'desc'],  ['grouping'])   # autofill FIRST col based on prev values
    RemoveBlankRecs(fldr + 'indented-fixed.csv', fldr + 'indented-fixed-and-no-blanks.csv', 2)

def delete_file(f):
    try:
        os.remove(f)
    except:
        pass

def csv_from_excel(excel_file, pth):
    opFname = ''
    print('converting file ' + excel_file + '  to folder ' + pth)
    workbook = xl.open_workbook(pth + '\\' + excel_file)
    all_worksheets = workbook.sheet_names()
    for worksheet_name in all_worksheets:
        if worksheet_name != 'Pivot':
            print('converting - ' + worksheet_name)
            worksheet = workbook.sheet_by_name(worksheet_name)
            opFname = pth + '\\' + os.path.splitext(excel_file)[0] + '_' + worksheet_name + '.csv'
            print('SAVING - ' + opFname)
            csv_file = open(opFname, 'wb')
            #csv_file = open(pth + ''.join([worksheet_name,'.csv']), 'wb')
            wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

            for rownum in xrange(worksheet.nrows):
                wr.writerow([unicode(entry).encode("utf-8") for entry in worksheet.row_values(rownum)])
            csv_file.close()
        else:
            print('ignoring tab - ' + worksheet_name)
    

def DownloadFile(url, fname):
    # bug here - you need to wait for download to finish
    net.DownloadFile(url, fname)

def addSampleData(fname, content):
    wr = csv.writer(open(fname, 'at'), quoting=csv.QUOTE_ALL, lineterminator='\n')
    wr.writerow(content)	
    
def CreateRandomCSVFile(fname):
    delete_file(fname)
    content = [['id', 'code', 'desc'], ['1', 'S', 'AAA'], ['2', 'B', 'BBB'], ['3', 'X', 'Long description']]
    for row in content:
        addSampleData(fname, row)
            
    
def CreateRandomIndentedCSVFile(fname):
    delete_file(fname)
    content = [['grouping', 'code', 'desc'], ['1', 'S', 'AAA'], [' ', 'T', 'BBB'], ['3', 'X', 'Long description'], ['', 'Y', 'Long description']]
    for row in content:
        addSampleData(fname, row)
            
def IntentifyColumns(fname):
    # returns a dict with detailed estimates of col types
    print('IntentifyColumns(' + fname + '):')
    
def DataSet(fname):
    # defines a dataset
    print('dataset defined = ' + fname)

def MapTo(opFile):
    pass

def GetColumnList(csvFile):
    with open(csvFile, 'rt') as inf:
        inrd = csv.reader(inf)
        names = next(inrd)
    inf.close()
    return names

def GetCountUniqueValues(fname, colNum, colText, topN_values, opFile):
    cols = collections.Counter()
    with open(fname) as input_file:
        for row in csv.reader(input_file, delimiter=','):
            cols[row[colNum]] += 1
    print (colText, Dict2String(cols.most_common()[0:topN_values]))
    addSampleData(opFile, colText + ',' +  Dict2String(cols.most_common()[0:topN_values]))

def AnalyseCSV_File(datafile, opFolder):
    baseName = opFolder + '\\' + os.path.basename(datafile).split('.')[0]
    tmpfile = baseName + '.txt'
    colHeaders = dat.GetColumnList(datafile)
    colNum = 0
    for col in colHeaders:
        colText = "".join(map(str,col))    #prints JUST the column name in the list item
        print(colText)
        dat.GetCountUniqueValues(datafile, colNum, colText, 10, baseName + '_COL_VALUES.csv')
        dat.GetColumnCounts(datafile, colNum, colText, baseName + '_COL_COUNTS.csv')
        colNum = colNum + 1

def split_CSV_by_Column_names(inputfilename):  # TOK
    with open(inputfilename, 'rb') as inf:
        inrd = csv.reader(inf)
        names = next(inrd)
        outfiles = [open(n+'.csv', 'wb') for n in names]
        ouwr = [csv.writer(w) for w in outfiles]
        for w, n in zip(ouwr, names):
            w.writerow([n])
        for row in inrd:
            for w, r in zip(ouwr, row):
                w.writerow([r])
        for o in outfiles: o.close()

def split_CSV_by_Column_Values(ipFile, colName):  
    with open(ipFile, 'rb') as inf:
        inrd = csv.reader(inf)
        names = next(inrd)
        for row in csv.reader(inf):
            opName = os.path.basename(ipFile)[:-4] + '_' + row[colName] + '.csv'
            if not os.path.exists(opName):
                createSampleFile(opName, names)
            #print("Appending to ", opName)
            addSampleData(opName, row)

        
def ExtractTable(fname, opFile, opCols, startRow=1, startCol=1, endRow=5, endCol=5):			
    print('Extracting ' + os.path.basename(fname) + ' to ' + opFile)
    curRow = 1
    curCol = 1
    cols = collections.Counter()
    
    csv_file = open(opFile, 'wb')
    #wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    
    with open(fname) as input_file:
    
        for hdr in opCols:
            csv_file.write('"' + hdr + '",')
        csv_file.write('\n')
        for row in csv.reader(input_file, delimiter=','):
            if curRow >= startRow:
                if curRow <= endRow:
                    curCol = 0
                    for col in row:
                        curCol = curCol + 1
                        if curCol >= startCol:
                            if curCol <= endCol:
                                colText = "".join(map(str,col)).strip('"').strip()    #prints JUST the column name in the list item
                                csv_file.write('"' + colText + '",')
                    #wr.writerow(row)
                    csv_file.write('\n')
            curRow = curRow + 1
    csv_file.close()
    

def AutoFillCSV(fname, opFile, colList, autoFillCols):
    # Converts sub total style data to a flat list, e.g. changes:
        # 3	HEADING	
            # 31	data 1
            # 32	data 2

    print('\nAutoFilling ' + os.path.basename(fname) + ' to ' + opFile)
    curCol = 1
    lastValues = []
    for c in colList:
        lastValues.append(c)
    print(lastValues)	
    csv_file = open(opFile, 'w')
    with open(fname) as input_file:
        for row in csv.reader(input_file, delimiter=','):
            for curCol, col in enumerate(row):
                colText = "".join(map(str,col)).strip('"').strip()    #prints JUST the column name in the list item
                if curCol in autoFillCols:
                    if colText == "":
                        colText = lastValues[curCol]
                    else:
                        lastValues[curCol] = colText
                csv_file.write('"' + colText + '",')
            csv_file.write('\n')
    csv_file.close()
    
    
def RemoveBlankRecs(fname, opFile, masterCol):
    # removes lines where col number 'masterCol' is blank
    print('cleaning ' + os.path.basename(fname) )
    curCol = 1
    rowText = ''
    csv_file = open(opFile, 'w')
    with open(fname) as input_file:
        for row in csv.reader(input_file, delimiter=','):
            keepRow = True
            rowText = ''
            for curCol, col in enumerate(row):
                colText = "".join(map(str,col)).strip('"').strip()    #prints JUST the column name in the list item
                if curCol == masterCol:
                    if colText == "":
                        keepRow = False
                rowText = rowText + '"' + colText + '",'
            rowText = rowText + '\n'
            if keepRow:
                csv_file.write(rowText)
    csv_file.close()


    
        
def GenerateSQL(csvFile, tblName, opFile, headerRow=1):
    """ Generates the SQL command to create the table and
    insert the data. Output of test.csv.sql is below:
        DROP TABLE MY_TABLE  CASCADE CONSTRAINTS;
        CREATE TABLE MY_TABLE ( 
        ID VARCHAR2(2000), 
        CODE VARCHAR2(2000), 
        DESC VARCHAR2(2000), 
        UPDATE_DATE DATE
        );

        INSERT INTO MY_TABLE (ID, CODE, DESC, UPDATE_DATE) VALUES (
        'id', 'code', 'desc',  sysdate ); 
        INSERT INTO MY_TABLE (ID, CODE, DESC, UPDATE_DATE) VALUES (
        '1', 'S', 'AAA',  sysdate ); 
        INSERT INTO MY_TABLE (ID, CODE, DESC, UPDATE_DATE) VALUES (
        '2', 'B', 'BBB',  sysdate ); 
        INSERT INTO MY_TABLE (ID, CODE, DESC, UPDATE_DATE) VALUES (
        '3', 'X', 'Long description',  sysdate ); 
        COMMIT;
    
    """
    
    import re
    if tblName == '':
        tbl = str(os.path.basename(csvFile).split('.')[0])
    else:
        tbl = tblName
    if opFile == '':	
        opFile = str(os.path.basename(csvFile).split('.')[0] + '.SQL')
        
    print("Generating SQL for table " + tbl + " via " + opFile)
    # read in the CSV file header
    cols = []
    SQL_file = open(opFile, 'w')   # Note - with one version of Python this needs wb
    with open(csvFile) as input_file:
        rowNum = 0
        for row in csv.reader(input_file, delimiter=','):
            rowNum = rowNum + 1
            if rowNum == headerRow:
                for col in row:
                    cols.append(clean_column_heading(col))
                sql = GenerateSQL_CreateTable(tbl, cols)
                #print(tbl, cols, sql)
                SQL_file.write(sql)
        
    # now generate the inserts
    with open(csvFile) as input_file:
        for row in csv.reader(input_file, delimiter=','):
            SQL_file.write(GenerateSQL_Insert(tbl, row, cols))
        SQL_file.write('COMMIT;')

def clean_column_heading(txt):
    """ make the column clean for databases """
    c1 = txt.strip().replace(' ', '_').replace('.', '_').upper().strip()

    return c1.strip('_')
        
def GenerateSQL_CreateTable(tbl, cols):
    txt = 'DROP TABLE ' + tbl + '  CASCADE CONSTRAINTS;\n'
    txt = txt + 'CREATE TABLE ' + tbl + ' ( \n'
    for c in cols:
        if c != '':
            txt = txt + '    ' + c + ' VARCHAR2(2000), \n'
    txt = txt + '    UPDATE_DATE DATE\n);\n\n'
    #print (txt)
    return txt

def GenerateSQL_Insert(tbl, row, cols):
    txt = 'INSERT INTO ' + tbl + ' ('
    for c in cols:
        if c != '':
            txt = txt + c + ', '
    txt = txt + 'UPDATE_DATE) VALUES (\n'
    for d in row:
        if 'Rahman, M.M.' in row:
            print (d)
        if d != '':
            txt = txt + '\'' + d[0:1999].strip().replace('\'','\'\'').replace('"', '') + '\'' + ', '
        else:
            txt = txt + 'NULL, '
    txt = txt + ' sysdate ); \n'
    return txt
    
def head(fip, fop, numRows):
    """ extract the first numLines from fin to fop """
    with open(fip, "r") as fin:
        with open(fop, "w") as fop:
            for lines in range(1, numRows):
                fop.write(fin.readline())
    
    
if __name__ == '__main__':
    TEST()	
    pass
    
