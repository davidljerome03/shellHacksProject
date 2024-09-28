import os
import requests
import sys

def getGoogleSheet(spreadsheet_id, outDir, outFile):
    url = f'https://docs.google.com/spreadsheets/d/1aHN-1YITwi3YZwLSmuqnLmWapImw_xviDkzUHoiK9y4/export?format=csv'
    response = requests.get(url)
    if response.status_code == 200:
        filepath = os.path.join(outDir, outFile)
        with open(filepath, 'wb') as f:
            f.write(response.content)
            print('CSV file saved to {}'.format(filepath))
    else:
        print(f'Error downloading Google Sheet: {response.status_code}')
        sys.exit(1)

outDir = 'tmp/'

os.makedirs(outDir, exist_ok = True)
filepath = getGoogleSheet('1aHN-1YITwi3YZwLSmuqnLmWapImw_xviDkzUHoiK9y4', outDir, "devnodes.csv")

sys.exit(0);