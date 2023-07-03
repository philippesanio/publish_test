class Main:
    def __init__(self):
        pass

    @classmethod
    def run(cls):
        print("This is a test in main.py")

    @classmethod
    def test_equal(cls, a, b) -> bool:
        return a == b

# main
if __name__ == "__main__":
    Main.run()
