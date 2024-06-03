from unittest import TestCase
from linked_list import LinkedList

class LinkedListTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_simple_operations(self):
        linked_list = LinkedList()

        linked_list.insert(0, 11)
        linked_list.pop(0)

        linked_list.insert(0, 3)
        linked_list.insert(1, 12)
        linked_list.insert(1, 13)
        linked_list.pop(1)
        linked_list.pop(1)
     
        linked_list.insert(0, 1)
        linked_list.insert(2, 7)
        linked_list.insert(3, 4)
        linked_list.insert(1, 2)
        linked_list.pop(3)
        linked_list.insert(0, 9)
        linked_list.insert(5, 9)
        linked_list.pop(5)
        linked_list.pop(0)
        i = 1
        temp = linked_list.first
        while temp is not None:
            self.assertEqual(i, temp.value)
            temp = temp.next
            i += 1

        self.assertEqual(4, linked_list.count)
        two_index = linked_list.find_index(2)
        self.assertEqual(1, two_index)
        linked_list.set(two_index, 42)
        life = linked_list.find_index(42)
        self.assertEqual(two_index, life)
        self.assertEqual(-1, linked_list.find_index(2))
        self.assertEqual(1, linked_list.first.value)
        self.assertEqual(4, linked_list.last.value)
        linked_list.clear()
        self.assertEqual(0, linked_list.count)
        self.assertIsNone(linked_list.first)
        self.assertIsNone(linked_list.last)
        
    def test_out_of_bounds(self):
        linked_list = LinkedList()
        count = 0
        try:
            linked_list.insert(3, 3)
        except IndexError:
            count += 1
        else:
            self.fail("Should have an exception")


        try:
            linked_list.pop(0)
        except IndexError:
            count += 1
        else:
            self.fail("Should have an exception")

        linked_list.insert(0, 1)
        linked_list.insert(0, 7)

        try:
            linked_list.pop(3)
        except IndexError:
            count += 1
        else:
            self.fail("Should have an exception")

        try:
            linked_list.set(5, 2)
        except IndexError:
            count += 1
        else:
            self.fail("Should have an exception")

        self.assertEqual(4, count)