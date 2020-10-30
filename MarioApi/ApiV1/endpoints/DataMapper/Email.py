from .Persistent import Persistent

class Email(Persistent):
    """
    Class for representing an Email in the Emails table of our database.

    Attributes:
        EmailAddress: varchar(256), Primary Key, Email address to send result notifications to
        Name: varchar(64), Name of the owner of the email.
    """

    def __init__(self, databaseConnectionManager):
        super().__init__(databaseConnectionManager)
        self.emailAddress = None
        self.name = None

    def create(self):
        try:
            self.db.get_cursor().execute("Insert into emails (emailAddress, name) values ('" + str(self.emailAddress) +
                                     "', '" + str(self.name) + "');")
            self.db.get_connection().commit()
            return True
        except:
            return False

    def read(self):
        try:
            cursor = self.db.get_cursor()
            cursor.execute("Select name from emails where emailAddress = '" + str(self.emailAddress) + "';")
            row = cursor.fetchone()
            if row:
                self.name = str(row[0])
            return True
        except:
            return False

    def read_first(self, column_name, value):
        """
        Reads the first value from the Emails table to match the specified parameters.

        Parameters:
            column_name (string): The column name to be searched through. Not case sensitive.
            value (string): The value to be looked for in the specified column. Case sensitive.
        """
        try:
            cursor = self.db.get_cursor()
            cursor.execute("Select * from emails where " + str(column_name) + " = '" + str(value) + "';")
            row = cursor.fetchone()
            if row:
                self.emailAddress = str(row[0])
                self.name = str(row[1])
            return True
        except:
            return False

    def update(self):
        try:
            self.db.get_cursor().execute("Update Emails "
                                         "set name = '" + str(self.name) + "' "
                                         "where emailAddress = '" + str(self.emailAddress) + "';")
            self.db.get_connection().commit()
            return True
        except:
            return False

    def delete(self):
        try:
            self.db.get_cursor().execute("Delete from emails where emailAddress = '" + str(self.emailAddress) + "';")
            self.db.get_connection().commit()
            return True
        except:
            return False

    def set_emailAddress(self, address):
        self.emailAddress = address

    def set_name(self, name):
        self.name = name

    def get_emailAddress(self):
        return self.emailAddress

    def get_name(self):
        return self.name