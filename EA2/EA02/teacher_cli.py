from teacher_crud import TeacherCRUD

class SimpleCLI:
    def __init__(self):
        self.commands = {}
        self.register_default_commands()

    def register_default_commands(self):
        self.commands["quit"] = self.quit

    def add_command(self, name, function):
        self.commands[name] = function

    def quit(self):
        print("Goodbye!")
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.display_commands()
            command = input("Enter a command: ").strip()
            self.execute_command(command)

    def display_commands(self):
        print(f'Commands: {", ".join(self.commands.keys())}')

    def execute_command(self, command):
        if command in self.commands:
            self.commands[command]()
        else:
            print("Invalid command. Try again.")

class TeacherCLI(SimpleCLI):
    def __init__(self, teacherCRUD: TeacherCRUD):
        self._teacherCRUD = teacherCRUD
        super().__init__()

    def register_default_commands(self):
        super().register_default_commands()
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        name = input('Enter professor name: ')
        birth_year = input('Birth year: ')
        cpf = input('CPF: ')
        self._teacherCRUD.create(name, birth_year, cpf)
        print('Professor created!')

    def read_teacher(self):
        name = input('Professor name: ')
        teacher = self._teacherCRUD.read(name)
        if teacher:
            print('Professor found:')
            self.display_teacher(teacher)
        else:
            print('Professor not found!')

    def update_teacher(self):
        name = input('Professor name: ')
        new_cpf = input('New CPF: ')
        teacher = self._teacherCRUD.update(name, new_cpf)
        if teacher:
            print('Professor updated:')
            self.display_teacher(teacher)
        else:
            print('Professor not found!')

    def delete_teacher(self):
        name = input("Professor name: ")
        self._teacherCRUD.delete(name)
        print('Deleted!')

    def display_teacher(self, teacher):
        for key, value in teacher.items():
            print(f'\t- {key}: {value}')

    def run(self):
        print("Welcome to the Teacher CLI! Available commands: create | read | update | delete | quit")
        super().run()
