import random
import numpy as np
import matplotlib.pyplot as plt
# let's create a fair coin object that can be flipped:
Results = []
maxs = []
mins = []


class Coin(object):
    '''this is a Modified coin, normal distribution'''
    sides = np.random.normal(100, 15, size=10000)
    last_result = None
    

    def flip(self):
        '''call coin.flip() to flip the coin and record it as the last result'''
        self.last_result = result = random.choice(self.sides)
        return result
        
# let's create some auxilliary functions to manipulate the coins:

def create_coins(number):
    '''create a list of a number of coin objects'''
    return [Coin() for _ in xrange(number)]

def flip_coins(coins):
    '''side effect function, modifies object in place, returns None'''
    for coin in coins:
        coin.flip()

def the_max(flipped_coins):
    return max(coin.last_result for coin in flipped_coins)

def the_min(flipped_coins):
    return min(coin.last_result for coin in flipped_coins)

def capture(flipped_coins):
    return list(coin.last_result for coin in flipped_coins)


def main():
    coins = create_coins(10)
    for i in xrange(100):
        flip_coins(coins)
        maxs.append(the_max(coins))
        mins.append(the_min(coins))       
        Results.extend(capture(coins))
        # I learned the difference between append and extednd, append in this case will create multi dimensional array
        
if __name__ == '__main__':
    main()

% matplotlib inline
plt.hist(Results)
# replace Results with maxs or mins to get the distribution of the extremes
plt.title('Distribution') 
plt.show()