# author: Tiffany Timbers
# date: 2020-02-23

"""Calculates and prints the square root of a given number."""

import click
import math

@click.command()
@click.option("--n", type=int, required=True, help="Number for which the square root should be calculated")
def main(n):
    print(math.sqrt(n))
    
    if number < 0:
  raise Exception("n should not a positive number")

if __name__ == "__main__":
    main()
