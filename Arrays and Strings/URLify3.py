#!/usr/local/bin/python3.6

def urlify(str, len):
    l = str.split()
    ret = ""
    for e in l[:-1]:
        ret += e
        ret += "%20"
    ret += l[-1]
    return ret

# Assume length is "real" length of string (not including trailing spaces)
def main():
    str = "my name is alex"
    print(urlify(str, len(str)))

if __name__ == '__main__':
    main()
