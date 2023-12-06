import math
from rich.console import Console

console = Console()


# sample
total_time = 71530
y_value = 940200
# input
total_time = 49979494
y_value = 263153213781851

# coefficients for quadratic formula
a = 1
b = -total_time
c = y_value

# calculate the discriminant
discriminant = b**2 - 4*a*c

# calculate two possible values of t
t1 = (-b + math.sqrt(discriminant)) / (2*a)
t2 = (-b - math.sqrt(discriminant)) / (2*a)

print(f"The two values of t are: {t1} and {t2}")
ts = [t1,t2]
ts.sort()
console.print(math.floor(ts[1]) - math.floor(ts[0]))
