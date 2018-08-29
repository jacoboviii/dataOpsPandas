import io
import pandas as pd
from flask import send_file
from io import BytesIO


def pdProcess(filename):
    # Importing Excel Sheet
    df = pd.read_excel(filename, sheet_name='Texas')

    # Select records by
    dfFiltered = df[(df.LOB == 'MULTI DWELLING UNIT MDU BUILD') | (df.LOB == 'RESIDENTIAL BUILD')]
    # Grab these columns
    dfFiltered = dfFiltered[['ISSUES', 'JOB_NAME', 'EXTERNAL_ID', 'REQUEST_NAME', 'LOB']]
    # Group by LOB
    dfGroup = dfFiltered.groupby('LOB')
    return dfGroup
    
def pdDownload(dataObject):
    #create an output stream
    fileOutput = io.BytesIO()
    writer = pd.ExcelWriter(fileOutput)

    # Loop through all the groups in the group object and create a new sheet for each group
    for gName, gDataFrame in dataObject:
        print(gName)
        gDataFrame.to_excel(writer,gName)
    
    writer.save()
    fileOutput.seek(0)
    return fileOutput