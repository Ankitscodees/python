import java.util.HashMap;
import java.util.Scanner;

public class MorseCodeConverter {
    public static void main(String[] args) {
        HashMap<Character, String> morseCode = new HashMap<>();
        morseCode.put('A', ".-"); morseCode.put('B', "-..."); morseCode.put('C', "-.-.");
        morseCode.put('D', "-.."); morseCode.put('E', "."); morseCode.put('F', "..-.");
        morseCode.put('G', "--."); morseCode.put('H', "...."); morseCode.put('I', "..");
        morseCode.put('J', ".---"); morseCode.put('K', "-.-"); morseCode.put('L', ".-..");
        morseCode.put('M', "--"); morseCode.put('N', "-."); morseCode.put('O', "---");
        morseCode.put('P', ".--."); morseCode.put('Q', "--.-"); morseCode.put('R', ".-.");
        morseCode.put('S', "..."); morseCode.put('T', "-"); morseCode.put('U', "..-");
        morseCode.put('V', "...-"); morseCode.put('W', ".--"); morseCode.put('X', "-..-");
        morseCode.put('Y', "-.--"); morseCode.put('Z', "--.."); morseCode.put(' ', "/");

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter text to convert to Morse code: ");
        String input = scanner.nextLine().toUpperCase();
        scanner.close();

        StringBuilder morseOutput = new StringBuilder();
        for (char c : input.toCharArray()) {
            morseOutput.append(morseCode.getOrDefault(c, "?")).append(" ");
        }

        System.out.println("Morse Code: " + morseOutput);
    }
}
