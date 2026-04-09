# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "1 + 1"
# Output: 2
# Example 2:

# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        result = 0  # For the on-going result
        sign = 1    # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():
                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch in ['+', '-']:
                # Evaluate the expression to the left of the operator sign
                result += sign * operand
                # Save the recently encountered operator sign
                sign = 1 if ch == '+' else -1
                # Reset operand
                operand = 0

            elif ch == '(':
                # Push the result and sign on to the stack, for later
                stack.append(result)
                stack.append(sign)
                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                result = 0

            elif ch == ')':
                # Evaluate the expression to the left of ')'
                result += sign * operand
                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                result *= stack.pop()    # stack pop 1, the sign before the parenthesis
                # Then add to the next top of stack
                # which is the result calculated before this parenthesis
                result += stack.pop()    # stack pop 2, the result calculated before this parenthesis
                # Reset operand
                operand = 0

        return result + (sign * operand)