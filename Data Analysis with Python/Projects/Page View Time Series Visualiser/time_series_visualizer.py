import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True)
df.set_index('date', drop=False)

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, axis = plt.subplots(1, 1)

    fig.set_figwidth(15)
    fig.set_figheight(5)

    plt.plot(df, color="#CF0500", linewidth=.9)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # Inspired by https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    df["year"] = pd.DatetimeIndex(df["date"]).year
    df["month"] = pd.DatetimeIndex(df["date"]).month

    df_grouped = df.groupby(["year", "month"]).mean().copy().reset_index()

    group_labels = pd.unique(df["year"])

    means = list()

    for i in range(1, 13):
        means.append(list(df_grouped[(df_grouped["month"] == i)]["value"]))
        if len(means[i - 1]) < 4:
            means[i - 1].insert(0, 0)

    x = np.arange(len(group_labels))  # the year label locations
    width = 0.05  # the width of the bars

    fig, axis = plt.subplots(figsize=(10, 13 * (2 / 3)))

    rects = list()
    size_differential = -11

    for i in range(0, 12):
        rects.append(axis.bar(x + ((size_differential + (2 * i)) / 2) * width, means[i], width, label=months[i]))

    # Add some text for labels, title and custom x-axis tick labels, etc.
    axis.set_xlabel("Years", fontsize=14)
    axis.set_ylabel("Average Page Views", fontsize=14)
    axis.set_xticks(x)
    axis.set_xticklabels(group_labels, rotation=90, ha="center")
    axis.legend(title="Months", title_fontsize="x-large", fontsize="x-large")

    fig.tight_layout()

    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
