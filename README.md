# Cardflip 

## Installation

1. Install PsychoPy (see below)
* This program made by PsychoPy3

PsychoPy is an open-source package for creating experiments in behavioral science.
https://www.psychopy.org/.

## About

Cardflip is a search task program for the economic experiment. This task is a simple card flip game that the subject (Player) can free to search the numbers written on cards. 

![AnyConv com__search](https://user-images.githubusercontent.com/38565854/101184228-d1083300-3693-11eb-86f0-ed48a7193ed8.gif)

## Description


Subject (Player) can flip a card by clicking the “Flip a new card” button. 
At the top of the main screen, the cost and probability of success are displayed. In addition, the highest number ever found in the round is always displayed at the top middle of the screen and is initially zero.
There are 16 cards on the screen, but if subjects fliped whole 16 cards and still wish to continue, they can obtain 16 new cards by clicking “Flip a new card.” In such cases, the previous highest number is still displayed on the screen. Subjects can finish the round by clicking the “Finish” button at any time. At the end of the round, the highest number of cards minus the total search cost is recorded as the result of the round.


## Usage

main/Cardflip.py is the main program.
By running the program, first, you can set session ID and participant ID.
After the 3 practice round, the main round will start.
In each round,  numbers written on the tail of the card is randomly distributed from Uniform distribution.
When all rounds are finished, only one result is randomly picked up from the main rounds and the reward is shown.
This reward recorded as /Payoff_file.csv  in the current directory.
Subjects all behavioral data is also recorded on /data .

main/condition_treatment.xlsx defines the following parameters of the round by each row.

a : lower bound 

b : Upper bound

para1: exchange rate for point.

Treat_s: search cost

Treat_q: probability of success

Fixed_fee: participation fee

## References
Consumer Search and Stock-out: A Laboratory Experiment (2020)  Ryo Mikami and Y. KITTAKA
ISER Discussion Paper No. 1104.
https://www.iser.osaka-u.ac.jp/library/dp/2020/DP1104.pdf

## Author

Ryo mikami
https://sites.google.com/view/ryomikami/home
