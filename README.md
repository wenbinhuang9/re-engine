# re-engine
A simple and tiny regular expression engine, only support *, |


# How to start 

```
from  re_engine import compile, match, search, findAll

pat = compile("(0|1)*001")

match_obj = pat.match(pat, "00")

match_obj = pat.search(pat, "1000001")

match_obj = pat.findAll(pat, "001001001")
```

# TODO
1. support group
2. support more re symbols, such as [], ., +