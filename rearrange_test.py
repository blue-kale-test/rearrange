import re

FullName = input('Enter your Last Name followed by a comma followed by your First Name: ')
#print(FullName)

comma_search = re.search(',', FullName)

if comma_search is None:
    print('a comma "," is required between the Last Name and the First Name')
    quit()
    
def rearrange_name():
    """Turns "LastName, FirstName" into "FirstName LastName"."""
    Names = FullName.split(', ')
    #print('This person gave', len(Names), 'name(s)')
    if len(Names) == 1:
        print(Names[0])
    elif len(Names) != 1:
        LastName = Names[0]
        FirstName = Names[1]
        print(FirstName, LastName)

rearrange_name()