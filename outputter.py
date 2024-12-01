

from AnimalClassifiers import Animal
from Hyenas import Hyena
from Lions import Lion
from Tigers import Tiger
from Bears import Bear
#oh my

from _datetime import date


list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []


current_date = date.today()
current_year = current_date.year


def calc_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)

    the_birth_day = ""

    if "spring" in the_season:
        the_birth_day = str(year_of_birthday) + "-03-21"
    elif "summer" in the_season:
        the_birth_day = str(year_of_birthday) + "-06-21"
    elif "fall" in the_season:
        the_birth_day = str(year_of_birthday) + "-09-21"
    elif "winter" in the_season:
        the_birth_day = str(year_of_birthday) + "-12-21"
    # if the birth season is unknown
    else:
        the_birth_day = str(year_of_birthday) + "-01-01"

    return the_birth_day


def process_one_line(one_line):

    a_species = ""
    a_sex = ""
    age_in_years = 99
    season = ""
    color = ""
    weight = ""
    origin_01 = ""
    origin_02 = ""

    arrivinganimaldata = one_line.strip().split(",")
    parsed_words = arrivinganimaldata[0].strip().split(" ")
    age_in_years = parsed_words[0]
    a_sex = parsed_words[3]
    a_species = parsed_words[4]
    parsed_words = arrivinganimaldata[1].strip().split(" ")
    season = parsed_words[2]
    color = arrivinganimaldata[2].strip();
    weight = arrivinganimaldata[3].strip();
    origin_01 = arrivinganimaldata[4].strip();
    origin_02 = arrivinganimaldata[5].strip();

    from_zoo = origin_01 + ", " + origin_02

    birth_day = calc_birth_date(season, age_in_years)

    if "hyena" in a_species:

        my_hyena = Hyena("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        my_hyena.name = Hyena.get_hyena_name(my_hyena)
        my_hyena.animal_id = "Hy" + str(Hyena.hyena_count).zfill(2)
        list_of_hyenas.append(my_hyena)

    if "lion" in a_species:

        my_lion = Lion("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        my_lion.name = Lion.get_lion_name(my_lion)
        my_lion.animal_id = "Li" + str(Lion.lion_count).zfill(2)
        list_of_lions.append(my_lion)

    if "tiger" in a_species:

        my_tiger = Tiger("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        my_tiger.name = Tiger.get_tiger_name(my_tiger)
        my_tiger.animal_id = "Ti" + str(Tiger.tiger_count).zfill(2)
        list_of_tigers.append(my_tiger)

    if "bear" in a_species:

        my_bear = Bear("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        my_bear.name = Bear.get_bear_name(my_bear)
        my_bear.animal_id = "Be" + str(Bear.bear_count).zfill(2)
        list_of_bears.append(my_bear)


file_path = "arrivingAnimals.txt"
with open(file_path) as file:
    for line in file:
        process_one_line(line)


print()
print("Zookeeper's Challenge Zoo Population")
print()
print("Hyena Habitat:")
print()
for hyena in list_of_hyenas:
    print(hyena.animal_id + ", " + hyena.name + "; birthdate: " + str(hyena.birth_date) + "; " + hyena.color +
          "; " + hyena.sex + "; " + hyena.weight + "; " + hyena.originating_zoo + "; arrived: " +
          str(hyena.date_arrival))
print(f"\n\nNumber of hyenas adopted: {Hyena.hyena_count}")

print()
print("Lion Habitat:")
print()
for lion in list_of_lions:
    print(lion.animal_id + ", " + lion.name + "; birthdate: " + str(lion.birth_date) + "; " + lion.color +
          "; " + lion.sex + "; " + lion.weight + "; " + lion.originating_zoo + "; arrived: " +
          str(lion.date_arrival))
print(f"\n\nNumber of lions adopted: {Lion.lion_count}")

print()
print("Tiger Habitat:")
print()
for tiger in list_of_tigers:
    print(tiger.animal_id + ", " + tiger.name + "; birthdate: " + str(tiger.birth_date) + "; " + tiger.color +
          "; " + tiger.sex + "; " + tiger.weight + "; " + tiger.originating_zoo + "; arrived: " +
          str(tiger.date_arrival))
print(f"\n\nNumber of tigers adopted: {Tiger.tiger_count}")

print()
print("Bear Habitat:")
print()
for bear in list_of_bears:
    print(bear.animal_id + ", " + bear.name + "; birthdate: " + str(bear.birth_date) + "; " + bear.color +
          "; " + bear.sex + "; " + bear.weight + "; " + bear.originating_zoo + "; arrived: " +
          str(bear.date_arrival))
print(f"\n\nNumber of bears adopted: {Bear.bear_count}")




print(f"\n\nNumber of animals adopted: {Animal.animal_count}")

