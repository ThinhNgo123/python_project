from excel_manipulation import ExcelManipulation

class UsersManager:
    UPDATE_SUCCESS = "Update success"
    UPDATE_ERROR   = "Update error"
    DELETE_SUCCESS = "Delete success"
    DELETE_ERROR   = "Delete error"

    def __init__(self, path, sheet):
        self.path = path 
        self.sheet = sheet
        self.excelManipulation = ExcelManipulation(path, sheet)
        self.data = self.excelManipulation.excelImport()
        self.lenData = len(self.data)

    def infoCheck(self, filed, value, index):
        '''
        This function check information for filed
        '''

        index = int(index)
        for i in range(self.lenData):
            if i == index:
                continue
            if self.data[i][filed] == value:
                return False
        return True

    def userCheck(self, *arg):
        '''
        check if match returns true else return false
        '''

        for filed, value in zip(self.excelManipulation.DEFAULT_FILED, arg):
            if filed != "Index":
                if not self.infoCheck(filed, value, arg[0]):
                    # print("false")
                    return False
        return True

    def userUpdate(self, index, stationName, ip, user, password):
        ''' this function used to update user in formation and save to excel file
        - idx: index of user  
        - stationName: 
        - ip: 
        - user: 
        - password: 
        '''

        try:
            if self.userCheck(index, stationName, ip, user, password):
                self.data[int(index)]["Station name"] = stationName
                self.data[int(index)]["IP"] = ip
                self.data[int(index)]["User"] = user
                self.data[int(index)]["Password"] = password
            
                self.excelManipulation.updateUserToExcel(index, stationName, ip, user, password)

                return self.UPDATE_SUCCESS
            else:
                return self.UPDATE_ERROR

        except:
            return self.UPDATE_ERROR

    def userDelete(self, index):
        ''' this is function used to delete user information
        - index:
        - @return 
        '''

        try:
            self.data.pop(int(index))
            self.excelManipulation.deleteFromRow(index)
            return self.DELETE_SUCCESS
        except:
            return self.DELETE_ERROR

    def getUserInfo(self, index):
        return self.excelManipulation.getUserFromExcel(index)
    
        