# Day-5 Keywords and Identifiers

# Keywords basically waise words ko bolte hai jo mtlb already defined kiye hua and uska kuch special meaning hota hai toh eslie wo words ko hmlog normally use ni kr skte hai

import keyword
print(keyword.kwlist)
# etne saare keywords hai python me
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Identifier mtlb name jo hmlog function , class ,variable, object , module sbko dete hai 

# rules to follow whenever we are giving name to identifiers

# do's
# can only start with alphabet or _
# followed by 0 or more letters _ and digits
# keywords ko hmlog identifiers ni baana skte hai

# dont's
# special character ya no se start ni ho skta hai

name = 'Kishan'
print(name)