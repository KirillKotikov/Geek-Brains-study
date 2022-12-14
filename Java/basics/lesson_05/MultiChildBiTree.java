package GB_java_lessons.lesson_05;

import java.util.ArrayList;
import java.util.List;

public class MultiChildBiTree {
    public static void main(String[] args) {
        MultiNode root = new MultiNode(1);

        MultiNode n2 = new MultiNode(2);
        MultiNode n3 = new MultiNode(3);

        MultiNode n4 = new MultiNode(4);
        MultiNode n5 = new MultiNode(5);
        MultiNode n6 = new MultiNode(6);

        MultiNode n7 = new MultiNode(7);
        MultiNode n8 = new MultiNode(8);
        MultiNode n9 = new MultiNode(9);
        MultiNode n11 = new MultiNode(11);
        MultiNode n20 = new MultiNode(20);

        root.children.add(n2);
        root.children.add(n3);

        n2.children.add(n4);
        n3.children.add(n5);
        n3.children.add(n6);

        n4.children.add(n7);
        n4.children.add(n8);
        n4.children.add(n9);

        n6.children.add(n11);
        n6.children.add(n20);

        System.out.println("\nВывод с отступами:");
        preOrder(root, "");
        System.out.println("\n");

        System.out.println("Вывод со скобками:");
        preOrderWithBrackets(root);
    }

    static void preOrder(MultiNode tree, String space) {
        if (tree != null) {
            System.out.println(space + tree.value);
            if (!tree.children.isEmpty()) {
                for (MultiNode children : tree.children) {
                    preOrder(children, space + "  ");
                }
            } else
                System.out.println(space + "  " + "nil");
        }
    }

    static void preOrderWithBrackets(MultiNode tree) {
        if (tree != null) {
            System.out.print("(" + tree.value + " ");
            if (!tree.children.isEmpty()) {
                for (int i = 0; i < tree.children.size(); i++) {
                    preOrderWithBrackets(tree.children.get(i));
                    if (i != tree.children.size() - 1)
                        System.out.print(", ");
                }
            } else
                System.out.print(", nil");
            System.out.print(")");
        }
    }
}

class MultiNode {
    int value;
    List<MultiNode> children = new ArrayList<>();

    public MultiNode(int value) {
        this.value = value;
    }
}