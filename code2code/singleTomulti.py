#!/usr/bin/env python

import re
import sys

source = """
/* 
 * not 
// a single line 
// comment 
*/

// include stuff
#include<stdio.h>

main()
{
    // comments with a '*/' !
    printf("Again, no single // line comment"); // comment
}
"""

pattern = re.compile(r"""   (//([^\r\n]*)) # match a single line comment
                          | "[^"]*"        # match a string literal
                          | /\*.*?\*/      # match a multi line comment
                          | .              # fall through: match any char
                      """
                         , re.X | re.S)

print("%s" % source)              

print('=' * 40)

for match in pattern.finditer(source):
    if match.group(1):
        # we found a single line comment
        s = match.group(2).replace('*/', '* /')
        sys.stdout.write("/*" + s + " */")
    else:
        # something other than a single line comment, just print it
        sys.stdout.write(match.group())