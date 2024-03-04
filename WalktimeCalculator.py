from collections import defaultdict
import heapq as heap
from itertools import permutations


class Graph:
    def __init__(self, filename):
        self.no_vertices = 0
        self.edges = []
        self.building_indices = {}  # Mapping from building names to indices
        self.parse_file(filename)

    def parse_file(self, filename):
        with open(filename, "r") as file:
            # Read the first line for the number of vertices
            self.no_vertices = int(file.readline())

            # Read remaining lines for edges
            for line in file:
                building1, building2, weight = line.strip().split(",")
                self.add_edge(building1, building2, float(weight))

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])
        if u not in self.building_indices:
            self.building_indices[u] = len(self.building_indices)
        if v not in self.building_indices:
            self.building_indices[v] = len(self.building_indices)

    def dijkstra(self, start, end):
        graph = defaultdict(list)

        for u, v, w in self.edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        parent_map = {building: None for building in graph}
        distance = {building: float("inf") for building in graph}
        distance[start] = 0

        pq = [(0, start)]

        # Iterate through all neighbors to find shortest distance
        while pq:
            current_distance, current_node = heap.heappop(pq)

            # Skip if visited
            if current_node in visited:
                continue

            # Add current node to visited set
            visited.add(current_node)

            # Update new time with weight
            for neighbor, weight in graph[current_node]:
                new_distance = distance[current_node] + weight

                # Updates the map with the most efficient route
                if new_distance < distance[neighbor]:
                    parent_map[neighbor] = current_node
                    distance[neighbor] = new_distance
                    heap.heappush(pq, (new_distance, neighbor))

        return parent_map, distance


def main():
    filename = "buildings.txt"  # Replace with your actual file name

    # Create the Graph object
    UT_Campus = Graph(filename)

    print()
    print("Welcome to your Walktime Calculator!")
    while True:
        while True:
            try:
                num_locations = int(input("How many locations plus the starting location would you like to stop by today (Enter 0 if done): "))
                print()
                if num_locations >= 0:
                    break
                else:
                    print("Please enter number of buildings you wish to visit")
                    print()
            except ValueError:
                print("Please enter number of buildings you wish to visit")
                print()
        if num_locations == 0:
            print()
            print("Have a good day!")
            return

        total_distance = float("inf")

        print("Buildings to choose from:")
        sorted_building_list = sorted(UT_Campus.building_indices.keys())
        sorted_buildings_str = ', '.join(sorted_building_list)
        print(sorted_buildings_str)
        print()

        # Input the starting building
        start_building = input("Enter the starting building: ")
        while start_building not in UT_Campus.building_indices:
            print("Invalid building name. Please enter valid building name.")
            print()
            start_building = input("Enter the starting building: ")
            print()

        # Input the list of buildings to visit
        not_visited = []
        for _ in range(num_locations):
            building = input("Enter a building to visit: ")
            while building not in UT_Campus.building_indices:
                print("Invalid building name. Please enter valid building name.")
                print()
                building = input("Enter a building to visit: ")
                print()
            not_visited.append(building)
            order = []
            order.append(building)

        else:
            selected_buildings = []
            for _ in range(num_locations):
                building = input("Enter a building to visit: ")
                while building not in UT_Campus.building_indices:
                    print("Invalid building name. Please enter valid building name.")
                    print()
                    building = input("Enter a building to visit: ")
                    print()
                selected_buildings.append(building)

            # Calculate the optimal path for the selected buildings directly
            total_distance = 0
            path = []
            for i in range(len(selected_buildings) - 1):
                start_building = selected_buildings[i]
                end_building = selected_buildings[i + 1]
                _, distance = UT_Campus.dijkstra(start_building, end_building)
                total_distance += distance[end_building]
                path.append(start_building)
                path.append(end_building)

            # Add the last building to the path
            path.append(selected_buildings[-1])

            print(f"Optimal path: {path}")
            print(f"Total travel time: {total_distance} min")
            print()


if __name__ == "__main__":
    main()
