def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    """
    :param n: Number of discs.
    :param from_rod: Start position of all discs.
    :param to_rod: In the end all discs should be on this position.
    :param aux_rod: Empty position at beginning.
    :return: Return step by step of all moves.
    """
    if n == 1:
        print(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        return
    tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)


tower_of_hanoi(3, 'A', 'C', 'B')
