from src.sorting_algorithms.insertion_sort import insertion_sort


def number_of_buckets(elements):
    return len(elements)


def hash_double(element: float, n_buckets: int):
    return n_buckets * element


def extract(buckets, elements):
    index = 0
    for k in range(0, len(buckets.keys())):
        sorted_bucket = insertion_sort(buckets[k])
        for e in sorted_bucket:
            elements[index] = e
            index += 1
    return elements


def bucket_sort(elements):
    n_buckets = number_of_buckets(elements)
    buckets = {k: [] for k in range(0, n_buckets)}

    for e in elements:
        bucket = hash_double(e, n_buckets)
        buckets[bucket].append(e)
    return extract(buckets, elements)


if __name__ == '__main__':
    print(bucket_sort([0.12, 0.5, 0.8, 0.9876]))
