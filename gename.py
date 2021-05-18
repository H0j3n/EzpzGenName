names_list = open("user.txt").readlines()
domain_name = "@company.local"

# Naming Function
def gen_names(names, list_names):
    conv_list = []
    list_rules = open("username.rules").readlines()
    found_mid = False
    for j in list_rules:
        conv_list.append(j)
    if len(names.split(" ")) > 2:
        first,mid,last = names.split(" ")
        print(first,mid,last)
        found_mid = True
    else:
        first,last = names.split(" ")
        print(first,last)
    for rule in list_rules:
        try:
            if ("mid" in rule) and (not found_mid):
                continue
            else:
                list_names.append(eval(rule))
        except:
            continue

# Variables
list_names = []

# Loop
for i in names_list:
    gen_names(i.strip(),list_names)

# Save in a file
f = open("list_user.txt", "w")
for lines in list_names:
    f.write(lines)
    f.write("\n")
f.close()
