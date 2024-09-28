import pandas

devnodes = {}
with open('devnodes.csv', mode='rU') as f:
    reader = csv.reader(f, delimiter=',')  # dialect=csv.excel_tab?
    for n, row in enumerate(reader):
        if not n:
            # Skip header row (n = 0).
            continue  
        devnodes, branch, length = row
        if devnodes not in devnodes:
            devnodes[devnodes] = list()
        devnodes[devnodes].append((branch, length))