import re
pattern="C"
str="C uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector for memory management."

if re.match(pattern,"Python is an interpreted high-level general-purpose programming language."):
    print("matched")
else:
    print("not matched")
if re.search(pattern,"Rather than having all of its functionality built into its core, Python was designed to be highly extensible"):
    print("findout")
else:
    print("not found")

print(re.findall(pattern,"Python strives for a simpler, less-cluttered syntax and grammar while giving developers a choice in their coding methodology,Rather than having all of its functionality built into its core, Python was designed to be highly extensible"))
new=re.sub(pattern,"Python",str)
print(new)