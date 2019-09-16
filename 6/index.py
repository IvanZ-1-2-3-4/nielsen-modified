import winsound
duration = 1000  # milliseconds
freq = 2000  # Hz
winsound.Beep(freq, duration)

for i in range(1, 10):
    import mnist_loader
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    training_data = list(training_data)
    import network
    print("{} neurons:".format(i))
    net = network.Network([784, i, i, i, i, i, i, 10])
    net.SGD(training_data, 10, 10, 3.0, test_data=test_data)

print("done")
winsound.Beep(freq, duration)
winsound.Beep(freq, duration)
