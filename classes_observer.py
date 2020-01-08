#!/home/valdemir/.virtualenvs/k36/bin/python
# -*- coding: utf-8 -*-
#Author: Valdemir Bezerra

'''
Vamos fazer a entrega de dados para 3 sistemas diferentes onde
um recebe em json
outro em xml
outro em soup

exemplo abstrato
'''

class FalaAdapter:
    def __init__(self, ser, *, falar):
        self.ser = ser
        metodo_de_fala = getattr(self.ser, falar)
        self.__setattr__('falar', metodo_de_fala)

class Bruxo:
    def __init__(self, bruxo):
        self.bruxo = bruxo

    def falar(self):
        self.bruxo.bruxeis()

class Genio:
    def __init__(self, genio):
        self.genio = genio

    def falar(self):
        self.genio.geneis()

class Deus:
    def __init__(self, deus):
        self.deus = deus

    def falar(self):
        self.deus.deuseis()


seres = [FalaAdapter(Bruxo(), falar='bruxeis'), FalaAdapter(Genio(), falar='geneis'), FalaAdapter(Deus(), falar='deuseis')]

for adapter in seres:
    adapter.falar()


