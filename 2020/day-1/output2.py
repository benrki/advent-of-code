SUM = 2020

with open("input.txt") as f:
    nums = list(map(int, f.read().splitlines()))

    for n in nums:
        SUM_NEEDED = SUM-n
        need = set()

        for n1 in nums:
            if n1 in need:
                print(n*n1*(SUM-n1-n))
                quit()
            need.add(SUM_NEEDED-n1)

