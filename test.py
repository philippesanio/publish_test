from main import Main

a = 1
b = 1

# test
def test_equal(a,b):
    assert Main.test_equal(a,b)

if __name__ == "__main__":
    test_equal(a,b)