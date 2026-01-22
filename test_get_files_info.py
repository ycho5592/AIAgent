from functions.get_files_info import get_files_info 

def test():
    result_1 = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result_1)


    result_2 = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result_2)

    result_3 = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result_3)

    result_4 = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result_4)

if __name__ == "__main__":
    test()