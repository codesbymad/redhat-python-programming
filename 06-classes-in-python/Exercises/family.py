class Family:
    def __init__(self, parent1, parent2, *children):
        self.parent1 = parent1
        self.parent2 = parent2
        self.children = list(children)

    def add(self, child):
        self.children.append(child)

    def __str__(self):
        fam = str(self.parent1) + " " + str(self.parent2) + " [\n"
        for child in self.children:
            fam += " - " + str(child) + "\n"
        fam += "]"
        return fam

    def __lt__(self, otherfam):
        return len(self.children) < len(otherfam.children)

    def __gt__(self, otherfam):
            return len(self.children) > len(otherfam.children)

    def __et__(self, otherfam):
            return len(self.children) == len(otherfam.children)