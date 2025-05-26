from abc import ABC, abstractmethod


class Staff(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def introduce(self):
        pass

    def clock_in(self):
        print("Clocked in!")


class Doctor(Staff):
    def __init__(self, name):
        super().__init__(name)

    def introduce(self):
        print(f"Hi, I am Dr. {self.name}, I treat patients.")


class Nurse(Staff):
    def __init__(self, name):
        super().__init__(name)

    def introduce(self):
        print(f"Hi, I am Nurse {self.name}, I assist in patient care.")


class Receptionist(Staff):
    def __init__(self, name):
        super().__init__(name)

    def introduce(self):
        print(f"Hi, I am {self.name}, I manage the front desk.")

    def clock_in(self):
        print(f"Receptionist {self.name} has clocked in at the front desk.")

if __name__ == "__main__":
 
    doctor = Doctor("Ahmed")
    nurse = Nurse("Sara")
    receptionist = Receptionist("John")

    
    staff_list = [doctor, nurse, receptionist]

    
    for staff in staff_list:
        staff.introduce()

    
    receptionist.clock_in()


