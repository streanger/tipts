import os
import time
import random
import datetime
from pathlib import Path
import numpy as np
import pandas as pd
from rich import print
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle

"""
useful:
    https://stackoverflow.com/questions/29672375/histogram-in-matplotlib-time-on-x-axis
    https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib
    https://matplotlib.org/stable/gallery/text_labels_and_annotations/date.html
    https://www.geeksforgeeks.org/how-to-change-the-number-of-ticks-in-matplotlib/
    https://stackoverflow.com/questions/13703720/converting-between-datetime-timestamp-and-datetime64
    https://stackoverflow.com/questions/9627686/plotting-dates-on-the-x-axis-with-pythons-matplotlib
    https://programtalk.com/python-examples/matplotlib.dates.date2num/
    https://www.geeksforgeeks.org/change-the-legend-position-in-matplotlib/
    
"""

def datetime_to_unix(date):
    """convert datetime object to unix time"""
    return date.timestamp()
    
    
def unix_to_datetime(unix_time):
    """convert unix to datetime"""
    out = datetime.datetime.fromtimestamp(unix_time)
    return out
    
    
def reduce_dates(dates_list, base_date=None):
    """reduce dates to single day time
    https://stackoverflow.com/questions/8474670/pythonic-way-to-combine-datetime-date-and-datetime-time-objects
    """
    if base_date is None:
        base_date = datetime.datetime.today()
    reduced = [datetime.datetime.combine(base_date, date.time()) for date in dates_list]
    return reduced
    
    
def random_dates(n):
    """random dates from today in range of n
    # base_date = datetime.date.now()
    # base_date = datetime.time.now()
    # base_date = datetime.datetime.now()
    """
    base_date = datetime.datetime.today()
    dates = []
    for x in range(n):
        days = random.randrange(30)
        hours = random.randrange(24)
        minutes = random.randrange(60)
        delta = datetime.timedelta(days=days, hours=hours, minutes=minutes)
        date = base_date + delta
        dates.append(date)
    return dates
    
    
def draw_hist(many_data, title, save_filename=None):
    """draw histogram from many list of dates
    many_data: list((name, dates_list))
    title: histogram title
    save_filename: name of file for output image
    (it need to be reimplemented, but for general purpose its fine)
    
    variable bins example:
        values = [y for x in many_data for y in x[1]]
        min_val = round(min(values).timestamp())
        max_val = round(max(values).timestamp())
        bins = np.linspace(min_val, max_val, 50)
        bins = [unix_to_datetime(date) for date in bins]
    """
    
    # ******** data setup & colors ********
    hist_number = len(many_data)
    cmap = plt.get_cmap('jet')
    colors = []
    histogram_data = []
    for index, (name, data) in enumerate(many_data):
        current_color = cmap(index/hist_number)
        colors.append(current_color)
        mpl_data = mdates.date2num(data)
        histogram_data.append(mpl_data)
        
    # ******** plot histogram ********
    bins = None
    fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor='grey')
    ax.hist(histogram_data, bins=bins, alpha=0.5, histtype='bar', ec='black', label='this', color=colors)
    ax.xaxis.grid()
    for label in ax.get_xticklabels(which='major'):
        label.set(rotation=30, horizontalalignment='right')
        
    # ******** date formatter & locator ********
    # there are many locators
    # without setting date formatter x-axis labels are numbers
    locator = mdates.AutoDateLocator()
    ax.xaxis.set_major_locator(locator)
    date_form = mdates.DateFormatter("%d/%m/%y\n%H:%M")
    ax.xaxis.set_major_formatter(date_form)
    
    # ******** create legend ********
    handles = [Rectangle((0,0), 1, 1, alpha=0.5, color=c, ec="k") for c in colors]
    labels= ["{}: {}".format(key+1, many_data[key][0]) for key, _ in enumerate(colors)]       # make it more clear
    plt.legend(handles, labels, loc='upper right')
    
    # ******** save & show ********
    plt.suptitle(title)
    if save_filename:
        plt.savefig(save_filename)
    plt.show()
    plt.close()
    return True
    
    
if __name__ == "__main__":
    os.chdir(str(Path(__file__).parent))
    many_data = [
        ('name1', random_dates(200)),
        ('name2', random_dates(200)),
        ('name3', random_dates(200)),
    ]
    # many_data = [
        # ('name1', reduce_dates(random_dates(200))),
        # ('name2', reduce_dates(random_dates(200))),
        # ('name3', reduce_dates(random_dates(200))),
    # ]
    draw_hist(many_data, 'title', save_filename='figure.png')
    