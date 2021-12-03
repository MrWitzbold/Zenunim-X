import discord
import time
import math
import random

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
                    weights[i].append((random.randint(0, 99)/100))
        else:
            neurons_aux = neurons_file.replace(" ", "").replace("[", "").replace("]", "").split(",")
            for i in range(0, len(neurons_aux)):
                neurons.append(float(neurons_aux[i]))
    
            weight_matrix_lines = weights_file.replace(" ", "").replace("[", "").split("]")
            print("\nweight matrix lines: " + str(weight_matrix_lines))
    
            for i in range(0, 820):
                current_weight_line = weight_matrix_lines[i]
                matrix_aux = current_weight_line.replace("[", "").replace("]", "").replace("'", "").split(",")
                matrix_line = []
                if len(matrix_aux) == 821:
                    del matrix_aux[0]
                print("\n\nMatrix aux of size " + str(len(matrix_aux)) + ": " + str(matrix_aux))
                for i in range(0, len(matrix_aux)):
                    matrix_line.append(float(matrix_aux[i]))
                weights.append(matrix_line)

        def save_state():
            file1 = open("weights.txt", "w")
            file1.write(str(weights))
            file2 = open("neurons.txt", "w")
            file2.write(str(neurons))
            file1.close()
            file2.close()

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

        def train(inputs, outputs, iterations):
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
    
                    for neuron_index in range(0, len(neuron_layers[0])):
                        neurons[neuron_index] = sigmoid(ord(input_[(neuron_index) % len(input_)])) # loop inside the input
                        
                    for layer in range(1, len(neuron_layers)): # remember that the neuron layers simply contain the indexes of the neurons
                        print("layer: " + str(layer))
                        for neuron_index in neuron_layers[layer]:
                            neuron_value = 0
                            for neuron_index_2 in range(0, len(neuron_layers[layer-1])):
                                neuron_value += neurons[neuron_index_2] * weights[neuron_index][neuron_index_2]
                            neurons[neuron_index] = sigmoid(neuron_value)
    
                    # Feed forward is over, now we're on the backpropagation
    
                    # First we'll calculate the error of the output layer
    
                    neural_output = neurons[len(neurons)-1]
    
                    error = ((neural_output - sigmoid(output))**2)/2
                    print("error = " + str(error))
                    print("Iteration  " + str(j) + " out of " + str(len(inputs)))
                    print(weights)
                    learning_rate = 0.0001
                    for line in range(0, len(weights)):
                        for column in range(0, len(weights[line])):
                            if weights[line][column] == 0:
                                weights[line][column] = 0.1
                            weights[line][column] = weights[line][column] - learning_rate*(error/weights[line][column])
                    
                save_state()

        def get_output(input_):
            def sigmoid(number):
                result = number/(math.sqrt(1 + number**2))
                return result
            
            def unsigmoid(x):
                print("Getting value for: " + str(abs(x)))
                result = abs(math.sqrt((0-x**2)/(x**2 - 1)))
                return result

            for neuron_index in range(0, len(neuron_layers[0])):
                        neurons[neuron_index] = sigmoid(ord(input_[(neuron_index) % len(input_)])) # loop inside the input
                        
            for layer in range(1, len(neuron_layers)): # remember that the neuron layers simply contain the indexes of the neurons
                print("layer: " + str(layer))
                for neuron_index in neuron_layers[layer]:
                    neuron_value = 0
                    for neuron_index_2 in range(0, len(neuron_layers[layer-1])):
                        neuron_value += neurons[neuron_index_2] * weights[neuron_index][neuron_index_2]
                    neurons[neuron_index] = sigmoid(neuron_value)

            neural_output = int(str(((unsigmoid(neurons[len(neurons)-1]))))[6] + str(((unsigmoid(neurons[len(neurons)-1]))))[7])
            print("Result before thing: " + str(((unsigmoid(neurons[len(neurons)-1])))))
            print("Result: " + str(neural_output))
            return neural_output

        self.train = train
        self.get_output = get_output

neural_network_for_text = text_neural_network()

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    guild = message.channel.guild
    global neural_network_for_text
    if str(message.content).split(" ")[0] == ";train" and str(message.author.id) == "774498932696547329": # takes iterations argument
        await message.channel.send("Starting training")
        print("Starting training")
        # idea: use some functions outside the whole discord thing to make the neural network
        # to update it, to write it to files etc
        # after you make some of the functions, start using them here to test
        bans = await guild.bans()
        usernames = []
        percentages = []
        iterations = round(int(str(message.content).split(" ")[1])/2)
        for ban in bans:
            if iterations == 0:
                break
            usernames.append(str(ban[1]).split("#")[0])
            iterations -= 1

        for username in usernames:
            percentages.append(100)

        amount_of_users = len(usernames)
        iterations_ = 0
        for member in guild.members:
            iterations_ += 1
            if iterations_ == amount_of_users:
                break
            member_name = str(member).split("#")[0]
            percentages.append(0)
            usernames.append(member_name)
        neural_network_for_text.train(usernames, percentages, 2)
        await message.channel.send("Finished training")
    
    if str(message.content).split(" ")[0] == ";scan-user":
        user_mention = str(message.content).split(" ")[1].replace("<@!", "").replace(">", "")
        username = str(message.guild.get_member(int(user_mention))).split("#")[0]
        await message.channel.send("Scanning " + username + "...")
        await message.channel.send(str(neural_network_for_text.get_output(username)) + "% evil")

    if str(message.content).split(" ")[0] == ";scan-all":
        await message.channel.send("Scanning server wickedness...")
        users = 0
        percentages = 0
        for member in guild.members:
            username = str(member).split("#")[0]
            percentages += neural_network_for_text.get_output(username)
            users += 1
        average = percentages/users
        await message.channel.send("This server is " + str(average) + "% evil")

    if str(message.content).split(" ")[0] == ";users-more-wicked-than":
        await message.channel.send("Scanning users...")
        wickedness = 60
        wicked_users = 0
        try:
            wickedness = int(str(message.content).split(" ")[1])
        except Exception as e:
            await message.channel.send("Invalid number, using 60 instead, ya dummy")

        for member in guild.members:
            username = str(member).split("#")[0]
            if neural_network_for_text.get_output(username) > wickedness:
                wicked_users += 1

        await message.channel.send("There are " + str(wicked_users) + " users more evil than " + str(wickedness) + "%")





        
        

token = open("token.txt", "r").read()
client.run(token, bot=True)
