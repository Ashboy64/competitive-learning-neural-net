import numpy as np

def sigmoid(x,derivative=False):
    if(derivative==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

np.random.seed(1)

weights = np.random.randn(3, 3)

training = np.array([[np.array([1,1,1]).reshape(1,-1)],
                    [np.array([0,1,1]).reshape(1,-1)],
                    [np.array([1,0,1]).reshape(1,-1)],
                    [np.array([0,0,1]).reshape(1,-1)]])


for x in range(1000):
    for iter in xrange(training.shape[0]):
#forwardPropagation:
        a_layer1 = training[iter][0]
        z_layer2 = np.dot(weights,a_layer1.T)
        a_layer2 = sigmoid(z_layer2)
        hypothesis_theta = a_layer2
        #print "hypothesis"
        #print hypothesis_theta

        temp = np.where(hypothesis_theta==np.amax(hypothesis_theta))[0]

        #print temp

#backPropagation:

        highestWeights = weights[temp]
        weights[temp] = 0.02*(a_layer1 - weights[temp])
        #print "weights"
        #print weights

for iter in xrange(training.shape[0]):
#forwardPropagation:
        a_layer1 = training[iter][0]
        z_layer2 = np.dot(weights,a_layer1.T)
        a_layer2 = sigmoid(z_layer2)
        hypothesis_theta = a_layer2
        print "hypothesis"
        print hypothesis_theta

        temp = np.where(hypothesis_theta==np.amax(hypothesis_theta))[0]
        print "temp"
        print temp
        print "iter"
        print iter
        print "wieghts[temp]"
        print weights[temp]
