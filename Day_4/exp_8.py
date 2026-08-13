class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def display_student(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")

class EngineeringStudent(Student):
    def __init__(self, name, roll_no, branch, semester):
        super().__init__(name, roll_no)
        self.branch = branch
        self.semester = semester
    
    def display_branch(self):
        print(f"Branch: {self.branch}")
        print(f"Semester: {self.semester}")
    
    def display_complete_details(self):
        self.display_student()
        self.display_branch()
        print("-" * 30)

# Create engineering student objects
student1 = EngineeringStudent("Alice Johnson", "E2023001", "Computer Science", 3)
student2 = EngineeringStudent("Bob Smith", "E2023002", "Electronics", 2)

# Display their details
print("Engineering Student 1 Details:")
student1.display_complete_details()

print("Engineering Student 2 Details:")
student2.display_complete_details()

class VLSIBlock:
    def __init__(self, name, technology):
        self.name = name
        self.technology = technology
    
    def display_info(self):
        print(f"Block Name: {self.name}")
        print(f"Technology: {self.technology}")

class Processor(VLSIBlock):
    def __init__(self, name, technology, cores, clock_speed):
        super().__init__(name, technology)
        self.cores = cores
        self.clock_speed = clock_speed
    
    def display_complete_info(self):
        self.display_info()
        print(f"Number of Cores: {self.cores}")
        print(f"Clock Speed: {self.clock_speed}")
        print("-" * 30)

class Memory(VLSIBlock):
    def __init__(self, name, technology, capacity, memory_type):
        super().__init__(name, technology)
        self.capacity = capacity
        self.memory_type = memory_type
    
    def display_complete_info(self):
        self.display_info()
        print(f"Capacity: {self.capacity}")
        print(f"Memory Type: {self.memory_type}")
        print("-" * 30)

# Create objects
processor1 = Processor("ARM Cortex-A78", "5nm", 8, "3.0 GHz")
memory1 = Memory("SRAM Cache", "7nm", "4 MB", "SRAM")

# Display information
print("Processor Information:")
processor1.display_complete_info()

print("Memory Information:")
memory1.display_complete_info()

class DesignBlock:
    def simulate(self):
        print("Simulating generic design block")

class ALU(DesignBlock):
    def simulate(self):
        print("Simulating ALU: Performing arithmetic and logic operations")

class RegisterFile(DesignBlock):
    def simulate(self):
        print("Simulating Register File: Testing read/write operations")

class Cache(DesignBlock):
    def simulate(self):
        print("Simulating Cache: Testing hit/miss scenarios and data retrieval")

# Create objects and store in list
design_blocks = [
    ALU(),
    RegisterFile(),
    Cache()
]

# Use for loop to call simulate() for every object
print("Simulation Results:")
print("-" * 40)
for block in design_blocks:
    block.simulate()

class VerificationComponent:
    def verify(self):
        print("Verifying generic component")

class ALUVerification(VerificationComponent):
    def verify(self):
        print("Verifying ALU: Testing arithmetic operations, logic gates, and overflow conditions")

class MemoryVerification(VerificationComponent):
    def verify(self):
        print("Verifying Memory: Testing read/write operations, address decoding, and data integrity")

class APBVerification(VerificationComponent):
    def verify(self):
        print("Verifying APB: Testing protocol compliance, timing constraints, and bus transactions")

# Create objects and store in list
verification_components = [
    ALUVerification(),
    MemoryVerification(),
    APBVerification()
]

# Use single for loop to call verify()
print("Verification Results:")
print("-" * 50)
for component in verification_components:
    component.verify()

