from string_utils import StringUtils


class TestStringUtils:

    def test_capitalize_positive(self):
        utils = StringUtils()
        assert utils.capitalize("skypro") == "Skypro"
        assert utils.capitalize("hello world") == "Hello world"
        assert utils.capitalize("123abc") == "123abc"
        assert utils.capitalize("тест") == "Тест"

    def test_capitalize_negative(self):
        utils = StringUtils()
        assert utils.capitalize("") == ""
        assert utils.capitalize(" ") == " "
        assert utils.capitalize("   ") == "   "

    def test_trim_positive(self):
        utils = StringUtils()
        assert utils.trim("   skypro") == "skypro"
        assert utils.trim("  hello") == "hello"
        assert utils.trim(" test") == "test"
        assert utils.trim("no_spaces") == "no_spaces"

    def test_trim_negative(self):
        utils = StringUtils()
        assert utils.trim("") == ""
        assert utils.trim(" ") == ""
        assert utils.trim("   ") == ""
        assert utils.trim("hello  ") == "hello  "

    def test_contains_positive(self):
        utils = StringUtils()
        assert utils.contains("SkyPro", "S") is True
        assert utils.contains("hello world", " ") is True
        assert utils.contains("12345", "3") is True
        assert utils.contains("тест", "е") is True

    def test_contains_negative(self):
        utils = StringUtils()
        assert not utils.contains("hello", "x")
        assert not utils.contains("SkyPro", "z")
        assert not utils.contains("", "a")
        assert not utils.contains(" ", "a")
        assert utils.contains("hello", "") is True

    def test_contains_edge_cases(self):
        utils = StringUtils()
        assert utils.contains("SkyPro", "Sky") is True
        assert not utils.contains("SkyPro", "s")
        assert utils.contains("hello hello", "o") is True

    def test_delete_symbol_positive(self):
        utils = StringUtils()
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert utils.delete_symbol("hello world", " ") == "helloworld"
        assert utils.delete_symbol("aaaabbbb", "a") == "bbbb"
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_negative(self):

        utils = StringUtils()
        assert utils.delete_symbol("hello", "x") == "hello"
        assert utils.delete_symbol("", "a") == ""
        assert utils.delete_symbol(" ", " ") == ""
        assert utils.delete_symbol("aaaa", "a") == ""

    def test_delete_symbol_edge_cases(self):
        utils = StringUtils()
        result = utils.delete_symbol("hello", "")
        print(f"delete_symbol('hello', '') = '{result}'")
        assert result == "hello"
        assert utils.delete_symbol("  hello  ", " ") == "hello"
        assert utils.delete_symbol("testtest", "t") == "eses"
