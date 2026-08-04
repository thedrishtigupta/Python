
def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def record():
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

    record()  # Initial arrangement

    def solve(num_disks, source, auxiliary, target):
        if num_disks == 1:
            disk = rods[source].pop()
            rods[target].append(disk)
            record()
            return

        solve(num_disks - 1, source, target, auxiliary)

        disk = rods[source].pop()
        rods[target].append(disk)
        record()

        solve(num_disks - 1, auxiliary, source, target)

    solve(n, 0, 1, 2)

    return "\n".join(moves)