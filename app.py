import io
import pandas as pd
from flask import send_file
from io import BytesIO


def pdProcess(filename):
    # Importing Excel Sheet
    df = pd.read_excel(filename, 0)

    # Select records by these conditions
    dfFiltered = df[(df.LOB == 'MULTI DWELLING UNIT MDU BUILD') | (df.LOB == 'RESIDENTIAL BUILD') | (df.LOB == 'REPLACEMENT')]
    # Grab these columns
    dfFiltered = dfFiltered[['JOB_NAME', 'EXTERNAL_ID', 'REQUEST_NAME', 'LOB', 'MSO']]
    # And Group by this category
    dfGroup = dfFiltered.groupby('MSO')

    #create an output stream
    fileOutput = io.BytesIO()
    writer = pd.ExcelWriter(fileOutput)

    # Loop through all the groups in the group object and create a new sheet for each group
    for gName, gDataFrame in dfGroup:
        print(gName)
        gDataFrame.to_excel(writer,gName)
    
    writer.save()
    fileOutput.seek(0)
    return fileOutput