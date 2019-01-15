import csv
import os

import guessit
import pymediainfo


def movie_index_results(username_input):
    movie_index = csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/UPDATES-TO-MOVIE-FILES-INDEX.csv'))
    movie_index_file_results = []

    for movie_file in movie_index:

        title = guessit.guessit(movie_file[0].rsplit('/', 1)[-1], options={'type': 'movie'})

        title_and_year = (movie_file[0].rsplit('/')[-2])

        mv_year = (title_and_year[-5:-1])

        mv_title = (title_and_year[0:-7])

        test = pymediainfo.MediaInfo.parse(movie_file[0])

        for track in test.tracks:

            if track.track_type == 'Video':
                movie_index_file_results.append(
                    [title.get('title'), title.get('year'), str(track.width) + 'x' + str(track.height),
                     title.get('container')])

    with open(r'/home/' + username_input + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', "a", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_index_file_results:
            csv_writer.writerow(movie_row)


def tv_show_index_results(username_input):
    tv_index = csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/UPDATES-TO-TV-FILES-INDEX.csv'))
    tv_index_file_results = []

    for tv_file in tv_index:

        title = guessit.guessit(tv_file[0].rsplit('/', 1)[-1], options={'type': 'episode'})

        title_and_year = (tv_file[0].rsplit('/')[-2])

        tv_year = (title_and_year[-5:-1])

        tv_title = (title_and_year[0:-7])

        test = pymediainfo.MediaInfo.parse(tv_file[0])

        for track in test.tracks:

            if track.track_type == 'Video':
                tv_index_file_results.append(
                    [title_and_year, title.get('title'), title.get('episode_title'), title.get('season'),
                     title.get('episode'), title.get('year'), str(track.width) + 'x' + str(track.height),
                     title.get('container')])

    with open(r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-RESULTS.csv', "a", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_index_file_results:
            csv_writer.writerow(tv_row)


def re_sort_csv_indices(username_input):
    movie_results = csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', "r"))
    sorted_movie_results = sorted(movie_results, key=lambda row: row[0])
    tv_results = csv.reader(open(r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-RESULTS.csv', "r"))
    sorted_tv_results = sorted(tv_results, key=lambda row: row[0])
    movie_results_file = []
    tv_results_file = []

    for line in sorted_movie_results:
        movie_results_file.append(line)

    with open(r'/home/' + username_input + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv', "w", newline="") as f:
        csv_writer = csv.writer(f)
        for movie_row in movie_results_file:
            csv_writer.writerow(movie_row)

    for line in sorted_tv_results:
        tv_results_file.append(line)

    with open(r'/home/' + username_input + '/MEDIA-INDEX/TV-FILES-RESULTS.csv', "w", newline="") as f:
        csv_writer = csv.writer(f)
        for tv_row in tv_results_file:
            csv_writer.writerow(tv_row)


def create_media_files_index_results_csv(username_input):
    movie_index_results(username_input)
    tv_show_index_results(username_input)
    re_sort_csv_indices(username_input)
    os.remove(r'/home/' + username_input + '/MEDIA-INDEX/OLD-MOVIE-FILES-INDEX.csv')
    os.remove(r'/home/' + username_input + '/MEDIA-INDEX/UPDATES-TO-MOVIE-FILES-INDEX.csv')
    os.remove(r'/home/' + username_input + '/MEDIA-INDEX/OLD-TV-FILES-INDEX.csv')
    os.remove(r'/home/' + username_input + '/MEDIA-INDEX/UPDATES-TO-TV-FILES-INDEX.csv')
