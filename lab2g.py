#!/usr/bin/env python3
import sys

#Author: Jeffrey Li
#Author ID: jli699
#Date Created: 2025/05/15

if len(sys.argv) == 1:
    timer = 3;
else:
    timer = int(sys.argv[1]);

while timer != 0:
    print(timer);
    timer -= 1;
print('blast off!')
