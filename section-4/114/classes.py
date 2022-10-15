# Classes Abstratas
from abc import ABC, abstractclassmethod


class A(ABC):

    @abstractclassmethod
    def falar(self):

        ...


class B(A):

    def falar(self):

        print('Falando...')
