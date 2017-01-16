def wrap(string, max_width):
    return textwrap.fill(string, max_width)

### textwrap.fill function could be written as:
### tmp = list(string)
### for i in range(0, len(string), max_width):
###     print "".join(tmp[i:i+max_width])
