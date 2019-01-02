import csv

import pymediainfo

tv_index = csv.reader(list(open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-INDEX-TEST.csv")))
test = pymediainfo.MediaInfo.parse(
    r"/home/bx/Videos/TEST/Honest Trailers (2012)/Honest Trailers - 801 - Venom.mp4")


def scrape_file_info_from_list():
    tv_file_results = []

    for track in test.tracks:
        tv_file_results.append([track.sampled_width]+[track.sampled_height])

    with open(r"/home/bx/PycharmProjects/B-MEDIA-INDEX/FILES/TV-FILES-RESULTS-TEST.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_file_results:
            csv_writer.writerow(tv_row)


scrape_file_info_from_list()
