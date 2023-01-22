from abc import abstractmethod, ABC


class ConsoleInterface(ABC):
    @abstractmethod
    def show_info(self):
        pass


class ShowContactResult(ConsoleInterface):
    def show_info(self):
        print('*' * 30, ' User Books ', '*' * 30)
        print(self.__str__())


class ShowNoteResult(ConsoleInterface):
    def show_info(self):
        print('~' * 30, ' Note Books ', '~' * 30)
        print(self.__str__())


class ShowHelpCommandsResult(ConsoleInterface):
    def show_info(self):
        print('#' * 30, ' Commands ', '#' * 30)
        print(self.__str__())
        print('Please choose command ....')