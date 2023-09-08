import os
import json
from pathlib import Path
import matplotlib.pyplot as plt


def read_json(filename):
    """read json file to dict"""
    data = {}
    try:
        with open(filename, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print('[x] FileNotFoundError: {}'.format(filename))
    return data


def example_data():
    data = {
        'hash-python-md5': {
            'color': 'green',
            'x': [1,2,3,4],
            'y': [2,4,6,8],
        },
        'hash-subprocess-md5': {
            'color': 'red',
            'x': [1,2,3,4],
            'y': [3,5,7,9],
        },
    }
    return data


if __name__ == "__main__":
    os.chdir(Path(__file__).parent)

    # get data
    # data = example_data()
    data = read_json('collected.json')

    # draw chart
    for key, value in data.items():
        plt.plot(value['x'], value['y'], color=value['color'], label=key)
    plt.legend()
    plt.grid()
    plt.xlabel("size[B]",  size=12)
    plt.ylabel("time[ms]", size=12)
    plt.title("speed vs file size", size=14)
    plt.xscale("log")
    plt.show()
