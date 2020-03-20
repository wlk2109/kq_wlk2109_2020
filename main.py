import sys
from CheckMapping import CheckMapping

def main():
    checker = CheckMapping()

    check = checker.check_mapping_better

    s1 = sys.argv[1]
    s2 = sys.argv[2]
    result = check(s1, s2)

    #print(result)

    return(result)


if __name__ == "__main__":
    main()