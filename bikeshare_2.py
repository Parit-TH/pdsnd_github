import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Month = ('All','January', 'February', 'March', 'April', 'May', 'June') # Use tuple for constant value
Day = ('All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input ('Which city do you prefer to look in Chicago,New York City,Washington:' ).lower()# Config the input format
    while city not in CITY_DATA:
        print("The City's name is incorrect.")
        city = input('Please choose one of city in Chicago,New York City ,Washington: ')


    # get user input for month (all, january, february, ... , june)
    month = input ('Which month do you prefer to look in from january to june <if you prefer all of jan to jun type "all">: ').title()
    while month not in Month:
        print ("The Month's name is incorrect.")
        month = input('Plesae type month you prefer to look in: ').title() # Must use .title because .dt format
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ('Which day do you prefer to look  <if you prefer all type "all">: ').title()
    while day not in Day:
        print ("The Day's name is incorrect.")
        month = input('Plesae type day you prefer to look in: ').title()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df =pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.weekday_name
    if month != 'All': # Focus on filter effect
       df = df[df['month'] == month]
    if day != 'All':
       df = df[df['day'] == day]
    #print(df) #check data farme
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    mode_month = df['month'].mode()[0]
    print('The most common month is:'+mode_month)
    # display the most common day of week
    mode_day = df['day'].mode()[0]
    print('The most common day is:'+mode_day)

    # display the most common start hour
    mode_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common hour is:'+str(mode_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mode_start_station = df['Start Station'].mode() [0]
    print('The most comon used start station is: '+mode_start_station)

    # display most commonly used end station
    mode_end_station= df['End Station'].mode() [0]
    print('The most comon used end station is: '+mode_end_station)

    # display most frequent combination of start station and end station trip
    df['trip']=df['Start Station']+','+df['End Station']
    mode_start_end_station = df['trip'].mode()[0]
    print('The most comon used start and end  station is: '+mode_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df ['duration'] = df['End Time']-df['Start Time']
    # display total travel time
    total_duration = df['duration'].sum()
    print ('The total duration of trip is '+str(total_duration))

    # display mean travel time
    mean_duration =df['duration'].mean()
    print ('The mean duration of  trip is '+str(mean_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('Count of user types\n{}\n'.format(count_user_type))

    # Display counts of gender
    count_gender = df['Gender'].value_counts()
    print('Count of user gender\n{}\n'.format(count_gender))


    # Display earliest, most recent, and most common year of birth
    earliest_year_birth = df['Birth Year'].min()
    most_recent_year_birth = df['Birth Year'].max()
    most_common_year_birth =df['Birth Year'].mode()[0]
    print('The earliset,most recent and most common year of birth are {}, {},{}'
          .format(earliest_year_birth,most_recent_year_birth,most_common_year_birth))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
