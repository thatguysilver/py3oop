# regex intro

import re, sys

pattern = sys.argv[1]
search_string = sys.argv[2]
match = re.match(pattern, search_string)

if match:
    template = "'{} matches pattern '{}'"
else:
    template = "'{} doesn't match pattern '{}'"

print(template.format(search_string, pattern))
