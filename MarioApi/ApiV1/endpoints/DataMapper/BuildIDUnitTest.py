import unittest

from .BuildID import BuildID
from ..DatabaseConnectionManager import DatabaseConnectionManager

class MyTestCase(unittest.TestCase):
    def test_insert_update_delete(self):
        db = DatabaseConnectionManager('priort', 'SE4330team')
        buildID = BuildID(db)
        buildID.set_buildid("777")
        buildID.set_drivetype("Lean")
        buildID.set_environment("Real Motors")

        received = buildID.create()
        expected = True
        self.assertEqual(expected, received)

        buildID.set_environment("HIL")
        buildID.set_drivetype("Rack")
        received2 = buildID.update()
        expected2 = True
        self.assertEqual(expected2, received2)

        received3 = buildID.delete()
        expected3 = True
        self.assertEqual(expected3, received3)

    def test_read(self):
        db = DatabaseConnectionManager('priort', 'SE4330team')
        buildID = BuildID(db)
        buildID.set_drivetype("Lean")
        buildID.set_environment("Emulator")

        received = buildID.read()
        expected = True
        self.assertEqual(expected, received)

        received2 = buildID.get_buildid()
        expected2 = "4"
        self.assertEqual(expected2, received2)

    def test_read_first(self):
        db = DatabaseConnectionManager('priort', 'SE4330team')
        buildID = BuildID(db)
        buildID.set_drivetype("Lean")

        received = buildID.read_first('drivetype', 'Lean')
        expected = True
        self.assertEqual(expected, received)

        expectedBuildID = '4'
        expectedDriveType = 'Lean'
        expectedEnvironment = 'Emulator'

        actualBuildID = buildID.get_buildid()
        actualDriveType = buildID.get_drivetype()
        actualEnvironment = buildID.get_environment()

        self.assertEqual(expectedBuildID, actualBuildID)
        self.assertEqual(expectedDriveType, actualDriveType)
        self.assertEqual(expectedEnvironment, actualEnvironment)

if __name__ == '__main__':
    unittest.main()
