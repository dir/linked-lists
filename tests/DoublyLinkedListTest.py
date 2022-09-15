from src.DoublyLinkedList import *
import unittest


class TestDoublyLinkedList(unittest.TestCase):
    def testCase1(self):
        list = DoublyLinkedList()

        self.assertIsNone(list.find("fred"))
        list.add("fred")
        self.assertEqual("fred", list.find("fred").value())

        self.assertIsNone(list.find("wilma"))
        list.add("wilma")

        self.assertEqual("fred",  list.find("fred").value())
        self.assertEqual("wilma", list.find("wilma").value())
        self.assertEqual(["fred", "wilma"], list.values())

    def testCase2(self):
        list = DoublyLinkedList()

        list.add("fred")
        list.add("wilma")
        list.add("betty")
        list.add("barney")

        self.assertEqual(["fred", "wilma", "betty", "barney"], list.values())

        list.delete(list.find("wilma"))
        self.assertEqual(["fred", "betty", "barney"], list.values())

        list.delete(list.find("barney"))
        self.assertEqual(["fred", "betty"], list.values())

        list.delete(list.find("fred"))
        self.assertEqual(["betty"], list.values())

        list.delete(list.find("betty"))
        self.assertEqual([], list.values())