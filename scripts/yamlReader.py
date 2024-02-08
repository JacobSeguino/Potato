import yaml

resourcesPath = "./resources/"

def yamlReader(ymalName, fate):
    with open(resourcesPath + ymalName, 'r') as stream:
        yamlOutput = yaml.safe_load(stream)

        return yamlOutput[fate]
