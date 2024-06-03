from unittest import TestCase
from double_linked_list import DoubleLinkedList, DoubleListNode

class DoubleLinkedListTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_simple_operations(self):
        linked_list = DoubleLinkedList()

        delete_me = linked_list.insert_after(None, 11)
        linked_list.remove(delete_me)

        old_node = linked_list.insert_after(None, 11)
        linked_list.remove(old_node)
        third_node = linked_list.insert_after(None, 3)
        first_node = linked_list.insert_after(None, 1)
        delete_node = linked_list.insert_after(first_node, 7)
        fourth_node = linked_list.insert_after(third_node, 4)
        second_node = linked_list.insert_after(first_node, 2)
        linked_list.remove(delete_node)
        bad_node = linked_list.insert_after(None, 9)
        last_node = linked_list.insert_after(fourth_node, 9)
        linked_list.remove(last_node)
        linked_list.remove(bad_node)

        i = 1
        temp = linked_list.first
        prev = None
        while temp is not None:
            self.assertEqual(i, temp.value)
            self.assertEqual(prev, temp.previous_node)
            prev = temp
            temp = temp.next
            i += 1

        self.assertEqual(4, linked_list.count)
        two_node = linked_list.find_after(2)
        self.assertEqual(second_node, two_node)
        additional_two_node = linked_list.insert_after(two_node, 2)
        second_two_node = linked_list.find_after(2, two_node)
        self.assertEqual(second_two_node, additional_two_node)
        two_node = linked_list.find_last(2)
        self.assertEqual(additional_two_node, two_node)
        second_two_node = linked_list.find_last(2, two_node)
        self.assertEqual(second_node, second_two_node)
        
        self.assertEqual(1, linked_list.first.value)
        self.assertEqual(4, linked_list.last.value)
        linked_list.clear()
        self.assertEqual(0, linked_list.count)
        self.assertIsNone(linked_list.first)
        self.assertIsNone(linked_list.last)

    def test_out_of_bounds(self):
        linked_list = DoubleLinkedList()
        node = DoubleListNode(4)
        count = 0
        try:
            linked_list.insert_after(node, 3)
        except ValueError:
            count += 1
        else:
            self.fail("Should have an exception")


        try:
            linked_list.remove(node)
        except ValueError:
            count += 1
        else:
            self.fail("Should have an exception")
        try:
          linked_list.remove(None)
        except TypeError:
            count += 1
            
        linked_list.insert_after(None, 5)
        try:
          linked_list.find_last(4, node)
        except ValueError:
            count += 1
        else:
            self.fail("Should have an exception")

        try:
          linked_list.find_after(4, node)
        except ValueError:
            count += 1
        else:
            self.fail("Should have an exception")

        self.assertEqual(5, count)