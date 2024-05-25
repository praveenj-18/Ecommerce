arr = []
while True:
    try:
        u_input = input()
        if u_input.lower() == 'done':
            break
        num = int(u_input)
        arr.append(num)
    except KeyboardInterrupt:
        break

sum_arr = sum(arr)
n = len(arr)
total_sum = ((n + 1) * (n + 2))//2  # Correcting the formula here
missing_num = total_sum - sum_arr
print("Missing number:", missing_num)
