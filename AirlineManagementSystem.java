import java.util.ArrayList;
import java.util.Scanner;

class Flight {
    int flightNumber;
    String destination;
    String departureTime;
    double price;

    public Flight(int flightNumber, String destination, String departureTime, double price) {
        this.flightNumber = flightNumber;
        this.destination = destination;
        this.departureTime = departureTime;
        this.price = price;
    }

    @Override
    public String toString() {
        return "Flight No: " + flightNumber + ", Destination: " + destination +
                ", Departure: " + departureTime + ", Price: $" + price;
    }
}

class Booking {
    int bookingId;
    String customerName;
    Flight flight;

    public Booking(int bookingId, String customerName, Flight flight) {
        this.bookingId = bookingId;
        this.customerName = customerName;
        this.flight = flight;
    }

    @Override
    public String toString() {
        return "Booking ID: " + bookingId + ", Customer: " + customerName + ", Flight: [" + flight + "]";
    }
}

public class AirlineManagementSystem {
    static ArrayList<Flight> flights = new ArrayList<>();
    static ArrayList<Booking> bookings = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);
    static int bookingCounter = 1;

    public static void main(String[] args) {
        initializeFlights();
        int choice;
        do {
            System.out.println("\n===== Airline Management System =====");
            System.out.println("1. View Available Flights");
            System.out.println("2. Book a Flight");
            System.out.println("3. View All Bookings");
            System.out.println("4. Cancel Booking");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine(); // consume newline

            switch (choice) {
                case 1:
                    viewFlights();
                    break;
                case 2:
                    bookFlight();
                    break;
                case 3:
                    viewBookings();
                    break;
                case 4:
                    cancelBooking();
                    break;
                case 5:
                    System.out.println("Exiting... Thank you!");
                    break;
                default:
                    System.out.println("Invalid choice! Try again.");
            }
        } while (choice != 5);
    }

    // Initialize some flights
    public static void initializeFlights() {
        flights.add(new Flight(101, "New York", "09:00 AM", 500.0));
        flights.add(new Flight(102, "London", "02:00 PM", 700.0));
        flights.add(new Flight(103, "Paris", "06:00 PM", 650.0));
        flights.add(new Flight(104, "Tokyo", "11:00 AM", 1200.0));
        flights.add(new Flight(105, "Sydney", "03:00 PM", 1500.0));
    }

    // View all flights
    public static void viewFlights() {
        System.out.println("\nAvailable Flights:");
        for (Flight f : flights) {
            System.out.println(f);
        }
    }

    // Book a flight
    public static void bookFlight() {
        viewFlights();
        System.out.print("Enter Flight Number to book: ");
        int fid = sc.nextInt();
        sc.nextLine();

        Flight selectedFlight = null;
        for (Flight f : flights) {
            if (f.flightNumber == fid) {
                selectedFlight = f;
                break;
            }
        }

        if (selectedFlight == null) {
            System.out.println("Flight not found!");
            return;
        }

        System.out.print("Enter your name: ");
        String name = sc.nextLine();
        bookings.add(new Booking(bookingCounter++, name, selectedFlight));
        System.out.println("Booking successful! Your Booking ID is " + (bookingCounter - 1));
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

    // Cancel booking
    public static void cancelBooking() {
        System.out.print("Enter Booking ID to cancel: ");
        int bid = sc.nextInt();
        for (int i = 0; i < bookings.size(); i++) {
            if (bookings.get(i).bookingId == bid) {
                bookings.remove(i);
                System.out.println("Booking canceled successfully!");
                return;
            }
        }
        System.out.println("Booking not found!");
    }
}
