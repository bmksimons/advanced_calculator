import unittest
import numpy
import operator_calc
import function_calc


class MyTestCase(unittest.TestCase):
    """ Test the classes function and operator """

    def test_operations(self):
        """ Tests the class operator """
        add_op = operator_calc.Operator(numpy.add, 0)
        self.assertEqual(3, add_op.execute(1, 2))
        sub_op = operator_calc.Operator(numpy.subtract, 0)
        self.assertEqual(3, sub_op.execute(5, 2))
        multi_op = operator_calc.Operator(numpy.multiply, 2)
        self.assertEqual(12, multi_op.execute(6, 2))
        div_op = operator_calc.Operator(numpy.divide, 2)
        self.assertEqual(3, div_op.execute(6, 2))

    def test_complex_operations(self):
        """ Tests the class operator more in depth """
        add_op = operator_calc.Operator(numpy.add, 0)
        sub_op = operator_calc.Operator(numpy.subtract, 0)
        multi_op = operator_calc.Operator(numpy.multiply, 2)
        div_op = operator_calc.Operator(numpy.divide, 2)
        self.assertEqual(7, add_op.execute(1, multi_op.execute(2, 3)))
        self.assertEqual(1, div_op.execute(6, multi_op.execute(2, 3)))
        self.assertEqual(-5, sub_op.execute(1, multi_op.execute(2, 3)))

    def test_functions(self):
        """ Tests the class fucntion """
        exp_func = function_calc.Function(numpy.exp)
        self.assertEqual(1, exp_func.execute(0))
        sin_func = function_calc.Function(numpy.sin)
        self.assertEqual(0, sin_func.execute(0))


if __name__ == '__main__':
    unittest.main()