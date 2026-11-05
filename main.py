from binary_expression_tree import BinaryExpressionTree

tree = BinaryExpressionTree.from_postfix("12 -2.5 /")
root = tree.root()

print(root.element(), tree.left(root).element(), tree.right(root).element())

print(tree.evaluate())  # Output: -4.8)

print(tree.to_infix())  # Output: ((12 / -2.5)))

print(tree.to_postfix())  # Output: 12 -2.5 /)

print("Preorder:", " ".join(p.element() for p in tree.preorder()))

print("Inorder:", " ".join(p.element() for p in tree.inorder()))

expressions = [
    "5 3 8 * +",
    "8 2 / 3 -",
    "12 -2.5 /",
    "4 0 /",
    "7 +",
    "2 3 +",
]

for expression in expressions:
    print("Input:", expression)
    try:
        tree = BinaryExpressionTree.from_postfix(expression)
        print("Infix:", tree.to_infix())
        print("Postfix:", tree.to_postfix())
        print("Result:", tree.evaluate())
    except (ValueError, ZeroDivisionError) as error:
        print("Error:", error)
    print()