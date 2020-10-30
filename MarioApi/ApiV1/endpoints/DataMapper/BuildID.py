from .Persistent import Persistent

class BuildID(Persistent):
    """
    Class for representing a BuildID in the BuildIDs table of our database.

    Attributes:
        BuildID: varchar(32), Primary Key
        DriveType: varchar(32), Foreign Key to DriveTypes
        Environment: varchar(32), Foreign Key to Environments
    """

    def __init__(self, databaseConnectionManager):
        super().__init__(databaseConnectionManager)
        self.buildid = None
        self.drivetype = None
        self.environment = None

    def create(self):
        try:
            self.db.get_cursor().execute("Insert into buildids (buildid, drivetype, environment) "
                            "values ('" + str(self.buildid) + "','" + str(self.drivetype) + "','" + str(self.environment) + "');")
            self.db.get_connection().commit()
            return True
        except:
            return False

    def read(self):
        try:
            cursor = self.db.get_cursor()
            cursor.execute("Select buildID from buildIDs "
                                "where driveType = '" + str(self.drivetype) + "' and Environment = '" + str(self.environment) + "';")
            row = cursor.fetchone()
            if row:
                self.buildid = str(row[0])
            return True
        except:
            return False

    def read_first(self, column_name, value):
        """
        Reads the first value from the BuildIDs table to match the specified parameters.

        Parameters:
            column_name (string): The column name to be searched through. Not case sensitive.
            value (string): The value to be looked for in the specified column. Case sensitive.
        """
        try:
            cursor = self.db.get_cursor()
            cursor.execute("Select * from buildIDs "
                                "where " + str(column_name) + " = '" + str(value) + "';")
            row = cursor.fetchone()
            if row:
                self.buildid = str(row[0])
                self.drivetype = str(row[1])
                self.environment = str(row[2])
            return True
        except:
            return False

    def update(self):
        """Updates the corresponding row in the BuildIDs table. Uses buildid as primary key."""
        try:
            self.db.get_cursor().execute("Update BuildIDs "
                                         "set drivetype = '" + str(self.drivetype) + "' , "
                                         "environment = '" + str(self.environment) + "' "
                                         "where buildid = '" + str(self.buildid) + "';")
            self.db.get_connection().commit()
            return True
        except:
            return False

    def delete(self):
        """Deletes the corresponding row in the BuildIDs table. Uses buildid as primary key."""
        try:
            self.db.get_cursor().execute("Delete from buildids where buildid = '" + str(self.buildid) + "';")
            self.db.get_connection().commit()
            return True
        except:
            return False

    def set_buildid(self, buildid):
        self.buildid = buildid

    def set_drivetype(self, drivetype):
        self.drivetype = drivetype

    def set_environment(self, environment):
        self.environment = environment

    def get_buildid(self):
        return self.buildid

    def get_drivetype(self):
        return self.drivetype

    def get_environment(self):
        return self.environment