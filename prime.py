#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
def is_prime_with_math_lib(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # print(f"{x} is divisible by {i}")
            return False
    return True


# In[6]:


def is_prime_with_sqrt_2(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # print(f"{x} is divisible by {i}")
            return False
    return True


# In[7]:


def is_prime_with_half_of_number(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            # print(f"{x} is divisible by {i}")
            return False
    return True







