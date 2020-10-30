import pyodbc


class DatabaseInit():
    """"A class to set up the databases used by the Mario pipeline manager."""

    def __init__(self):
        """Initializes the databases connection."""
        server = 'tcp:projectspike.database.windows.net'
        database = 'ProjectsSpike'
        username = 'priort'
        password = 'SE4330team'
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        self.cursor = self.cnxn.cursor()


    def setup(self):

        # Creating new tables
        self.cursor.execute("CREATE TABLE DriveTypes("
                       "driveType varchar(32) NOT NULL PRIMARY KEY);")
        self.cursor.execute("CREATE TABLE Environments("
                       "environment varchar(32) NOT NULL PRIMARY KEY);")
        self.cursor.execute("Create table BuildIDs("
                            "buildID varchar(32) NOT NULL PRIMARY KEY, "
                            "nickname varchar(255),"
                            "driveType varchar(32), "
                            "environment varchar(32), "
                            "nickname varchar(255),"
                            "unique (driveType, Environment), "
                            "foreign key (driveType) references DriveTypes(driveType) on update cascade on delete cascade, "
                            "foreign key (Environment) references Environments(environment) on update cascade on delete cascade);")
        self.cursor.execute("Create table PowerCards("
                            "powerCardID varchar(32) NOT NULL, "
                            "value varchar(255), "
                            "Primary Key (powerCardID)); ")
        self.cursor.execute("Create table Firmwares("
                            "firmwareID varchar(32) NOT NULL, "
                            "value varchar(255), "
                            "Primary Key (firmwareID));")
        self.cursor.execute("Create table Applications("
                            "applicationID varchar(32) NOT NULL, "
                            "value varchar(255), "
                            "Primary Key (applicationID));")
        self.cursor.execute("Create table Emails("
                            "emailAddress varchar(256) NOT NULL,"
                            "name varchar(64),"
                            "Primary Key (emailAddress));")
        self.cursor.execute("Create table EmailGroups("
                            "groupName varchar(32) NOT NULL,"
                            "emailAddress varchar(256) NOT NULL,"
                            "Primary Key (groupName, emailAddress));")
        self.cursor.execute("CREATE TABLE Configurations("
                            "configID varchar(32) NOT NULL PRIMARY KEY, "
                            "buildID varchar(32), "
                            "applicationID varchar(32), "
                            "firmwareID varchar(32), "
                            "powerCardID varchar(32), "
                            "foreign key (buildID) references BuildIDs(buildID) on update cascade on delete cascade, "
                            "foreign key (applicationID) references Applications(applicationID) on update cascade on delete cascade, "
                            "foreign key (firmwareID) references Firmwares(firmwareID) on update cascade on delete cascade, "
                            "foreign key (powerCardID) references PowerCards(powerCardID) on update cascade on delete cascade);")
        self.cursor.execute("CREATE TABLE Users("
                            "email varchar(255) NOT NULL PRIMARY KEY, "
                            "descriptor varchar(255));")
        self.cursor.execute("CREATE TABLE Artifacts("
                            "artifactID varchar(255) NOT NULL, "
                            "artifactName varchar(255), "
                            "configID varchar(32) NOT NULL,"
                            "foreign key (configID) references Configurations(configID) on update cascade on delete cascade,"
                            "Primary Key (artifactID, configID));")
        self.cnxn.commit()

        #TODO Email Groups, Generic Artifact, value on any artifact tables