import pandas as pd
from flask import send_file
from io import BytesIO

def pdProcess(filename):
    # ## Importing Excel Sheet
    excel = pd.read_excel(filename, sheet_name='Texas')
    excel.head()

    # List all the columns in the spreadsheet
    list(excel)

    # ## Applying a filter
    non_commercial = excel[(excel.LOB == 'MULTI DWELLING UNIT MDU BUILD') | (excel.LOB == 'RESIDENTIAL BUILD')]
    # Grab only the series listed
    non_commercial = non_commercial[['ISSUES', 'JOB_NAME', 'EXTERNAL_ID', 'REQUEST_NAME']]
    non_commercial.head()
    
    #create an output stream
    fileOutput = '/Users/jacoboperez/Desktop/test.xlsx'
    writer = pd.ExcelWriter(fileOutput)
    non_commercial.to_excel(writer,'Sheet1')
    non_commercial.to_excel(writer,'Sheet2')
    writer.save()