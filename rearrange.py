import re

def rearrange(name):
    names=re.search(r'(.*) (.*)',name)
    print("{} {}".format(names.group(2),names.group(1)))

rearrange('amd ll')
