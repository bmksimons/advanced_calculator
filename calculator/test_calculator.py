import unittest
import calculator


class MyTestCase(unittest.TestCase):
    """ Tests the calculator as a unity and the individually algorithms """

    def test_initializing(self):
        calc = calculator.Calculator()
        self.assertEqual(
            2, calc.functions['sqrt'].execute(
                calc.operators["add"].execute(
                    2, 2)))

    def test_rpn_calculation(self):
        """ Tests the rpn calculation individually """
        calc = calculator.Calculator()
        calc.get_output_queue().push(1)
        calc.get_output_queue().push(2)
        calc.get_output_queue().push(calc.operators["add"])
        calc.get_output_queue().push(2)
        calc.get_output_queue().push(calc.operators["multiply"])
        self.assertEqual(6, calc.rpn_calculation())

    def test_shunting_yard(self):
        """ Tests the shunting yard algorithm individually """
        calc = calculator.Calculator()
        calc.get_nn_queue().push("(")
        calc.get_nn_queue().push(1)
        calc.get_nn_queue().push(calc.operators["add"])
        calc.get_nn_queue().push(2)
        calc.get_nn_queue().push(")")
        calc.get_nn_queue().push(calc.operators["multiply"])
        calc.get_nn_queue().push(2)
        self.assertEqual([1,
                          2,
                          calc.operators["add"],
                          2,
                          calc.operators["multiply"]],
                         calc.shunting_yard().get_items())

    def test_text_to_nn(self):
        """ Tests the text_to_nn algorithm individually """
        calc = calculator.Calculator()
        self.assertEqual(["(",
                          1,
                          calc.operators["add"],
                          2,
                          ")",
                          calc.operators["multiply"],
                          2],
                         calc.text_to_nnq("(1 add 2) multiply 2").get_items())

    def test_calculation(self):
        """ Test the calculator from start to finish """
        calc = calculator.Calculator()
        self.assertEqual(
            48, calc.calculate_expression("(1 add 23) multiply 2"))
        calc2 = calculator.Calculator()
        self.assertEqual(-6, calc2.calculate_expression("-2 multiply 3"))
        calc3 = calculator.Calculator()
        self.assertEqual(10, calc3.calculate_expression("sqrt(-10 multiply -10)"))


if __name__ == '__main__':
    unittest.main()