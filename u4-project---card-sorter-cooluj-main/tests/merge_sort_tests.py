from card_loader import get_cards
from merge_sort import merge_sort
from tests.sort_tests_base import SortTestBase

class MergeTests(SortTestBase):

    def test_sort_by_name(self):
        cards = get_cards()
        merge_sort(cards, "Name")
        self.assert_list_sorted(cards, "Name")

    def test_sort_by_cost(self):
        cards = get_cards()
        merge_sort(cards, "Cost")
        self.assert_list_sorted(cards, "Cost")

