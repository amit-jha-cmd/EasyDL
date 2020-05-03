

class Generate:
    def __init__(self, structure, framework = "pytorch"):
        # print("PyTorch version: " + )
        self.structure = structure
        self.framework = framework
    
    def log(self):
        print("model structure: ", self.structure)
        print("Framework: ", self.framework)

    def build(self):
        pass
