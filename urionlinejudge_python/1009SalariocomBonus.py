#!/usr/bin/python
# -*- coding: utf-8 -*-
nome = input()
salario = float(input())
totalvendas = float(input())
totalreceber = salario + totalvendas * 15 / 100
print(('TOTAL = R$ {:.2f}'.format(totalreceber)))
