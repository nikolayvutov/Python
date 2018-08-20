import re

text = 'ds3bhj y1ter/wfsdg 1nh_jgf ds2c_vbg\\4htref'

pattern = r'[a-zA-Z][a-zA-Z0-9_]{3,25}'
match = re.findall(pattern, text)

print(match)

