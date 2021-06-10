httprunner还支持的断言方法不止于此。由httprunner3.0 源码parser_test.py文件可知，httprunner还支持以下的断言方法：

def test_get_uniform_comparator(self):
    self.assertEqual(parser.get_uniform_comparator("eq"), "equals")
    self.assertEqual(parser.get_uniform_comparator("=="), "equals")
    self.assertEqual(parser.get_uniform_comparator("lt"), "less_than")
    self.assertEqual(parser.get_uniform_comparator("le"), "less_than_or_equals")
    self.assertEqual(parser.get_uniform_comparator("gt"), "greater_than")
    self.assertEqual(parser.get_uniform_comparator("ge"), "greater_than_or_equals")
    self.assertEqual(parser.get_uniform_comparator("ne"), "not_equals")

    self.assertEqual(parser.get_uniform_comparator("str_eq"), "string_equals")
    self.assertEqual(parser.get_uniform_comparator("len_eq"), "length_equals")
    self.assertEqual(parser.get_uniform_comparator("count_eq"), "length_equals")

    self.assertEqual(parser.get_uniform_comparator("len_gt"), "length_greater_than")
    self.assertEqual(parser.get_uniform_comparator("count_gt"), "length_greater_than")
    self.assertEqual(parser.get_uniform_comparator("count_greater_than"), "length_greater_than")

    self.assertEqual(parser.get_uniform_comparator("len_ge"), "length_greater_than_or_equals")
    self.assertEqual(parser.get_uniform_comparator("count_ge"), "length_greater_than_or_equals")
    self.assertEqual(parser.get_uniform_comparator("count_greater_than_or_equals"), "length_greater_than_or_equals")

    self.assertEqual(parser.get_uniform_comparator("len_lt"), "length_less_than")
    self.assertEqual(parser.get_uniform_comparator("count_lt"), "length_less_than")
    self.assertEqual(parser.get_uniform_comparator("count_less_than"), "length_less_than")

    self.assertEqual(parser.get_uniform_comparator("len_le"), "length_less_than_or_equals")
    self.assertEqual(parser.get_uniform_comparator("count_le"), "length_less_than_or_equals")
    self.assertEqual(parser.get_uniform_comparator("count_less_than_or_equals"), "length_less_than_or_equals")
	
从上文可以看到，validate支持等于、不等于、少于、多余等多种规则的校验。