import gym
from gym import error, spaces, utils
from gym.utils import seeding

class CrossyRoadEnv(gym.Env):
  metadata = {'render.modes': ['human']}

#   def __init__(self):
#     ...
#   def step(self, action):
#     ...
#   def reset(self):
#     ...
#   def render(self, mode='human'):
#     ...
#   def close(self):
#     ...

def __init__(self):
        self.action_space = gym.spaces.Discrete(5)
        self.observation_space = gym.spaces.Discrete(2)
def step(self, action):
        state = 1
    
        if action == 2:
            reward = 1
        else:
            reward = -1
            
        done = True
        info = {}
        return state, reward, done, info
def reset(self):
        state = 0
        return state


