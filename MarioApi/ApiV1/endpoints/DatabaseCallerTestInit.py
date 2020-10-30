import pyodbc


class DatabaseCallerTestInit():
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
        self.cursor.execute("CREATE TABLE testDriveTypes("
                            "driveType varchar(32) NOT NULL PRIMARY KEY);")
        self.cursor.execute("CREATE TABLE testEnvironments("
                            "environment varchar(32) NOT NULL PRIMARY KEY);")
        self.cursor.execute("Create table testBuildIDs("
                            "buildID varchar(32) NOT NULL PRIMARY KEY, "
                            "nickname varchar(255),"
                            "driveType varchar(32), "
                            "Environment varchar(32), "
                            "unique (driveType, Environment), "
                            "foreign key (driveType) references testDriveTypes(driveType) on update cascade on delete cascade, "
                            "foreign key (Environment) references testEnvironments(environment) on update cascade on delete cascade);")
        self.cursor.execute("Create table testPowerCards("
                            "powerCardID varchar(32) NOT NULL, "
                            "value varchar(255), "
                            "Primary Key (powerCardID)); ")
        self.cursor.execute("Create table testFirmwares("
                            "firmwareID varchar(32) NOT NULL, "
                            "value varchar(255), "
                            "Primary Key (firmwareID));")
        self.cursor.execute("Create table testApplications("
                            "applicationID varchar(32) NOT NULL, "
                            "value varchar(255), "
                            "Primary Key (applicationID));")
        self.cursor.execute("Create table testEmails("
                            "emailAddress varchar(256) NOT NULL,"
                            "name varchar(64),"
                            "Primary Key (emailAddress));")
        self.cursor.execute("CREATE TABLE testConfigurations("
                            "configID varchar(32) NOT NULL PRIMARY KEY, "
                            "buildID varchar(32) references testBuildIDs(buildID) on update cascade on delete cascade, "
                            "applicationID varchar(32) references testApplications(applicationID) on update cascade on delete cascade, "
                            "firmwareID varchar(32) references testFirmwares(firmwareID) on update cascade on delete cascade, "
                            "powerCardID varchar(32) references testPowerCards(powerCardID) on update cascade on delete cascade);")
        self.cursor.execute("CREATE TABLE testUsers("
                            "email varchar(255) NOT NULL PRIMARY KEY, "
                            "descriptor varchar(255));")
        self.cursor.execute("CREATE TABLE testArtifacts("
                            "artifactID varchar(255) NOT NULL, "
                            "artifactName varchar(255), "
                            "configID varchar(32) NOT NULL,"
                            "foreign key (configID) references testConfigurations(configID) on update cascade on delete cascade,"
                            "Primary Key (artifactID, configID));")
        self.cnxn.commit()

    def wipeTables(self):

        self.cursor.execute("drop table testArtifacts;"
                            "drop table testConfigurations;"
                            "drop table testBuildids;"
                            "drop table testDriveTypes;"
                            "drop table testEnvironments;"
                            "drop table testApplications;"
                            "drop table testPowerCards;"
                            "drop table testFirmwares;"
                            "drop table testEmails;"
                            "drop table testUsers;")
        self.cnxn.commit()

    def addDummyValues(self):
        self.cursor.execute("insert into testDriveTypes (driveType) values ('driveType1'), ('driveType2'), ('driveType3'), ('driveType4');")
        self.cursor.commit()
        self.cursor.execute("insert into testEnvironments (environment) values ('environment1'), ('environment2'), ('environment3'), ('environment4');")
        self.cnxn.commit()

        self.cursor.execute("insert into testbuildids (buildid, drivetype, environment) values ('build1' , 'driveType1', 'environment1'), ('build2' , 'driveType1', 'environment2'), "
                            "('build3' , 'driveType1', 'environment3'), ('build4' , 'driveType2', 'environment1'), ('build5' , 'driveType2', 'environment2'), "
                            "('build6' , 'driveType2', 'environment3'), ('build7' , 'driveType3', 'environment1'), ('build8' , 'driveType3', 'environment2'), "
                            "('build9' , 'driveType3', 'environment3');")
        self.cursor.execute("insert into testpowercards (powercardID, value) values ('demoPowerCard1', 'dummyValue');")
        self.cnxn.commit()
        self.cursor.execute("insert into testapplications (applicationID, value) values ('demoApplication1', 'dummyValue');")
        self.cnxn.commit()
        self.cursor.execute("insert into testfirmwares (firmwareID, value) values ('demoFirmware1', 'dummyValue');")
        self.cnxn.commit()
        self.cursor.execute("insert into testEmails (emailAddress, name) values ('DoeJ@email.com', 'John Doe');")
        self.cnxn.commit()
        self.cursor.execute("insert into testConfigurations (configID, buildID, applicationID, firmwareID, powerCardID) values ('TestConfig', 'build1', 'demoApplication1', "
                            "'demoFirmware1', 'demoPowerCard1');")
        self.cnxn.commit()
        self.cursor.execute("insert into testUsers (email, descriptor) values ('email@email.com', 'goodDescriptor')")
        self.cnxn.commit()
        self.cursor.execute("insert into testArtifacts (artifactID, artifactName, configID) values ('art1', 'Artifact 1', 'TestConfig'), ('art2', 'Artifact 2', 'TestConfig');")
        self.cnxn.commit()
