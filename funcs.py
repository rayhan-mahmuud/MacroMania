import re

def macro_placer(sizmek):

    pattern = "\[timestamp\]&z=0"
    match = re.compile(pattern)
    new = '<a href="'
    newmatch = re.compile(new)
    match2 = match.sub("{{cacheBust}}&ucmtrue&ncu={{escapedClickTag}}", sizmek)

    return newmatch.sub('<a href="{{clickTag}}', match2)