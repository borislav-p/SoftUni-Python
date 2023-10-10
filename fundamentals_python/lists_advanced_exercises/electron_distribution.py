number_electrons = int(input())
shells = []
electrons_used = 0
shell_number = 0
while number_electrons > electrons_used:
    shell_number += 1
    current_shell = 2 * shell_number ** 2

    if number_electrons - electrons_used < current_shell:
        current_shell = number_electrons - electrons_used
    electrons_used += current_shell

    shells.append(current_shell)
print(shells)
