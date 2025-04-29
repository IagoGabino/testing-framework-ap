from test_framework.core import TestCase

class MyTest(TestCase):
    def set_up(self):
        print("set_up")

    def tear_down(self):
        print("tear_down")

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")

    def test_c(self):
        print("test_c")

if __name__ == "__main__":
    for method in ["test_a", "test_b", "test_c"]:
        test = MyTest(method)
        test.run()