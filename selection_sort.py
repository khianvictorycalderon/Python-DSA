# Assuming the user has entered number only list and no number duplication
inp_list = input("Enter list of integers separated by comma ',' without duplication:\n")

# Converting each separated input into number (also known as casting)
# If there are error here, the operation would not be performed
num_list = [int(item) for item in inp_list.split(",")] # Inline for loop

# Single selection sorting algorithm, it also outputs the number of operation performed, and each operation performed
operation = 0
for item in range(len(num_list)):
    order = num_list[item:] # Order of operation
    min_num = min(order) # Get the smallest number of the current operation
    min_num_index = order.index(min_num) # Get the index of the smallest number per operation

    if min_num_index != 0:
        num_list.pop(min_num_index + item) # Remove the current smallest number
        num_list.insert(item, min_num) # Then re-insert it next the smallest number
        operation += 1
        print(f"Operation {operation}: moved {min_num} -> {num_list}")