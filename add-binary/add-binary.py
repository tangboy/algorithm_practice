#!/usr/bin/env python
import math

def add_binary(a, b):
    alen = len(a)
    blen = len(b)
    result = ''
    carry = 0
    while alen > 0 or blen > 0:
        abit = 0 if(alen <= 0) else int(a[alen-1])
        bbit = 0 if(blen <= 0) else int(b[alen-1])
        tmp = abit + bbit + carry
        result = str(tmp %10) + result
        carry = math.floor(tmp/10)
        alen -= 1
        blen -= 1
    
    if carry:
        result = str(carry) + result
    
    return result