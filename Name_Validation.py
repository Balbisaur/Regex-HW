import re
names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

def verify_names(names):
    name_verification = r"[A-Z][a-z]*(?: [A-Z][a-z]*)"
    for name in names:
        if re.match(name_verification, name):
            print(name)
        else:
            print('invalid name')
        
verify_names(names)
