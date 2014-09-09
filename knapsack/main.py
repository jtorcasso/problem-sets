'''The Knapsack Problem - Introduction to Dynamic Programming

For items i=0,...,N we have weights w=w_0,...,w_N worth
v=v_0,...,v_N. We have a knapsack which can hold a total
of weight W. We want to maximize the value of the items
contained in our knapsack.

'''
import numpy as np

def knapsack(values, weights, W):
	'''the knapsack problem

	Parameters
	----------
	values : array
		values of potential knapsack items
	weights : array
		integer weights of potential knapsack items
	W : scalar
		maximum weight of the knapsack

	Returns
	-------
	maxval, maxset : scalar, set
		maximum value of knapsack items, the set of
		items
	'''

	assert len(values) == len(weights)
	assert all([isinstance(w, (int, np.int)) for w in weights])
	assert (w > 0).all() & (W > 0)

	# Setting Up Value Matrix, Shape = (# items, # possible weights)
	V = np.zeros((len(values), len(xrange(W+1))))

	# Decision Matrix
	keep = np.zeros(V.shape)

	# Foreach set of possible items (1,...,i) and weight w, find 
	# the optimal bundle of items and their total value
	for i in xrange(1, len(values)):
		for w in xrange(W+1):

			# If the next item in the set could fit
			if (weights[i] < w):

				# If current item's value plus the value of the
				# optimal choice of the remaining items (with
				# the weight left in the sack) is greater than
				# the optimal value using the set of previously 
				# available items and current weight, then set
				# the value to the former. Otherwise set the 
				# value to the latter
				if values[i] + V[i-1, w-weights[i]] > V[i-1, w]:
					V[i,w] = values[i] + V[i-1, w-weights[i]]
					keep[i,w] = 1
					continue

			V[i,w] = V[i-1,w]
			keep[i,w] = 0

	K = W + 1
	maxset = []
	for i in xrange(len(values)-1, 0, -1):
		if keep[i,K-1]:
			maxset.append(i)
			K = K - weights[i]

	return V[len(values)-1,W], set(maxset)

if __name__ == '__main__':
	values = np.random.uniform(5, 30, 10)
	weights = np.random.randint(0, 20, 10)
	W = int(2.*sum(weights)/4)

	print 'Total Allowable Weight: ', W
	print knapsack(values, weights, W)



