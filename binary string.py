all_inputs = []

while True:
    binary = input("Enter a binary string: ").strip()
    binary = binary.replace(" ", "").strip()

    if binary.lower() == 'b':
        print()
        break
    if binary.lower() == 'e':
        print()
        break

    if not binary:
        print("Please enter 1 and 0.")
        continue

    if not all(bit in {'0', '1'} for bit in binary):
        print("Invalid input. Please enter only 0 and 1.")
        continue

    state = 'q0'
    for bit in binary:
        bit = int(bit)
        if state == 'q0':
            state = 'q0' if bit == 0 else 'q1'
        elif state == 'q1':
            state = 'q2' if bit == 0 else 'q0'
        elif state == 'q2':
            state = 'q1' if bit == 0 else 'q2'

    decimal = int(binary, 2)
    remainder = decimal % 3
    result = "Accepted" if state == 'q0' else "Rejected"

    all_inputs.append({
    'binary': binary,
    'decimal': decimal,
    'state': state,
    'result': result
})
    print()
    print(f"Binary: {binary}")
    print(f"Decimal: {decimal}")
    print(f"Remainder mod 3: {remainder}")
    print(f"Final state: {state}")
    print(result)
    print()

print("Binary \t\t\t\t\t Decimal \t State \t\t Result")
print("----------------------------------------------------------------------------------------")
for entry in all_inputs:
    print(f"{entry['binary']} \t\t\t\t\t {entry['decimal']} \t\t {entry['state']}\t\t{entry['result']}")

print("Bye bye")
print("sheesh")
print("napaka angas")
