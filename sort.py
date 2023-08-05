import argparse
from SortingAlgorithm import SorterFactory, VALID_SORT_ALGORITHM, SORT_ALGORITHM_NAME

parser = argparse.ArgumentParser(
        prog="Sort Algorithm",
        description="Run implemented sort algorithm"
)

parser.add_argument(
    "-sa",
    "--sort-algorithm",
    choices=VALID_SORT_ALGORITHM,
    default=VALID_SORT_ALGORITHM[0],
    help=f"choose implemented algorithm to run: {SORT_ALGORITHM_NAME}"
)

parser.add_argument(
    "order",
    choices=["asc", "desc"],
    help="choose sort order"
)

parser.add_argument(
    "array",
    nargs="*",
    type=int,
    help="input array of integer to sort, separate by space")

if __name__ == "__main__":
    args = parser.parse_args()
    sorter = SorterFactory.create_sorter(args.sort_algorithm)
    print(f"Chosen sort algorithm: {SORT_ALGORITHM_NAME[args.sort_algorithm]}")
    print(f"Here is some info about {SORT_ALGORITHM_NAME[args.sort_algorithm]}: ")
    print(sorter.__doc__)
    print(f"Input array: {args.array}")
    res = sorter.sort(args.array, args.order)
    print(f"Sorted array: {res}")