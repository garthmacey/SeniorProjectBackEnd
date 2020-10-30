import unittest

from .DriveType import DriveType
from ..DatabaseConnectionManager import DatabaseConnectionManager

class MyTestCase(unittest.TestCase):
    def test_insert_delete(self):
        db = DatabaseConnectionManager('priort', 'SE4330team')
        drivetype = DriveType(db)
        drivetype.set_drivetype("test_drive")

        received = drivetype.create()
        expected = True
        self.assertEqual(expected, received)

        received2 = drivetype.delete()
        expected2 = True
        self.assertEqual(expected, received)

if __name__ == '__main__':
    unittest.main()
