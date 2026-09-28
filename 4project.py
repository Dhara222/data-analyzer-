data = []

print("Welcome to the Data Analyzer and Transformer Program")


def input_data():
    """Input 1D or 2D dataset from user."""
    global data

    print("\nChoose Array Type:")
    print("1. 1D Array")
    print("2. 2D Array")

    array_type = int(input("Enter your choice: "))

    if array_type == 1:
        value = input("\nEnter data for a 1D array (separated by spaces): ")
        data = list(map(int, value.split()))

        print("\nData:", data)
        print("\nData has been stored successfully!")

    elif array_type == 2:
        rows = int(input("\nEnter number of rows: "))
        columns = int(input("Enter number of columns: "))

        data = []

        for i in range(rows):
            while True:
                value = input(f"Enter values for Row {i + 1}: ")
                row = list(map(int, value.split()))

                if len(row) == columns:
                    data.append(row)
                    break
                else:
                    print(f"Please enter exactly {columns} values.")

        print("\n2D Data:")
        for row in data:
            print(row)

        print("\nData has been stored successfully!")

    else:
        print("\nInvalid array type!")


def statistics(*args):
    """Calculate dataset statistics."""
    minimum = min(args)
    maximum = max(args)
    total = sum(args)
    average = total / len(args)

    return minimum, maximum, total, average


def display_statistics(**kwargs):
    """Display dataset statistics."""

    print("\nDataset Statistics:")
    for key, value in kwargs.items():
        print(key, ":", value)


while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data summary (built-in function)")
    print("3. Calculate factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Value)")
    print("7. Exit Program")

    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        input_data()

    elif choice == 2:
        if data and isinstance(data[0], list):
            user_data = [value for row in data for value in row]
        else:
            user_data = data

        print("\nData summary:")
        print("- Total elements:", len(user_data))
        print("- Minimum value:", min(user_data))
        print("- Maximum value:", max(user_data))
        print("- Sum of all values:", sum(user_data))

        averages = sum(user_data) / len(user_data)
        print("- Average value:", averages)

    elif choice == 3:

        number = int(input("\nEnter a number to calculate its factorial: "))

        def factorial(n):
            if n == 1 or n == 0:
                return 1
            return n * factorial(n - 1)

        result = factorial(number)

        print("\nFactorial of", number, "is:", result)

    elif choice == 4:

        if data and isinstance(data[0], list):
            user_data = [value for row in data for value in row]
        else:
            user_data = data

        user = int(input("\nEnter the Threshold value to filter out data above this value: "))

        m = list(filter(lambda x: x >= user, user_data))

        print("\nFiltered Data (values >=", user, "):", ",".join(map(str, m)))

    elif choice == 5:

        if data and isinstance(data[0], list):
            numbers = [value for row in data for value in row]
        else:
            numbers = data

        while True:
            print("\nChoose sorting option:")
            print("1. Ascending")
            print("2. Descending")

            A = int(input("\nEnter your choice: "))

            if A == 1:
                numbers.sort()
                print("\nSorted Data in Ascending Order: ", numbers)
                break

            elif A == 2:
                numbers.sort(reverse=True)
                print("\nSorted Data in Descending Order: ", numbers)
                break

            else:
                print("Invalid choice. Please enter 1 or 2.")

    elif choice == 6:

        if data and isinstance(data[0], list):
            user_data = [value for row in data for value in row]
        else:
            user_data = data

        minimum, maximum, total, average = statistics(*user_data)

        display_statistics(
            minimum=minimum,
            maximum=maximum,
            total=total,
            average=average)

    elif choice == 7:

        print("Thankyou for using the Data Analyzer and Transformer Program. Goodbye")
        break

    else:
        print("\nInvalid choice!")
