phrase = input()
if ":)" in phrase and ":(" in phrase:
    print("double agent")
elif ":)" in phrase:
    print("alive")
elif ":(" in phrase:
    print("undead")
else:
    print("machine")