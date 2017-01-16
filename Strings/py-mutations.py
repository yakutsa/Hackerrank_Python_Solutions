def mutate_string(string, position, character):
    tmp = list(string)
    tmp[position] = character
    string = "".join(tmp)
    return string
