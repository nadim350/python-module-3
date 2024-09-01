SIZE_LIMIT = 42

length = float(input("Enter the length of the zander in centimeters: "))

if length >= SIZE_LIMIT:
    print("The zander meets the size limit. You may keep the fish.")
else:
    below_limit = SIZE_LIMIT - length
    print("The zander does not meet the size limit. You must release it back into the lake.")
    print(f"The fish is {below_limit:.2f} centimeters below the size limit.")
