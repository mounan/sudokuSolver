#!/usr/bin/env python
# coding: utf-8

# In[102]:

import sys
origin_result = open(sys.argv[1], "r")
digits = origin_result.read()


# In[103]:


import re
digits = re.sub("SAT\\n","",digits)
digits = re.sub("0\\n","",digits)
digits = re.sub(r"-[0-9]*","",digits)
digits = digits.split()
digits = list(map(int, digits))
for i in range(0, len(digits)):
    digits[i] = digits[i] % 100 % 10

# In[104]:


ans = open("final_answer.txt", "w")
for i in range(0, len(digits)):
    ans.write(str(digits[i]) + " ")
    if (i+1)%9 == 0:
        ans.write("\n")






