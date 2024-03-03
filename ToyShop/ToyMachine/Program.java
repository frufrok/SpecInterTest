package ToyMachine;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Program {
    public static void main(String[] args) {
        ToyMachine machine;
        if (args.length > 3) {
            machine = new ToyMachine(List.of(args));
        }
        else {
            ArrayList<String> defaultToys = new ArrayList<>();
            defaultToys.add("1 2 конструктор");
            defaultToys.add("2 2 робот");
            //defaultToys.add("3 2 кукла");
            machine = new ToyMachine(defaultToys);
            for (String arg : args) {
                machine.putToyByString(arg);
            }
        }
        // Куклу добавим методом добавления игрушек.
        machine.putToyByString("3 2 кукла");

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("winnings.txt"))) {
            for (int i = 0; i < 10; i++) {
                writer.append(String.format("%d\n", machine.getToy().getId()));
            }
            System.out.printf("File %s is written.\n", "winnings.txt");
        } catch (IOException e) {
            System.out.printf("Error writing file: %s\n", e.getMessage());
        }
        catch (NullPointerException e) {
            System.out.println("Error getting toys. Check ToyMachine is ready to game.");
            List<String> warnings = machine.getWarnings();
            if (!warnings.isEmpty()) {
                System.out.println("List of warnings:");
                for (int i = 0; i < warnings.size(); i++) {
                    System.out.printf("\t%d.) %s\n", i + 1, warnings.get(i));
                }
            }
        }
    }
}
