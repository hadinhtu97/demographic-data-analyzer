import pandas as pd


def calculate_demographic_data():
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()
    print('Race count:\n', race_count)

    average_age_men = df['age'].mean()
    print('Average age of men: ', average_age_men)

    a = df['education'].value_counts()
    percentage_bachelors = a['Bachelors'] / len(df) * 100
    print('Percentage of people who have a Bachelor degree: ', percentage_bachelors)


    a = df['education'].value_counts()
    higher_education = (a['Bachelors'] + a['Masters'] +
                        a['Doctorate']) / len(df) * 100
    lower_education = 100 - higher_education
    print('Percentage of people with advanced education:', higher_education)
    print('Percentage of people without advanced education:', lower_education)

    a = df.loc[df['salary'] == '>50K', ['education']].value_counts()
    higher_education_rich = (
        a['Bachelors'] + a['Masters'] + a['Doctorate']) / len(df) * 100
    lower_education_rich = (
        a.sum() - a['Bachelors'] - a['Masters'] - a['Doctorate']) / len(df) * 100
    print('Percentage of people with advanced education and make more than 50K:',
          higher_education_rich)
    print('Percentage of people without advanced education and make more than 50K:',
          lower_education_rich)

    min_work_hours = df['hours-per-week'].min()
    print('Minimum number of hours a person works per week:', min_work_hours)

    a = df[df['salary'] == '>50K']
    num_min_workers = df['hours-per-week'].value_counts()[1]
    rich_percentage = num_min_workers / len(a) * 100
    print('Number of people who work the minimum number of hours per week: ', num_min_workers)
    print('Percentage of the people who work the minimum number of hours per week have a salary of >50K: ', rich_percentage)

    a = df.loc[df['salary'] == '>50K', ['native-country']].value_counts()
    highest_earning_country = a.index[0][0]
    highest_earning_country_percentage = a.iloc[0] / a.sum() * 100
    print('Country has the highest percentage of people that earn >50K:',
          highest_earning_country)
    print('Percentage of country has the highest percentage of people that earn >50K:',
          highest_earning_country_percentage)

    a = df.loc[(df['salary'] == '>50K') &
               (df['native-country'] == 'India'), ['occupation']].value_counts()
    top_IN_occupation = a.index[0][0]
    print('The most popular occupation for those who earn >50K in India: ',
          top_IN_occupation)
