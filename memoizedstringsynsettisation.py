#import nltk
#nltk.download('wordnet')
# C:\Users\Student\AppData\Roaming\nltk_data
import timeit
from functools import lru_cache
from pprint import pprint


from wordnet2relationmapping import *

pprint(wordnet_lookers)

import pywsd

@lru_cache(maxsize=None)
def lazy_lemmatize(sample):
    return pywsd.allwords_wsd.disambiguate(sample)


