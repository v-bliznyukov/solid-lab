import abc


class Needs(abc.ABC):
    @abc.abstractmethod
    def pray(self):
        pass

    @abc.abstractmethod
    def play_sports(self):
        pass

    @abc.abstractmethod
    def get_married(self):
        pass

    @abc.abstractmethod
    def own_company(self):
        pass

    @abc.abstractmethod
    def become_employee(self):
        pass
