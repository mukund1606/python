# Plot the graph for import of the minerals in India for the last 10 years (y - rate of growth, x - year)

import matplotlib.pyplot as plt
import pandas as pd


def mineralImports():
    # Load the data from a CSV file
    data = pd.read_csv("mineral_imports.csv")

    # Extract the years and grain exports data
    years = data["Year"]
    iron_imports = data["Iron"]
    copper_imports = data["Copper"]
    magnesium_imports = data["Magnesium"]
    calcium_imports = data["Calcium"]
    phosphorus_imports = data["Phosphorus"]
    gold_imports = data["Gold"]
    silver_imports = data["Silver"]
    platinum_imports = data["Platinum"]
    palladium_imports = data["Palladium"]
    rhodium_imports = data["Rhodium"]

    # Plotting the graph
    plt.plot(years, iron_imports, label="Iron")
    plt.plot(years, copper_imports, label="Copper")
    plt.plot(years, magnesium_imports, label="Mg")
    plt.plot(years, calcium_imports, label="Ca")
    plt.plot(years, phosphorus_imports, label="P")
    # plt.plot(years, gold_imports, label='Gold')
    # plt.plot(years, silver_imports, label='Silver')
    # plt.plot(years, platinum_imports, label='Platinum')
    # plt.plot(years, palladium_imports, label='Palladium')
    # plt.plot(years, rhodium_imports, label='Rhodium')

    # Set the title and labels
    plt.title("Mineral Imports")
    plt.xlabel("Year")
    plt.ylabel("Growth Rate")


def main():
    # Plot Size full screen
    plt.rcParams["figure.figsize"] = (20, 10)
    mineralImports()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
