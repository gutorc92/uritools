import unittest
from curitools.views.academic import ListView
import os

class TestSubmissionsPage(unittest.TestCase):


    def test_extract_table(self):
        repositorio_dir = os.path.dirname(os.path.realpath(__file__))
        file_name = os.path.join(repositorio_dir, "listasview.html")
        fn = open(file_name, 'r')
        text = fn.read()
        fn.close()
        s = ListView(text)
        s.extract_table()
        s.get_max_length()
        self.assertEqual(len(s.max_column), 4)
        s.print_table()
        self.assertEqual(len(s.data), 23)

    
if __name__ == '__main__':
    unittest.main()
