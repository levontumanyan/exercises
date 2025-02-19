import java.util.Stack;

public class BalancedParentheses {
	public static void main(String[] args) {
		System.out.println("The string (())) is balanced: " + check_balanced("(()))"));
		System.out.println("The string (()) is balanced: " + check_balanced("(())"));
		System.out.println("The string (((( is balanced: " + check_balanced("(((("));
		System.out.println("The string ))))) is balanced: " + check_balanced(")))))"));
		System.out.println("The string ())(() is balanced: " + check_balanced("())(()"));
		System.out.println("The string (()))( is balanced: " + check_balanced("(()))("));
	}

	public static boolean check_balanced(String expression) {
		Stack<Character> stack = new Stack<>();

		for (int i = 0; i < expression.length(); i++) {
			if (expression.charAt(i) == '(') {
				stack.push(expression.charAt(i));
			}
			else if (expression.charAt(i) == ')') {
				if (stack.isEmpty() || stack.pop() == ')') {
					return false;
				}
			}
		}

		return stack.isEmpty();
	}
}
