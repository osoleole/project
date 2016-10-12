from collections import namedtuple, defaultdict

header =  'Company Name                                                  Form Type   CIK         Date Filed  File Name'
header_fields = ['Company Name', 'Form Type', 'CIK', 'Date Filed', 'File Name']

record = 'AMERICAN MEDICAL HOLDINGS INC                                 10-K        861439      1993-11-29  edgar/data/861439/0000912057-94-000263.txt         ' 


def index_fields(header_fields, header):
    ''' Find 'start' and 'end' indexes of fields. Return the dictionary with the
    'field name' and 'start' and 'end' indexes '''
    indx = []
    indx_dict = dict()

    for v in header_fields:
        indx.append(header.index(v))
    indx.append(None)

    for i, v in enumerate(header_fields):
        di = dict()
        di['start'] = indx[i]
        di['end'] = indx[1:][i]
        indx_dict[v] = di
    return indx_dict

def get_record(header_fields, header, record):
    ''' Extracts fields from records. Returns dictionary with key as header and records as record field'''
    indxs = index_fields(header_fields, header)
    records_dict = dict()

    for k, v in indxs.items():
        records_dict[k] = record[v['start']:v['end']].strip()
    return records_dict

    

print(index_fields(header_fields, header))
print(get_record(header_fields, header, record))


