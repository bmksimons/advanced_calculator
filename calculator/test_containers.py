import queue
import unittest
import stack


class MyTestCase(unittest.TestCase):
    """ Tests the methods 'push', 'peek' and 'pop' in stack and queue """

    def test_push(self):
        """ Tests 'push' for stack and queue """
        stack_1 = stack.Stack()
        queue_2 = queue.Queue()
        stack_1.push(2)
        self.assertEqual(2, stack_1.peek())
        queue_2.push(2)
        self.assertEqual(2, queue_2.peek())
        stack_1.push(3)
        self.assertEqual(stack_1.get_items()[0], 2)

    def test_peek_stack(self):
        """ Tests 'peek' for stack """
        stack_1 = stack.Stack()
        stack_1.push(1)
        stack_1.push(2)
        stack_1.push(3)
        self.assertEqual(stack_1.peek(), 3)

    def test_pop_stack(self):
        """ Tests 'pop' for stack """
        stack_1 = stack.Stack()
        stack_1.push(1)
        stack_1.push(2)
        stack_1.push(3)
        self.assertEqual(stack_1.pop(), 3)
        self.assertEqual(stack_1.peek(), 2)

    def test_peek_queue(self):
        """ Tests 'peek' for queue """
        queue_1 = queue.Queue()
        queue_1.push(1)
        queue_1.push(2)
        queue_1.push(3)
        self.assertEqual(queue_1.peek(), 1)

    def test_pop_queue(self):
        """ Tests 'pop' for queue """
        queue_1 = queue.Queue()
        queue_1.push(1)
        queue_1.push(2)
        queue_1.push(3)
        self.assertEqual(queue_1.pop(), 1)
        self.assertEqual(queue_1.peek(), 2)


if __name__ == '__main__':
    unittest.main()
