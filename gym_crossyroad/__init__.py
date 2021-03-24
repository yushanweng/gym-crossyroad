from gym.envs.registration import register
 
register(id='CrossyRoad-v0', 
    entry_point='gym_crossyroad.envs:CrossyRoadEnv', 
)
