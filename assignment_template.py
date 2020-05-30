"""
COMP1730/6730 S1 2020 - Project Assignment.

Author: <u7075575>
"""
import csv
import matplotlib.pyplot as plt
import math

from assignment_helpers import plot_volumes, volume_to_area


def read_dataset(filepath):
    """
    read_dataset function will take the file path as the input, read it and return the data set.
    Parameters:
    filepath: file path of the data set.
    Returns:
    List of list. First element(date) in list of list is string, and the rest of it will be float.
    """
    data_file = open(filepath, mode="r")
    data_reader = csv.reader(data_file)
    # exclude reading header.
    header = next(data_reader)
    data_set = []
    for line in data_reader:
        # Store first column as str, and rest of it as float.
        line = [line[0], ] + [float(element) for element in line[1:]]
        data_set.append(line)
    data_file.close()
    return data_set


def date(data):
    """
    date function will return the first column(date) of the data set.
    Parameters:
    data: The list of list return from read_dataset function.
    Return:
    List with str element.
    """
    _date = [line[0] for line in data]
    return _date


def volume(data):
    """
    volume function will return the second column(volume) of the data set.
    Parameters:
    data: The list of list return from read_dataset function.
    Return:
    List with float element.
    """
    _volume = [line[1] for line in data]
    return _volume


def area(data):
    """
    area function will return the third column(area) of the data set.
    Parameters:
    data: The list of list return from read_dataset function.
    Return:
    List with float element.
    """
    _area = [line[2] for line in data]
    return _area


def rainfall(data):
    """
    rainfall function will return the fifth column(rainfall) of the data set.
    Parameters:
    data: The list of list return from read_dataset function.
    Return:
    List with float element.
    """
    _rainfall = [line[4] for line in data]
    return _rainfall


def max_temp(data):
    """
    max_temp function will return the sixth column(max temp) of the data set.
    Parameters:
    data: The list of list return from read_dataset function.
    Return:
    List with float element.
    """
    _max_temp = [line[5] for line in data]
    return _max_temp


def largest_area(data):
    """
    largest_area function will return the largest lake area in the data set.
    Parameters:
    data: The list of list return from read_dataset function.
    Return:
    float: The largest area of the lake.
    """
    max_area = max(area(data))
    return max_area


def average_volume(data):
    """
    average_volume function will return the average volume of lake in the data set.
    Parameters:
    data: The list of list return from read_dataset function.
    Return:
    float: The average volume of the lake.
    """
    total_volume = sum(volume(data))
    # Sum up all volume and divide the size of the data.
    mean_volume = (total_volume / len(volume(data)))
    return mean_volume


def most_average_rainfall(data):
    """
    most_average_rainfall function will return year and month which have the
    closest rainfall to the average in the data set.
    Parameters:
    data: The list of list return from read_dataset function.
    Return:
    tuple: Year and month have the rainfall which closest to average.
    """
    total_rainfall = sum(rainfall(data))
    average_rainfall = (total_rainfall / len(rainfall(data)))
    # An marker of which row have the closest rainfall to average rainfall
    index = 0
    # First month(element) be the closest rainfall to average rainfall initially.
    rainfall_closest_to_average = abs(rainfall(data)[0] - average_rainfall)
    for element in range(len(rainfall(data))):
        # Iterate all rainfall in data set, and keep updating rainfall_closest_to_average if we find a closer one.
        if abs(rainfall(data)[element] - average_rainfall) < rainfall_closest_to_average:
            rainfall_closest_to_average = abs(rainfall(data)[element] - average_rainfall)
            # Also replace the index which the value's index.
            index = element
    # Closest year and month. A tuple with year in the first element and month in the second element.
    closest_month_and_year = (date(data)[index][:4], date(data)[index][4:])
    return closest_month_and_year


def hottest_month(data):
    """
    hottest_month function will return the month which have the
    hottest average temperature.
    Parameters:
    data: The list of list return from read_dataset function.
    Return:
    int: month which is hottest.
    """
    month_list = [line[0][4:] for line in data]

    # Getting the index of each month, and add all max temp to each month's total.
    # January
    jan_total = 0.0
    jan_index = [element for element, month in enumerate(month_list) if month == '01']
    for month in jan_index:
        jan_total = jan_total + max_temp(data)[month]
    # February
    feb_total = 0.0
    feb_index = [element for element, month in enumerate(month_list) if month == '02']
    for month in feb_index:
        feb_total = feb_total + max_temp(data)[month]
    # March
    mar_total = 0.0
    mar_index = [element for element, month in enumerate(month_list) if month == '03']
    for month in mar_index:
        mar_total = mar_total + max_temp(data)[month]
    # April
    apr_total = 0.0
    apr_index = [element for element, month in enumerate(month_list) if month == '04']
    for month in apr_index:
        apr_total = apr_total + max_temp(data)[month]
    # May
    may_total = 0.0
    may_index = [element for element, month in enumerate(month_list) if month == '05']
    for month in may_index:
        may_total = may_total + max_temp(data)[month]
    # June
    jun_total = 0.0
    jun_index = [element for element, month in enumerate(month_list) if month == '06']
    for month in jun_index:
        jun_total = jun_total + max_temp(data)[month]
    # July
    jul_total = 0.0
    jul_index = [element for element, month in enumerate(month_list) if month == '07']
    for month in jul_index:
        jul_total = jul_total + max_temp(data)[month]
    # Aug
    aug_total = 0.0
    aug_index = [element for element, month in enumerate(month_list) if month == '08']
    for month in aug_index:
        aug_total = aug_total + max_temp(data)[month]
    # Sep
    sep_total = 0.0
    sep_index = [element for element, month in enumerate(month_list) if month == '09']
    for month in sep_index:
        sep_total = sep_total + max_temp(data)[month]
    # Oct
    oct_total = 0.0
    oct_index = [element for element, month in enumerate(month_list) if month == '10']
    for month in oct_index:
        oct_total = oct_total + max_temp(data)[month]
    # Nov
    nov_total = 0.0
    nov_index = [element for element, month in enumerate(month_list) if month == '11']
    for month in nov_index:
        nov_total = nov_total + max_temp(data)[month]
    # Dec
    dec_total = 0.0
    dec_index = [element for element, month in enumerate(month_list) if month == '12']
    for month in dec_index:
        dec_total = dec_total + max_temp(data)[month]

    # all_average is a list which contain all months' average max temp.
    all_average = [(jan_total / len(jan_index)), (feb_total / len(feb_index)), (mar_total / len(mar_index)),
                   (apr_total / len(apr_index)), (may_total / len(may_index)), (jun_total / len(jun_index)),
                   (jul_total / len(jul_index)), (aug_total / len(aug_index)), (sep_total / len(sep_index)),
                   (oct_total / len(oct_index)), (nov_total / len(nov_index)), (dec_total / len(dec_index))]
    # Get the highest temp.
    hottest = max(all_average)
    # Index record the hottest month.
    highest_temp_month = 0
    for temp in all_average:
        if temp == hottest:
            # Set highest_temp_month to the hottest temp index and + 1,
            # because the order in all average list is from January to December.
            highest_temp_month = all_average.index(temp) + 1
    return highest_temp_month


def area_vs_volume(data):
    """
    area_vs_volume function will create a figure with three subplots which shows the relationship between lake's
    volume and area.
    Parameters:
    data: The list of list return from read_dataset function.
    """
    # Total three subplots in the figure.
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 7.5))
    fig.set_figheight(7.5)
    fig.set_figwidth(10)
    # First plot x = date, y = volume. Showing the lake's volumes over the data period.
    ax1.plot(date(data), volume(data), color='g', label='volume')
    ax1.legend(loc="upper right")
    ax1.set_xlabel('date')
    ax1.set_ylabel('volumes', fontsize=12)
    # x axis label will overlap if showing every year and month. Therefore, only display January's label.
    # xticks contain all years of January.
    xticks = []
    for element in range(0, len(date(data)), 12):
        xticks.append(element)
    # First plot format setting.
    ax1.set_xticks(xticks)
    ax1.tick_params(axis='x', labelsize=8)
    position_ax1 = ax1.get_position()
    position_ax1.y0 = position_ax1.y0 + 0.04
    position_ax1.y1 = position_ax1.y1 + 0.04
    ax1.set_position(position_ax1)
    # Rotate x label 45 degree to avoid overlap.
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
    # Second plot x = date, y = area. Showing the lake's areas over the data period.
    ax2.plot(date(data), area(data), color='b', label='area')
    # Second plot format setting.
    ax2.legend(loc="upper right")
    ax2.set_ylabel('areas', fontsize=12)
    ax2.set_xlabel('date')
    ax2.set_xticks(xticks)
    ax2.tick_params(axis='x', labelsize=8)
    position_ax2 = ax2.get_position()
    position_ax2.y0 = position_ax2.y0 - 0.00001
    position_ax2.y1 = position_ax2.y1 - 0.00001
    ax2.set_position(position_ax2)
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
    # diff
    # List of the difference of areas between each month.
    areas_diff = []
    # List of the difference of volumes between each month.
    volumes_diff = []
    # List of the ration of areas_diff over volumes_diff
    diff_ratio = []
    # We don't know the difference for last data and it's next month's data. So length will be 1 shorter than our
    # data set.
    date_diff = date(data)[:len(date(data)) - 1]
    # The difference for the area size and the next month's area size, and add to areas_diff list.
    for index in range(len(area(data)) - 1):
        diff_area_element = area(data)[index + 1] - area(data)[index]
        areas_diff.append(diff_area_element)
    # The difference for the volume size and the next month's volume size, and add to volume_diff list.
    for index in range(len(volume(data)) - 1):
        diff_volumes_element = volume(data)[index + 1] - volume(data)[index]
        volumes_diff.append(diff_volumes_element)
    # Ratio of two factor's difference. It can show the size area which gain or lose from one litre of volumes gain
    # or lose between each month.
    for index in range(len(volumes_diff)):
        diff_ratio_element = areas_diff[index] / volumes_diff[index]
        diff_ratio.append(diff_ratio_element)
    # Third plot x = date, y = the ration of volumes difference and areas difference each month.
    ax3.plot(date_diff, diff_ratio, color='r', label='ratio')
    # Third plot format setting.
    ax3.legend(loc="upper right")
    ax3.set_ylabel('Size difference by 1 liter of volume changes', fontsize=8)
    ax3.set_xlabel('date')
    ax3.set_xticks(xticks[:len(xticks)])
    ax3.tick_params(axis='x', labelsize=8)
    position_ax3 = ax3.get_position()
    position_ax3.y0 = position_ax3.y0 - 0.03
    position_ax3.y1 = position_ax3.y1 - 0.03
    ax3.set_position(position_ax3)
    plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)
    plt.title("Lake George's areas vs volume.(From 1990 - 2018)", pad=400, fontsize=16)
    ax1.grid()
    ax2.grid()
    ax3.grid()
    plt.show()


def lake_george_simple_model(data, evaporation_rate):
    """
    lake_george_simple_model function will return a list with the forecasting volume base on the assumption
    and the starting point will be the first volume in the data set.
    Parameters:
    data: The list of list return from read_dataset function.
    evaporation_rate: An integer represent constant evaporation_rate for each month.
    Returns:
    List: contain the simple expected Lake's volumes.
    """
    # Assume catchment area be the largest area in the data set.
    catchment_area = largest_area(data)
    # Assume surface area also be the largest area in the data set.
    surface_area = largest_area(data)
    # The first volume in the data set will be the starting point of this model.
    model_volume = [volume(data)[0]]

    # We already assume the first point, so start with second element.
    for element in range(1, len(rainfall(data))):
        if model_volume[element - 1] + (rainfall(data)[element] * catchment_area) - (
                evaporation_rate * surface_area) > 0:
            # new model volume will take the previous volume add the rain it got then minus the water which be
            # evaporate.
            model_volume_new = model_volume[element - 1] + (rainfall(data)[element] * catchment_area) - (
                    evaporation_rate * surface_area)
            model_volume.append(model_volume_new)
        # However, the volume doesn't make sense lower than 0, so the lowest model volume can only be 0.
        if model_volume[element - 1] + (rainfall(data)[element] * catchment_area) - (
                evaporation_rate * surface_area) <= 0:
            model_volume_new = 0.0
            model_volume.append(model_volume_new)
    return model_volume


def lake_george_complex_model(data):
    """
    lake_george_complex_model function will return a list with the forecasting volume base on the assumption
    and the starting point will be the first volume in the data set. But the evaporation rate will change by multiple
    factors each month.
    Parameters:
    data: The list of list return from read_dataset function.
    Returns:
    List: contain the complex expected Lake's volumes.
    """
    solar_exposure = [line[3] for line in data]
    min_temp = [line[6] for line in data]
    humidity = [line[7] for line in data]
    wind_speed = [line[8] for line in data]
    model_volume = [volume(data)[0]]
    catchment_area = largest_area(data)
    surface_area = largest_area(data)

    # Same as simple model, start point already be set so start at second element.
    for element in range(1, len(rainfall(data))):

        # evaporation rate = −3 min_temp + 1.6 max_temp − 2.5 wind + 4.5 solar_exposure − 0.4 humidity
        evaporation_rate = -3 * min_temp[
            element] + 1.6 * max_temp(data)[element] - 2.5 * wind_speed[element] + 4.5 * solar_exposure[element] - 0.4 * \
                           humidity[element]
        if model_volume[element - 1] + (rainfall(data)[element] * catchment_area) - (
                evaporation_rate * surface_area) > 0:
            model_volume_new = model_volume[element - 1] + (rainfall(data)[element] * catchment_area) - (
                    evaporation_rate * surface_area)
            model_volume.append(model_volume_new)
        # The volume can't be lower than 0.
        if model_volume[element - 1] + (rainfall(data)[element] * catchment_area) - (
                evaporation_rate * surface_area) <= 0:
            model_volume_new = 0.0
            model_volume.append(model_volume_new)

    return model_volume


def evaluate_model(data, volumes):
    """
    evaluate_model function can return the model error by mean squared error method.
    Parameters:
    data: The list of your model volume.
    volumes: The real value of volumes.
    Returns:
    Float: The model error of your data. Closer to zero means that is more similar with real value.
    """
    # The real value in the data.
    real_volume = volume(data)
    # MSE method
    diff = []
    for index in range(len(real_volume)):
        difference = math.pow((volumes[index] - real_volume[index]), 2)
        diff.append(difference)
    model_error = (1 / len(diff)) * sum(diff)
    return model_error


data = read_dataset('assignment_lake_george_data.csv')
# print(type(date(data)[0]))
# print(type(average_volume(data)))
# print(type(most_average_rainfall(data)))
# print(type(hottest_month(data)))
area_vs_volume(data)
#plot_volumes(lake_george_simple_model(data, 63))
#plot_volumes(lake_george_complex_model(data))
#plot_volumes(lake_george_simple_model(data, 55))
print(evaluate_model(data, lake_george_complex_model(data)))
print(evaluate_model(data, lake_george_simple_model(data, 64)))
