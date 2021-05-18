__author__ = 'Ankit Pant'
__email__ = "maven7@tutanota.com"
__status__ = "alpha"

import datetime
class Project:

    """
    Class that encapsulates basic attributes of a project item. Each project item corresponds to an instance of this class.
    """

    def __init__(self, pid, pName, pStatus):
        """
        Initialize the attributes of a newly created project item.
        """

        self.projectId = pid
        self.projectName = pName
        self.projectStatus = pStatus
        self.projectCreationDate = datetime.datetime.now()
        self.projectModifiedDate = datetime.datetime.now()


    def updateStatus(self, status):
        """
        Updates the status of a particular project item, when the project item is moved from one stage to another.
        """

        self.projectStatus = status
        self.projectModifiedDate = datetime.datetime.now()

    def updateTitle(self, name):
        """
        Updates the name of a particular project item, when the project name is changed for that particular project item.
        """
        
        self.projectName = name
        self.projectModifiedDate = datetime.datetime.now()

