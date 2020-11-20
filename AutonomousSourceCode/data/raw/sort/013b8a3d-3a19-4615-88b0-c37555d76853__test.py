import unittest


def sort(list):
    return sorted(list)

class Tester(unittest.TestCase):
    def setUp(self):
        self.x=1

    def test_add(self):
        list=[5,3,1]
        list=sort(list)
        self.assertEqual(list[0],1)


if __name__ =='__main__':
    unittest.main()


