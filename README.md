# EzpzGenName

![](./src/banner.png)

# What is EzpzGenName?

**Disclaimer: This tool is not a bruteforcing tool and does not perform network-level authentication.**

**EzpzGenName** is a tool written in Python by [@aniqfakhrul](https://github.com/aniqfakhrul) and [@H0j3n](https://github.com/H0j3n) which we encounter some scenario that needed to generate custom principal names to **bruteforcing** valid users in **Keberoast**. What makes **EzpzGenName** differents, you can specify your own custom.rule file *(Refer default file : usernames.rule)*

This tool will be updated from time to time with any new rules we found. Feels free to make a PR to make EzpzGenName better.


# Usage

### 1. Usernames only

```
# Usage
python3 gename.py -n user.txt -r usernames.rule

# Output
alex-james
```

### 2. Formatting

- New Format

```
# Usage
python3 gename.py -n user.txt -r usernames.rule -d "company.local" -f new

# Output
alex-james@company.local
```

- Old Format

```
# Usage
python3 gename.py -n user.txt -r usernames.rule -d "company.local" -f old

# Output
company.local\alex-james
```

### 3. Output

```
# Usage
python3 gename.py -n user.txt -r usernames.rule -o /tmp/user.txt

# output
[+] Saved to : /tmp/user.txt
```
