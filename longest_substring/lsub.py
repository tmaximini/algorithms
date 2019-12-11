# find the longest common substring of 2 strings
def long_substr(str1, str2):
    substr = ''
    if (len(str2) > len(str1)):
        str1, str2 = str2, str1
    for i in range(len(str1)):
        for j in range(len(str2)):
            if j > len(substr) and is_substr(str1[i:i+j], str2):
                substr = str1[i:i+j]
    return substr
            


# checks if 'find' is a substring of 'string'
def is_substr(find, string):
    if len(string) < 1 and len(find) < 1:
        return False
    if find not in string:
        return False
    return True



print long_substr('hello, my friend', 'When hell freezes over!')
print long_substr('wurstsuppe', 'Ich habe Durst!')