import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

// ===================== CUSTOM EXCEPTIONS =====================

class InvalidRomanNumeralException extends Exception {
    public InvalidRomanNumeralException(String message) {
        super(message);
    }
}

class InvalidNumberRangeException extends Exception {
    public InvalidNumberRangeException(String message) {
        super(message);
    }
}

// ===================== ROMAN CONVERTER =====================

class RomanConverter {

    private static final Map<Character, Integer> romanMap = new HashMap<>();

    static {
        romanMap.put('I', 1);
        romanMap.put('V', 5);
        romanMap.put('X', 10);
        romanMap.put('L', 50);
        romanMap.put('C', 100);
        romanMap.put('D', 500);
        romanMap.put('M', 1000);
    }

    // Roman → Arabic
    public static int romanToArabic(String roman) throws InvalidRomanNumeralException {
        roman = roman.toUpperCase();
        int total = 0, prev = 0;

        for (int i = roman.length() - 1; i >= 0; i--) {
            char c = roman.charAt(i);

            if (!romanMap.containsKey(c)) {
                throw new InvalidRomanNumeralException("ERROR: Invalid Roman character → " + c);
            }

            int value = romanMap.get(c);

            if (value < prev) total -= value;
            else total += value;

            prev = value;
        }

        if (total < 1 || total > 3999) {
            throw new InvalidRomanNumeralException("ERROR: Roman numeral out of range (1–3999)");
        }

        assert total >= 1 && total <= 3999 : "Assertion failed: Roman number must be 1–3999";

        return total;
    }

    // Arabic → Roman
    public static String arabicToRoman(int number) throws InvalidNumberRangeException {
        if (number < 1 || number > 3999)
            throw new InvalidNumberRangeException("ERROR: Number must be between 1 and 3999");

        assert number >= 1 && number <= 3999 : "Assertion failed: Arabic number must be 1–3999";

        int[] arabic = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < arabic.length; i++) {
            while (number >= arabic[i]) {
                result.append(roman[i]);
                number -= arabic[i];
            }
        }
        return result.toString();
    }
}


// ===================== NUMBER TO WORDS CONVERTER =====================

class NumberToWords {

    private static final String[] ones = {
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
            "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    };

    private static final String[] tens = {
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    };

    public static String convert(int number) throws InvalidNumberRangeException {

        if (number < 1 || number > 3999)
            throw new InvalidNumberRangeException("ERROR: Number must be between 1 and 3999");

        assert number >= 1 && number <= 3999 : "Assertion failed: Number must be within 1–3999";

        if (number < 20)
            return ones[number];

        else if (number < 100)
            return tens[number / 10] + ((number % 10 > 0) ? " " + ones[number % 10] : "");

        else if (number < 1000)
            return ones[number / 100] + " Hundred" +
                    ((number % 100 > 0) ? " " + convert(number % 100) : "");

        else
            return ones[number / 1000] + " Thousand" +
                    ((number % 1000 > 0) ? " " + convert(number % 1000) : "");
    }
}



// ===================== MAIN MENU APPLICATION =====================

public class ConverterApp {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n===== MASTER CONVERTER PROGRAM =====");
            System.out.println("1. Roman → Arabic");
            System.out.println("2. Arabic → Roman");
            System.out.println("3. Arabic → Words");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            choice = Integer.parseInt(sc.nextLine());

            try {

                switch (choice) {

                    case 1:
                        System.out.print("Enter Roman Numeral: ");
                        String roman = sc.nextLine();
                        int value = RomanConverter.romanToArabic(roman);
                        System.out.println("Arabic Value: " + value);
                        break;

                    case 2:
                        System.out.print("Enter Arabic Number (1–3999): ");
                        int num1 = Integer.parseInt(sc.nextLine());
                        String romanVal = RomanConverter.arabicToRoman(num1);
                        System.out.println("Roman Numeral: " + romanVal);
                        break;

                    case 3:
                        System.out.print("Enter Arabic Number (1–3999): ");
                        int num2 = Integer.parseInt(sc.nextLine());
                        String words = NumberToWords.convert(num2);
                        System.out.println("In Words: " + words);
                        break;

                    case 4:
                        System.out.println("Exiting program...");
                        break;

                    default:
                        System.out.println("Invalid choice. Try again.");
                        break;
                }

            } catch (InvalidNumberRangeException | InvalidRomanNumeralException e) {
                System.out.println(e.getMessage());

            } catch (NumberFormatException e) {
                System.out.println("ERROR: Input must be numeric when required.");

            } finally {
                System.out.println("Operation Completed.\n");
            }

        } while (choice != 4);

        sc.close();
    }
}
