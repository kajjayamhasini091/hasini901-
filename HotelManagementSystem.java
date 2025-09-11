import java.util.ArrayList;
import java.util.Scanner;

class Booking {
    int roomNumber;
    String customerName;
    int nights;
    double pricePerNight;

    public Booking(int roomNumber, String customerName, int nights, double pricePerNight) {
        this.roomNumber = roomNumber;
        this.customerName = customerName;
        this.nights = nights;
        this.pricePerNight = pricePerNight;
    }

    public double getTotalPrice() {
        return nights * pricePerNight;
    }

    @Override
    public String toString() {
        return "Room: " + roomNumber + ", Customer: " + customerName + ", Nights: " + nights + ", Price/Night: " + pricePerNight + ", Total: " + getTotalPrice();
    }
}

public class HotelManagementSystem {

    static ArrayList<Booking> bookings = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;
        do {
            System.out.println("\n====== Hotel Management System ======");
            System.out.println("1. Add Booking");
            System.out.println("2. View All Bookings");
            System.out.println("3. Search Booking by Room Number");
            System.out.println("4. Update Booking");
            System.out.println("5. Delete Booking");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine(); // consume newline

            switch (choice) {
                case 1:
                    addBooking();
                    break;
                case 2:
                    viewBookings();
                    break;
                case 3:
                    searchBooking();
                    break;
                case 4:
                    updateBooking();
                    break;
                case 5:
                    deleteBooking();
                    break;
                case 6:
                    System.out.println("Exiting... Thank you!");
                    break;
                default:
                    System.out.println("Invalid choice! Try again.");
            }
        } while (choice != 6);
    }

    // Add Booking
    public static void addBooking() {
        System.out.print("Enter Room Number: ");
        int room = sc.nextInt();
        sc.nextLine();
        System.out.print("Enter Customer Name: ");
        String name = sc.nextLine();
        System.out.print("Enter Number of Nights: ");
        int nights = sc.nextInt();
        System.out.print("Enter Price per Night: ");
        double price = sc.nextDouble();

        bookings.add(new Booking(room, name, nights, price));
        System.out.println("Booking added successfully!");
    }

    // View all bookings
    public static void viewBookings() {
        if (bookings.isEmpty()) {
            System.out.println("No bookings found!");
            return;
        }
        System.out.println("\nAll Bookings:");
        for (Booking b : bookings) {
            System.out.println(b);
        }
    }

    // Search booking
    public static void searchBooking() {
        System.out.print("Enter Room Number to search: ");
        int room = sc.nextInt();
        for (Booking b : bookings) {
            if (b.roomNumber == room) {
                System.out.println("Booking Found: " + b);
                return;
            }
        }
        System.out.println("Booking not found!");
    }

    // Update booking
    public static void updateBooking() {
        System.out.print("Enter Room Number to update: ");
        int room = sc.nextInt();
        sc.nextLine();

        for (Booking b : bookings) {
            if (b.roomNumber == room) {
                System.out.print("Enter new Customer Name: ");
                b.customerName = sc.nextLine();
                System.out.print("Enter new Number of Nights: ");
                b.nights = sc.nextInt();
                System.out.print("Enter new Price per Night: ");
                b.pricePerNight = sc.nextDouble();
                System.out.println("Booking updated successfully!");
                return;
            }
        }
        System.out.println("Booking not found!");
    }

    // Delete booking
    public static void deleteBooking() {
        System.out.print("Enter Room Number to delete: ");
        int room = sc.nextInt();

        for (int i = 0; i < bookings.size(); i++) {
            if (bookings.get(i).roomNumber == room) {
                bookings.remove(i);
                System.out.println("Booking deleted successfully!");
                return;
            }
        }
        System.out.println("Booking not found!");
    }
}
