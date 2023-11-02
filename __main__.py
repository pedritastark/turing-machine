#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:18:01 2023

@author: sebastianpedraza
"""

import re

'''
Description: This function is used to decode a binary secuence and transform it into a turing machine

Input: Binary secuence (string) -> Binary secuence at this form 0[function 1]00[function 2]00...00[function n] = 0{init state encoded}0{symbol read encoded}0{final state encoded}0{symbol replace}0
{move}00{init state (for second transition function)}0...{move (for n transition function)}0

Output: Turing machine (strng) -> code to be builded in https://turingmachinesimulator.com
'''
def binMachineConverter(binarysecuence: str)-> None:

    moves = {'1': '>', '11': '<', '111': '-'}
    states = {('1' * i): ('q' + str(i)) for i in range(1, len([parte.replace("00", "") for parte in re.split(r"00", binarysecuence[1:-1])])+1)}
    alphabet = {'1': '_', '11': 'a', '111': 'b'}

    for k, funcion in enumerate([parte.replace("00", "") for parte in re.split(r"00", binarysecuence[1:-1])]):
        print('\n')
        function_data = []

        for v in zip([x for x in re.split(r'0', funcion) if x], ['inicial state', 'read', 'final state', 'replace', 'move']):
            key, label = v

            if label == 'move': function_data.append(moves[key])

            elif label in ['inicial state', 'final state']: function_data.append(states[key])

            elif label in ['read', 'replace']: function_data.append([alphabet[key]][0])

        print(f"{function_data[0]},{function_data[1]}\n{function_data[2]},{function_data[3]},{function_data[4]}")




'''
Description: This function is used to encode a turing machine to a binary secuence

Input: Turing machine (list[transition function 1], [transition function 2], ..., [transition function n]) -> Turing machines can be builded just having the transition
functions that the machine have, so we define functions in this form [transition function] = [init state, symbol read, final state, symbol replace, move]

Output: Binary secuence (string) -> Binary secuence at this form 0[function 1]00[function 2]00...00[function n] = 0{init state encoded}0{symbol read encoded}0{final state encoded}0{symbol replace}0
{move}00{init state (for second transition function) encoded}0...{move (for n transition function) encoded}0
'''
def machineBinConverter(machine: list[list]) -> None:

    moves = {'>': '1', '<': '11', '-': '111'}
    states = {('q' + str(i)): ('1' * i) for i in range(1, 5)}
    alphabet = {'_': '1', 'a': '11', 'b': '111'}

    data = ''
    for function in machine:
        function_data = '0'
        for v in zip(function, ['init state', 'read', 'final state', 'replace', 'move']):
            key, label = v

            if label == 'move': function_data += moves[key] + '0'

            elif label in ['init state', 'final state']: function_data += states[key] + '0'

            elif label in ['read', 'replace']: function_data += alphabet[key] + '0'
        data += function_data
    print(data)




binarysecuence = '010110111011010011101110111101110100111101110111101110100111101101111101101001111010110101110'

machinecode = [['q1','a','q3','a','>'], ['q3', 'b', 'q4', 'b', '>'], ['q4', 'b', 'q4', 'b', '>']]

binMachineConverter(binarysecuence)
machineBinConverter(machinecode)








