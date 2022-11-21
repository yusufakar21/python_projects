import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        try:
            city=input("Please enter one of the following cities: Chicago, New York City, Washington \n").lower()
            if city in list(CITY_DATA.keys()):
                break
            error
        except:
            print()
            print()
            print('Please make sure you write the city name correct.')
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month=input("If you want to filter by month, please write name of the month. Otherwise write 'all'. \n").lower()
            if month in ['all','january', 'february', 'march', 'april', 'may', 'june']:
                break
            error
        except:
            print()
            print()
            print('Please make sure you write the month name correct or it is a month between January and June.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day=input("If you want to filter by day, please write name of the day. Otherwise write 'all'. \n").lower()
            if day in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']:
                break
            error
        except:
            print()
            print()
            print('Please make sure you write the day name correct.')

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months=['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month=df['month'].mode()[0]
    print('The most common month is {}.'.format(months[most_common_month-1].title()))

    # TO DO: display the most common day of week
    most_common_dow=df['day_of_week'].mode()[0]
    print('The most common day of week is {}.'.format(most_common_dow))

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_common_hour=df['hour'].mode()[0]
    print('The most common start hour is {}:00.'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_starts=df['Start Station'].mode()[0]
    print('The most common start station is {}.'.format(most_common_starts))

    # TO DO: display most commonly used end station
    most_common_ends=df['End Station'].mode()[0]
    print('The most common end station is {}.'.format(most_common_ends))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station'] + ',' + df['End Station']
    most_common_combination=df['combination'].mode()[0]
    print('The most common combination of stations is {}.'.format(most_common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_seconds=df['Trip Duration'].sum()
    hr=int(total_seconds/3600)
    mnt=int((total_seconds%3600)/60)
    sc=(total_seconds%3600)%60
    print('Total travel time is {} hours {} minutes {} seconds.'.format(hr,mnt,sc))

    # TO DO: display mean travel time
    mean_seconds=df['Trip Duration'].mean()
    hr=int(mean_seconds/3600)
    mnt=int((mean_seconds%3600)/60)
    sc=int((mean_seconds%3600)%60)
    print('Average travel time is {} hours {} minutes {} seconds.'.format(hr,mnt,sc))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    info_list=[]
    for i in df['User Type'].unique()[:2]:
        info_list.append((df['User Type']==i).sum())
        info_list.append(i)
    a,b,c,d=tuple(info_list)
    print('There are {} {} and {} {} user types.'.format(a,b,c,d)) 

    # TO DO: Display counts of gender
    try:
        info_list=[]
        for i in df['Gender'].unique()[:2]:
            info_list.append((df['Gender']==i).sum())
            info_list.append(i)
        a,b,c,d=tuple(info_list)
        print('There are {} {} and {} {} users.'.format(a,b,c,d))
    except:
        print('Sorry! We do not have gender info for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The earliest birth year is {}.'.format(str(int(df['Birth Year'].min()))))
        print('The most recent birth year is {}.'.format(str(int(df['Birth Year'].max()))))
        print('The most common birth year is {}.'.format(str(int(df['Birth Year'].mode()[0]))))
    except:
        print('Sorry! We do not have birth year info for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    
    user_answer=input("Do you want to see the first 5 rows of data? Please enter yes or no.\n").lower()
    start_loc = 0

    while user_answer=='yes':
        print(df.iloc[df.index[start_loc:start_loc+5]])
        start_loc += 5
        user_answer = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
