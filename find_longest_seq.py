"""Q: Max same-character substing """ 
from __future__ import print_function
s = "qqqqqQQQTTTTTTTsssRRDDeee"
max_pos = 0
max_len = 1;
curr_char = s[0]
curr_len = 1

for (i, x) in enumerate(s[1:]):
    if x == curr_char:
        curr_len = curr_len + 1

    if x != curr_char or i == len(s[1:]) - 1:
        curr_char = x
        if curr_len > max_len:
            max_len = curr_len
            max_pos = i - curr_len + 1
        curr_len = 1 # Setting to 1 in either case



print("String: '%s'" % s)
print("Max same-character substring: '%s'" % s[max_pos: max_pos + max_len])

