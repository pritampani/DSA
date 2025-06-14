class A {
    int a = 3, b = 5;
    int c = a + b;

    void show() {
        System.out.println(c);
    }
}

class Inheritance2 extends A {
    int a = 5, b = 3;
    int c = a - b;

    void dis() {
        System.out.println(c);
    }
}

public class Inheritance1 {
    public static void main(String[] args) {
        Inheritance2 obj = new Inheritance2();
        obj.dis();
        obj.show();
    }
}
