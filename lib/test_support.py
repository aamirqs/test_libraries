class TestSupport:
    def test_assert(self, expression, message):
        if not expression:
            raise Exception("")

        pass

    def test_assert_expected(self, actual, expected, message):
        return self.test_assert(str(actual).strip() == str(expected).strip(), message)

    def test_critical(self, message):
        pass

    def logger(self):
        pass


class Error(Exception):
    pass


test_obj = TestSupport()
