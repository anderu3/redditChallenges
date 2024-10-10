
bio_data = [
    ('Frank', 1910, 1975),
    ('Grace', 1935, 1980),
    ('Hank',  1922, 1968),
    ('Ivy',   1940, 1995),
    ('Jake',  1953, 1990),
]

# the left side is what is the biggest that is still less than the right's smallest


def most_active(bio_data):
    smallest_ending_year = 2000
    biggest_starting_year = 0

    #check for smallest year and assign
    for i in range((len(bio_data))):
        if smallest_ending_year > bio_data[i][2]:
            smallest_ending_year = bio_data[i][2]
        #smallest_ending_year is now the smallest right-side number
    
    for i in range((len(bio_data))):                        
        if biggest_starting_year < bio_data[i][1]:
            if bio_data[i][1] < smallest_ending_year:
                biggest_starting_year = bio_data[i][1]

    return (biggest_starting_year, smallest_ending_year)

print(most_active(bio_data))