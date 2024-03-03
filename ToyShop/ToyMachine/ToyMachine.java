package ToyMachine;

import java.util.*;

public class ToyMachine {

    private final HashMap<Integer, Toy> availableToys = new HashMap<Integer, Toy>();
    private final List<String> warnings = new ArrayList<>();
    public ToyMachine(List<String> toys) {
        if (toys != null) {
            for (String that : toys) {
                try {
                    String[] params = that.split(" ");
                    int id = Integer.parseInt(params[0]);
                    if (availableToys.containsKey(id)) {
                        throw new RuntimeException(String.format("Toy with ID = %d already exists.", id));
                    }
                    this.availableToys.put(id,
                            new Toy(id, Integer.parseInt(params[1]), params[2]));
                }
                catch (RuntimeException e) {
                    this.warnings.add(String.format("Error parsing \"%s\": %s.", that, e.getMessage()));
                }
            }
        }
        else {
            this.warnings.add("Machine was constructed with null list.");
        }
    }

    public List<Toy> getAvailableToys() {
        return new ArrayList<>(this.availableToys.values());
    }

    public boolean isReadyToGet() {
        return this.availableToys.size() > 2;
    }

    public Toy getToy() {
        if (isReadyToGet()) {
            HashMap<Integer, Toy> choiceMap = new HashMap<>();
            int n = 0;
            for (Toy toy : this.getAvailableToys()) {
                for (int i = 0; i < toy.getWeight(); i++) {
                    choiceMap.put(n, toy);
                    n++;
                }
            }
            Random random = new Random();
            return choiceMap.get(random.nextInt(0, n));
        }
        else {
            return null;
        }
    }

    public boolean putToy (Toy toy) {
        try {
            if (availableToys.containsKey(toy.getId())) {
                throw new RuntimeException(String.format("Toy with ID = %d already exists.", toy.getId()));
            }
            this.availableToys.put(toy.getId(), toy);
            return true;
        }
        catch (RuntimeException e) {
            this.warnings.add(String.format("Error putting toy \"%s\": %s.", toy.toString(), e.getMessage()));
            return false;
        }
    }

    public boolean putToyByString(String string) {
        try {
            String[] params = string.split(" ");
            int id = Integer.parseInt(params[0]);
            if (availableToys.containsKey(id)) {
                throw new RuntimeException(String.format("Toy with ID = %d already exists.", id));
            }
            this.availableToys.put(Integer.parseInt(params[0]),
                    new Toy(Integer.parseInt(params[0]), Integer.parseInt(params[1]), params[2]));
            return true;
        }
        catch (RuntimeException e) {
            this.warnings.add(String.format("Error parsing \"%s\": %s.", string, e.getMessage()));
            return false;
        }
    }

    public List<String> getWarnings() {
        return new ArrayList<>(this.warnings);
    }
}
