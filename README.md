# re-engine
A simple and tiny regular expression engine, only support *, |


# How to start 

```
from  re_engine import compile

pat = compile("(0|1)*001")

ans = pat.match("00")
```

# TODO
1. support findall and find interface
2. support group
3. add more re symbols