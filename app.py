import io
import pandas as pd
from flask import send_file
from io import BytesIO


def pdProcess(filename):
    # Importing Excel Sheet
    excel = pd.read_excel(filename, sheet_name='Texas')
    excel.head()

    # List all the columns in the spreadsheet
    list(excel)

    # Applying a filter
    dataFrameOut = excel[(excel.LOB == 'MULTI DWELLING UNIT MDU BUILD') | (excel.LOB == 'RESIDENTIAL BUILD')]
    # Grab only the series listed
    dataFrameOut = dataFrameOut[['ISSUES', 'JOB_NAME', 'EXTERNAL_ID', 'REQUEST_NAME']]
    dataFrameOut.head()
    return dataFrameOut
    
def pdDownload(dataFrame):
    #create an output stream
    fileOutput = io.BytesIO()
    writer = pd.ExcelWriter(fileOutput)
    dataFrame.to_excel(writer,'Sheet1')
    dataFrame.to_excel(writer,'Sheet2')
    writer.save()
    fileOutput.seek(0)
    return fileOutput