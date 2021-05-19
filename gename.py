import argparse

# Color
class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

# Print Banner
def banner():
    print(color.BLUE+'''
    ____ ___  ___  ___  ____ ____ _  _ _  _ ____ _  _ ____
    |___   /  |__]   /  | __ |___ |\ | |\ | |__| |\/| |___
    |___  /__ |     /__ |__] |___ | \| | \| |  | |  | |___

              Credits : @aniqfakhrul & @H0j3n
    '''+color.END)
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
    # Save in a file
    f = open(output_file, "w")
    for lines in list_names:
        if newFormat:
            f.write(lines+domain_name)
        else:
            f.write(domain_name+lines)
        f.write("\n")
    f.close()
    print(color.GREEN+"[+]"+color.END+" Saved to : "+output_file)

if __name__ == "__main__":
    banner()
    parser = argparse.ArgumentParser(description='A tool that can generate User Principal Name with Custom Rules written in Python')
    parser.add_argument('-n','--names', help='Read list of names line by line.',required=True)
    parser.add_argument('-r','--rules', help='Read list of rules line by line.',default="usernames.rule")
    parser.add_argument('-o','--output',help='Output to different paths',default="list_user.txt")
    parser.add_argument('-d','--domain',help='Add domain if available')
    parser.add_argument('-f','--format',help='Formatting to use "new" or "old" format',default="new")

    args = parser.parse_args()
    txt_names = args.names
    newFormat = False
    output_file = args.output
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
    main()
