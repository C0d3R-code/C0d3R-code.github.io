import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// --- 1. INTERFACE ---
interface Billable {
    double calculateFine(int daysOverdue);
}

// --- 2. ABSTRACTION ---
abstract class LibraryItem {
    private String title;
    private String id;
    private boolean isCheckedOut;

    public LibraryItem(String title, String id) {
        this.title = title;
        this.id = id;
        this.isCheckedOut = false;
    }

    public void checkOut() {
        if (isCheckedOut) {
            System.out.println("Error: Item is already currently rented out.");
        } else {
            this.isCheckedOut = true;
            System.out.println("Success: You have rented '" + title + "'.");
        }
    }

    public void returnItem() {
        this.isCheckedOut = false;
    }

    public String getTitle() { return title; }
    public String getId() { return id; }
    public boolean isCheckedOut() { return isCheckedOut; }

    public abstract void displayDetails();
}

// --- 3. INHERITANCE & POLYMORPHISM (Book) ---
class Book extends LibraryItem implements Billable {
    private String author;

    public Book(String title, String id, String author) {
        super(title, id);
        this.author = author;
    }

    @Override
    public void displayDetails() {
        String status = isCheckedOut() ? "[Rented]" : "[Available]";
        System.out.printf("%-12s %-10s %-20s %-20s%n", status, getId(), getTitle(), "Author: " + author);
    }

    @Override
    public double calculateFine(int daysOverdue) {
        return daysOverdue * 0.50; // $0.50 per day
    }
}

// --- 4. INHERITANCE & POLYMORPHISM (DVD) ---
class DVD extends LibraryItem implements Billable {
    private String director;

    public DVD(String title, String id, String director) {
        super(title, id);
        this.director = director;
    }

    @Override
    public void displayDetails() {
        String status = isCheckedOut() ? "[Rented]" : "[Available]";
        System.out.printf("%-12s %-10s %-20s %-20s%n", status, getId(), getTitle(), "Director: " + director);
    }

    @Override
    public double calculateFine(int daysOverdue) {
        return daysOverdue * 2.00;
    }
}

// --- 5. ENCAPSULATION (Manager) ---
class Library {
    private List<LibraryItem> items;

    public Library() {
        items = new ArrayList<>();
    }

    public void addItem(LibraryItem item) {
        items.add(item);
        System.out.println("Item added to system successfully.");
    }

    public LibraryItem findItem(String id) {
        for (LibraryItem item : items) {
            if (item.getId().equalsIgnoreCase(id)) {
                return item;
            }
        }
        return null;
    }

    public void viewInventory() {
        System.out.println("\n--- CURRENT INVENTORY ---");
        System.out.printf("%-12s %-10s %-20s %-20s%n", "STATUS", "ID", "TITLE", "DETAILS");
        System.out.println("---------------------------------------------------------------");
        if (items.isEmpty()) {
            System.out.println("Library is empty.");
        } else {
            for (LibraryItem item : items) {
                item.displayDetails();
            }
        }
        System.out.println("---------------------------------------------------------------");
    }
}

// --- 6. MAIN INTERACTIVE CLASS ---
public class LibrarySystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Library myLibrary = new Library();
        boolean running = true;

        myLibrary.addItem(new Book("The Hobbit", "B001", "J.R.R. Tolkien"));
        myLibrary.addItem(new DVD("Inception", "D001", "Christopher Nolan"));

        while (running) {
            System.out.println("\n=== LIBRARY MANAGEMENT SYSTEM ===");
            System.out.println("1. Add New Book");
            System.out.println("2. Add New DVD");
            System.out.println("3. Rent an Item");
            System.out.println("4. Return an Item (Process Fines)");
            System.out.println("5. View Inventory");
            System.out.println("6. Exit");
            System.out.print("Select an option: ");

            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    System.out.print("Enter Book Title: ");
                    String bTitle = scanner.nextLine();
                    System.out.print("Enter Unique ID (e.g., B002): ");
                    String bId = scanner.nextLine();
                    System.out.print("Enter Author: ");
                    String author = scanner.nextLine();
                    myLibrary.addItem(new Book(bTitle, bId, author));
                    break;

                case "2":
                    System.out.print("Enter DVD Title: ");
                    String dTitle = scanner.nextLine();
                    System.out.print("Enter Unique ID (e.g., D002): ");
                    String dId = scanner.nextLine();
                    System.out.print("Enter Director: ");
                    String director = scanner.nextLine();
                    myLibrary.addItem(new DVD(dTitle, dId, director));
                    break;

                case "3":
                    myLibrary.viewInventory();
                    System.out.print("Enter ID of item to rent: ");
                    String rentId = scanner.nextLine();
                    LibraryItem rentItem = myLibrary.findItem(rentId);

                    if (rentItem != null) {
                        rentItem.checkOut();
                    } else {
                        System.out.println("Error: Item ID not found.");
                    }
                    break;

                case "4":
                    System.out.print("Enter ID of item to return: ");
                    String returnId = scanner.nextLine();
                    LibraryItem returnItem = myLibrary.findItem(returnId);

                    if (returnItem != null) {
                        if (returnItem.isCheckedOut()) {
                            System.out.print("How many days is the item overdue? (0 if on time): ");
                            int days = 0;
                            try {
                                days = Integer.parseInt(scanner.nextLine());
                            } catch (NumberFormatException e) {
                                System.out.println("Invalid number, assuming 0 days.");
                            }

                            returnItem.returnItem();
                            System.out.println("Success: " + returnItem.getTitle() + " has been returned.");

                            if (returnItem instanceof Billable && days > 0) {
                                double fine = ((Billable) returnItem).calculateFine(days);
                                System.out.println("$$ ALERT: Late Fee Generated: $" + String.format("%.2f", fine));
                            } else {
                                System.out.println("Item returned on time. No fines.");
                            }
                        } else {
                            System.out.println("This item is already in the library (not rented out).");
                        }
                    } else {
                        System.out.println("Error: Item ID not found.");
                    }
                    break;

                case "5":
                    myLibrary.viewInventory();
                    break;

                case "6":
                    running = false;
                    System.out.println("Exiting system. Goodbye!");
                    break;

                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }
        scanner.close();
    }
}