# Plot the graph to show export of different grains in India for the last 10 years (y - rate of growth, x - year)

import matplotlib.pyplot as plt
import pandas as pd


def grainExports():
    # Load the data from a CSV file
    data = pd.read_csv("grain_exports.csv")

    # Extract the years and grain exports data
    years = data["Year"]
    wheat_exports = data["Wheat"]  # y
    rice_exports = data["Rice"]  # y
    maize_exports = data["Maize"]
    barley_exports = data["Barley"]
    shorghum_exports = data["Sorghum"]
    millet_exports = data["Millet"]
    bulgur_exports = data["Bulgur"]
    farro_exports = data["Farro"]
    quinoa_exports = data["Quinoa"]
    black_rice_exports = data["Black Rice"]

    # Plotting the graph
    plt.plot(years, wheat_exports, label="Wheat", marker="o")
    plt.plot(years, rice_exports, label="Rice", marker="o")
    plt.plot(years, maize_exports, label="Maize", marker="o")
    plt.plot(years, barley_exports, label="Barley", marker="o")
    # plt.plot(years, shorghum_exports, label="Shorghum", marker="o")
    plt.plot(years, millet_exports, label="Millet", marker="o")
    # plt.plot(years, bulgur_exports, label="Bulgur", marker="o")
    # plt.plot(years, farro_exports, label="Farro", marker="o")
    # plt.plot(years, quinoa_exports, label="Quinoa", marker="o")
    # plt.plot(years, black_rice_exports, label="Black Rice", marker="o")

    # Set the title and labels
    plt.title("Grain Exports")
    plt.xlabel("Year")
    plt.ylabel("Growth Rate")


def main():
    # Plot Size full screen
    plt.rcParams["figure.figsize"] = (20, 10)
    grainExports()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
