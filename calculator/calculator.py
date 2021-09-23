import numbers
import re
import queue
import numpy
import stack
import operator_calc
import function_calc


class Calculator:
    """ Calculates an expression written in text format """

    def __init__(self):
        self.operators = {
            "add": operator_calc.Operator(
                numpy.add, 0), "subtract": operator_calc.Operator(
                numpy.subtract, 0), "multiply": operator_calc.Operator(
                numpy.multiply, 2), "divide": operator_calc.Operator(
                numpy.divide, 2), }

        self.functions = {"exp": function_calc.Function(numpy.exp),
                          "log": function_calc.Function(numpy.log),
                          "sin": function_calc.Function(numpy.sin),
                          "cos": function_calc.Function(numpy.cos),
                          "sqrt": function_calc.Function(numpy.sqrt)}
        self.nn_queue = queue.Queue()  # the normal notation queue
        self.output_queue = queue.Queue()  # the RPN queue
        self.operator_stack = stack.Stack()  # sorting out the elements
        self.rpn_stack = stack.Stack()

    def get_nn_queue(self):
        return self.nn_queue

    def get_output_queue(self):
        return self.output_queue

    def get_operator_stack(self):
        return self.operator_stack

    def get_rpn_stack(self):
        return self.rpn_stack

    def rpn_calculation(self):
        """ Finishes the calculation via rpn calculation """
        for i in self.output_queue.get_items():
            if isinstance(i, numbers.Number):
                self.rpn_stack.push(i)
            elif isinstance(i, function_calc.Function):
                num = self.rpn_stack.pop()
                self.rpn_stack.push(i.execute(num))
            elif isinstance(i, operator_calc.Operator):
                num1 = self.rpn_stack.pop()
                num2 = self.rpn_stack.pop()
                self.rpn_stack.push(i.execute(num1, num2))
        return self.rpn_stack.get_items()[0]

    def shunting_yard(self):
        """ Takes the nn-queue and turns it into a queue the rpn calculation can read """
        for i in self.nn_queue.get_items():
            if isinstance(i, numbers.Number):
                self.output_queue.push(i)
            elif isinstance(i, function_calc.Function) or i == "(":
                self.operator_stack.push(i)
            elif i == ")":
                while len(self.operator_stack.get_items()) > 0:
                    num = self.operator_stack.pop()
                    if num != "(":  # to throw away the (
                        self.output_queue.push(num)
            elif isinstance(i, operator_calc.Operator):
                while len(self.operator_stack.get_items()
                          ) > 0 and self.operator_stack.peek() != '(':
                    if isinstance(
                            self.operator_stack.peek(),
                            operator_calc.Operator) and self.operator_stack.peek().get_strength() < i.get_strength():
                        break
                    num = self.operator_stack.pop()
                    self.output_queue.push(num)
                self.operator_stack.push(i)
        for i in self.operator_stack.get_items():
            num = self.operator_stack.pop()
            self.output_queue.push(num)
        return self.output_queue

    def text_to_nnq(self, text):
        """ Takes a text string and turns it into a queue in normal notation"""
        text = text.replace(" ", "")
        j = 0
        for i in range(len(text)):
            match = re.search("^[-0123456789.]+", text[j:])
            if match is not None:
                if match.group(0) == "-":
                    minus_num = text[j:(j + 2)]
                    self.nn_queue.push(int(minus_num))
                    j += match.end(0) + 1
                else:
                    self.nn_queue.push(int(match.group(0)))
                    j += match.end(0)
                continue
            targets = "|".join(["^" + func for func in self.functions.keys()])
            match = re.search(targets, text[j:])
            if match is not None:
                if match.group(0) == "exp":
                    self.nn_queue.push(self.functions["exp"])
                elif match.group(0) == "log":
                    self.nn_queue.push(self.functions["log"])
                elif match.group(0) == "sin":
                    self.nn_queue.push(self.functions["sin"])
                elif match.group(0) == "cos":
                    self.nn_queue.push(self.functions["cos"])
                elif match.group(0) == "sqrt":
                    self.nn_queue.push(self.functions["sqrt"])
                j += match.end(0)
                continue
            targets = "|".join(["^" + op for op in self.operators.keys()])
            match = re.search(targets, text[j:])
            if match is not None:
                if match.group(0) == "add":
                    self.nn_queue.push(self.operators["add"])
                elif match.group(0) == "subtract":
                    self.nn_queue.push(self.operators["subtract"])
                elif match.group(0) == "multiply":
                    self.nn_queue.push(self.operators["multiply"])
                elif match.group(0) == "divide":
                    self.nn_queue.push(self.operators["divide"])
                j += match.end(0)
                continue
            match = re.search(r"^\(|^\)", text[j:])
            if match is not None:
                self.nn_queue.push(match.group(0))
                j += match.end(0)
                continue
            if j > len(text):
                break
        return self.nn_queue

    def calculate_expression(self, text):
        self.text_to_nnq(text)
        self.shunting_yard()
        return self.rpn_calculation()