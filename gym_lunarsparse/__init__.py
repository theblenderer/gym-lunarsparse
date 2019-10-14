from gym.envs.registration import register

register(
    id='lunarsparse-v0',
    entry_point='gym_lunarsparse.envs:LunarSparseEnv',
)
register(
    id='lunarsparse-extrahard-v0',
    entry_point='gym_foo.envs:LunarSparseExtraHardEnv',
)