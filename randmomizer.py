'''Randomizer demo for class.'''
import random
import secrets
from collections import defaultdict

import matplotlib.pyplot as plt


def generate_secrets_list(size=100, min_val=0, max_value=100) -> list:
    '''Generate a list of random integers of size.'''
    '''Uses the secrets cryptographic function.'''
    random_list = []
    
    for i in range(1,size+1):
        #rand_int = random.randrange(1,100)
        rand_int = secrets.randbelow(max_value+1) #maximum is exclusive
        #print(rand_int)
        random_list.append(rand_int)
    
    return random_list


def generate_random_list(size=100, min_val=0, max_value=100) -> list:
    '''Generate a list of random integers of size.'''
    '''Uses basic random function.'''
    random_list = []
    
    for i in range(1,size+1):
        rand_int = random.randrange(1,100)
        #print(rand_int)
        random_list.append(rand_int)
    
    return random_list


def create_bar_chart(categories: list, values: list, title=''):
    '''Create a bar charg using categories as the x-axis and values as the y-axis.'''
    '''A title for the chart can be given.'''
    # Create bar chart
    _fig, ax = plt.subplots()
    #bars = ax.bar(categories, values, color='skyblue')
    ax.bar(categories, values, color='skyblue')
    
    # Add labels directly using the bar_label function
    #ax.bar_label(bars, padding=3)
    
    # Add titels and labels
    ax.set_title(title)
    ax.set_xlabel("Numbers")
    ax.set_ylabel("Count")
    
    # Display
    #plt.show()
    plt.draw()
    plt.show(block=False)



def process_random_list(random_list: list):
    '''Process and gather statistics on the random list.'''
    '''Send the results to be printed.'''
    random_list.sort() #sort the list
    
    # Grouping items by value
    grouped = defaultdict(list)
    for item in random_list:
        grouped[item].append(item)
    
    #print(grouped) #looks like  {'apple': ['apple', 'apple', 'apple'], 'banana': ['banana', 'ba
    
    distribution_dict = {}
    
    keys_list = list(grouped.keys())
    #print(f"Length of keys_list: {len(keys_list)}")
    
    for key in keys_list:
        #print(f"{key} {grouped[key]}")
        key_count = len(grouped[key])
        #print(f"{key} {key_count}")
        
        distribution_dict[key] = key_count
        
    #print(distribution_dict)
    
    # Need categories (x-axis) and values (y-axis) for the bar graph.
    categories = list(distribution_dict.keys())
    values = []
    
    #print(categories)
    #print(f"Length of categories: {len(categories)}")
    
    highest_value_count = distribution_dict[next(iter(distribution_dict))] #value of the first item in the dictionary
    highest_number = 0
    lowest_value_count = distribution_dict[next(iter(distribution_dict))] #value of the first item in the dictionary
    lowest_number = 0
    
    for category in categories:
        #print(f"{category} {distribution_dict[category]}")
        values.append(distribution_dict[category])
        if distribution_dict[category] >= highest_value_count:
            highest_number = category
            highest_value_count = distribution_dict[category]
            #print(f"Highest is now {category}")
        if distribution_dict[category] <= lowest_value_count:
            lowest_number = category
            lowest_value_count = distribution_dict[category]
            #print(f"Lowest is now {category}")
    
    num_list = [float(i) for i in categories]
    average = round((sum(values) / len(num_list)),2)
    highest = max(values)
    lowest = min(values)
    
                    
    print(f"Highest Count = {highest} of {highest_number}")
    print(f"Lowest Count = {lowest} of {lowest_number}")
    print(f"Average Count = {average}")
    #print(statistics.stdev(num_list))
    
    #create_bar_chart(categories, values)
    
    return (categories, values)



if __name__ == "__main__":
    '''Main area that calls the rest.'''
    LIST_SIZE = 10000000
    list_sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
    
    print(f"Generating up to {LIST_SIZE} random values.")
    
    
    
    '''
    # Using the regular python random
    random_list = generate_random_list(size=LIST_SIZE, min_val=0, max_value=100)
    #print(f"{random_list}")
    #print(f"Length of random_list: {len(random_list)}")
    categories, values = process_random_list(random_list)
    create_bar_chart(categories, values, "Random List")
    '''
    
    for size in list_sizes:
        # Using python cyrptographic secrets module
        secrets_list = generate_secrets_list(size=size, min_val=0, max_value=100)
        categories, values = process_random_list(secrets_list)
        create_bar_chart(categories, values, size)
    
    
    # Wait for user input before removing graphics.
    x = input("Press <Enter> to quit.")
    