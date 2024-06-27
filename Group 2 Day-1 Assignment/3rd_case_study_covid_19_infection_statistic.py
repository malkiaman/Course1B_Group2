import statistics

# List of newly infected patients per day during the first 20 days
infection_data = [
    174, 335, 278, 214, 422, 513, 737, 672, 489, 412,
    1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342
]

# Calculating statistics
minimum = min(infection_data)
maximum = max(infection_data)
range_value = maximum - minimum
mean = statistics.mean(infection_data)
median = statistics.median(infection_data)
variance = statistics.variance(infection_data)
standard_deviation = statistics.stdev(infection_data)

# Displaying statistics
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range_value}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {standard_deviation}")
