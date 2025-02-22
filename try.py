import re

text_to_match = "SomeCamelCase"

res = re.sub(r'([a-z])([A-Z])', r'\1_\2', text_to_match)
res = res.lower()
print(res)
