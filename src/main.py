from src.utils import get_all_operations, sort_operations, sort_descending_order, get_formated_operation



def main():
    all_operations = get_all_operations()
    filtered_operations = sort_operations(all_operations)
    sorted_operations = sort_descending_order(filtered_operations)
    five_last_operations = sorted_operations[:5]
    for operation in five_last_operations:
        print(get_formated_operation(operation))
        print()


if __name__ == "__main__":
    main()