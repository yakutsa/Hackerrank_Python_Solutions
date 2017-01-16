def count_substring(string, sub_string):
    temp_list_s = list(string)
    temp_list_ss = list(sub_string)
    for i in range(len(string)):
        if temp_list_s[i:i+len(temp_list_ss)] == temp_list_ss:
            results += 1
    return results
