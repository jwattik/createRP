# -*- coding: UTF-8 -*-

import csv


def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


if __name__ == "__main__":
    data = ["г Новосибирск, ул Планетная, д 30 к 2а; 3ad41994-d671-4bcc-a5ff-a39c4d6cfadc; 5406782252; retail point "
            "create in csv".split(";")]

    path = "output.csv"
    csv_writer(data, path)