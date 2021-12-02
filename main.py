import discord
import time

class __text_neural_network():
    def __init__(self):
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
                neurons.append(0)
                weights.append([])
            for i in range(0, len(weights)):
                for i in range(0, 820):
                    weights[i].append(0)
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

    def save_state(self):
        open("weights.txt", "w").write(str(self.weights))
        open("neurons.txt", "w").write(str(self.neurons))





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
        

token = open("token.txt", "r").read()
client.run(token, bot=True)
