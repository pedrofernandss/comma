import random
import string
from typing import List

def select_random_source(sources_list: List) -> string:
    selected_url = random.choice(sources_list)
    
    return selected_url
