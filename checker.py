import re

# Checks if all characters are special
def special_matches(s):
    pwd = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    count = 0
    for i in range(0, len(pwd)):
        if pwd[i] in s:
            count += 1
        else:
            pass
    if len(s) == count:
        return True
    else:
        return False

# Checks if any character is special
def any_special(s):
    p = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for i in range(0, len(p)):
        if p[i] in s:
            return True
    return False
password = input("Enter password : ")
pwd = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
if len(re.findall("[0-9]",password)) == len(password):
    print("Password contains only digits (d)")
if len(re.findall("[a-z]|[A-Z]", password)) == len(password):
    print("Password contains alphabets only(a)")
if len(re.findall("[a-z]",password)) == len(password):
    print("Password contains only lower case alphabets(l-a)")
if len(re.findall("[A-Z]", password)) == len(password):
    print("Password only contains uppercase alphabets(u-a)")
if special_matches(password):
    print("Password only contains special characters (s)")
if re.search(r'(?=.*\d+)(?=.*[a-z]|[A-Z])', password):
    print("The pattern is: (a+d+)")
if re.search(r'(?=.*\d+)(?=.*[a-z])', password):
    print("The pattern is: (l-a)+d+")
if re.search(r'(?=.*\d+)(?=.*[A-Z])', password):
    print("The pattern is: (u-a)+d+")
if re.search(r'(?=.*[a-z]|[A-Z])', password) != None and any_special(password):
    print("The pattern is of type a+s+")
if re.search(r'(?=.*[a-z])', password) != None and any_special(password):
    print("The pattern is of type (l-a)+s+") 
if re.search(r'(?=.*[A-Z])', password) != None and any_special(password):
    print("The pattern is of type (u-a)+s+")   
if re.search(r'(?:^[a-z]+)(?:\d$)',password):
    print(f"Pattern is of type (l-a)+||d{1}")
if re.search(r'(^[a-z]+)(\d{2}$)',password):
    print(f"Pattern is of type (l-a)+||d{2} ")
if re.search(r'(^[a-z]+)(\d{3}$)', password):
    print(f"Pattern is of type (l-a)+||d{3} ")
if re.search(r'(^[a-z]+)(\d{4}$)',password):
    print(f"Pattern is of type (l-a)+||d{4} ")
if re.search(r'(^[a-z]+)(\d{5}$)',password):
    print(f"Pattern is of type (l-a)+||d{5} ")
if re.search(r'(^[a-z]+)(\d{6}$)', password):
    print(f"Pattern is of type (l-a)+||d{6} ")
if re.search(r'(^[a-z]+)(\d{7}$)', password):
    print(f"Pattern is of type (l-a)+||d{7} ")
if re.search(r'(^[a-z]+)(\d{8}$)', password):
    print(f"Pattern is of type (l-a)+||d{8} ")
if re.search(r'(^[a-z]+)(\d{9}$)', password):
    print(f"Pattern is of type (l-a)+||d{9} ")
if re.search(r'(^[a-z]+)(\d{10}$)', password):
    print(f"Pattern is of type (l-a)+||d{10} ")
    pass
# elif re.search(r'(?=.*\d+)(?=.*[a-z])', password):
#     print("The pattern is: (a+d+)")