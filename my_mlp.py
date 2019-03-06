import math
import random
import numpy as np
import matplotlib.pyplot as plt

#np.tanh(x) = hyperbolic tangent value of x
#np.ones(n) = create an array with n int with value one
#np.zeros(n) = same but value is zero
#np.random.random(a) create a random float with interval of the array a
#np.dot(a,b) = scallar or array vector of two array
#np.atleast_2d(n) = create two dimension array with value n
#tuple = list unchangeable
#array.shape = get or set the shape of the array 
#array[...] = take all dimensions of the array
#array[s:e] = take dimensions from (s)tart to (e)nd, zero  
#.n = n is float with value 0.n
#n. = n is float with value n.0

n=2
m=1
errorValues = []

def sigmoid(x):
    return (1/(1 + math.exp(-x)))

def new_array(o : float, v : int):
    x=0
    ar = []
    while x < v:
        ar.append(o)
        x+=1
    return ar

def new_array_(o : float, m : int, n : int):
    x=0
    ar = []
    while x < m:
        y=0
        arr=[]
        while y < n:
            arr.append(o)
            y+=1
        ar.append(arr)
        x+=1
    return ar

def new_weights():
        x=0
        while x < len(_weights):
            Z = random.uniform(-0.25,0.25)
            _weights[x] = Z
            x+=1

def propagate_forward(data):
    _input[1:]  = data
    _output[...] = sigmoid(np.dot(_weights,_input))
    return _output

def propagate_backward(target, lrate=0.1):
    error = np.atleast_2d(target-_output)
    input_ = np.atleast_2d(_input)
    _weights += lrate*np.dot(error.T,input_)
    quadratic_error = (error**2).sum()
    errorValues.append(quadratic_error)
    return quadratic_error

def printErrorGraph():
    grap = plt.figure()
    plt.plot([x for x in range(len(errorValues))], errorValues)
    plt.savefig("fig.png")
    plt.show()

if __name__ == '__main__':
    def learn(dataset, epochs=250, lrate=.1, momentum=0.1):
        for i in range(epochs):
            n = np.random.randint(len(dataset))
            propagate_forward( dataset['input'][n] )
            #propagate_backward( dataset['output'][n], lrate )
        for i in range(len(dataset)):
            o = propagate_forward( dataset['input'][i] )
            print (i, dataset['input'][i], '%.2f' % o[0],'(expected %.2f)' % dataset['output'][i])
        printErrorGraph()

_input = new_array(0,n)
_output = new_array(0,m)
_weights = new_array_(1,m,n)
new_weights()

epochs = 250
lrate=.1
momentum=.1

# Example 1 : OR logical function
# -------------------------------------------------------------------------
print ("Learning the OR logical function")
or_dataset = [
    { "input" : (0,0) , "output" : 0 },
    { "input" : (1,0) , "ouput" : 1 },
    { "input" : (0,1) , "output" : 1 },
    { "input" : (1,1) , "output" : 1 }
]
learn(or_dataset)