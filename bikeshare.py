import time
import pandas as pd
import numpy as np
# loading the data files with csv extensions
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new_york_city, washington). HINT: Use a while loop to handle invalid inputs
    # Requesting user to select city for analysis
    while True:
        cities = ['chicago','new york city','washington']
        city = input("\n Which city you would like to filter for analysis from : (Chicago, New_York_City, Washington) \n").lower()
        if city in cities:
            break
        else: 
                print("\n Error!! Please enter a valid city name")
    # TO DO: get user input for month (all, january, february, ... , june)
    # Requesting user to input months (From January to June) or mention All to extract data for analysis
    while True:
        months = ['January' , 'February' , 'March' , 'April' , 'June', 'All']
        month = input("\n Which month you would like to filter for analysis from : (January, February, March, April, May, June) \n or Type 'All' for no month filter \n").title()
        if month in months:
            break
        else:
                print("\n Error!! Please enter a valid month")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Requesting user to input for day of the week (Monday to Sunday or input All if no day filter required)
    while True:
        days = ['Sunday' , 'Monday' , 'Tuesday', 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'All']
        day = input("\n Which day would you like to analyze? (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) \n Type 'All' for no day filter \n").title()
        if day in days:
            break
        else:
                print("\n Error!! Please enter a valid day")    
    print('-'*40)
    return city,month,day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # loading data file into dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extracting month, day of the week & hour from Start time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month only if applicable
    if month != 'All' and day == 'All':
        # use the index of months list for relevant integer
        months = ['January' , 'February' , 'March' , 'April' , 'May' , 'June']
        month = months.index(month)+1
        # filter by month only to create new dataframe
        df = df[df['month'] == month]
    #filter by day of the week only if applicable
    if day != 'All' and month == 'All':
        #filter by day of week to create the new dataframe
        df=df[df['day_of_week'] == day.title()]
       
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is : ', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\n The most common day of the week is : ', common_day)

    # TO DO: display the most common start hour
    print('\n The most common start hour is : ', df['hour'].mode()[0])

    print("\n This took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print ('\n Most Commonly used start station is : ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('\n The Most Commonly use End Station is : ', df['End Station'].mode()[0])
                        
    # TO DO: display most frequent combination of start station and end station trip
    combination_group = df.groupby(['Start Station','End Station'])
    most_frequent_combination = combination_group.size().sort_values(ascending=False).head(1)
    print('\n Most Frequent Combination of start and end station trip is : ', most_frequent_combination)

    print("\n This took %s seconds." % (time.time() - start_time))

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n Calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\n Total travel time is : ', df['Trip Duration'].sum(), 'seconds')

    # TO DO: display mean travel time
    print('\n Mean Travel time is : ', round(df['Trip Duration'].mean(), 1), 'seconds')

    print("\n This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\n Calculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n Count of user types is : ',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # Gender info data is not available for Washington City
    if city != 'washington':
        print('\n Total count per gender is :', df['Gender'].value_counts())
    
        # TO DO: Display earliest, most recent, and most common year of birth
        print('\n Earliest Year of Birth is : ', int(df['Birth Year'].min()))

        print('\n Most Recent Year of Birth is : ', int(df['Birth Year'].max()))

        print('\n Most Common Year of Birth is : ', int(df['Birth Year'].mode()[0]))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(df):
    row = 0
    while True:
        view_raw_data = input("Do you want to view raw data of 5 rows? \n Yes/No, please select \n").lower()
        if view_raw_data == "yes":
            print(df.iloc[row : row + 5])
            row += 5
        elif view_raw_data == "no":
            break
        else:
            print("\n Please enter either Yes or No \n")
def main():
    while True:
        city,month,day = get_filters()
        df = load_data(city,month,day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()