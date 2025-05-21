from interface import Interface
from best_first_search import best_first_search, heuristic_manhattan, heuristic_euclidean, heuristic_chebyshev

def main():
    heuristic_map = {
        "Manhattan": heuristic_manhattan,
        "Euclidean": heuristic_euclidean,
        "Chebyshev": heuristic_chebyshev
    }
    interface = Interface()
    for action in interface.run():
        if action == "run_algorithm":
            print("Running algorithm...")  # Debug
            grid = interface.get_grid()
            print(f"Start: {grid.start}, End: {grid.end}")  # Debug
            heuristic_name = interface.get_heuristic_name()
            heuristic_func = heuristic_map[heuristic_name]
            print(f"Using heuristic: {heuristic_name}")  # Debug
            path, visited_count = best_first_search(grid, grid.start, grid.end, heuristic_func)
            print(f"Path found: {path}, Visited: {visited_count}")  # Debug
            interface.set_visited_count(visited_count)
            if path:
                interface.apply_path(path)
            else:
                interface.show_no_path()

if __name__ == "__main__":
    main()