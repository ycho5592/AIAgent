from functions.get_file_content import get_file_content

def test():

    result1 = get_file_content("calculator", "lorem.txt")
    print(result1)

    result2 = get_file_content("calculator", "main.py")
    print(result2)
    result3 = get_file_content("calculator", "pkg/calculator.py")
    print(result3)
    result4 = get_file_content("calculator", "/bin/cat")
    print(result4)
    result5 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result5)

if __name__ == "__main__":
    test()