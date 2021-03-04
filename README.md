# pi-generator

*Inspired by Matt Parker from Stand-up Maths*

The probability of drawing a pair of cofactors in a sample is exactly 6/(pi^2). This program uses that maths to calculate pi from any sample size using python's standard math and random libraries. I can fairly reliably get an average of ~3.14 when samples = 1_000_000 and r = 1_000_000.

test_generate.py will take a less precise pi calculation and average it over many iterations, showing a gradual improvement in accuracy in graphical form. install `pandas` to run
