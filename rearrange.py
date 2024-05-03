#!/usr/bin/env python3

import re

def rearrange_name(name):
    result = re.search("^([\w .]*), ([\w .]*)$", name)
    try:
        return "{} {}".format(result[2], result[1])
    except TypeError:
        return name

# the output as expected would come out from an another testing program
