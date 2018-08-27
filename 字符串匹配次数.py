def count_substring(string, sub_string):
    count = 0
    lenString = len(string)
    lenSub_string = len(sub_string)
    for i in range(0, lenString-lenSub_string+1):
        if string[i:len(sub_string)+i] == sub_string:
            count += 1
    return count

print(count_substring('ABCDCDC', 'CDC'))
