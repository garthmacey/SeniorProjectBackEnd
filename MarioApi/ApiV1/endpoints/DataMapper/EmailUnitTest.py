import unittest

from .Email import Email
from ..DatabaseConnectionManager import DatabaseConnectionManager

class MyTestCase(unittest.TestCase):
    def test_insert_update_delete(self):
        db = DatabaseConnectionManager('priort', 'SE4330team')
        email = Email(db)
        email.set_emailAddress("doej@email.com")
        email.set_name("John Doe")

        received = email.create()
        expected = True
        self.assertEqual(expected, received)

        email.set_name("Jane Doe")
        received2 = email.update()
        expected2 = True
        self.assertEqual(expected2, received2)

        received3 = email.delete()
        expected3 = True
        self.assertEqual(expected3, received3)

    def test_readfirst(self):
        db = DatabaseConnectionManager('priort', 'SE4330team')
        email = Email(db)
        email.set_emailAddress("doej@email.com")
        email.set_name("John Doe")
        email.create()

        testEmail = Email(db)
        testEmail.read_first("name", "John Doe")
        receivedName = testEmail.get_name()
        expectedName = "John Doe"
        receivedAddress = testEmail.get_emailAddress()
        expectedAddress = "doej@email.com"
        self.assertEqual(expectedName, receivedName)
        self.assertEqual(expectedAddress, receivedAddress)

        email.delete()

if __name__ == '__main__':
    unittest.main()