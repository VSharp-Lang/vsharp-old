# vs_random.py
# Converts random functions in V# to their corresponding functions
# in Python.

def work(content):
    cont = content.replace("System.Random.Int", "random.randint")
    cont = cont.replace("System.Random.ReturnState", "random.getstate")
    cont = cont.replace("System.Random.Seed", "random.seed")
    cont = cont.replace("System.Random.ReturnRandBits", "random.getrandbits")
    cont = cont.replace("System.Random.Range", "random.randrange")
    cont = cont.replace("System.Random.Choice", "random.choice")
    cont = cont.replace("System.Random.Choices", "random.choices")
    cont = cont.replace("System.Random.Shuffle", "random.shuffle")
    cont = cont.replace("System.Random.Sample", "random.sample")
    cont = cont.replace("System.Random.Default", "random.random")
    cont = cont.replace("System.Random.Float", "random.uniform")
    cont = cont.replace("System.Random.Triangular", "random.triangular")
    cont = cont.replace("System.Random.Gammavariate", "random.gammavariate")
    cont = cont.replace("System.Random.Gauss", "random.gauss")
    cont = cont.replace("System.Random.Lognormvariate", "random.lognormvariate")
    cont = cont.replace("System.Random.Vonmisesvariate", "random.vonmisesvariate")
    cont = cont.replace("System.Random.Paretovariate", "random.paretovariate")
    cont = cont.replace("System.Random.Weibullvariate", "random.weibullvariate")
    cont = cont.replace("System.Random.Normalvariate", "random.normalvariate")
    cont = cont.replace("System.Random.Betavariate", "random.betavariate")
    return cont
