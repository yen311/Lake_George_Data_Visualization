"""
COMP1730/6730 S1 2020 - Project Assignment.

Author: <your university ID here>
"""
import csv
import matplotlib.pyplot as plt
import math


from assignment_helpers import plot_volumes


def read_dataset(filepath):
    data_file = open(filepath, mode="r")
    data_reader = csv.reader(data_file)
    header = next(data_reader)

    data_set = []
    for line in data_reader:
        line = [line[0], ] + [float(element) for element in line[1:]]
        data_set.append(line)
    data_file.close()
    return data_set


def largest_area(data):
    area = [line[2] for line in data]
    max_area = max(area)
    return max_area


def average_volume(data):
    volume = [line[1] for line in data]
    total_volume = sum(volume)
    mean_volume = (total_volume / len(volume))
    return mean_volume


def most_average_rainfall(data):
    date = [line[0] for line in data]
    rainfall = [line[4] for line in data]
    total_rainfall = sum(rainfall)
    average_rainfall = (total_rainfall / len(rainfall))

    index = 0
    closest_month_and_year = abs(rainfall[0] - average_rainfall)
    for element in rainfall:
        if abs(element - average_rainfall) < closest_month_and_year:
            closest_month_and_year = abs(element - average_rainfall)
            index = rainfall.index(element)
    closest_month_and_year = (date[index][:4], date[index][4:])
    return closest_month_and_year


def hottest_month(data):
    max_temp = [line[5] for line in data]
    date = [line[0][4:] for line in data]
    # January
    Jan_total = 0.0
    Jan_index = [element for element, month in enumerate(date) if month == '01']
    for month in Jan_index:
        Jan_total = Jan_total + max_temp[month]
    # February
    Feb_total = 0.0
    Feb_index = [element for element, month in enumerate(date) if month == '02']
    for month in Feb_index:
        Feb_total = Feb_total + max_temp[month]
    # March
    Mar_total = 0.0
    Mar_index = [element for element, month in enumerate(date) if month == '03']
    for month in Mar_index:
        Mar_total = Mar_total + max_temp[month]
    # April
    Apr_total = 0.0
    Apr_index = [element for element, month in enumerate(date) if month == '04']
    for month in Apr_index:
        Apr_total = Apr_total + max_temp[month]
    # May
    May_total = 0.0
    May_index = [element for element, month in enumerate(date) if month == '05']
    for month in May_index:
        May_total = May_total + max_temp[month]
    # June
    Jun_total = 0.0
    Jun_index = [element for element, month in enumerate(date) if month == '06']
    for month in Jun_index:
        Jun_total = Jun_total + max_temp[month]
    # July
    Jul_total = 0.0
    Jul_index = [element for element, month in enumerate(date) if month == '07']
    for month in Jul_index:
        Jul_total = Jul_total + max_temp[month]
    # Aug
    Aug_total = 0.0
    Aug_index = [element for element, month in enumerate(date) if month == '08']
    for month in Aug_index:
        Aug_total = Aug_total + max_temp[month]
    # Sep
    Sep_total = 0.0
    Sep_index = [element for element, month in enumerate(date) if month == '09']
    for month in Sep_index:
        Sep_total = Sep_total + max_temp[month]
    # Oct
    Oct_total = 0.0
    Oct_index = [element for element, month in enumerate(date) if month == '10']
    for month in Oct_index:
        Oct_total = Oct_total + max_temp[month]
    # Nov
    Nov_total = 0.0
    Nov_index = [element for element, month in enumerate(date) if month == '11']
    for month in Nov_index:
        Nov_total = Nov_total + max_temp[month]
    # Dec
    Dec_total = 0.0
    Dec_index = [element for element, month in enumerate(date) if month == '12']
    for month in Dec_index:
        Dec_total = Dec_total + max_temp[month]

    all_average = [(Jan_total / len(Jan_index)), (Feb_total / len(Feb_index)), (Mar_total / len(Mar_index)),
                   (Apr_total / len(Apr_index)), (May_total / len(May_index)), (Jun_total / len(Jun_index)),
                   (Jul_total / len(Jul_index)), (Aug_total / len(Aug_index)), (Sep_total / len(Sep_index)),
                   (Oct_total / len(Oct_index)), (Nov_total / len(Nov_index)), (Dec_total / len(Dec_index))]
    hottest = max(all_average)
    highest_temp_month = 0
    for temp in all_average:
        if temp == hottest:
            highest_temp_month = all_average.index(temp) + 1
    return highest_temp_month


def area_vs_volume(data):
    areas = [line[2] for line in data]
    volumes = [line[1] for line in data]
    date = [line[0] for line in data]

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
    fig.set_figheight(15)
    fig.set_figwidth(15)
    # volume
    ax1.plot(date, volumes, color='g', label='volume')
    ax1.plot(date, areas, color='r', label='area')
    ax1.legend(loc="upper right")
    ax1.set_xlabel('date')
    ax1.set_ylabel('volumes', fontsize=16)
    xticks = []
    for element in range(0, len(date), 12):
        xticks.append(element)
    ax1.set_xticks(xticks)
    ax1.tick_params(axis='x', labelsize=10)
    position_ax1 = ax1.get_position()
    position_ax1.y0 = position_ax1.y0 + 0.04
    position_ax1.y1 = position_ax1.y1 + 0.04
    ax1.set_position(position_ax1)
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
    # area
    ax2.plot(date, areas, color='b', label='area')
    ax2.legend(loc="upper right")
    ax2.set_ylabel('areas', fontsize=16)
    ax2.set_xlabel('date')
    ax2.set_xticks(xticks)
    ax2.tick_params(axis='x', labelsize=10)

    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
    plt.title("Lake George's areas vs volume.(From 1990 - 2018)", pad=360, fontsize=24)
    ax1.grid()
    ax2.grid()
    plt.show()


def lake_george_simple_model(data, evaporation_rate):
    volume = [line[1] for line in data]
    catchment_area = 950000000 * 0.16
    surface_area = largest_area(data)
    rainfall = [line[4] for line in data]
    start_point = volume[0]
    model_volume = [start_point]

    for element in range(1, len(rainfall)):
        if model_volume[element - 1] + (rainfall[element] * catchment_area) - (
                evaporation_rate * surface_area) > 0:
            model_volume_new = model_volume[element - 1] + (rainfall[element] * catchment_area) - (
                    evaporation_rate * surface_area)
            model_volume.append(model_volume_new)
        if model_volume[element - 1] + (rainfall[element] * catchment_area) - (
                evaporation_rate * surface_area) <= 0:
            model_volume_new = 0.0
            model_volume.append(model_volume_new)
    return model_volume


def lake_george_complex_model(data):
    catchment_area = 950000000 * 0.16
    surface_area = largest_area(data)
    volume = [line[1] for line in data]
    solar_exposure = [line[3] for line in data]
    rainfall = [line[4] for line in data]
    max_temp = [line[5] for line in data]
    min_temp = [line[6] for line in data]
    humidity = [line[7] for line in data]
    wind_speed = [line[8] for line in data]

    start_point = volume[0]
    model_volume = [start_point]
    for element in range(1, len(rainfall)):
        evaporation_rate = -3 * min_temp[
            element] + 1.6 * max_temp[element] - 2.5 * wind_speed[element] + 4.5 * solar_exposure[element] - 0.4 * \
                           humidity[element]
        if model_volume[element - 1] + (rainfall[element] * catchment_area) - (
                evaporation_rate * surface_area) > 0:
            model_volume_new = model_volume[element - 1] + (rainfall[element] * catchment_area) - (
                    evaporation_rate * surface_area)
            model_volume.append(model_volume_new)
        if model_volume[element - 1] + (rainfall[element] * catchment_area) - (
                evaporation_rate * surface_area) <= 0:
            model_volume_new = 0.0
            model_volume.append(model_volume_new)
    return model_volume


def evaluate_model(data, volumes):
    real_volume = [line[1] for line in data]
    diff = []
    for index in range(len(real_volume)):
        difference = math.pow((volumes[index] - real_volume[index]), 2)
        diff.append(difference)
    model_error = (1 / len(diff)) * sum(diff)
    return model_error



data = read_dataset('assignment_lake_george_data.csv')
# print(data)
print(largest_area(data))

#print(average_volume(data))
#print(most_average_rainfall(data))
#print(hottest_month(data))
#area_vs_volume(data)
plot_volumes(lake_george_simple_model(data, 60))

#print(evaluate_model(data, lake_george_complex_model(data)))
