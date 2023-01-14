import csv
from scipy.interpolate import LinearNDInterpolator
import numpy
import pandas as pd


def csv_reader(file_obj):
    csv.DictReader(file_obj)


if __name__ == "__main__":
    lines = []
    lines_track = []
    lat_arr_model = []
    lon_arr_model = []
    h_arr_model = []
    lat_arr_track = []
    lon_arr_track = []
    inter = []
    with open('Track_20211010.xyz', newline='') as track:
        reader_track = csv.reader(track, delimiter=',', quotechar='|')
        for row in reader_track:
            lines_track.append(([float(row[0]), float(row[1]), float(row[2])]))
            #print(lines_track[0][1])
    with open('dtu_model_all.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            lines.append([row[0], row[1], row[2]])
    for line in lines:
        d = "\"'EN°"
        for char in d:
            line[0] = line[0].replace(char, "")
            line[1] = line[1].replace(char, "")
            line[2] = line[2].replace(char, "")
        lon_spl = line[0].strip().split(" ")
        lon_arr_model.append(float(lon_spl[0]) + float(lon_spl[1]) / 60.0 + float(lon_spl[2]) / 3600.0)
        lat_spl = line[1].strip().split(" ")
        lat_arr_model.append(float(lat_spl[0]) + float(lat_spl[1]) / 60.0 + float(lat_spl[2]) / 3600.0)
        h_arr_model.append(float(line[2]))
    inter = LinearNDInterpolator(list(zip(lon_arr_model, lat_arr_model)), h_arr_model)
    h_iter = [inter(i[0], i[1]).item() for i in lines_track]  # if (i[0] > 0.0) and (i[0] < 100.0)]
    lst1 = [i[0] for i in lines_track]
    lst2 = [i[1] for i in lines_track]
    print(1)
    with open('Track_iter.csv', 'w') as fw:
        fw.write(f"{','.join(['Latitude_deg', 'Longitude_deg', 'Height_dtu_m'])}\n")
        for i, j in zip(lines_track, h_iter):
            fw.write(f'{i[0]},{i[1]},{j}\n')

    #data = dict(Latitude_deg=lst1, Longitude_deg=lst2, Height_dtu_m=lst3)
    #df = pd.DataFrame(data)
    #df.to_csv('Inter_track.csv', sep=',', index=False)
