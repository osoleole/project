from collections import defaultdict
f = open('2012_qtr1.idx').readlines()

COMPANY_NAME = 'Company Name'
FORM_TYPE = 'Form Type'
CIK = 'CIK'
DATE_FIELD = 'Date Filed'
FILE_NAME = 'File Name'
STARTLINE = len(f)
VALUES = [COMPANY_NAME, FORM_TYPE, CIK, DATE_FIELD, FILE_NAME, ]
INDXS = defaultdict(dict)
DATA = []

# fine the start line
for i, line in enumerate(f):
    if len([v for v in VALUES if v in line]) == len(VALUES):
        for n, val in enumerate(VALUES):
            INDXS[val]['start'] = line.index(val)
            if n != 0:
                pre = VALUES[n - 1]
                INDXS[pre]['end'] = INDXS[val]['start'] - 1

        STARTLINE = i + 2
        break

for line in f[STARTLINE:]:
    company_data = {}
    for val in VALUES:
        indxs = INDXS[val]
        company_data[val] = line[indxs['start']: indxs.get('end', len(line))].strip()
    DATA.append(company_data)
