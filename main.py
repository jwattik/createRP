# -*- coding: UTF-8 -*-

import csv

from APIClient import APIClient
from Body import Body

login = input('login: ')
password = input('password: ')


# def csv_reader(file_obj):
#     """
#     Read a csv file
#     """
#     reader = csv.reader(file_obj)
#     for row in reader:
#         data = Body(address=row[0], inn=row[2], name=row[3], phone=row[1]).__dict__
#         print(" ".join(row))
#         client = APIClient(login=login, password=password, data=data)
#         status = client.retail_points()
#         print(status.status_code, status.content)

def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        data = Body(posLinkToken=row[5]).__dict__
        print(" ".join(row))
        client = APIClient(login=login, password=password, data=data, count=row[4])
        status = client.retail_point_update()
        print(status.status_code, status.content)


if __name__ == "__main__":
    csv_path = "output.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)
