import unittest

from binary_expression_tree import BinaryExpressionTree


class TestBinaryExpressionTree(unittest.TestCase):
    def test_addition(self):
        tree = BinaryExpressionTree.from_postfix("2 3 +")
        self.assertEqual(tree.evaluate(), 5.0)

    def test_nested_operators(self):
        expression = "5 3 8 * +"
        tree = BinaryExpressionTree.from_postfix(expression)
        self.assertEqual(tree.evaluate(), 29.0)
        self.assertEqual(tree.to_infix(), "(5 + (3 * 8))")
        self.assertEqual(tree.to_postfix().split(), expression.split())

    def test_operand_order(self):
        tree = BinaryExpressionTree.from_postfix("8 2 / 3 -")
        self.assertEqual(tree.evaluate(), 1.0)

    def test_negative_decimal(self):
        tree = BinaryExpressionTree.from_postfix("12 -2.5 /")
        self.assertAlmostEqual(tree.evaluate(), -4.8)

    def test_too_few_operands(self):
        with self.assertRaises(ValueError):
            BinaryExpressionTree.from_postfix("7 +")

    def test_division_by_zero(self):
        tree = BinaryExpressionTree.from_postfix("4 0 /")
        with self.assertRaises(ZeroDivisionError):
            tree.evaluate()