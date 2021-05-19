import argparse
parser = argparse.ArgumentParser(description='A tool that can generate User Principal Name with Custom Rules written in Python')
parser.add_argument('-n','--names', help='Read list of names line by line.',required=True)
parser.add_argument('-r','--rules', help='Read list of rules line by line.',default="usernames.rule")
parser.add_argument('-d','--domain',help='Add domain if available')
parser.add_argument('-f','--format',help='Formatting to use new or old format',default="new")

args = parser.parse_args()
txt_names = args.names
newFormat = False
if args.domain:
    if args.format == "new":
        domain_name = "@"+args.domain
        newFormat = True
    else:
        domain_name = args.domain + "\\"
else:
    domain_name = ""
txt_rules = args.rules

names_list = open(txt_names).readlines()

# Naming Function
def gen_names(names, list_names):
    conv_list = []
    list_rules = open(txt_rules).readlines()
    found_mid = False
    for j in list_rules:
        conv_list.append(j)
    if len(names.split(" ")) > 2:
        first,mid,last = names.split(" ")
        found_mid = True
    else:
        first,last = names.split(" ")
    for rule in list_rules:
        try:
            if ("mid" in rule) and (not found_mid):
                continue
            else:
                list_names.append(eval(rule))
        except:
            continue

def main():
    # Variables
    list_names = []

    # Loop
    for i in names_list:
        gen_names(i.strip().lower(),list_names)
    print("[+] Saved: list_users.txt")

    # Save in a file
    f = open("list_user.txt", "w")
    for lines in list_names:
        if newFormat:
            f.write(lines+domain_name)
        else:
            f.write(domain_name+lines)
        f.write("\n")
    f.close()

if __name__ == "__main__":
    main()
