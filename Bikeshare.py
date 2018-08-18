import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york.csv',
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
    while True:
        print('Would you like to see data for Chicago,New York or Washington?')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city=input()
        city=city.lower()
        if city in CITY_DATA:
            print('\ngrt so you chose',city,' as your city')
            break
        else:
            print('it was a wrong city,would you like to start it again?')
            que=input()
            if que.lower()!='yes':
                exit()
                
    print('\nenter the month from january to june for which you want to filter data:')
    month=input()
    month=month.lower()
    print('\nenter the day for which you want to filter data:')
    day=input()
    day=day.lower()
        
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
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    #filteration of data by month
    while True:
        if month!='all':
            months=['january','february','march','april','may','june']
            if month in months:
                month=months.index(month)+1
                df=df[df['month']==month]
                break
            else:
                print('it was a wrong month,would you like to start it again?')
                que=input()
                if que.lower()=='yes':
                    city,month,day=get_filters()
                elif que.lower()!='yes':
                    exit()
          
     #filteration of data by day of week
    while True:
        if day!='all':
            days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
            if day in days:
                df=df[df['day_of_week']==day.title()]
                break
            else:
                print('it was a wrong day of week,would you like to start it again?')
            que=input()
            if que.lower()=='yes':
                city,month,day=get_filters()
            elif que.lower()!='yes':
                
                exit()
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
     
    # display the most common month
    print('The most common month for travelling is:')
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    common_month=df['month'].mode()[0]
    if common_month==1:
        print('january')
    elif common_month==2:
        print('february')
    elif common_month==3:
        print('march')
    elif common_month==4:
        print('april')
    elif common_month==5:
        print('may')
    elif common_month==6:
        print('june')
    
    # display the most common day of week
   # print('/nmost common day of week is:')
    df['day_of_week']=df['Start Time'].dt.dayofweek
    common_day=df['day_of_week'].mode()[0]
    if common_day==0:
        print('\nthe most common day of week is:monday')
    elif common_day==1:
        print('\nthe most common day of week is:tuesday')
    elif common_day==2:
        print('\nthe most common day of week is:wednesday')
    elif common_day==3:
        print('\nthe most common day of week is:thursday')
    elif common_day==4:
        print('\nthe most common day of week is:friday')
    elif common_day==5:
        print('\nthe most common day of week is:saturday')
    elif common_day==6:
        print('\nthe most common day of week is:sunday')

    # display the most common start hour
    df['start_hour']=df['Start Time'].dt.dayofweek
    common_hour=df['start_hour'].mode()[0]
    print('\nthe most common start hour is:',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('Most Frequent Start Hour:',popular_hour)
    # TO DO: display most commonly used start station
    popular_station=df['Start Station'].mode()[0]
    print('\nMost Coomonly Used Start Station:',popular_station)


    # TO DO: display most commonly used end station
    end_station=df['End Station'].mode()[0]
    
    print('\nMost Coomonly Used End Station:',end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    print(df['Trip Duration'].describe())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Count of User Types is:')
    user_types=df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    print('\nCount of Gender Type is:')
    if 'Gender' in df.columns: 
        gender_types=df['Gender'].value_counts()
        print(gender_types)
    else:
       print('none')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        common_birth=int(df['Birth Year'].mode()[0])
        print('Most common year of birth is :',common_birth)
        ear=int(df['Birth Year'].min())
        print('earliest year of birth:',ear)      
        ear_max=int(df['Birth Year'].max())
        print('most recent year of birth:',ear_max)
    else:
        print('no data to show')
    
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
