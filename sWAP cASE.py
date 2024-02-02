def swap_case(s):

    string = ""

    for letter in s:

        if letter.isupper() == True:

            string+=(letter.lower())

        else:

            string+=(letter.upper())
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
