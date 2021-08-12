#Q20 긍정형 전방탐색

import re

p = re.compile(".*[@].*[.](?=com$|net$).*$")
print(p.match("ldonghae320@gmail.com"))

