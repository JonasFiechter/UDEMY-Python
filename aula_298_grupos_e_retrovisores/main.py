# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
#[abc]

import re

print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', text,))