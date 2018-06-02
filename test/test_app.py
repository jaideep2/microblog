import unittest

class AppTest(unittest.TestCase):
    def test_app_so_we_can_test_furthur(self):
        self.assertIsNone(None)

class FormsTest(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual([1, 2], [1, 2])

class ModelsTest(unittest.TestCase):
    def test_assert_is(self):
        self.assertIs([1, 2], [1, 2])

class RoutesTest(unittest.TestCase):
    def test_exception(self):
        try:
            response = 'bababa'
            if "K" in response:
                raise ValueError("Not found")
        except ValueError:
            return
        self.fail("ValueError was not raised")

class MigrationsTest(unittest.TestCase):
    pass

class TemplatesTest(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()