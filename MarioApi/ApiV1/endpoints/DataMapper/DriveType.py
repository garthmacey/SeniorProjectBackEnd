from .Persistent import Persistent

class DriveType(Persistent):
    """
    Class for representing a DriveType in the DriveTypes table of our database.

    Attributes:
        DriveType: varchar(32), Primary Key
    """

    def __init__(self, databaseConnectionManager):
        super().__init__(databaseConnectionManager)
        self.drivetype = None

    def create(self):
        try:
            self.db.get_cursor().execute("Insert into drivetypes (drivetype) values ('" + str(self.drivetype) + "');")
            self.db.get_connection().commit()
            return True
        except:
            return False

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        try:
            self.db.get_cursor().execute("Delete from drivetypes where drivetype = '" + str(self.drivetype) + "';")
            self.db.get_connection().commit()
            return True
        except:
            return False

    def set_drivetype(self, drivetype):
        self.drivetype = drivetype

    def get_drivetype(self):
        return self.drivetype