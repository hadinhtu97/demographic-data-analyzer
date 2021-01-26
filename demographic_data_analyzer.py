import pandas as pd


def calculate_demographic_data():
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    print('Race count:\n', race_count)

    # What is the average age of men?
    average_age_men = df['age'].mean()
    print('Average age of men: ', average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    a = df['education'].value_counts()
    percentage_bachelors = a['Bachelors'] / len(df) * 100
    print('Percentage of people who have a Bachelor degree: ', percentage_bachelors)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    a = df['education'].value_counts()
    higher_education = (a['Bachelors'] + a['Masters'] +
                        a['Doctorate']) / len(df) * 100
    lower_education = 100 - higher_education
    print('Percentage of people with advanced education:', higher_education)
    print('Percentage of people without advanced education:', lower_education)

    # percentage with salary >50K
    a = df.loc[df['salary'] == '>50K', ['education']].value_counts()
    higher_education_rich = (
        a['Bachelors'] + a['Masters'] + a['Doctorate']) / len(df) * 100
    lower_education_rich = (
        a.sum() - a['Bachelors'] - a['Masters'] - a['Doctorate']) / len(df) * 100
    print('Percentage of people with advanced education and make more than 50K:',
          higher_education_rich)
    print('Percentage of people without advanced education and make more than 50K:',
          lower_education_rich)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    print('Minimum number of hours a person works per week:', min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    a = df[df['salary'] == '>50K']
    num_min_workers = df['hours-per-week'].value_counts()[1]
    rich_percentage = num_min_workers / len(a) * 100
    print('Number of people who work the minimum number of hours per week: ', num_min_workers)
    print('Percentage of the people who work the minimum number of hours per week have a salary of >50K: ', rich_percentage)

    # What country has the highest percentage of people that earn >50K?
    a = df.loc[df['salary'] == '>50K', ['native-country']].value_counts()
    highest_earning_country = a.index[0][0]
    highest_earning_country_percentage = a.iloc[0] / a.sum() * 100
    print('Country has the highest percentage of people that earn >50K:',
          highest_earning_country)
    print('Percentage of country has the highest percentage of people that earn >50K:',
          highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
    a = df.loc[(df['salary'] == '>50K') &
               (df['native-country'] == 'India'), ['occupation']].value_counts()
    top_IN_occupation = a.index[0][0]
    print('The most popular occupation for those who earn >50K in India: ',
          top_IN_occupation)
