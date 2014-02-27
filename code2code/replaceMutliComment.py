#!/usr/bin/env python

import re
import sys

source = """
/** 
 * not 
// a single line 
// comment 
*/

// include stuff
#include<stdio.h>

main()
{
    /* comments with a */
    printf("Again, no single // line comment"); // comment
}
"""
pattern = re.compile(r"""/\*.*?\*/""", re.X | re.S)
print("%s" % source)              
print('=' * 40)
print re.sub(pattern,"",source)
