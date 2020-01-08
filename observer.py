#!/home/valdemir/.virtualenvs/k36/bin/python
# -*- coding: utf-8 -*-
#Author: Valdemir Bezerra

'''
PErmitir que um objeto seja capaz de notificar outro objeto

dependência um para  muitos. quando um objeto mudo, todos os seus dependentes são notificados e atualiuzados
'''

class Observador:
    def atualizar(self, data):
        pass

class Observavel(Observador):
    def __init__(self):
        self._observers =[]

    def registrar_observador(self, observer):
        self._observers.append(observer)

    def remover_observador(self, observer):
        self._observers.remove(observer)

    def notificar_observadores(self, data):
        for observer in self._observers:
            observer.atualizar(self, data)