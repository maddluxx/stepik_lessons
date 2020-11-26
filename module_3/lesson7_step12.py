import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

if __name__ == "__main__":
    try:
        unittest.main()

    finally:
        # успеваем скопировать код за 30 секунд
        #time.sleep(10)
        # закрываем браузер после всех манипуляций
        #browser.quit()
        print('Yay!')

# не забываем оставить пустую строку в конце файла