from .Persistent import Persistent

class Environment(Persistent):
    """
    Class for representing an Environment in the Environments table of our database.

    Attributes:
        Environment: varchar(32), Primary Key
    """

    def __init__(self, databaseConnectionManager):
        super().__init__(databaseConnectionManager)
        self.environment = None

    def create(self):
        try:
            self.db.get_connection().execute("Insert into environments (environment) values ('" + str(self.environment) + "');")
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
            self.db.get_cursor().execute("Delete from environments where environment = '" + str(self.environment) + "';")
            self.db.get_connection().commit()
            return True
        except:
            return False

    def set_environment(self, environment):
        self.environment = environment

    def get_environment(self):
        return self.environment