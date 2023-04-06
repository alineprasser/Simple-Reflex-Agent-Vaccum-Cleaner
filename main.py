from time import time
import random

class VacuumCleaner:

    def __init__(self, environment, pos_x):
        self.environment = environment
        self.pos_x = pos_x
        self.size_x = len(environment[0])
        self.pos_cleared = []
        self.spent_energy = 0
        self._energy_values = {
            'move' : 5,
            'clear' : 10,
            'is_dirty' : 1,
            'wait' : 0
        }

    def spendEnergy(self, action):
        self.spent_energy += self._energy_values[action]

    def isDirty(self):
        self.spendEnergy('is_dirty')
        is_dirty = self.environment[0][self.pos_x] == 1
        return is_dirty
    
    def clear(self):
        self.spendEnergy('clear')
        self.environment[0][self.pos_x] = 0
        self.pos_cleared.append(self.pos_x)
    
    def move(self, moveTo):
        if moveTo == 'move_left':
            self.spendEnergy('move')
            self.pos_x -= 1
        elif moveTo == 'move_right':
            self.spendEnergy('move')
            self.pos_x += 1            
    
    def wait(self, seconds):
        self.spendEnergy('wait')
        time.sleep(seconds)
  
    def validActions(self):
        valid_actions = [] #['wait']
        
        if self.isDirty():
            valid_actions += ['clear']
        
        if self.pos_x > 0:
            valid_actions += ['move_left']

        if self.pos_x < self.size_x-1:
            valid_actions += ['move_right']
        
        print(valid_actions)
        return valid_actions

    def executeAction(self, action):
        print('Executando acao (%s)' % action)
        print(self.environment)
        if action == "move_right":
            self.move("move_right")
        elif action == "move_left":
            self.move("move_left")
        elif action == "clear":
            self.clear()
        elif action == "wait":
            self.wait(1)
        else:
            print('Erro: Ação inválida (%s)' % action)

    def run(self, n_times):
        for _ in range(n_times):
            valid_actions = self.validActions()
            action = random.sample(valid_actions, 1)[0]
            self.executeAction(action)
        print(self.pos_cleared) 

  
    def alterMove(self):
      if self.pos_x == 0:
        self.move("move_right")
      else:
        self.move("move_left")
  
    def simpleReflexAgent(self):
      if self.isDirty():
        self.clear()
        self.alterMove()
      elif self.pos_x not in self.pos_cleared:
        self.pos_cleared.append(self.pos_x)
        self.alterMove()

    def runSimpleAgent(self):
      print('Environment inicial: ', self.environment)
      while len(self.pos_cleared) != self.size_x:
        self.simpleReflexAgent()
        print('Rodou agent')
        print('Environment atual: ', self.environment)
      return 0
          

environment = [[1, 0]]
pos_x = 1
vc = VacuumCleaner(environment, pos_x)

vc.runSimpleAgent()