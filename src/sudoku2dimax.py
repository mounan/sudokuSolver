#!/usr/bin/env python
# coding: utf-8

# ### Get the name of the sudoku file

# In[25]:

import sys
txt = sys.argv[1]
# ### Open the sudoku file and  an output cnf file
print(txt)
# In[26]:


puzzle = open(txt, "r")
cnf = txt.replace("txt", "cnf")
dimacs = open(cnf, "w")


# ###  A function return the index of vars

# In[27]:


def s(x, y, z):
    return 100 * x + 10 * y + z


# ### Read the puzzle and fill up the list for the preassigned_entries

# In[28]:


preassigned_entries = []

row_number = 1
column_number = 0

for _ in range(1, 10):
    line = puzzle.readline()
    digits = line.split()
    column_number = 0
    for digit in digits:
        column_number += 1
        if digit != "x":
            preassigned_entries.append(
                s(row_number, column_number, int(digit))
            )
    row_number += 1


# ### A DIMACS file begins with a line containing 'p' followed by 'cnf', the number of variables, and the number of clauses

# In[29]:


dimacs.write(f"p cnf 729 {8829 + len(preassigned_entries)}\n")

# Write the preassigned entries to the file
for entry in preassigned_entries:
    dimacs.write(f"{entry} 0\n")

# There is at least one number in each entry
for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 10):
            dimacs.write(f"{s(x, y, z)} ")
        dimacs.write("0\n")

# Each number appears at most once in each row
for y in range(1, 10):
    for z in range(1, 10):
        for x in range(1, 9):
            for i in range(x + 1, 10):
                dimacs.write(f"{-s(x, y, z)} {-s(i, y, z)} 0\n")

# Each number appears at most once in each column
for x in range(1, 10):
    for z in range(1, 10):
        for y in range(1, 9):
            for i in range(y + 1, 10):
                dimacs.write(f"{-s(x, y, z)} {-s(x, i, z)} 0\n")

# Each number appears at most once in each 3x3 block
for z in range(1, 10):
    for i in range(0, 3):
        for j in range(0, 3):
            for x in range(1, 4):
                for y in range(1, 4):
                    for k in range(y + 1, 4):
                        dimacs.write(
                            f"{-s(3 * i + x, 3 * j + y, z)} {-s(3 * i + x, 3 * j + k, z)} 0\n"
                        )

# Each number appears at most once in each 3x3 block
for z in range(1, 10):
    for i in range(0, 3):
        for j in range(0, 3):
            for x in range(1, 4):
                for y in range(1, 4):
                    for k in range(x + 1, 4):
                        for l in range(1, 4):
                            dimacs.write(
                                f"{-s(3 * i + x, 3 * j + y, z)} {-s(3 * i + k, 3 * j + l, z)} 0\n"
                            )


# ### Close files

# In[30]:


# Close the puzzle file
puzzle.close()

# Close the DIMACS file
dimacs.close()

print(cnf)
# In[ ]:




