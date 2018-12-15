import os

import matplotlib.pylab as plt

movie_p_dir = os.listdir(r"/home/bx/Videos/CHASE/MOVIES/")
tv_p_dir = os.listdir(r"/home/bx/Videos/CHASE/TV/")

movie_years_range = range(1900, 2100, 1)
tv_show_years_range = range(1900, 2100, 1)

movie_years_dict = {}
tv_show_years_dict = {}

data = {1920: 1, 1922: 1, 1923: 1, 1925: 1, 1927: 2, 1930: 1, 1931: 5, 1932: 8, 1933: 4, 1934: 3,
        1935: 4, 1936: 4, 1937: 4, 1938: 1, 1939: 5, 1940: 9, 1941: 4, 1942: 6, 1943: 4, 1944: 5,
        1945: 1, 1946: 5, 1947: 2, 1948: 2, 1949: 4, 1950: 4, 1951: 6, 1952: 1, 1953: 7, 1954: 9,
        1955: 12, 1956: 8, 1957: 7, 1958: 7, 1959: 8, 1960: 6, 1961: 10, 1962: 9, 1963: 13,
        1964: 14, 1965: 14, 1966: 9, 1967: 16, 1968: 10, 1969: 14, 1970: 11, 1971: 18, 1972: 11,
        1973: 16, 1974: 9, 1975: 12, 1976: 16, 1977: 21, 1978: 21, 1979: 19, 1980: 30, 1981: 28,
        1982: 30, 1983: 39, 1984: 51, 1985: 50, 1986: 49, 1987: 52, 1988: 58, 1989: 56, 1990: 59,
        1991: 51, 1992: 61, 1993: 81, 1994: 73, 1995: 79, 1996: 77, 1997: 73, 1998: 74, 1999: 79,
        2000: 75, 2001: 78, 2002: 71, 2003: 76, 2004: 84, 2005: 77, 2006: 110, 2007: 109, 2008: 137,
        2009: 130, 2010: 122, 2011: 125, 2012: 130, 2013: 181, 2014: 206, 2015: 236, 2016: 229,
        2017: 252, 2018: 240}


def get_movie_years_for_dict():
    for media_movie in movie_p_dir:
        media_movie_year = int(media_movie.strip()[-5:-1])
        if media_movie_year in movie_years_range:
            if media_movie_year not in movie_years_dict:
                movie_years_dict[media_movie_year] = []
            movie_years_dict[media_movie_year].append(media_movie)
    media_movie_year_totals = {}
    for movie_year_values, value in sorted(movie_years_dict.items()):
        media_movie_year_totals[movie_year_values] = len(value)
    print(media_movie_year_totals)


get_movie_years_for_dict()
