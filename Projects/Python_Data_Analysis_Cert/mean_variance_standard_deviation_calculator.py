import pandas as pd

# Make Sure to round all calculations to the nearest tenth
def calculate_demographic_data(print_data=True):
  # Read data from file
  # age,workclass,fnlwgt,education,education-num,marital-status,occupation,relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,salary
  df = pd.read_csv('adult.data.csv', 
                  delimiter=','
                  )
  len_df = len(df)
  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts().sort_index()
  

  # What is the average age of men?
  average_age_men = round(df.groupby(['sex']).get_group('Male').mean()[0], 1)

  # What is the percentage of people who have a Bachelor's degree?
  sorted_education = df['education'].value_counts(sort=True).sort_index()
  percentage_bachelors = round(sorted_education[9]/df.shape[0]*100, 1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  len_higher_ed_Over_50 = len(df.loc[((df['education'] == 'Bachelors') & (df['salary'] == '>50K')) | ((df['education'] == 'Masters') & (df['salary'] == '>50K')) | ((df['education'] == 'Doctorate') & (df['salary'] == '>50K'))])
  len_higher_ed_un50 = len(df.loc[((df['education'] == 'Bachelors') & (df['salary'] == '<=50K')) | ((df['education'] == 'Masters') & (df['salary'] == '<=50K')) | ((df['education'] == 'Doctorate') & (df['salary'] == '<=50K'))])
  len_all_higher_ed = len_higher_ed_un50 + len_higher_ed_Over_50
  higher_education_rich = round(len_higher_ed_Over_50/len_all_higher_ed*100, 1)

  # What percentage of people without advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
  # **************************************************************************************************
  all_ed_over_50 = df.groupby('education')['salary'].apply(lambda x: x.str.contains('>50K').sort_index().sum()).sum()
  mask_miss   = ~df.loc[:, 'education'].str.contains('Bachelors')
  mask_mrs    = ~df.loc[:, 'education'].str.contains('Doctorate')
  mask_master = ~df.loc[:, 'education'].str.contains('Masters')
  fifty_K = ~df.loc[:, 'salary'].str.contains('<=50K')
  total_o_50_bad_ed = len(df.loc[mask_miss & mask_mrs & mask_master & fifty_K, ('education', 'salary')])
  lower_education_rich = round(total_o_50_bad_ed/len_df*100, 1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  hours_per_week = df['hours-per-week']
  min_work_hours = hours_per_week.min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  len_num_min_hours_over_50 = len(df.loc[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')])
  sum_work_1hr = len(df.loc[(df['hours-per-week'] == 1)])
  
  # Percentage of rich among those who work fewest hours
  rich_percentage = round(len_num_min_hours_over_50/sum_work_1hr*100, 1)
  

  # What country has the highest percentage of people that earn >50K?
  over_50_con = df.groupby("native-country", sort=False)["salary"].apply(lambda ser: ser.str.contains(">50K").sum()).nlargest()
  # nlargest just returns the number
  highest_earning_country = over_50_con.index[0]
  highest_earning_country_percentage = None

  # Identify the most popular occupation for those who earn >50K in India.
  finding_occupation_India = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
  finding_max_occ = df['occupation'].value_counts()
  top_IN_occupation = finding_max_occ.index[0] # need to slice it for answer

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