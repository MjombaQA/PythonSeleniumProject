from example import Example

import unittest


class MyTestCase(unittest.TestCase):
    def test_add(self):
        result = Example.__add__(self,10,20)
        self.assertEqual(result,30)

    def test_sub(self):
        result = Example.__sub__(self,34,17)
        self.assertEqual(result,17)





if __name__ == '__main__':
    unittest.main()
