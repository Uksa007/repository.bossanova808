# -*- coding: utf-8 -*- 
import xbmc

DAYS = { "Mon": xbmc.getLocalizedString( 11 ),
         "Tue": xbmc.getLocalizedString( 12 ),
         "Wed": xbmc.getLocalizedString( 13 ),
         "Thu": xbmc.getLocalizedString( 14 ),
         "Fri": xbmc.getLocalizedString( 15 ),
         "Sat": xbmc.getLocalizedString( 16 ),
         "Sun": xbmc.getLocalizedString( 17 )}

WEATHER_CODES = { 'Clearing shower'                 : '11',
                  'Cloudy'                          : '26',
                  'Cloud and wind increasing'       : '23',
                  'Cloud increasing'                : '26',
                  'Drizzle'                         : '11',
                  'Drizzle clearing'                : '32',
                  'Fog then sunny'                  : '20',
                  'Frost then sunny'                : '28',
                  'Hazy'                            : '21',
                  'Heavy rain'                      : '40',
                  'Heavy showers'                   : '12',
                  'Increasing sunshine'             : '32',
                  'Late shower'                     : '11',
                  'Late thunder'                    : '00',
                  'Mostly cloudy'                   : '26',
                  'Mostly sunny'                    : '30',
                  'Overcast'                        : '26',
                  'Possible shower'                 : '11',
                  'Possible thunderstorm'           : '37',
                  'Rain'                            : '40',
                  'Rain and snow'                   : '05',
                  'Rain clearing'                   : '39',
                  'Rain developing'                 : '12',
                  'Rain tending to snow'            : '05',
                  'Showers'                         : '11',
                  'Showers easing'                  : '11',
                  'Showers increasing'              : '11',
                  'Snow'                            : '41',
                  'Snowfalls clearing'              : '05',
                  'Snow develping'                  : '41',
                  'Snow showers'                    : '41',
                  'Snow tending to rain'            : '05',
                  'Sunny'                           : '32',
                  'Thunderstorms'                   : '38',
                  'Thunderstorms clearing'          : '37',
                  'Windy'                           : '23',
                  'Windy with rain'                 : '12',
                  'Windy with showers'              : '23',
                  'Windy with snow'                 : '13',
                  'Wind and rain increasing'        : '12',
                  'Wind and showers easing'         : '23',                                 
                  'Unknown'                         : 'na',
                  'nt_unknown'                      : 'na'}

"""   These are the weather codes fro XBMC is seems               
N/A Not Available
00 Rain/Lightning
01 Windy/Rain
02 Same as 01
03 Same as 00
04 Same as 00
05 Cloudy/Snow-Rain Mix
06 Hail
07 Icy/Clouds Rain-Snow
08 Icy/Haze Rain
09 Haze/Rain
10 Icy/Rain
11 Light Rain
12 Moderate Rain
13 Cloudy/Flurries
14 Same as 13
15 Flurries
16 Same as 13
17 Same as 00
18 Same as 00
19 Dust
20 Fog
21 Haze
22 Smoke
23 Windy
24 Same as 23
25 Frigid
26 Mostly Cloudy
27 Mostly Cloudy/Night
28 Mostly Cloudy/Sunny
29 Partly Cloudy/Night
30 Partly Cloudy/Day
31 Clear/Night
32 Clear/Day
33 Hazy/Night
34 Hazy/Day
35 Same as 00
36 Hot!
37 Lightning/Day
38 Lightning
39 Rain/Day
40 Rain
41 Snow
42 Same as 41
43 Windy/Snow
44 Same as 30
45 Rain/Night
46 Snow/Night
47 Thunder Showers/Night 
"""