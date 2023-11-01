benchmark = "Benchmark"


def format_table(benchmarks, algos, results):
    first_column_wight = max(map(len, benchmarks + [benchmark]))
    sum_len = first_column_wight + len(algos) + 2
    head = f"| {benchmark: <{first_column_wight}} |"
    algos_wight = [0] * len(algos)
    for i in range(len(algos)):
        algos_wight[i] = max([len(str(results[j][i])) for j in range(len(results))] + [len(algos[i])])
        head += f" {algos[i]: <{algos_wight[i]}} |"
        sum_len += algos_wight[i] + 2
    print(head)
    print("|", "-" * sum_len, "|", sep="")
    for i in range(len(benchmarks)):
        line = f"| {benchmarks[i]: <{first_column_wight}} |"
        for j in range(len(results[i])):
            line += f" {results[i][j]: <{algos_wight[j]}} |"
        print(line)


format_table(["b", "w", "weqweqweqweqwewqewqewqewqewqewq"],
             ["quick sort", "merge sort", "bubble sort", "asdqweqweqwewqeqweq"],
             [[1.238675356346456, 1.56, 2.0, 1], [3.3, 2.9, 3.9, 1], [1, 2, 3, 1]])
