# Assuming the user has entered number only list and no number duplication
inp_list = input("Enter list of integers separated by comma ',' without duplication:\n")

# Converting each separated input into number (also known as casting)
# If there are error here, the operation would not be performed
num_list = [int(item) for item in inp_list.split(",")] # Inline for loop

# Bubble sorting algorithm, it also outputs the number of operation performed, and each operation performed
swap_count = 0

# Outer loop: how many passes through the list
for pass_num in range(len(num_list) - 1):
    for index in range(len(num_list) - 1 - pass_num):
        if num_list[index] > num_list[index + 1]:
            num_list[index], num_list[index + 1] = num_list[index + 1], num_list[index]
            swap_count += 1
            print(f"Step {swap_count}: {num_list}")
