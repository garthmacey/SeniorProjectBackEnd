import unittest

from .Environment import Environment
from ..DatabaseConnectionManager import DatabaseConnectionManager

class MyTestCase(unittest.TestCase):

    def test_insert_delete(self):
        db = DatabaseConnectionManager('priort', 'SE4330team')
        environment = Environment(db)
        environment.set_environment("test_environment")

        received = environment.create()
        expected = True
        self.assertEqual(expected, received)

        received2 = environment.delete()
        expected2 = True
        self.assertEqual(expected, received)

if __name__ == '__main__':
    unittest.main()
