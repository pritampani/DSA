import java.util.Scanner;

class Box {
    private double width;
    private double height;
    private double depth;

    public Box(double width, double height, double depth) {
        this.width = width;
        this.height = height;
        this.depth = depth;
    }

    public double getVolume() {
        return width * height * depth;
    }
}

class BoxWeight extends Box {
    private double weight;

    public BoxWeight(double width, double height, double depth, double weight) {
        super(width, height, depth);
        this.weight = weight;
    }

    public double calculateShippingCost(double distance, double volumeCostPerKM) {
        return distance * (getVolume() * volumeCostPerKM) + weight; // Assuming weight is part of shipping cost
    }
}

public class main1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter dimensions of the box (width height depth):");
        double width = scanner.nextDouble();
        double height = scanner.nextDouble();
        double depth = scanner.nextDouble();

        System.out.println("Enter weight of the box:");
        double weight = scanner.nextDouble();

        System.out.println("Enter the distance in kilometers:");
        double distance = scanner.nextDouble();

        System.out.println("Enter the volume cost per kilometer:");
        double volumeCostPerKM = scanner.nextDouble();

        BoxWeight box = new BoxWeight(width, height, depth, weight);
        double shippingCost = box.calculateShippingCost(distance, volumeCostPerKM);

        System.out.println("Volume of the box: " + box.getVolume() + " cubic units");
        System.out.println("Shipping cost for the box: " + shippingCost + " currency units");
    }
}