from matplotlib import pyplot as plt
from collections import Counter
import random
import matplotlib.animation as animation


def linear_plot() -> bool:
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    plt.plot(years, gdp, color="green", marker="o", linestyle="solid")

    plt.title("Номинальный ВВП")

    plt.ylabel("Млрд $")

    plt.savefig("im/linear_plot.png")
    plt.show()
    return True


def historgram_plot() -> bool:
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]

    # plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
    plt.bar(range(len(movies)), num_oscars)

    plt.title("My Favorite Movies")     # add a title
    plt.ylabel("# of Academy Awards")   # label the y-axis

    # label x-axis with movie names at bar centers
    plt.xticks(range(len(movies)), movies)

    plt.savefig("im/historgram_plot.png")
    plt.show()
    return True


def upper_histogram_plot() -> bool:
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

    # Bucket grades by decile, but put 100 in with the 90s
    histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

    plt.bar([x + 5 for x in histogram.keys()],  # Shift bars right by 5
            histogram.values(),                 # Give each bar its correct height
            10,                                 # Give each bar a width of 8
            edgecolor=(0, 0, 0))                # Black edges for each bar

    plt.axis([-5, 105, 0, 5])                  # x-axis from -5 to 105,
                                            # y-axis from 0 to 5

    plt.xticks([10 * i for i in range(11)])    # x-axis labels at 0, 10, ..., 100
    plt.xlabel("Decile")
    plt.ylabel("# of Students")
    plt.title("Distribution of Exam 1 Grades")
    plt.savefig("im/upper_histogram_plot.png")
    plt.show()
    return True


def misunderstandable_histogram_plot() -> bool:
    mentions = [500, 505]
    years = [2017, 2018]

    plt.bar(years, mentions, 0.8)
    plt.xticks(years)
    plt.ylabel("# of times I heard someone say 'data science'")

    # if you don't do this, matplotlib will label the x-axis 0, 1
    # and then add a +2.013e3 off in the corner (bad matplotlib!)
    plt.ticklabel_format(useOffset=False)

    # misleading y-axis only shows the part above 500
    plt.axis([2016.5, 2018.5, 499, 506])
    plt.title("Look at the 'Huge' Increase!")
    plt.savefig("im/misunderstandable_histogram_plot.png")
    plt.show()
    return True


def understandable_histogram_plot() -> bool:
    mentions = [500, 505]
    years = [2017, 2018]

    plt.bar(years, mentions, 0.8)
    plt.xticks(years)
    plt.ylabel("# of times I heard someone say 'data science'")

    # if you don't do this, matplotlib will label the x-axis 0, 1
    # and then add a +2.013e3 off in the corner (bad matplotlib!)
    plt.ticklabel_format(useOffset=False)

    # misleading y-axis only shows the part above 500
    plt.axis([2016.5, 2018.5, 0, 550])
    plt.title("Not So Huge Anymore")    
    plt.savefig("im/understandable_histogram_plot.png")
    plt.show()
    return True 

def line_chart_plot() -> bool:
    variance     = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    total_error  = [x + y for x, y in zip(variance, bias_squared)]
    xs = [i for i, _ in enumerate(variance)]

    # We can make multiple calls to plt.plot
    # to show multiple series on the same chart
    plt.plot(xs, variance,     'g-',  label='variance')    # green solid line
    plt.plot(xs, bias_squared, 'r-.', label='bias^2')      # red dot-dashed line
    plt.plot(xs, total_error,  'b:',  label='total error') # blue dotted line

    # Because we've assigned labels to each series,
    # we can get a legend for free (loc=9 means "top center")
    plt.legend(loc=9)
    plt.xlabel("model complexity")
    plt.xticks([])
    plt.title("The Bias-Variance Tradeoff")
    plt.savefig("im/line_chart_plot.png")
    plt.show()
    return True 

def scatterplot() -> bool:
    friends = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    plt.scatter(friends, minutes)

    # label each point
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label,
            xy=(friend_count, minute_count), # Put the label with its point
            xytext=(5, -5),                  # but slightly offset
            textcoords='offset points')

    plt.title("Daily Minutes vs. Number of Friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes spent on the site")
    plt.savefig("im/scatterplot.png")
    plt.show()
    return True 

def scatterplot_axes_not_comparable() -> bool:
    test_1_grades = [ 99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]

    plt.scatter(test_1_grades, test_2_grades)
    plt.title("Axes Aren't Comparable")
    plt.xlabel("test 1 grade")
    plt.ylabel("test 2 grade")
    plt.savefig("im/scatterplot_axes_not_comparable.png")
    plt.show()
    return True 


def scatterplot_axes_comparable() -> bool:
    test_1_grades = [ 99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]
    plt.scatter(test_1_grades, test_2_grades)
    plt.title("Axes Are Comparable")
    plt.axis("equal")
    plt.xlabel("test 1 grade")
    plt.ylabel("test 2 grade")
    plt.savefig("im/scatterplot_axes_comparable.png")
    plt.show()
    return True 



def simpliest_plot() -> bool:
    x, y = [1,2,3,4,5], [0,9,8,7,6]
    plt.plot(x, y)
    plt.xlabel("Plot number X")
    plt.ylabel("Plot numbre Y")
    plt.title("Trying plots")
    plt.savefig("im/simpliest_plot.png")
    plt.show()
    return True

def two_plots_with_legend() -> bool:
    x, y = [1,2,3,4,5], [0,9,8,7,6]
    y2 = [4, 7, 1, 5, 3]
    plt.plot(x, y, label="First")
    plt.plot(x, y2, label="Second")
    plt.xlabel("Plot number X")
    plt.ylabel("Plot numbre Y")
    plt.title("Trying plots")
    plt.legend()
    plt.savefig("im/two_plots_with_legend.png")
    plt.show()
    return True

def bar_charts() -> bool:
    x, y = [1,3,5,7,5], [0,9,8,7,6]
    x2, y2 = [2, 4, 6, 9, 10], [5, 2, 6, 8, 1]
    plt.bar(x, y, label="First Bar", color="g")
    plt.bar(x2, y2, label="Second Bar", color="r")
    plt.xlabel("Numbers")
    plt.ylabel("Height")
    plt.title("Trying bar_charts")
    plt.legend()
    plt.savefig("im/bar_charts.png")
    plt.show()
    return True

def histogram() -> bool:
    test_scores = [94, 69, 78, 89, 78, 85, 96, 65, 35, 32, 64, 36, 86, 96, 65, 34]
    x = [i for i in range(len(test_scores))]
    bins = [i for i in range(10, 101, 10)]
    plt.hist(test_scores, bins, histtype="bar", rwidth=0.8, cumulative=True)
    plt.savefig("im/histogram.png")
    plt.show()
    return True

def scatter_plots() -> bool:
    test_scores = [94, 69, 78, 89, 78, 85, 96, 65, 35, 32, 64, 36, 86, 96, 65, 34]
    time_spent = [56, 30, 40, 48, 45, 47, 55, 30, 25, 15, 40, 37, 50, 58, 40, 32]
    plt.scatter(time_spent, test_scores)
    plt.xlabel("Time spent on test")
    plt.ylabel("Test score")
    plt.title("Time on score")
    plt.savefig("im/scatter_plots.png")
    plt.show()
    return True

def stack_plots() -> bool:
    year = [i for i in range(1, 11)]
    taxes = [12, 23, 34, 45, 56, 63, 22, 83, 56, 62]
    overhead = [30, 22, 9, 29, 17, 12, 14, 24, 49, 35]
    entertainment = [41, 32, 27, 13, 19, 12, 22, 18, 28, 20]

    plt.plot([], [], color='m', label="taxes")
    plt.plot([], [], color='c', label="overhead")
    plt.plot([], [], color='b', label="entertainment")

    plt.stackplot(year, taxes, overhead, entertainment, colors=["m", "c", "b"])
    plt.legend()
    plt.title("Company expenses")
    plt.xlabel("Years")
    plt.ylabel("Cost, in thousands")
    plt.savefig("im/stack_plots.png")
    plt.show()
    return True

def pie_charts() -> bool:
    labels = ["taxes", "overhead", "entertainment"]
    sizes = [25, 35, 12]
    colors = ["c", "m", "b"]
    plt.pie(sizes, labels=labels, colors=colors, startangle=90, autopct="%1.1f%%", shadow=True, explode=(0, 0.1, 0))
    plt.axis("equal")
    plt.savefig("im/pie_charts.png")
    plt.show()
    return True

def messy_plot() -> bool:
    for i in range(8):
        x = []
        y = []
        for j in range(1, 10):
            ys = random.randrange(0,15)
            xs = j
            x.append(xs)
            y.append(ys)

        plt.plot(x, y, label=i)
    plt.legend()
    plt.savefig("im/messy_plot.png")
    plt.show()
    return True


def live_graphs() -> bool:
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    def animate(i):
        pull_data = open("example.txt", "r").read()
        data_list = pull_data.split("\n")
        xs, ys = [], []
        for line in data_list:
            if len(line) > 1:
                x, y = line.split(",")
                xs.append(int(x))
                ys.append(int(y))
        # plt.clear()
        plt.plot(xs, ys)
    plt.show()
    return True
