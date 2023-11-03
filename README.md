# Description
This repository is dedicated to the development of a tool and associated resources for encoding a Turing machine into binary sequences, and binary sequences to Turing machine.

# Motivation

In computer theory class, looking at turing machines, we saw a way to encode and decode them from binary sequences. It seemed like a good idea to automate this process using python.

# Topics
The topics that u need to know for grasp the repository are:
## turing machine
A turing machine it's a 7-tuple composed by 
  - Q states set
  - ∑ entry alphabet 
  - ß tape alphabet
  - ∂ transition function
  - q0 ∈ Q (init state)
  - qa ∈ Q (aceptation state)
  - qreject ∈ Q (rejection state) qreject != qa


## encode algorithm
With just the transition functions, we can construct the Turing machine, knowing that it comprises a 7-tuple.

Note:


A transition function can be displayed at this (init state, read symbol) ->  (finish state, replace symbol, move)
Just with this we can denote  
  - ∑  = {read symbol, replace symbol} -> set where we add symbols used for all functions
  - Q = {init state, finish state} -> set where we add states used for all functions

To encode the Tuing machine in a binary sequence we gonna a compose a sequence that have this structure: 

       0[function 1]00[function 2]00...00[function n]0

more explicitly as follows: 

      0{init state encoded}0{symbol read encoded}0{final state encoded}0{symbol replace}0{move}00{init state (for second transition function) encoded}0...{move (for n transition function) encoded}0


## decode algorithm
Once we have encoded the concepts, we can proceed to decode the Turing machine, thereby converting the binary sequence into the transition functions.

Knowing that a encode turing machine have this structure:

    0[function 1]00[function 2]00...00[function n]0

Note that a function have this structure:

    [function 1] = 0{init state}0{read symbol}0{finish state}0{replace symbol}0{move}0

Now we can easly build all the function that compose the turing machine.


         




