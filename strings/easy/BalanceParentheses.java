import java.util.Stack;

public class BalanceParentheses {
	public static void main(String[] args) {
		System.out.println("Hello, world!");
		System.out.println("() is balanced: " + is_balanced("()"));
		System.out.println("()) is balanced: " + is_balanced("())"));
		System.out.println("(())) is balanced: " + is_balanced("(()))"));
		System.out.println(")))) is balanced: " + is_balanced("))))"));
		System.out.println("((((((())))))) is balanced: " + is_balanced("((((((()))))))"));
	}

	private static boolean is_balanced(String expression) {
		Stack<Character> stack = new Stack<>();
		
		for (int i = 0; i < expression.length(); i++) {
			if (expression.charAt(i) == '(') {
				stack.push(expression.charAt(i));
			}
			else if (expression.charAt(i) == ')') {
				if (stack.empty() || stack.pop() != '(') {
					return false;
				}
			}
		}

		if (stack.empty()) {
			return true;
		}

		return false;
	}
}
