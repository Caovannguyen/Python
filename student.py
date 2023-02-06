class Student:

    def __init__(self, name, date_of_birth, email, phone_number, address, company):
        """
        constructor
        :param name:
        :param date_of_birth:
        :param email:
        :param phone_number:
        :param address:
        :param company:
        """
        self.name = name
        self.date_ofd_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.company = company

    def show_info(self):
        print("Họ và tên:", self.name)
        print("Ngày sinh:", self.date_ofd_birth)
        print("Email:", self.email)
        print("Số điện thoại:", self.phone_number)
        print("Địa chỉ:", self.address)
        print("Đơn vị công tác:", self.company)

    def get_info(self, address='Hà Nội', company='ITPlus'):
        # self.address = address
        # self.company = company
        print("Họ và tên:", self.name)
        print("Ngày sinh:", self.date_ofd_birth)
        print("Email:", self.email)
        print("Số điện thoại:", self.phone_number)
        print("Địa chỉ:", address)
        print("Đơn vị công tác:", company)


my_info = Student('Tiến Phan anh', '01-12-1995', 'tienquy011295@gmail.com', '0965489736', 'Nghệ An', 'Viễn Chinh Tech')
# my_info.show_info()

# Không điền thông tin địa chỉ, đơn vị làm việc
# my_info.get_info()

# điền đầy đủ
my_info.get_info('Nghệ An', 'TH')