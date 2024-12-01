
from AnimalClassifiers import Animal


class Hyena(Animal):

    hyena_count = 0

    list_of_hyena_names = []

    file_path = 'animalNames.txt'
    with open(file_path) as file:
        lines = file.readlines()

        line_num = 1
        for line in lines:
            if line_num == 3:
                list_of_hyena_names.extend(line.strip().split(', '))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id="an_id", birth_date="2099-01-01", color="a_color", sex="a_sex",
                 weight="a_weight", originating_zoo="a_zoo", date_arrival="2099-01-01"):

        Hyena.hyena_count += 1

        super().__init__("hyena", name, animal_id, birth_date, color, sex, weight, originating_zoo, date_arrival)

    def get_hyena_name(self):
        return self.list_of_hyena_names.pop(0)

