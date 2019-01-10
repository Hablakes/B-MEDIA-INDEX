import csv

extensions = (".3gp", ".asf", ".asx", ".avc", ".avi", ".bdmv", ".bin", ".bivx", ".dat", ".disc", ".divx", ".dv",
              ".dvr-ms", ".evo", ".fli", ".flv", ".h264", ".img", ".iso", ".m2ts", ".m2v", ".m4v", ".mkv", ".mov",
              ".mp4", ".mpeg", ".mpg", ".mt2s", ".mts", ".nrg", ".nsv", ".nuv", ".ogm", ".pva", ".qt", ".rm", ".rmvb",
              ".srt", ".strm", ".svq3", ".ts", ".ty", ".viv", ".vob", ".vp3", ".wmv", ".xvid", ".webm")

years_range = range(1900, 2100, 1)
movie_string = str("MOVIE")
tv_string = str("TV")

username_input = [input("ENTER YOUR USERNAME (CASE-SENSITIVE):")]


def movie_files_info_query():
    movie_files_results_list = list(
        csv.reader(open(r'/home/' + username_input[0] + '/MEDIA-INDEX/MOVIE-FILES-RESULTS.csv')))
    mv_query_action = input("ENTER SEARCH QUERY (MOVIES):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    mv_query_action_lower = str(mv_query_action.lower())
    for movie_file in sorted(movie_files_results_list):
        if mv_query_action_lower in movie_file[0].lower():
            print()
            print("MOVIE TITLE:")
            print(movie_file[0])
            print()
            print("MOVIE YEAR:")
            print(movie_file[1])
            print()
            print("MOVIE RESOLUTION:")
            print(movie_file[2])
            print()
            print("MOVIE FILE TYPE:")
            print(movie_file[3])
            print()
            print()
            print("--------------------------------------------------------------------------------------------------")


def tv_files_info_query():
    tv_files_results_list = list(csv.reader(open(r'/home/' + username_input[0] + '/MEDIA-INDEX/TV-FILES-RESULTS.csv')))
    tv_show_query_action = input("ENTER SEARCH QUERY (TV SHOWS):")
    print()
    print("--------------------------------------------------------------------------------------------------")
    print()
    tv_show_query_action_lower = str(tv_show_query_action.lower())
    for tv_file in sorted(tv_files_results_list):
        if tv_show_query_action_lower in tv_file[0].lower():
            print()
            print("TV SHOW TITLE:")
            print(tv_file[0])
            print()
            print("TV SHOW EPISODE TITLE:")
            print(tv_file[1])
            print()
            print("TV SHOW SEASON #:")
            print(tv_file[2])
            print()
            print("TV SHOW EPISODE #:")
            print(tv_file[3])
            print()
            print("TV SHOW YEAR:")
            print(tv_file[4])
            print()
            print("TV SHOW RESOLUTION:")
            print(tv_file[5])
            print()
            print("TV SHOW FILE-TYPE:")
            print(tv_file[6])
            print()
            print()
            print("--------------------------------------------------------------------------------------------------")

        elif tv_show_query_action_lower in tv_file[1].lower():
            print()
            print("TV SHOW TITLE:")
            print(tv_file[0])
            print()
            print("TV SHOW EPISODE TITLE:")
            print(tv_file[1])
            print()
            print("TV SHOW SEASON #:")
            print(tv_file[2])
            print()
            print("TV SHOW EPISODE #:")
            print(tv_file[3])
            print()
            print("TV SHOW YEAR:")
            print(tv_file[4])
            print()
            print("TV SHOW RESOLUTION:")
            print(tv_file[5])
            print()
            print("TV SHOW FILE-TYPE:")
            print(tv_file[6])
            print()
            print()
            print("--------------------------------------------------------------------------------------------------")


movie_files_info_query()
tv_files_info_query()
