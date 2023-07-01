import time
import pandas as pd
import numpy as np
import datetime

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
    citys = ['chicago', 'new york city', 'washington']
    city=[]
    
    while city not in citys:
        print('What city (chicago, new york city, washington) are you interested in?')
        city_input = input("Insert your city name here:").lower()
        if city_input not in citys:
            print('Did you make a tipo? Your input is not valid.')
       
        else:
            city =  city_input
            
     # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    month=[]
    while month not in months:
        print('What month ((january, february, ... , june) write the full month name or *all*) are you      interested in?')
        month_input = input("Insert your month name here:").lower()
        if month_input not in months:
            print('Did you make a tipo? Your input is not valid.')
       
        else:
            month =  month_input
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    day=[]
    while day not in days:
        print('What day (pls. write the full day name) are you interested in?')
        day_input = input("Insert your day name here:").lower()
        if day_input not in days:
            print('Did you make a tipo? Your input is not valid.')
        else:
            day=day_input
            



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
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        #df_mask = df['col_name']=='specific_value'
        #filtered_df = df[df_mask]
        df = df[df['month']==month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month

    # find the most common month 
    popular_month = df['month'].mode()[0]
    
    print('The most popular month to travel is {}'.format(popular_month))


    # TO DO: display the most common day of week
    # extract day from the Start Time column to create an day column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # find the most common day 
    popular_day = df['day_of_week'].mode()[0]
    
    print('The most popular day to travel is {}'.format(popular_day))


    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour 
    popular_hour = df['hour'].mode()[0]
    
    print('The most popular hour to travel is {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    
    print('The most popular station to start the travel is: {}'.format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    
    print('The most popular station to end the travel is: {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df_1=pd.DataFrame(df['Start Station']+ [' to '] +df['End Station'],columns=['Start End Route'])
    df=df.append(df_1,sort=True)
    
    popular_route = df['Start End Route'].mode()[0]
    print('The most popular route is: {}'.format(popular_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total Travel time is: {} h and {}min.'.format(  ((total_travel_time/3600).astype(int)),( ( ((total_travel_time/3600)- ((total_travel_time/3600).astype(int)) )*60).astype(int))  )) # calculating full hours and minutes


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    print('The mean travel time is: {}min.'.format((mean_travel_time/60).astype(int))) # returning travel time mean in full min.


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('There are {} customers and there are {} Subscribers'. format(str(user_types['Customer']), str(user_types['Subscriber'])))

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    print('There are {} males and there are {} females'. format(gender_types['Male'],gender_types['Female']))


    # TO DO: Display earliest, most recent, and most common year of birth
    age_stats = df['Birth Year'].describe()
    print('The oldest user is born in {}, the younges user is born in {} and the average year of birth is {} '.format(age_stats['min'].astype(int), age_stats['max'].astype(int), age_stats['mean'].astype(int)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_request(counter,df):
    """ funktion checks if user wants to see (more) raw data and handles error input of user"""
    raw_data_answer = input('\nWould you like to see (more) raw data? Enter yes or no.\n')
    while raw_data_answer.lower() not in ['yes','no']:
        print('Did you make a typo?')
        raw_data_answer = input('\nWould you like to see (more) raw data? Enter yes or no.\n')
    if raw_data_answer.lower()=='yes':
        raw_data_display(counter,df)
        
    return raw_data_answer.lower() 

def raw_data_display(counter,df):
    """showing raw data to the user if he wants"""
    print('Here are 5 rows of raw data ')
    pd.set_option(“display.max_columns”,200)
    if (counter+1)*5< df.shape[0]:   #checking if enough rows are left to print something
        df_display=df.iloc[counter*5:((counter+1)*5),:]  # show following 5 rows
        print(df_display)
        counter+=1  # increas counter for next possible set if he wants to se more 
        raw_data_request(counter,df)
    elif(counter+1)*5-df.height()>0:  # if not enough rows left to show 5 new rows, showing rest
        rest=(counter+1)*5-df.height()
        print('last rows in raw data are displayed.')
        df_display=df.iloc[[couner*5,rest],:]
        print(df_display)
    else: # if no new rows left at all stop printing -backup
        stopper=True
        print('nothing to show anymore.')
        
def restart_func():
    #asking user for input to restart
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() == 'no':
        restart_user_inp=restart
        print('ok-stopping') # printing to inform user
       
    elif restart.lower() == 'yes':
        print('restart') #printing to inform user
        restart_user_inp=restart
        
    elif  restart.lower() not in ('no','yes'):
        print('Did you make a typo?') # handling typo
        restart_user_inp=restart
        restart_func()   # ask user again after typo
    return restart_user_inp
    
    



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        try:
            user_stats(df)
        except KeyError:
            print('\nNo data for "age" and "gender" in "user_stats" in selected dataset.\n')
        counter=0
        raw_data_answer=raw_data_request(counter,df)
        restart_user_inp=restart_func()
        if restart_user_inp!= 'yes':
            break

        
        
            


if __name__ == "__main__":
	main()
