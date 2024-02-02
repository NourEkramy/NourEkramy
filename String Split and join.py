

def split_and_join(line):
    # write your code here
    string=""

    for letter in line:
        if letter==' ':
            string+='-'
        else:
            string+=letter
        
    return string
        
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
