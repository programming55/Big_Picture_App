import datetime
class Project:

    def __init__(self, pid, pName, pStatus):
        self.projectId = pid
        self.projectName = pName
        self.projectStatus = pStatus
        self.projectCreationDate = datetime.datetime.now()
        self.projectModifiedDate = datetime.datetime.now()


    def updateStatus(self, status):
        self.projectStatus = status
        self.projectModifiedDate = datetime.datetime.now()

    def updateTitle(self, name):
        self.projectName = name
        self.projectModifiedDate = datetime.datetime.now()

