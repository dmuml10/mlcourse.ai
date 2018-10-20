import pandas as pd
import statistics

PATH = '../data/athlete_events.csv'

#1. How old were the youngest male and female participants of the 1996 Olympics?
def youngest_participants():
    data = pd.read_csv(PATH)
    male = data.query('Year == 1996').query("Sex == 'M'").get('Age').min()
    female = data.query('Year == 1996').query("Sex == 'F'").get('Age').min()
    print(male)
    print(female)

#2. What was the percentage of male gymnasts among all the male participants of the 2000 Olympics? Round the answer to the first decimal.
def male_gymnasts_percentage():
    data = pd.read_csv(PATH)
    maleTotal = data.query('Year == 2000').query("Sex == 'M'")
    maleGymnasts = maleTotal.query('Sport == "Gymnastics"')
    maleTotal = maleTotal.shape[0]
    maleGymnasts = maleGymnasts.shape[0]
    print(maleGymnasts * 100 / maleTotal)

#3. What are the mean and standard deviation of height for female basketball players participated in the 2000 Olympics? Round the answer to the first decimal.
def mean_and_standard_dev():
    players = data = pd.read_csv(PATH).query('Year == 2000').query("Sex == 'F'").query('Sport == "Basketball"')
    mean = players.sum().get('Height')
    print(mean/players.shape[0])

    list = players['Height'].tolist()
    print(statistics.stdev(list))

#4. Find a sportsperson participated in the 2002 Olympics, with the highest weight among other participants of the same Olympics. What sport did he or she do?
def max_weight():
    data = pd.read_csv(PATH)
    data = data.query('Year == 2002')
    print(data[data['Weight'] == data.get('Weight').max()])

#5. How many times did Pawe Abratkiewicz participate in the Olympics held in different years?
def num_participate():
    data = pd.read_csv(PATH)
    data = data.query('Name == "Pawe Abratkiewicz"')
    data = data.drop_duplicates('Year')
    print(data.shape[0])

#6. How many silver medals in tennis did Australia win at the 2000 Olympics?
def australia_wins():
    data = pd.read_csv(PATH)
    data = data.query('Year == 2000').query('Medal == "Silver"').query('Team == "Australia"').query('Sport == "Tennis"').shape[0]
    print(data)

#7. Is it true that Switzerland won fewer medals than Serbia at the 2016 Olympics? Do not consider NaN values in Medal column. *
def switzerland_vs_serbia():
    data = pd.read_csv(PATH)
    data = data.query('Year == 2016')
    sw = data.query('Team == "Switzerland"').query('Medal != "Nan"').shape[0]
    sr = data.query('Team == "Serbia"').query('Medal != "Nan"').shape[0]
    print(sw)
    print(sr)

#8. What age category did the fewest and the most participants of the 2014 Olympics belong to? *
def age_category():
    data = pd.read_csv(PATH)
    data = data.query('Year == 2014')
    young = data.query('Age >= 25 and Age <35').shape[0]
    print(young)

#9. Is it true that there were Summer Olympics held in Lake Placid? Is it true that there were Winter Olympics held in Sankt Moritz? *
def winter_summer_olympics():
    data = pd.read_csv(PATH)
    sum = data.query('Season == "Summer"').query('City == "Lake Placid"')
    win = data.query('Season == "Winter"').query('City == "Sankt Moritz"')
    print(sum)
    print(win)

#10. What is the absolute difference between the number of unique sports at the 1995 Olympics and 2016 Olympics? *
def unique_sport_difference():
    data = pd.read_csv(PATH)
    old = data.query('Year == 1996').drop_duplicates('Sport').shape[0]
    new = data.query('Year == 2016').drop_duplicates('Sport').shape[0]
    print(old)
    print(new)
