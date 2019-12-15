import random
import matplotlib.pyplot as plot

plot.xlabel('Number of successful trials')
plot.ylabel('Frequency')

while True:
    s = int(input("Enter number of simulations.\n> "))
    n = int(input("Enter number of trials per simulation.\n> "))
    p = float(input("Enter probability of trial success.\n> "))

    results = []
    for i in range(s):
        successes = sum(random.random() <= p for j in range(n))
        results.append(successes)

    for r in results:
        plot.plot(r, results.count(r), 'r.')

    plot.show()
    print('\n---\n')
