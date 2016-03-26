import time
import random
from sense_hat import SenseHat

class Firework():
	
	def __init__(self):
		self.pos = [random.randint(1,6), 0]
		self.color = [255, 255, 255]
		self.vert_speed = 1
		self.horz_speed = 0
		self.explode = False
		
	def animate(self):
		if self.pos[1] < 4:
			self.pos[0] = self.pos[0] + self.horz_speed
			self.pos[1] = self.pos[1] + self.vert_speed
		else:
			if not self.explode:
				self.burst = Burst(self.pos[:], self.color[:])
				self.explode = True
			self.burst.animate()
		
	def render(self, sensehat):
		if not self.explode:
			sensehat.set_pixel(self.pos[0], self.pos[1], self.color[0], self.color[1], self.color[2])
		else:
			self.burst.render(sensehat)

class Burst():

	def __init__(self, pos):
		self.pos = pos
		self.color = [random.choice([0,255]), random.choice([0,255]), random.choice([0,255])]
		self.vert_speed = 0
		self.horz_speed = 0
		self.particle_count = 10;
		self.particle = []
		self.create_particles();
		
	def create_particles(self):
		for i in range(0, self.particle_count):
			self.particle.append(Particle(self.pos[:], self.color[:]))
		
	def animate(self):
		for i in range(0, self.particle_count):
			self.particle[i].animate()
			
	def render(self, sensehat):
		for i in range(0, self.particle_count):
			self.particle[i].render(sensehat)
		
class Particle():

	def __init__(self, pos, color):
		self.pos = pos
		self.color = color
		self.vert_speed = random.randint(-1,0,1)
		if self.vert_speed == 0:
			self.horz_speed = random.randint(-1,1)
		else:
			self.horz_speed = random.randint(-1,0,1)
	def animate(self):
		self.pos[0] = self.pos[0] + self.horz_speed
		self.pos[1] = self.pos[1] + self.vert_speed
		
	def render(self, sensehat):
		if self.pos[0] < 0 or self.pos[0] > 7 or self.pos[1] < 0 or self.pos[1] > 7:
			return
		sensehat.set_pixel(self.pos[0], self.pos[1], self.color[0], self.color[1], self.color[2])
		
		
sense = SenseHat()
fw = []
fw_count = 9
frame_count = 0

for i in range(0, fw_count):
	fw.append(Firework())
	
while True:
	sense.clear()
	for i in range(0, fw_count):
		if (frame_count > i * 10) {
			fw[i].animate()
			fw[i].render(sense)
		}
	time.sleep(0.35)
	