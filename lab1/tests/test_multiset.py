import unittest

from lab1.task1.multiset import MultiSet


class TestMultiSet(unittest.TestCase):

    def test_valid_init(self):
        set_to_test = MultiSet("{a,b,c}")
        self.assertEqual(len(set_to_test), 3)
        self.assertIn("a", set_to_test)
        self.assertIn("b", set_to_test)
        self.assertIn("c", set_to_test)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            MultiSet("a,b,c") 
        with self.assertRaises(ValueError):
            MultiSet("{a,{b}}}}") 
        with self.assertRaises(ValueError):
            MultiSet("{a,}") 
        with self.assertRaises(ValueError):
            MultiSet("{,1") 

    def test_empty_init(self):
        empty_set = MultiSet()
        self.assertTrue(empty_set.is_empty())

    def test_empty_nested_set(self):
        empty_nested_set = MultiSet("{{}}")
        self.assertIn("{}", str(empty_nested_set))

    def test_validate_sets(self):
        set_to_test = MultiSet()
        self.assertFalse(set_to_test._validate(""))
        self.assertFalse(set_to_test._validate("{,}"))
        self.assertTrue(set_to_test._validate("{1,2,{3}}"))
        self.assertFalse(set_to_test._validate("{a,,b}"))
        self.assertFalse(set_to_test._validate("{a,{b}"))
        self.assertFalse(set_to_test._validate("{a"))
        self.assertFalse(set_to_test._validate("abc"))

    def test_add_element(self):
        set1 = MultiSet()
        set1.add("{{1}}")
        set1.add("{x}")
        self.assertEqual(len(set1), 2)

    def test_remove_element(self):
        set1=MultiSet("{1,{2,3},{}}")
        self.assertTrue(set1.remove("1"))
        self.assertEqual(len(set1), 2)
        self.assertFalse(set1.remove("2")) 
        self.assertTrue(set1.remove("{}"))
        self.assertEqual(len(set1), 1)

    def test_power_of_set(self):
        set_to_test = MultiSet("{1,{2,{3,{4}}}}")
        self.assertEqual(len(set_to_test), 2)

    def test_contains(self):
        set_to_test = MultiSet("{x,{y,z}}")
        self.assertIn("x", set_to_test)    
        self.assertNotIn("1", set_to_test)
        self.assertIn("{y,z}",set_to_test)

    def test_is_empty(self):
        set_to_test = MultiSet("{}")
        self.assertTrue(set_to_test.is_empty())
        set_to_test.add("1")
        self.assertFalse(set_to_test.is_empty())

    def test_union_of_sets(self):
        set1 = MultiSet("{1,2,3}")
        set2 = MultiSet("{1,3,{},{2}}")
        result = set1.union_of_sets(set2)
        self.assertEqual(str(result), "{1,2,3,{},{2}}")

    def test_intersection_of_sets(self):
        set1 = MultiSet("{a,a,b}")
        set2 = MultiSet("{a,c}")
        result = set1.intersection_of_sets(set2)
        self.assertEqual(str(result), "{a}")

    def test_difference_of_sets(self):
        set1 = MultiSet("{1,2,{5}}")
        set2 = MultiSet("{4,1,{}}")
        result = set1.difference_of_sets(set2)
        self.assertEqual(str(result), "{2,{5}}")

    def test_boolean_of_sets(self):
        set_to_test = MultiSet("{1,2,{}}")
        boolean_string = set_to_test.boolean_of_set()
        expected_subsets = [
            "{}","{1}","{2}","{{}}","{1,2}",       
            "{1,{}}","{2,{}}","{1,2,{}}"     
        ]
        for subset in expected_subsets:
            with self.subTest(subset=subset):
                self.assertIn(subset, boolean_string)

    def test_subset_to_str(self):
        set_to_test = MultiSet("{a}")
        self.assertEqual(set_to_test._subset_to_str({}), "{}")
        self.assertEqual(set_to_test._subset_to_str({"a": 2}), "{a,a}")

    def test_backtrack_generates_subsets(self):
        set_to_test = MultiSet("{a}")
        result = []
        set_to_test._backtrack(0, {}, ["a"], [2], result)
        expected = [
            {},           
            {"a": 1},     
            {"a": 2}      
        ]
        for subset in expected:
            with self.subTest(subset=subset):
                self.assertIn(subset, result)

    def test_clear_and_pass_to_parser_string_empty(self):
        set1 = MultiSet()
        set1.clear_and_pass_to_parser_string("")  # просто не падает
        self.assertTrue(set1.is_empty())
        set2 = MultiSet()
        set2.clear_and_pass_to_parser_string("{    a,  { b} }")
        self.assertIn("a", set2)
        self.assertIn("{b}", set2)  
        self.assertEqual(len(set2), 2)


