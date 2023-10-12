string = "acdbddbbbbaaac"

import re

pattern = r'^(?=(?:[^a]*a){0,}(?:[^b]*b){0,}(?:[^c]*c){0,}(?:[^d]*d){0,}$)(?=^.*a(?:.*c.*){0,}(?:.*d(?:.*b.*){0,}){0,}.*$).*$'


if re.match(pattern, string):
    print(f'{string} is balanced.')
else:
    print(f'{string} is not balanced.')

