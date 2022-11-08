/*Tests both contains() and find()*/
/*Output should be:
true
false
3
null
false
true
true
false
null
8
9
null
1
3
4
6
8
9
11
 * 
 */

public class TestBST2 {


	public static void main(String[] args)
	{
		
		BinarySearchTree<Integer> tree = new BinarySearchTree<Integer>();
		
		tree.insert(6);
		tree.insert(2);
		tree.insert(4);
		tree.insert(3);
		tree.insert(1);
		tree.insert(8);
		tree.insert(11);
	
		
		System.out.println(tree.contains(3));
		System.out.println(tree.contains(5));
		
		System.out.println(tree.find(3));
		System.out.println(tree.find(5));
		
		
		tree.remove(2);
		tree.insert(8);
		tree.insert(9);

		System.out.println(tree.contains(2));
		System.out.println(tree.contains(8));
		System.out.println(tree.contains(9));
		System.out.println(tree.contains(10));

		
		System.out.println(tree.find(2));
		System.out.println(tree.find(8));
		System.out.println(tree.find(9));
		System.out.println(tree.find(10));
		
		
		tree.printTree();
		
		
		
	}

}
