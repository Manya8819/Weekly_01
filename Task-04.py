temperatures = []

for i in range(5):
    temp = float(input(f"Enter temperature for day {i+1}: "))
    temperatures.append(temp)

average = sum(temperatures) / len(temperatures)
print("Average temperature over 5 days:", average)
