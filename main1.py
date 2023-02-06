# __author__ = "ITPLUS"


class People:
    count = 0

    def __init__(self, people_name, age):
        """
        constructor
        :param people_name:
        :param age:
        """
        self.name = people_name
        self.age = age
        People.count += 1

    def show_info(self):
        """
        print information
        :return:
        """
        print('Name:', self.name)
        print('Age:', self.age)


nguyen_van_a = People('Nguyen Van A', 18)
# nguyen_van_a.show_info()
# del nguyen_van_a.age
nguyen_van_a.gender = 'Male'
# print(nguyen_van_a.gender)
# print(nguyen_van_a.age)
# print(getattr(nguyen_van_a, 'name'))
# print(hasattr(nguyen_van_a, 'weight'))
# print(hasattr(nguyen_van_a, 'name'))
setattr(nguyen_van_a, 'name', 'Nguyen Van Manh')

delattr(nguyen_van_a, 'age')
nguyen_van_a.show_info()


nguyen_van_b = People('Nguyen Van B', 25)
nguyen_van_b.show_info()
# print(nguyen_van_b.age)
# print(nguyen_van_b.gender)
# print(People.count)

