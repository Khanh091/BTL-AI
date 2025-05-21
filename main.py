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
            grid = interface.get_grid()
            heuristic_name = interface.get_heuristic_name()
            heuristic_func = heuristic_map[heuristic_name]
            path, visited_count = best_first_search(grid, grid.start, grid.end, heuristic_func)
            interface.set_visited_count(visited_count)
            if path:
                interface.apply_path(path)
            else:
                interface.show_no_path()

if __name__ == "__main__":
    main()