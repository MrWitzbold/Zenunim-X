import discord
import time
import math

# next thing to do: training function with list of inputs and outputs
# use ord() to get the ASCII value of a character

class text_neural_network():
    def __init__(self):
        neuron_layers = []
        neurons_ever = 0
        for i in range(0, 40):
            layer = 40 - i
            current_neurons = []
            for j in range(0, layer):
                current_neurons.append(j + neurons_ever)
            neurons_ever += layer
            neuron_layers.append(current_neurons)

        print("Neuron layers: " + str(neuron_layers))
        print("Amount of layers: " + str(len(neuron_layers)))
        print("Neurons ever: " + str(neurons_ever))

        first_time_executing = False
        weights_file = 0
        neurons_file = 0
    
        weights = []
        neurons = []
    
        # every layer has 40 - i neurons
        # so the second layer has 39 neurons
        # the thirst has 38
        # etc...
    
        try:
            weights_file = open("weights.txt", "r").read()
            neurons_file = open("neurons.txt", "r").read()
        except Exception as ex:
            print(str(ex))
            first_time_executing = True
        
        if first_time_executing:
            for i in range(0, 820): # i tested it, it's correct
                neurons.append(0.1)
                weights.append([])
            for i in range(0, len(weights)):
                for i in range(0, 820):
                    weights[i].append(0.1)
        else:
            neurons_aux = neurons_file.replace(" ", "").replace("[", "").replace("]", "").split(",")
            for i in range(0, len(neurons_aux)):
                neurons.append(float(neurons_aux[i]))
    
            weight_matrix_lines = weights_file.replace(" ", "").replace("[", "").split("]")
    
            for i in range(0, 820):
                current_weight_line = weight_matrix_lines[i]
                matrix_aux = current_weight_line.replace("[", "").replace("]", "").split(",")
                matrix_line = []            
                for i in range(0, len(matrix_aux)):
                    matrix_line.append(float(matrix_aux[i]))
                weights.append(matrix_line)

        self.weights = weights
        self.neurons = neurons
        self.neuron_layers = neuron_layers

        def save_state(self):
            open("weights.txt", "w").write(str(self.weights))
            open("neurons.txt", "w").write(str(self.neurons))

        def get_neuron_layer(self, neuron):
            for i in range(0, len(self.neuron_layers)):
                if neuron in self.neuron_layers[i]:
                    return i
    
        def is_connected(self, neuron1, neuron2):
            if get_neuron_layer(neuron1) == get_neuron_layer(neuron2):
                return False
            if get_neuron_layer(neuron1) > get_neuron_layer(neuron2): # If it's ahead, then it needs to know if the other one is right behind it
                if neuron2 in self.neuron_layers[get_neuron_layer(neuron1)-1]:
                    return True
            if get_neuron_layer(neuron1) < get_neuron_layer(neuron2): # If it's beind, then the other one needs to check if it's right in front of it
                if neuron1 in self.neuron_layers[get_neuron_layer(neuron2)-1]:
                    return True

        def train(self, inputs, outputs, iterations):
            neurons = self.neurons
            weights = self.weights
            neuron_layers = self.neuron_layers

            def sigmoid(number):
                result = number/(math.sqrt(1 + number**2))
                return result
            
            def unsigmoid(x):
                print("Getting value for: " + str(abs(x)))
                result = abs(math.sqrt((0-x**2)/(x**2 - 1)))
                return result

            for i in range(0, iterations):
                print("Iteration: " + str(i))

                # The values from the inputs to the first 40 neurons, we're gonna pass panually
                # For the values of the next neurons, we'll use a function that says which neurons
                # are connected to the current neuron
                # and a function to get the connections' respective weights from the matrix

                for j in range(0, len(inputs)):
                    input_ = inputs[j]
                    output = outputs[j]
    
                    # First we'll pass the input values to the first 40 neurons
    
                    for neuron_index in range(0, len(neurons[0])):
                        neurons[0][neuron_index] = sigmoid(ord(input_[(neuron_index) % len(input_)])) # loop inside the input
                        
                    print("Initial neurons: " + str(neurons[0]))
    
                    for layer in range(1, len(neuron_layers)): # remember that the neuron layers simply contain the indexes of the neurons
                        for neuron_index in range(0, len(neuron_layers[layer])):
                            neuron_value = 0
                            for neuron_index_2 in range(0, len(neuron_layers[layer-1])):
                                neuron_value += neurons[layer-1][neuron_index_2] * weights[neuron_index][neuron_index_2]
                            neurons[layer][neuron_index] = neuron_value
                    
                    print("Trained neurons: " + str(neurons))
    
                    # Feed forward is over, now we're on the backpropagation
    
                    # First we'll calculate the error of the output layer
    
                    neural_output = neurons[len(neurons)]
    
                    error = ((neural_output - sigmoid(output))**2)/2

                    learning_rate = 0.0001

                    for line in range(0, len(weights)):
                        for column in range(0, len(weights[line])):
                            weights[line][column] -= weights[line][column] - learning_rate*(error/weights[line][column])
                    
                    save_state()


                







client = discord.Client()

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    if str(message.content).split(" ")[0] == ";train":
        print("Starting training")
        # idea: use some functions outside the whole discord thing to make the neural network
        # to update it, to write it to files etc
        # after you make some of the functions, start using them here to test
        neural_network_for_text = text_neural_network()
        

token = open("token.txt", "r").read()
client.run(token, bot=True)
