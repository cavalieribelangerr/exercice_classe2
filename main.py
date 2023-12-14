from random import randint

class NPC:
    def __init__(self, force, agilite, constitution, intelligence, sagesse, charisme):
        self.force = force
        self.agilite = agilite
        self.constitution = constitution
        self.intelligence = intelligence
        self.sagesse = sagesse
        self. charisme = charisme



class Kobold(NPC):
    def __init__(self, force, agilite, constitution, intelligence, sagesse, charime):
        super().__init__(force, agilite, constitution, intelligence, sagesse, charime)


class Heros(NPC):
    def __init__(self, force, agilite, constitution, intelligence, sagesse, charime):
        super().__init__(force, agilite, constitution, intelligence, sagesse, charime)