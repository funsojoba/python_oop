class ArrayStat:
    def __init__(self, array_list):
        self.array_list = array_list
        self.array_dict = {}
        self.splitted_list = []

    def split(self):

        new_list = "".join([str(i) for i in self.array_list])
        return list(new_list)

    def split_to_int(self):
        new_list = [int(i) for i in self.split()]
        return new_list

    def calculate_mean(self):
        mean = sum(self.split_to_int()) / len(self.split_to_int())
        rounded_mean = str(round(mean, 2))
        return rounded_mean

    def calculate_mode(self):
        modal_list = []
        modal_list_index = 0
        for i in self.split_to_int():
            modal_list.append(self.split_to_int().count(i))
            modal_list_index = modal_list.index(max(modal_list))
        return self.split_to_int()[modal_list_index]

    def calculate_median(self):
        main_list = self.split_to_int()
        main_list.sort()
        middle_value = len(main_list)//2

        if len(main_list) % 2 == 0:
            return main_list[middle_value - 1: middle_value + 1]
        else:
            return main_list[middle_value]

    def get_dict(self):
        dict_output = f""" mode: {self.calculate_mode()} mean: {self.calculate_mean()} median: {self.calculate_median()}
        """
        self.array_dict = dict_output
        return self.array_dict


my_array = ArrayStat([1, 2, 3, 4, 5, 5, 13, 6, 7, 7, 7, 8, 9, 9])


print(my_array.get_dict())