def capitalize(string):
    string = string[0].upper() + string[1:]
    for i in range(len(string)):
        if string[i] == " ":
            string = string[:i+1] + string[i+1].upper() + string[i+2:]
    return string
