from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test():
    #result = get_files_info("calculator", ".")
    #print("Result for current directory:")
    #print(result)
    #print("")

    #result = get_files_info("calculator", "pkg")
    #print("Result for 'pkg' directory:")
    #print(result)

    #result = get_files_info("calculator", "/bin")
    #print("Result for '/bin' directory:")
    #print(result)

    #result = get_files_info("calculator", "../")
    #print("Result for '../' directory:")
    #print(result)


    ##result = get_file_content("calculator", "lorem.txt")
    ##print("Result for opening 'lorem.txt':")
    ##print(result)
    ##print("")

    #result = get_file_content("calculator", "main.py")
    #print("Result for opening 'main.py' file:")
    #print(result)
    #print("")

    #result = get_file_content("calculator", "pkg/calculator.py")
    #print("Result for opening 'pkg/calculator.py' file:")
    #print(result)

    #result = get_file_content("calculator", "/bin/cat")
    #print("Result for opening '/bin/cat' file:")
    #print(result)

    #result = get_file_content("calculator", "pkg/does_not_exist.py")
    #print("Get file result for 'pkg/does_not_exist.py' file:")
    #print(result)



    #result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    #print("Result for writing 'lorem.txt' file:")
    #print(result)
    #print("")

    #result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    #print("Result for writing 'pkg/morelorem.txt' file:")
    #print(result)
    #print("")

    #result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    #print("Result for writing '/tmp/temp.txt' file:")
    #print(result)
    #print("")

    result = run_python_file("calculator", "main.py")
    print("Running calculator main.py, should print instructions")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Running calculator main.py, return sum")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Running calculator test.py, should run unit tests")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Running calculator /main.py, should error")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Running calculator nonexistent.py, should error")
    print(result)
    print("")
    
    
if __name__ == "__main__":
    test()