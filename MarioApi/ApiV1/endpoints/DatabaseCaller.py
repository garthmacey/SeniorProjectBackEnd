import pyodbc


class DatabaseCaller():
    """"A class to manage the databases used by the Mario pipeline manager."""
    #TODO: Remove default information for security
    server = 'tcp:projectspike.database.windows.net'
    database = 'ProjectsSpike'
    username = 'priort'
    password = 'SE4330team'

    #self.cursor.execute("SQL code") : runs SQL code on the database
    #self.cnxn.commit(): commits any waiting changes to the database


    def __init__(self):
        """Initializes the databases connection."""
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + DatabaseCaller.server + ';DATABASE=' + DatabaseCaller.database + ';UID=' + DatabaseCaller.username + ';PWD=' + DatabaseCaller.password)
        self.cursor = self.cnxn.cursor()

    def valid_input(self, input):
        """Checks input to determine whether it has suspicious characters often used for SQL injections.
        Returns True if input seems valid, returns False if input seems suspicious."""
        if ("'" in input or '"' in input or '=' in input or '(' in input or ')' in input or ';' in input or '*' in input):
            return False
        return True

    def drive_types_get(self):
        """Gets a list of all drive types from the DriveTypes table."""
        self.cursor.execute("select * from Drivetypes;")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def drive_types_insert(self, drivetype):
        """Insert a drive type into the database with name drivetype"""
        if (not (self.valid_input(drivetype))):
            return False
        try:
            self.cursor.execute("insert into Drivetypes (drivetype) values ('" + (drivetype) + "');")
            self.cnxn.commit()
            return True
        except:
            return False

    def environments_insert(self, environment):
        """Insert an environment into the database with name environment"""
        if (not (self.valid_input(environment))):
            return False
        try:
            self.cursor.execute("insert into Environments (environment) values ('" + (environment) + "');")
            self.cnxn.commit()
            return True
        except:
            return False

    def environments_get(self):
        """Gets a list of all environments from the Environments table."""
        self.cursor.execute("Select * from Environments;")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def drive_types_get(self):
        """Gets a list of drive types from the DriveTypes table."""
        self.cursor.execute("select * from Drivetypes;")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def drive_types_insert(self, driveType):
        """Insert a value into the DriveTypes table."""
        if (not (self.valid_input(driveType))):
            return False
        value = self.drive_types_get()
        if str(driveType) in value:
            return False
        self.cursor.execute("Insert into Drivetypes (driveType) values ('"
                            + str(driveType) + "');")
        self.cnxn.commit()
        return True

    def drive_types_update(self, oldDriveType, driveType):
        """Update a value of the DriveTypes table."""
        if not self.valid_input(oldDriveType) or not self.valid_input(driveType):
            return False
        value = self.drive_types_get()
        if not str(oldDriveType) in value or str(driveType) in value:
            return False
        self.cursor.execute("Update Drivetypes set driveType = '"
                            + str(driveType) + "' where driveType =  '" + str(oldDriveType) + "';")
        self.cnxn.commit()
        return True

    def drive_types_delete(self, driveType):
        '''Deletes the power card from the database with name driveType'''
        try:
            if not self.valid_input(driveType):
                return False
            self.cursor.execute("delete from DriveTypes where driveType = '" + str(driveType) + "';")
            self.cnxn.commit()
            return True
        except:
            return False

    def environment_get(self):
        """Gets a list of environments from the Environments table."""
        self.cursor.execute("Select * from Environments;")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def environment_insert(self, environment):
        """Insert a value into the Environments table."""
        if (not (self.valid_input(environment))):
            return False
        value = self.environment_get()
        if str(environment) in value:
            return False
        self.cursor.execute("Insert into Environments (environment) values ('"
                            + str(environment) + "');")
        self.cnxn.commit()
        return True

    def environment_update(self, oldEnvironment, environment):
        """Update a value of the Environments table."""
        if (not (self.valid_input(oldEnvironment)) or not (self.valid_input(environment))):
            return False
        value = self.environment_get()
        if not str(oldEnvironment) in value or str(environment) in value:
            return False
        self.cursor.execute("Update Environments set environment = '"
                            + str(environment) + "' where environment =  '" + str(oldEnvironment) + "';")
        self.cnxn.commit()
        return True

    def environment_delete(self, environment):
        '''Deletes the power card from the database with name environment'''
        try:
            if (not (self.valid_input(environment))):
                return False
            self.cursor.execute("delete from Environments where environment = '" + str(environment) + "';")
            self.cnxn.commit()
            return True
        except:
            return False

    def buildIDs_get(self, driveType, environment):
        """Gets a buildID given the drive type and the  environment."""
        if (not (self.valid_input(driveType) and self.valid_input(environment))):
            return False
        self.cursor.execute("Select buildID from BuildIDs "
                            "where driveType = '" + str(driveType) + "' and Environment = '" + str(environment) + "';")
        row = self.cursor.fetchone()
        if row:
            value = str(row[0])
            return value
        return None

    def buildIDs_getAll(self):
        """Gets all build Ids of builds in the database."""
        self.cursor.execute("Select buildID from BuildIDs; ")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def buildIDs_insert(self, buildID, driveType, environment, nickname):
        """Insert a value into the buildIDs table."""
        if (not (self.valid_input(buildID) and self.valid_input(driveType) and self.valid_input(environment))):
            return False
        value = self.buildIDs_get(driveType, environment)
        if (value):
            return False
        value = self.buildIDs_getAll()
        if str(buildID) in value:
            return False
        self.cursor.execute("Insert into BuildIDs (buildID, driveType, Environment, nickname) values ('"
                            + str(buildID) + "', '" + str(driveType) + "', '" + str(environment) + "', '" + str(nickname) + "');")
        self.cnxn.commit()
        return True

    def buildIDs_patch(self, oldBuildID, buildID, driveType, environment, nickname):
        """Updates a buildID mapping in the buildIDs table."""
        if (not (self.valid_input(oldBuildID) and self.valid_input(buildID) and self.valid_input(driveType) and self.valid_input(environment))):
            return False
        value = self.buildIDs_get(driveType, environment)
        if (value):
            return False
        value = self.buildIDs_getAll()
        if str(buildID) in value or not str(oldBuildID) in value:
            return False
        self.cursor.execute("Update BuildIDs Set buildID='" + str(buildID) + "', driveType='" + str(driveType)
                            + "', Environment='" + str(environment) + "', nickname='" + str(nickname)
                            + "' where buildID='" + str(oldBuildID) + "';")
        self.cnxn.commit()
        return True

    def buildIDs_delete(self, buildID):
        """Deletes a buildID mapping from the buildIDs table"""
        if not self.valid_input(buildID):
            return False
        value = self.buildIDs_getAll()
        if not str(buildID) in value:
            return False
        self.cursor.execute("Delete from BuildIDs where buildID='" + str(buildID) + "';")
        self.cnxn.commit()
        return True

    def buildIDs_getMaps(self):
        """Gets all build IDs with their associated driveType and EnvType"""
        self.cursor.execute("Select * from BuildIDs;")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(row)
            row = self.cursor.fetchone()
        return values

    def powercards_insert(self, powercard, value):
        '''Inserts a power card into the database with name powercard'''
        try:
            if (not (self.valid_input(powercard) and self.valid_input(value))):
                return False
            powercards = self.powercards_get_names()
            if (powercard in powercards):
                return False
            self.cursor.execute(
                "insert into PowerCards (powerCardID, value) values ('" + str(powercard) + "', '" + str(value) + "');")
            self.cnxn.commit()
            return True
        except:
            return False

    def powercards_delete(self, powercard):
        '''Deletes the power card from the database with name powercard'''
        try:
            if (not (self.valid_input(powercard))):
                return False
            self.cursor.execute("delete from Powercards where powercardID = '" + str(powercard) + "';")
            self.cnxn.commit()
            return True
        except:
            return False

    def powercards_get_names(self):
        '''Gets the name of all power cards from the database'''
        self.cursor.execute("Select powercardID from Powercards; ")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def powercards_get(self, powercard):
        """Gets row from Powercards table with key powercard."""
        if (not (self.valid_input(powercard))):
            return False
        powercards = self.powercards_get_names()
        if (powercard not in powercards):
            return False
        self.cursor.execute("Select * from Powercards where powercardID = '" + str(powercard) + "';")
        row = self.cursor.fetchone()
        if row:
            values = {'powercardID': str(row[0]),
                      'value': str(row[1])}
        return values

    def applications_insert(self, application, value):
        '''Inserts an application into the database with name application and value of value'''
        try:
            if (not (self.valid_input(application) and self.valid_input(value))):
                return False
            applications = self.applications_get_names()
            if (application in applications):
                return False
            self.cursor.execute(
                "insert into Applications (applicationID, value) values ('" + str(application) + "', '" + str(
                    value) + "');")
            self.cnxn.commit()
            return True
        except:
            return False

    def applications_delete(self, application):
        '''Deletes an application from the database with name application'''
        try:
            if (not (self.valid_input(application))):
                return False
            self.cursor.execute("delete from Applications where applicationID = '" + str(application) + "';")
            self.cnxn.commit()
            return True
        except:
            return False

    def applications_get_names(self):
        '''Gets the name of all applications in the database'''
        self.cursor.execute("Select applicationID from Applications; ")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def applications_get(self, application):
        """Gets row from Applications table with key application."""
        if (not (self.valid_input(application))):
            return False
        applications = self.applications_get_names()
        if (application not in applications):
            return False
        self.cursor.execute("Select * from Applications where applicationID = '" + str(application) + "';")
        row = self.cursor.fetchone()
        if row:
            values = {'applicationID': str(row[0]),
                      'value': str(row[1])}
        return values

    def firmwares_insert(self, firmware, value):
        '''Inserts a row into the Firmwares table with key firmware.'''
        try:
            if (not (self.valid_input(firmware) and self.valid_input(value))):
                return False
            firmwares = self.firmwares_get_names()
            if (firmware in firmwares):
                return False
            self.cursor.execute(
                "insert into Firmwares (firmwareID, value) values ('" + str(firmware) + "', '" + str(value) + "');")
            self.cnxn.commit()
            return True
        except:
            return False

    def firmwares_delete(self, firmware):
        '''Deletes row from Firmwares table with key firmware.'''
        try:
            if (not (self.valid_input(firmware))):
                return False
            self.cursor.execute("delete from Firmwares where firmwareID = '" + str(firmware) + "';")
            self.cnxn.commit()
            return True
        except:
            return False

    def firmwares_get_names(self):
        '''Gets the names of all firmwares in the database'''
        self.cursor.execute("Select firmwareID from Firmwares; ")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def firmwares_get(self, firmware):
        """Gets row from Firmwares with key firmware."""
        if (not (self.valid_input(firmware))):
            return False
        firmwares = self.firmwares_get_names()
        if (firmware not in firmwares):
            return False
        self.cursor.execute("Select * from Firmwares where firmwareID = '" + str(firmware) + "';")
        row = self.cursor.fetchone()
        if row:
            values = {'firmwareID': str(row[0]),
                      'value': str(row[1])}
        return values

    def drive_types_get_by_environment(self, environment):
        '''Gets all drive types from BuildIDs that have the specified test environment.'''
        if (not (self.valid_input(environment))):
            return False
        self.cursor.execute("Select drivetype from Buildids where environment = '" + str(environment) + "';")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def environments_get_by_drive_type(self, drivetype):
        '''Gets all environments from BuildIDs that have the specified drivetype'''
        if (not (self.valid_input(drivetype))):
            return False
        self.cursor.execute("Select environment from Buildids where drivetype = '" + str(drivetype) + "';")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(str(row[0]))
            row = self.cursor.fetchone()
        return values

    def emails_insert(self, emailAddress, name):
        """Inserts a row into the Emails table."""
        try:
            if (not (self.valid_input(emailAddress) and self.valid_input(name))):
                return False
            self.cursor.execute("Insert into Emails (emailAddress, name) values ('" + str(emailAddress) +
                                "', '" + str(name) + "');")
            self.cnxn.commit()
            return True
        except:
            return False

    def emails_getAll(self):
        """Returns all rows in the Emails table. Returns array of format (address, name)."""
        self.cursor.execute("Select * from Emails order by name;")
        values = []
        row = self.cursor.fetchone()
        while row:
            values.append(((str(row[0])), (str(row[1]))))
            row = self.cursor.fetchone()
        return values

    def emails_delete(self, emailAddress):
        """Deletes a row from the Emails table with key emailAddress."""
        try:
            if (not (self.valid_input(emailAddress))):
                return False
            self.cursor.execute("Delete from Emails where emailAddress = '" + str(emailAddress) + "';")
            self.cnxn.commit()
            return True
        except:
            return False


    def configurations_insert(self, configID, buildID, applicationID, firmwareID, powerCardID):
        """Inserts a row into the Configurations table with key configID."""
        try:
            if (not(self.valid_input(configID) and self.valid_input(buildID) and self.valid_input(applicationID) and self.valid_input(firmwareID) and self.valid_input(powerCardID))):
                return False
            self.cursor.execute("Insert into Configurations (configID, buildID, applicationID, firmwareID, powerCardID) values ('" + str(configID) + "', '" + str(buildID) +
                                "', '" + str(applicationID) + "', '" + str(firmwareID) +"', '" + str(powerCardID) + "');")
            self.cnxn.commit()
            return True
        except:
            return False

    def configurations_get_names(self):
        """Gets all rows from the configurations table. Returns array of format (configID)."""
        try:
            self.cursor.execute("Select configID from Configurations;")
            row = self.cursor.fetchone()
            values = []
            while (row):
                values.append(row[0])
                row = self.cursor.fetchone()
            return values
        except:
            return False

    def configurations_get(self, configID):
        """Gets row from Configurations table with key configID. Also gets row from BuildIDs table with
        the matching buildID from the configuration."""
        try:
            if (not (self.valid_input(configID))):
                return False
            self.cursor.execute("Select buildID, applicationID, firmwareID, powerCardID from Configurations where configID = '" + str(configID) +"';")
            row = self.cursor.fetchone()
            buildID = row[0]
            applicationID = row[1]
            firmwareID = row[2]
            powerCardID = row[3]
            self.cursor.execute("Select drivetype, environment from BuildIDs where buildID = '" + str(buildID) + "';")
            row = self.cursor.fetchone()
            drivetype = row[0]
            environment = row[1]
            values = [buildID, drivetype, environment, applicationID, firmwareID, powerCardID]
            return values
        except:
            return False


    def configurations_update(self, configID, buildID, applicationID, firmwareID, powerCardID):
        """Updates row in Configurations table. Updates row with key configID."""
        try:
            if (not(self.valid_input(configID) and self.valid_input(buildID) and self.valid_input(applicationID) and self.valid_input(firmwareID) and self.valid_input(powerCardID))):
                return False
            self.cursor.execute("Update Configurations "
                                "set buildID = '" + str(buildID) + "', "
                                "applicationID = '" + str(applicationID) + "', "
                                "firmwareID = '" + str(firmwareID) + "', "
                                "powerCardID = '" + str(powerCardID) + "' "
                                "where configID = '" + str(configID) + "';")
            self.cnxn.commit()
            return True
        except:
            return False

    def configurations_delete(self, configID):
        """Deletes row from Configurations table. Deletes row with key configID."""
        try:
            if (not(self.valid_input(configID))):
                return False
            self.cursor.execute("Delete from Configurations where configID = '" + str(configID) + "';")
            self.cnxn.commit()
            return True
        except:
            return False

    def users_get(self, email):
        """Gets a row from the Emails table. Gets row with key email."""
        try:
            if (not(self.valid_input(email))):
                return False
            self.cursor.execute("Select descriptor from Users where email = '" + str(email) + "';")
            row = self.cursor.fetchone()
            return row[0]
        except:
            return False

    def users_insert(self, email, descriptor):
        """Inserts a row into the Emails table. Inserts with key email."""
        try:
            if (not(self.valid_input(email) and self.valid_input(descriptor))):
                return False
            self.cursor.execute("Insert into Users(email, descriptor) values ('" + str(email) + "', '" + str(descriptor) + "');")
            self.cnxn.commit()
            return True
        except:
            return False

    def users_delete(self, email):
        """Deletes a row from the Emails table. Deletes row with key email."""
        try:
            if (not(self.valid_input(email))):
                return False
            self.cursor.execute("Delete from Users where email = '" + str(email) + "';")
            self.cnxn.commit()
            return True
        except:
            return False

    def users_update(self, email, descriptor):
        """Updates a row of the Emails table. Updates descriptor based on key email."""
        try:
            if (not(self.valid_input(email) and self.valid_input(descriptor))):
                return False
            self.cursor.execute("Update Users "
                                "set descriptor = '" + str(descriptor) + "' "
                                "where email = '" + str(email) + "';")
            self.cnxn.commit()
            return True
        except:
            return False

    def artifacts_insert(self, artifactID, artifactName, configID):
        """Inserts a row to the Artifacts table with key artifactID and configID."""
        try:
            if (not(self.valid_input(artifactID) and self.valid_input(artifactName) and self.valid_input(configID))):
                return False
            self.cursor.execute("Insert into Artifacts(artifactID, artifactName, configID) values "
                                "('" + str(artifactID) + "', '" + str(artifactName) + "', '" + str(configID) + "');")
            self.cnxn.commit()
            return True
        except:
            return False

    def artifacts_get_all(self, configID):
        """Returns all rows from the Artifacts table. Returns array of format (artifactID, artifactName, configID)."""
        try:
            if (not(self.valid_input(configID))):
                return False
            self.cursor.execute("Select * from Artifacts where configID = '" + str(configID) + "';")
            values = []
            row = self.cursor.fetchone()
            while row:
                values.append(((str(row[0])), (str(row[1])), (str(row[2]))))
                row = self.cursor.fetchone()
            return values
        except:
            return False

    def artifacts_delete(self, artifactID, configID):
        """Deletes a row from the Artifacts table. Deletes artifact with key artifactID and configID."""
        try:
            if (not(self.valid_input(artifactID) and self.valid_input(configID))):
                return False
            self.cursor.execute("Delete from Artifacts where artifactID = '" + str(artifactID) + "' and configID = '" + str(configID) + "';")
            self.cnxn.commit()
            return True
        except:
            return False

    def artifacts_update(self, artifactID, artifactName, configID):
        """Updates a row of the Artifacts table. Updates artifactName for a given key of artifactID and configID."""
        try:
            if (not(self.valid_input(artifactID) and self.valid_input(artifactName) and self.valid_input(configID))):
                return False
            self.cursor.execute("Update Artifacts "
                                "set artifactName = '" + str(artifactName) + "' "
                                "where artifactID = '" + str(artifactID) + "' and configID = '" + str(configID) + "';")
            self.cnxn.commit()
            return True
        except:
            return False

    #TODO Fix outputs from input sanitizer. Create inserts for all tables
    #TODO Add nickname to BuildIDs