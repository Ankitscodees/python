def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solves the Tower of Hanoi puzzle for n disks.
    Moves disks from the source rod to the target rod using the auxiliary rod.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target)
    
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    
    # Move the n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Test the function
num_disks = 3
print(f"Solving Tower of Hanoi for {num_disks} disks:")
tower_of_hanoi(num_disks, 'A', 'C', 'B')
