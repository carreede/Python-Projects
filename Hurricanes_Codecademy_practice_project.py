# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,
          74]



# write your update damages function here:
multiplier= {"B":1000000000, "M":1000000}
def update_damages(a_list):
    new_damages= []
    for i in range(len(a_list)):
        item= a_list[i]
        if not(item[-1] == "B" or item[-1] == "M"):
            new_damages.append(item)
        elif item[-1] == "B":
            new_damages += [float(item[:-1])* multiplier["B"]]
        elif item[-1] == "M":
            new_damages += [float(item[:-1]) *multiplier["M"]]
    return new_damages



# write your construct hurricane dictionary function here:
def create_dictionary(name, months, years, winds, areas, damage, deaths):
    hurricane_dictionary= {}
    for i in range(len(name)):
        hurricane_dictionary[name[i]]= {"Name": name[i], "Months": months[i], "Years": years[i], "Max Sustained Winds": winds[i], "Areas Affected": areas[i],"Damages": damages[i], "Deaths": deaths[i]}
    return hurricane_dictionary



# write your construct hurricane by year dictionary function here:
def change_key_to_year(dictionary):
    new_dictionary= {values["Years"]: values for values in dictionary.values()}
    return new_dictionary



# write your count affected areas function here:
def count_affected_areas(dictionary):
    area_count= {}
    for values in dictionary.values():
        areas_list = values["Areas Affected"]
        for indivisual_areas in areas_list:
            if not(indivisual_areas) in area_count:
                area_count[indivisual_areas]= 1
            else:
                area_count[indivisual_areas]+= 1
    return area_count


# write your find most affected area function here:
def most_affected(dictionary):
    most_affected= 0
    most_affected_area= {}
    for items in dictionary.items():
        if items[1] > most_affected:
            most_affected= items[1]
            most_affected_area= items
        else:
            pass
    return most_affected_area


# write your greatest number of deaths function here:
def greatest_num_deaths(dictionary):
    death_toll_by_area= {values["Name"]: values["Deaths"] for values in dictionary.values()}
    greatest_num= 0
    for x in death_toll_by_area.items():
        if x[1] > greatest_num:
            greatest_num = x[1]
            greatest_death_toll= x
        else:
            pass
    return greatest_death_toll



# write your catgeorize by mortality function here:
def categorize_by_mortality(dictionary):
    mortality_scale= {0:0, 1:100, 2:500, 3:1000, 4:10000}
    mortality_dictionary= {1:"", 2:"", 3:"", 4:"", 5:""}
    for x in dictionary.values():
        deaths= x['Deaths']
        if deaths <= mortality_scale[0]:
            try:
                mortality_dictionary[1] += [x]
            except:
                mortality_dictionary[1] = [x]
        elif deaths <= mortality_scale[1]:
            try:
                mortality_dictionary[2] += [x]
            except:
                mortality_dictionary[2] = [x]
        elif deaths <= mortality_scale[2]:
            try:
                mortality_dictionary[3] += [x]
            except:
                mortality_dictionary[3] = [x]
        elif deaths <= mortality_scale[3]:
            try:
                mortality_dictionary[4] += [x]
            except:
                mortality_dictionary[4] = [x]
        elif deaths <= mortality_scale[4]:
            try:
                mortality_dictionary[5] += [x]
            except:
                mortality_dictionary[5] = [x]
    return mortality_dictionary



# write your greatest damage function here:
def greatest_damage(dictionary):
    greatest_damage= {}
    dam= 0
    for x in dictionary.values():
        damage= x["Damage"]
        try:
            if float(damage) > dam:
                damage = dam
                greatest_damage["Most Damage"]= x["Name"], x["Damage"]
            else:
                pass
        except:
            if damage == "Damages not recorded":
                pass
    return greatest_damage



# write your catgeorize by damage function here:
def categorize_by_damage(dictionary):
    damage_scale= {0:0, 1:100000000, 2:1000000000, 3:10000000000, 4:50000000000}
    damage_dictionary= {1:"", 2:"", 3:"", 4:"", 5:""}
    for x in dictionary.values():
        damage = x['Damage']
        if damage == "Damages not recorded":
            try:
                damage_dictionary[1] += [x]
            except:
                damage_dictionary[1] = [x]
        elif float(damage) <= damage_scale[1]:
            try:
                damage_dictionary[2] += [x]
            except:
                damage_dictionary[2] = [x]
        elif float(damage) <= damage_scale[2]:
            try:
                damage_dictionary[3] += [x]
            except:
                damage_dictionary[3] = [x]
        elif float(damage) <= damage_scale[3]:
            try:
                damage_dictionary[4] += [x]
            except:
                damage_dictionary[4] = [x]
        elif float(damage) <= damage_scale[4]:
            try:
                damage_dictionary[5] += [x]
            except:
                damage_dictionary[5] = [x]
    return damage_dictionary

#EXTRA

#Change Damage to Scientific Notaiton
multiplier= {"B":1000000000, "M":1000000}
def update_damages_to_scientific_notation(a_list):
    new_damages= []
    for i in range(len(a_list)):
        item= a_list[i]
        if not(item[-1] == "B" or item[-1] == "M"):
            new_damages.append(item)
        elif item[-1] == "B":
            new_num= float(item[:-1])* multiplier["B"]
            new_damages += ["{:.2e}".format(new_num)]
        elif item[-1] == "M":
            new_num= float(item[:-1])* multiplier["M"]
            new_damages += ["{:.2e}".format(new_num)]
    return new_damages
