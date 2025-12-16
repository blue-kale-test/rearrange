import re
def rearrnage(name):
    last_name, first_name = re.split(',', name)
    return (f'{first_name} {last_name}')

print(rearrnage('Turing,Alan'))
print(rearrnage('Antoanette Currie,Marrie'))