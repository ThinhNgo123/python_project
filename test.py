from time import time
from user_manager import UsersManager
from excel_manipulation import ExcelManipulation

def main():
    # path = "D:\Data\Project_company\python_project\\test2.xlsx"
    path1 = "D:\Data\Project_company\\atDataLogger_Manager_Tool\\test.xlsx"
    sheet = "Sheet"
    start = time()
    user = UsersManager(path1, sheet)
    print(user.data)
    # print(user.userUpdate(1, "thuy dien hoa binh", "192.168.1.2", "admin", "123456"))
    print(user.userUpdate("2", "thuy dien son la", "192.168.1.100", "admin1", "12345678"))
    print(user.userUpdate("98", "thuy dien", "192.168.1.20", "user98", "abcdef"))
    print(f"{(time() - start)}s")


if __name__ == "__main__":
    main()
    