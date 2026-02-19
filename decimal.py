all_inputs = []

while True:
    user_input = input("Enter a decimal number or Press B or E to exit: ").strip()

    if user_input.lower() == 'b':
        print("Bye bye")
        print("sheesh")
        break
    if user_input.lower() == 'e':
        print("Exit the program")
        print("sheesh")
        break

    if not user_input.isdigit():
        print("Invalid input. Please enter a valid decimal number.")
        continue

    decimal_value = int(user_input)
    binary = bin(decimal_value)[2:]  

    
    state = 'q0'
    for bit in binary:
        bit = int(bit)
        if state == 'q0':
            state = 'q0' if bit == 0 else 'q1'
        elif state == 'q1':
            state = 'q2' if bit == 0 else 'q0'
        elif state == 'q2':
            state = 'q1' if bit == 0 else 'q2'

    remainder = decimal_value % 3
    result = "Accepted" if state == 'q0' else "Rejected"

    all_inputs.append({
        'binary': binary,
        'decimal': decimal_value,
        'state': state,
        'result': result
    })

    print()
    print(f"Decimal: {decimal_value}")
    print(f"Binary: {binary}")
    print(f"Remainder mod 3: {remainder}")
    print(f"Final state: {state}")
    print(result)
    print()

# Summary Table
print("Decimal\t\tBinary\t\t\tState\t\t\t\tResult")
print("---------------------------------------------------------------")
for entry in all_inputs:
    print(f"{entry['decimal']}\t\t{entry['binary']}\t\t{entry['state']}\t\t{entry['result']}")


print("Program ended.")
