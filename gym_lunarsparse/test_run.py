import gym
import gym_lunarsparse

env = gym.make("lunarsparse-v0")
observation = env.reset()

for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  observation, reward, done, info = env.step(action)
  print('Reward is %f' % reward)

  if done:
    observation = env.reset()
env.close()
