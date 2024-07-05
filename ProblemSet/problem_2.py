s = 'eobobobobbohbobbrqoxiob'
bob_count = 0

for i, char in enumerate(s):
    if char == "b" and s[i:i+3] =="bob":
        bob_count += 1

print("Number of times bob occurs is: ",bob_count)