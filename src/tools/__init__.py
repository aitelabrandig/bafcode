from .google.search import GoogleSearch
from .docs.write import DocsWrite



# Define your commands  here
command_mapping = {        
    "googleSearch": GoogleSearch,
    "docsWrite": DocsWrite,
        }