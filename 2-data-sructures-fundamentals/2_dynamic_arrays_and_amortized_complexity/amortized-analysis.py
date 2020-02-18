# Issue 24:
# Let's imagine we add support to our dynamic array for a new operation PopBack (which removes the last element), 
# and that PopBack never reallocates the associated dynamically-allocated array. Calling PopBack on an empty dynamic array is an error.

# If we have a sequence of 48 operations on an empty dynamic array: 24 PushBack and 24 PopBack (not necessarily in that order), 
# we clearly end with a size of 0.

# Question: What are the minimum and maximum possible final capacities given such a sequence of 48 operations on an empty dynamic array? 
# Assume that PushBack doubles the capacity.

# Answer: minimum: 1, maximum: 32

# The minimum is achieved when we alternate with one PushBack followed by one PopBack. 
# The size of the array never exceeds 1, so the capacity also never exceeds 1. 
# The maximum is achieved when we have 24 PushBacks followed by 24 PopBacks. 
# The maximum size is 24, so the corresponding capacity is 32 (next highest power-of-2). 