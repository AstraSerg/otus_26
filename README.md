# otus_26
## Analilze set Netflix TV Shows and Movies.csv from kaggle 

Results:

```
2025-07-16 22:09:35.798 $ ./numpy_analize.py
--------------------------------------------------------------------------------
Columns in dataset:
Index(['index', 'id', 'title', 'type', 'description', 'release_year',
       'age_certification', 'runtime', 'imdb_id', 'imdb_score', 'imdb_votes'],
      dtype='object')
--------------------------------------------------------------------------------
Sample of data:
   index        id                            title   type                                        description  release_year age_certification  runtime    imdb_id  imdb_score  imdb_votes
0      0   tm84618                      Taxi Driver  MOVIE  A mentally unstable Vietnam War veteran works ...          1976                 R      113  tt0075314         8.3    795222.0
1      1  tm127384  Monty Python and the Holy Grail  MOVIE  King Arthur, accompanied by his squire, recrui...          1975                PG       91  tt0071853         8.2    530877.0
2      2   tm70993                    Life of Brian  MOVIE  Brian Cohen is an average young Jewish man, bu...          1979                 R       94  tt0079470         8.0    392419.0
3      3  tm190788                     The Exorcist  MOVIE  12-year-old Regan MacNeil begins to adapt an e...          1973                 R      133  tt0070047         8.1    391942.0
4      4   ts22164     Monty Python's Flying Circus   SHOW  A British sketch comedy series with the shows ...          1969             TV-14       30  tt0063929         8.8     72895.0
--------------------------------------------------------------------------------
Unvoted shows:
ID: tm144046, Title: Jackass Presents: Bad Grandpa .5
ID: tm163066, Title: Xenos
ID: tm995893, Title: The Crossing
ID: tm826563, Title: A Cinderella Story: Christmas Wish
ID: tm835869, Title: Jarhead: Law of Return
ID: tm931436, Title: Welcome to Sudden Death
ID: tm1172010, Title: The Lockdown Plan
ID: tm984018, Title: Cops and Robbers
ID: tm1113921, Title: In Vitro
ID: tm1039147, Title: Audible
ID: tm1096769, Title: Lead Me Home
ID: tm1040688, Title: Three Songs for Benazir
ID: tm1159301, Title: Forgive Us Our Trespasses
ID: tm1119455, Title: Camp Confidential: America's Secret Nazis
ID: tm1161223, Title: Cat Burglar
ID: tm1108010, Title: Rabbids Invasion - Mission To Mars
Count: 16
--------------------------------------------------------------------------------
Top voted shows:
ID: ts160526, Title: Khawatir, IMDb Score: 9.6, Votes: 3046.0
ID: ts265844, Title: #ABtalks, IMDb Score: 9.6, Votes: 7.0
ID: ts4, Title: Breaking Bad, IMDb Score: 9.5, Votes: 1727694.0
ID: ts3371, Title: Avatar: The Last Airbender, IMDb Score: 9.3, Votes: 297336.0
ID: ts90621, Title: Kota Factory, IMDb Score: 9.3, Votes: 66985.0
ID: ts85398, Title: Our Planet, IMDb Score: 9.3, Votes: 41386.0
ID: ts37660, Title: Reply 1988, IMDb Score: 9.2, Votes: 6557.0
ID: ts78298, Title: My Mister, IMDb Score: 9.2, Votes: 5481.0
ID: ts296563, Title: Who Rules The World, IMDb Score: 9.2, Votes: 81.0
ID: ts222333, Title: Arcane, IMDb Score: 9.1, Votes: 175412.0
ID: ts81120, Title: The Last Dance, IMDb Score: 9.1, Votes: 108321.0
ID: ts20682, Title: Attack on Titan, IMDb Score: 9.0, Votes: 325381.0
ID: ts11313, Title: DEATH NOTE, IMDb Score: 9.0, Votes: 302147.0
ID: ts32835, Title: Hunter x Hunter, IMDb Score: 9.0, Votes: 87857.0
ID: tm853783, Title: David Attenborough: A Life on Our Planet, IMDb Score: 9.0, Votes: 31180.0
ID: tm432327, Title: C/o Kancharapalem, IMDb Score: 9.0, Votes: 6562.0
ID: ts52922, Title: Leah Remini: Scientology and the Aftermath, IMDb Score: 9.0, Votes: 5761.0
ID: ts28516, Title: Okupas, IMDb Score: 9.0, Votes: 2326.0
ID: tm76557, Title: No Longer Kids, IMDb Score: 9.0, Votes: 943.0
ID: ts121189, Title: Raja, Rasoi Aur Anya Kahaniyaan, IMDb Score: 9.0, Votes: 327.0
--------------------------------------------------------------------------------
Top 10 shows by type:

--- Top 10 MOVIEs by IMDb Score and Votes ---
       id                                    title  imdb_score  imdb_votes
 tm853783 David Attenborough: A Life on Our Planet         9.0     31180.0
 tm432327                        C/o Kancharapalem         9.0      6562.0
  tm76557                           No Longer Kids         9.0       943.0
 tm166740     Chhota Bheem & Krishna in Mayanagari         9.0         5.0
  tm92641                                Inception         8.8   2268288.0
 tm122434                             Forrest Gump         8.8   1994599.0
 tm907872                      Sky Tour: The Movie         8.8      1036.0
tm1038686                       Bo Burnham: Inside         8.7     44074.0
 tm129763                               Anbe Sivam         8.7     20595.0
 tm455981                            Rubaru Roshni         8.7       584.0

--- Top 10 SHOWs by IMDb Score and Votes ---
      id                      title  imdb_score  imdb_votes
ts160526                   Khawatir         9.6      3046.0
ts265844                   #ABtalks         9.6         7.0
     ts4               Breaking Bad         9.5   1727694.0
  ts3371 Avatar: The Last Airbender         9.3    297336.0
 ts90621               Kota Factory         9.3     66985.0
 ts85398                 Our Planet         9.3     41386.0
 ts37660                 Reply 1988         9.2      6557.0
 ts78298                  My Mister         9.2      5481.0
ts296563        Who Rules The World         9.2        81.0
ts222333                     Arcane         9.1    175412.0
--------------------------------------------------------------------------------
The most productiev years:

--- Top 10 Years by Number of Releases ---
 Year  Count of Releases
 2019                749
 2018                733
 2021                687
 2020                657
 2017                555
 2016                351
 2015                226
 2022                182
 2014                151
 2013                134

```
