import time
import random
from sense_hat import SenseHat

sense = SenseHat()


class Firework():
	
	def __init__(self):
		self.pos = [random.randint(1,6), 0]
		self.color = [random.choice([0,255]), random.choice([0,255]), random.choice([0,255])]
		self.vert_speed = 1
		self.horz_speed = 0
		self.explode = False
		
	def animate(self):
		if self.pos[1] < 5:
			self.pos[0] = self.pos[0] + self.horz_speed
			self.pos[1] = self.pos[1] + self.vert_speed
		else:
			if !self.explode:
				self.burst = Burst(self.pos)
				self.explode = True
			self.burst.animate()
		
	def render(self, sensehat):
		if !self.explode:
			sensehat.set_pixel(self.pos[0], self.pos[1], self.color[0], self.color[1], self.color[2])
		else:
			self.burst.render()

class Burst():

	def __init__(self):
		self.pos = [0,0]
		self.color = [0,0,0]
		self.vert_speed = 0
		self.horz_speed = 0
		self.particle_count = 5;
		self.create_particles();
		
	def create_particles(self):
		for i in range(0, particle_count):
			self.particle[i] = Particle(self.pos)
		
	def animate(self):
		for i in range(0, particle_count):
			self.particle[i].animate()
			
	def render(self, sensehat):
		for i in range(0, particle_count):
			self.particle[i].render(sensehat)
		
class Particle():

	def __init__(self, pos):
		self.pos = pos
		self.color = [0,0,0]
		self.vert_speed = random.randint(-1,1)
		self.horz_speed = random.randint(-1,1)
		
	def animate(self):
		self.pos[0] = self.pos[0] + self.horz_speed
		self.pos[1] = self.pos[1] + self.vert_speed
		
	def render(self, sensehat):
		if self.pos[0] < 0 or self.pos[0] > 7 or self.pos[1] < 0 or self.pos[1] > 7:
			return
		sensehat.set_pixel(self.pos[0], self.pos[1], self.color[0], self.color[1], self.color[2])
		
fw = Firework()	
while True:
	sense.clear()
	fw.animate()
	fw.render(sensehat)
	sense.set_rotation(180)
	