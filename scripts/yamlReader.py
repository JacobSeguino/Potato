import yaml

resourcesPath = "./resources/"
test1="grassAndMud.yaml"
test2="aKnockAtTheDoor.yaml"
test3="inTheGarden.yaml"

def yamlReader(ymalName, fate):
    with open(resourcesPath + ymalName, 'r') as stream:
        yamlOutput = yaml.safe_load(stream)

        # print(yamlOutput[fate])
        return yamlOutput[fate]

