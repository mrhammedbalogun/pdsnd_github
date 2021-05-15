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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please choose a city. Eg chicago, new york city or washington: ").lower()
    while city not in ["chicago", "new york city", "washington"]:
        city = input("Please choose a city in the right format. Eg chicago, new york city or washington: ")


    # get user input for month (all, january, february, march... , june)
    month = input("Please choose a month. Eg all, january, february, ... , june: ").lower()
    while month not in ["all", "january", "february", "march", "april", "may", "june"]:
        city = input("Please choose a month in the right format. Eg all, january, february, march, april, may, june: ")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please choose a day. Eg all, monday, tuesday, ... sunday: ").lower()
    while day not in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        city = input("Please choose a day in the right format. Eg all, monday, tuesday, wednesday, thursday, friday, saturday, sunday: ")


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

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

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month is {}'.format(common_month))


    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day is {}'.format(common_day))


    # display the most common start hour
    start_hour = df['Start Time'].dt.hour.mode()[0] #df['hour'].mode()[0]
    print('Most common start hour is {}'.format(start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station is {}'.format(common_start_station))


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station is {}'.format(common_end_station))


    # display most frequent combination of start station and end station trip
    df['S_E Combination'] = (df['Start Station'] + ' - ' + df['End Station'])
    
    common_combination = str(df['S_E Combination'].mode()[0])
    print('Most frequent combination of start station and end station trip is: {}'.format(common_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    total_travelTime = df['Trip Duration'].sum()
    total_travelTime = (str(int(total_travelTime//86400)) + 'd ' + str(int((total_travelTime % 86400)//3600)) + 'h ' + str(int(((total_travelTime % 86400) % 3600)//60)) +
                         'm ' + str(int(((total_travelTime % 86400) % 3600) % 60)) + 's')

    print('Total travel time is: {}'.format(total_travelTime))


    # display mean travel time
    mean_travelTime = df['Trip Duration'].mean()
    mean_travelTime = (str(int(mean_travelTime//60)) + 'm ' +
                        str(int(mean_travelTime % 60)) + 's')
    print('Mean travel time is {}'.format(mean_travelTime))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts().to_string()
    print('User type count: \n{}\n'.format(count_user_type))


    # Display counts of gender
    
    try:
        genderCount = df['Gender'].value_counts().to_string()
        print('Gender count: \n{}'.format(genderCount))
    except:
        
        print("Gender count not available")
    


    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nEarliest year of birth: {}'.format(earliest_birth_year))
        print('Most recent year of birth: {}'.format(recent_birth_year))
        print('Most common year of birth: {}'.format(common_birth_year))
    except:
        print('\nYear of birth not available')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    
    raw_data_input_data = input("\nYou have selected to see individual raw data? Enter 'yes' or 'no'\n").strip().lower()    
    if raw_data_input_data in ("yes", "y"):
        i = 0

        while True: 
                                
            if (i + 5 > len(df.index) - 1):
                print(df.iloc[i:len(df.index), :])
                print("You've reached the end of the rows")
                break

            print(df.iloc[i:i+5, :])
            i += 5
            
            next_five_input = input("\nWould you like to see the next 5 rows? Enter 'yes' or 'no'\n").strip().lower()
            if next_five_input not in ("yes", "y"):
                break 




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        while True:
            select_data = input("\nPlease select the information you would like to obtain. Enter RD or PD\n\n [rd] Raw Data\n [pd] Processed Data\n\n\n>").lower()
                                 
            if select_data == 'rd':
                display_data(df)

                break
                
            elif select_data == 'pd':
                process_data = input("\nYou have selected to see PROCESSED DATA, which includes:\n\n\n- Time Statistics Data\n- Station Statistics Data\n- Trip Duration Statistics Data\n- Users Statistics Data\n\nEnter 'yes' to proceed, or 'no' to go back.\n\n\n>").strip().lower()    
                if process_data in ("yes", "y"):
                
                    time_stats(df)
                    station_stats(df)
                    trip_duration_stats(df)
                    user_stats(df)

                    break
            

        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
