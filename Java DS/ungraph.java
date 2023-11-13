import java.util.*;

public class ungraph {
    public static void main(String[] args) {
        Vertex v1 = new Vertex(1);
        Vertex v2 = new Vertex(2);
        Vertex v3 = new Vertex(3);

        Graph graph = new Graph();

        graph.addVertex(v1);
        graph.addVertex(v2);
        graph.addVertex(v3);

        graph.addEdge(v1, v2);

        graph.printGraph();
    }
}

class Vertex {
    int id;
    List<Vertex> neighbours;

    public Vertex(int id){
        this.id=id;
        this.neighbours=new ArrayList<>();
    }

    public void addNeighbor(Vertex neighbour){
        neighbours.add(neighbour);
    }
}


class Graph {
    List<Vertex>vertices;

    public Graph(){
        this.vertices = new ArrayList<>();
    }

    public void addVertex(Vertex vertex){
        vertices.add(vertex);
    }

    public void addEdge(Vertex v1, Vertex v2){
        v1.addNeighbor(v2);
        v2.addNeighbor(v1);  // Undirected Graph
    }

    public void printGraph() {
        for (Vertex vertex : vertices){
            System.out.print("Vertex " + vertex.id + ": ");
            for (Vertex neighbour : vertex.neighbours){
                System.out.print(neighbour.id + " ");
            }
            System.out.println();
        }
    }
}