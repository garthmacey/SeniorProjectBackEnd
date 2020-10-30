import abc

class Persistent(abc.ABC):
    """
    Class for representing persistent data types in a database table.
    Each table should be its own subclass of Persistent.
    Each subclass should have attributes matching the columns in its table.
    """

    def __init__(self, databaseConnectionManager):
        """
        Initializes the databases connection.

        Parameters:
            databaseConnectionManager: A DatabaseConnectionManager connected to the database to be manipulated.
        """
        self.db = databaseConnectionManager
        # subclasses should have super().__init__(databaseConnectionManager)
        # before their init

    @abc.abstractmethod
    def create(self):
        """Inserts the persistent data type into its table."""
        pass

    @abc.abstractmethod
    def read(self):
        """Reads the persistent data type from its table based on primary key(s)."""
        pass

    @abc.abstractmethod
    def update(self):
        """Updates the persistent data type in its table based on the primary key(s)."""
        pass

    @abc.abstractmethod
    def delete(self):
        """Deletes the persistent data type in its table based on the primary key(s)."""
        pass