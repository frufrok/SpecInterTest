package ToyMachine;

import java.util.Objects;

public class Toy {
    private final int id;
    private final int weight;
    private final String name;
    public Toy(int id, int weight, String name) {
        this.id = id;
        this.weight = weight;
        this.name = name;
    }
    public int getId() {
        return this.id;
    }

    public int getWeight() {
        return this.weight;
    }

    public String getName() {
        return this.name;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Toy toy = (Toy) o;
        return id == toy.id && weight == toy.weight && Objects.equals(name, toy.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, weight, name);
    }

    @Override
    public String toString() {
        return String.format("%d %d %s", this.id, this.weight, this.name);
    }
}
