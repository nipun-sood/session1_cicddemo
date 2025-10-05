import unittest
from .logic import get_initials, get_last_names_logic

class DummyConn:
    # Dummy connection for testing
    def cursor(self):
        return self
    def execute(self, query, params):
        self.first_name = params[0]
        return self
    def fetchall(self):
        # Simulate DB response for first name "Virat"
        if self.first_name == "Virat":
            return [("Kohli",), ("Sharma",)]
        return []
    def close(self):
        pass

class TestLogic(unittest.TestCase):
    def test_get_initials(self):
        self.assertEqual(get_initials("Virat", "Kohli"), "VK")
        self.assertEqual(get_initials("Sachin", "Tendulkar"), "ST")
        self.assertEqual(get_initials("Rahul", "Dravid"), "RD")
        # first or last name test case
        self.assertEqual(get_initials("", "Obama"), "O")
        self.assertEqual(get_initials("Madonna", ""), "M")
        # both names empty
        self.assertEqual(get_initials("", ""), "")

    def test_get_last_names_logic(self):
        conn = DummyConn()
        result = get_last_names_logic(conn, "Virat")
        self.assertIn('Virat "VK" Kohli', result)
        self.assertIn('Virat "VS" Sharma', result)
        self.assertEqual(len(result), 2)

if __name__ == "__main__":
    unittest.main()
