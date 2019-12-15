# Binomial Simulator
A tool which demonstrates the shape of the binomial distribution by simulating independent experiments. The user inputs the number of simulations **s**, the number of trials per simulation **n**, and the probability of trial success **p**.

For each simulation, **n** trials are run, each with an independent probability **p** of success, and the number of successes out of **n** is recorded. Then, number of successes is plotted against number of simulations. That is, for a point (x, y), there were y simulations out of **n** for which x trials were successful.

Changing the values of **n** and **p** changes the underlying probability distribution, whereas increasing **s** causes the plot to more closely resemble that distribution.

# User Guide
This program requires Python 3 and Matplotlib to be installed. You can install Matplotlib with ``pip install matplotlib``.

# What Did I Learn?
 - How to use the basic features of Matplotlib.
 - Probability distributions are real! You can plot them!
