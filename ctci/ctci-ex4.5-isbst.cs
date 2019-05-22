using System;

public class MainClass {
	public class Node {
		public int Data { get; set; }
		public Node Right { get; set; }
		public Node Left { get; set; }

		public static bool operator<(Node left, Node right) {
			if(left == null || right == null)
				return false;
			return left.Data < right.Data;
		}

		public static bool operator>(Node left, Node right) {
			if(left == null || right == null)
				return false;
			return left.Data > right.Data;
		}
	}

	public static void Main() {
		Console.WriteLine(IsBST(ReadTree1()) ? "Yes" : "No");
		Console.WriteLine(IsBST(ReadTree2()) ? "Yes" : "No");
		Console.WriteLine(IsBST(ReadTree3()) ? "Yes" : "No");
	}

	public static Node ReadTree1() {
		return new Node{Data= 5,
				Left= new Node{Data= 3, 
					Left= new Node{Data= 7},
					Right= new Node{Data= 6}
					},
				Right= new Node{Data= 7,
					Left= new Node{Data= 6}
					}
				};
	}

	public static Node ReadTree2() {
		return new Node{Data= 10,
				Left= new Node{Data= 5, 
					Left= new Node{Data= 1},
					Right= new Node{Data= 8,
						Right= new Node{Data= 9
					}
					},
				},
				Right= new Node{Data= 15,
					Left= new Node{Data= 12},
					Right= new Node{Data= 16}
					}
			};
	}

	public static Node ReadTree3() {
		return new Node{Data= 10,
				Left= new Node{Data= 10},
				Right= new Node{Data= 15,
					Left= new Node{Data= 13}
					}
				};
	}



	public static bool IsBST(Node n) {
		if(IsInLimits(n, null, null)) 
			return true;
		return false;
	}
	
	public static bool IsInLimits(Node n, Node min, Node max) {
		Console.WriteLine("IsInLimits(" + n.Data + ", " + (min != null ? min.Data.ToString() : "") + ", " +
				(max != null ? max.Data.ToString() : "") + ")");
		
		if(min != null && !(min < n))
			return false;
		if(max != null && !(n < max))
			return false;
		if(n.Left != null && !IsInLimits(n.Left, min, n))
			return false;
		if(n.Right != null && !IsInLimits(n.Right, n, max))
			return false;
		return true;
	}
}
