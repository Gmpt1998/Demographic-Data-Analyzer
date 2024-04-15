import pandas as pd


def calculate_demographic_data(print_data=True):
    #read data from file
    df = pd.read_csv('adult.data.csv')

    #how many of each race are represented in this dataset? this should be a pandas series with race names as the index lables.
    race_count = df['race'].value_counts()

    #what is the average of age of men
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    #what is the percentage of people who have a Bachelor's degree?
    percentage_bachelors =  (df['education'] == 'Bachelors').mean() * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors','Masters', 'Doctorate'])]
    higher_education_rich = (higher_education['salary'] == '>50K').mean() * 100

    # What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors','Masters', 'Doctorate'])]
    lower_education_rich = (lower_education['salary'] == '>50K').mean() * 100

     # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

     # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = (df[df['native-country'] == highest_earning_country]['salary'] == '>50K').mean() * 100 

    # Identify the most popular occupation for those who earn >50K in India.
    IN_occupation_stats = df[df['native-country'] == 'India']
    top_IN_occupation = IN_occupation_stats[IN_occupation_stats['salary'] == '>50K']['occupation'].mode()[0]

    #
    race_count = race_count.round(1)
    average_age_men = round(average_age_men, 1)
    percentage_bachelors = round(percentage_bachelors, 1)
    higher_education_rich = round(higher_education_rich, 1)
    lower_education_rich = round(lower_education_rich, 1)
    rich_percentage = round(rich_percentage, 1)
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
