import re
text = "The quick brown fox jumps over the lazy dog"


if x := re.search(r"^The.*dog$", text):
    print("SI")
else:
    print ("NO")