from bs4 import BeautifulSoup

# remove non ansi from text
# example
# re.sub(r'[^\x00-\x7F]+','', '\xa0\n\n\n\n\n\n\n\n\n')
# or
# regex = re.compile(r'[^\x00-\x7F]+')
# regex.sub('', '\xa0\n\n\n\n\n\n\n\n\n')
def get_doc_as_strings(doc):
    bs_doc = BeautifulSoup(doc, 'html_parser')
    return bs_doc.get_text()



