#!/bin/python3

import math
import os
import random
import re
import sys

S = input().strip()
try:
    test = int(S)
    print(test)
except:
    print("Bad String")