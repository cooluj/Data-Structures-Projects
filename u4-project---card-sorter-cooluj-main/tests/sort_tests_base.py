from typing import Dict, List
from unittest import TestCase

class SortTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def assert_list_sorted(self, list: List[Dict], key: str):
        for i in range(len(list) - 1):
            self.assertLessEqual(list[i][key], list[i + 1][key])