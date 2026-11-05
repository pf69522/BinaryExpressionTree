from stack import Stack


class BinaryExpressionTree:
    class _Node:
        def __init__(self, token):
            self.element = token
            self.parent = None
            self.left = None
            self.right = None
    class Position:
        def __init__(self, node):
            self._node = node

        def element(self):
            return self._node.element

    def __init__(self, token):
        self._root = self._Node(token)

    def root(self):
        return self.Position(self._root)
    
    def left(self, position):
        node = position._node.left
        if node is None:
            return None
        return self.Position(node)

    def right(self, position):
        node = position._node.right
        if node is None:
            return None
        return self.Position(node)

    def parent(self, position):
        node = position._node.parent
        if node is None:
            return None
        return self.Position(node)

    def _attach_subtrees(self, left_tree, right_tree):
        self._root.left = left_tree._root
        self._root.right = right_tree._root

        self._root.left.parent = self._root
        self._root.right.parent = self._root

        left_tree._root = None
        right_tree._root = None

    @classmethod
    def from_postfix(cls, postfix_expression):
        tokens = postfix_expression.split()
        if not tokens:
            raise ValueError("The postfix expression is empty.")

        stack = Stack()

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                if stack.size() < 2:
                    raise ValueError(f"Operator {token!r} needs two operands.")

                right_tree = stack.pop()
                left_tree = stack.pop()
                tree = cls(token)
                tree._attach_subtrees(left_tree, right_tree)
                stack.push(tree)
            else:
                try:
                    float(token)
                except ValueError:
                    raise ValueError(f"Unsupported token: {token!r}") from None

                stack.push(cls(token))

        if stack.size() != 1:
            raise ValueError("The postfix expression has extra operands.")

        return stack.pop()

    def evaluate(self):
        return self._evaluate(self.root())

    def _evaluate(self, position):
        token = position.element()
        left = self.left(position)
        right = self.right(position)

        if left is None and right is None:
            return float(token)

        left_value = self._evaluate(left)
        right_value = self._evaluate(right)

        if token == "+":
            return left_value + right_value
        if token == "-":
            return left_value - right_value
        if token == "*":
            return left_value * right_value
        if token == "/":
            if right_value == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return left_value / right_value

        raise ValueError(f"Unsupported operator: {token!r}")

    def to_infix(self):
        return self._to_infix(self.root())

    def _to_infix(self, position):
        left = self.left(position)
        right = self.right(position)
        token = position.element()

        if left is None and right is None:
            return token

        left_text = self._to_infix(left)
        right_text = self._to_infix(right)
        return f"({left_text} {token} {right_text})"

    def postorder(self):
        yield from self._postorder(self.root())

    def _postorder(self, position):
        if position is None:
            return

        yield from self._postorder(self.left(position))
        yield from self._postorder(self.right(position))
        yield position

    def to_postfix(self):
        return " ".join(position.element() for position in self.postorder())

    def preorder(self):
        yield from self._preorder(self.root())

    def _preorder(self, position):
        if position is None:
            return

        yield position
        yield from self._preorder(self.left(position))
        yield from self._preorder(self.right(position))

    def inorder(self):
        yield from self._inorder(self.root())

    def _inorder(self, position):
        if position is None:
            return

        yield from self._inorder(self.left(position))
        yield position
        yield from self._inorder(self.right(position))