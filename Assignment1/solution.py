import pandas as pd

PATH = 'athlete_events.csv'

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
    return maleGymnasts * 100 / maleTotal
#3. What are the mean and standard deviation of height for female basketball players participated in the 2000 Olympics? Round the answer to the first decimal.
def mean_and_standard_dev():
    players = data = pd.read_csv(PATH).query('Year == 2000').query("Sex == 'F'").query('Sport == "Basketball"')
    mean = players.sum().get('Height')
    print(mean/players.shape[0])

    list = players['Height'].tolist()

mean_and_standard_dev()
