import winsound
duration = 1000  # milliseconds
freq = 2000  # Hz
winsound.Beep(freq, duration)

for j in range(1, 10):
    # Loop for 1 through 10 hidden layers
    for i in range(1, 10):
        print("{} neurons:".format(i))
        # Loop for 1 through 10 neurons per hidden layer

        # Load MNIST data
        import mnist_loader
        training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
        training_data = list(training_data)

        # Load network
        import network

        # Initialise network structure
        # Array [784, i, i, ..., 10] shows the number of neurons
        # in each layer of the network in order
        net = network.Network([784, i, i, ... j times ..., i, 10])

        # Perform stochastic gradient descent on the initialised
        # network for 10 epochs and with a learning rate of 3
        net.SGD(training_data, 10, 10, 3.0, test_data=test_data)

print("done")
winsound.Beep(freq, duration)
winsound.Beep(freq, duration)
