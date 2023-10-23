benchmark = "Benchmark"


def format_table(benchmarks, algos, results):
    first_column_wight = max(map(len, benchmarks + [benchmark]))
    sum_len = first_column_wight + len(algos) + 2
    head = f"| {benchmark: <{first_column_wight}} |"
    for i in algos:
        head += f" {i} |"
        sum_len += len(i) + 2
    print(head)
    print("|", "-" * sum_len, "|", sep="")
    for i in range(len(benchmarks)):
        line = f"| {benchmarks[i]: <{first_column_wight}} |"
        for j in range(len(results[i])):
            line += f" {results[i][j]: <{len(algos[j])}} |"
        print(line)


format_table(["best case", "the worst case"],
             ["quick sort", "merge sort", "bubble sort", ],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
