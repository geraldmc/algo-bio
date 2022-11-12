# hash_distribution.py

from collections import Counter

def distribute(items, num_containers, hash_function):
    return Counter([hash_function.hash_func_mod(item) % num_containers for item in items])

def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")