import  re
pattern="[A-Z][0-9][a-z]"
if re.search(pattern,"S6g"):
    print("matched")
else:
    print("not matched")