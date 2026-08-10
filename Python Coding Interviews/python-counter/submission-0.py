from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    list_s1 = list(s1)
    list_s2 = list(s2)
    counter = Counter(list_s1)
    counter.update(list_s2)
    return counter
    
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
