from card_loader import get_cards
from quick_sort import quick_sort
from tests.sort_tests_base import SortTestBase

class QuickSortTests(SortTestBase):

    def test_sort_by_name(self):
        cards = get_cards()
        quick_sort(cards, "Name")
        self.assert_list_sorted(cards, "Name")

    def test_sort_by_cost(self):
        cards = get_cards()
        quick_sort(cards, "Cost")
        self.assert_list_sorted(cards, "Cost")