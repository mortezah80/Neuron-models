from pymonntorch import Behavior
import numpy as np

class SetCurrent(Behavior):
	def initialize(self, ng):
		self.offset = self.parameter("value")
		self.s_current = self.parameter("s_current")
		self.e_current = self.parameter("e_current")
	def forward(self, ng):
		if ng.network.iteration * ng.network.dt > self.e_current:
			ng.I = ng.vector(mode=0)
		elif ng.network.iteration * ng.network.dt > self.s_current:
			ng.I = ng.vector(mode=self.offset)
		else:
			ng.I = ng.vector(mode=0)
		# ng.I += ng.vector(mode="normal(0,10)")
		# ng.I += ng.vector(mode="normal(0, 4)")

	# def forward(self, ng):
	# 	ng.I.fill_(self.offset)


class StepFunction1(Behavior):
	def initialize(self, ng):
		self.value = self.parameter("value")
		self.t0 = self.parameter("t0")
		self.t1 = self.parameter("t1")
		ng.I = ng.vector(mode=self.value)

	def forward(self, ng):
		if ng.network.iteration * ng.network.dt > self.t0:
			ng.I += ng.vector(mode=self.value)* ng.network.dt


class StepFunction2(Behavior):
	def initialize(self, ng):
		self.value = self.parameter("value")
		self.t0 = self.parameter("t0")
		self.t1 = self.parameter("t1")
		ng.I = ng.vector(mode=0)

	def forward(self, ng):
		if ng.network.iteration * ng.network.dt > self.t0:
			sin_temp = np.sin(ng.network.iteration/3) * self.value
			ng.I = ng.vector(mode=float(sin_temp))


class StepFunction(Behavior):
	def initialize(self, ng):
		self.value = self.parameter("value")
		self.t0 = self.parameter("t0")
		self.t1 = self.parameter("t1")
		self.t2 = self.parameter("t2")
		self.t3 = self.parameter("t3")
		self.t4 = self.parameter("t4")
		ng.I = ng.vector(mode=0)

	def forward(self, ng):
		if ng.network.iteration * ng.network.dt > self.t4:
			sin_temp = np.sin(ng.network.iteration/10)*100
			ng.I = ng.vector(mode=float(sin_temp))
		elif ng.network.iteration * ng.network.dt == self.t4:
			ng.I = ng.vector(mode=0)


		elif ng.network.iteration * ng.network.dt > self.t3:
			ng.I += ng.vector(mode=10) * ng.network.dt
		elif ng.network.iteration * ng.network.dt == self.t3:
			ng.I = ng.vector(mode=0)

		elif ng.network.iteration * ng.network.dt > self.t2:
			sin_temp = np.sin(ng.network.dt)
			ng.I = ng.vector(mode=60)
		elif ng.network.iteration * ng.network.dt == self.t2:
			ng.I = ng.vector(mode=0)

		elif ng.network.iteration * ng.network.dt > self.t1:
			ng.I = ng.vector(mode=0)
		elif ng.network.iteration * ng.network.dt == self.t1:
			ng.I = ng.vector(mode=20)

		elif ng.network.iteration * ng.network.dt > self.t0:
			ng.I = ng.vector(mode=0)

		elif ng.network.iteration * ng.network.dt == self.t0:
			# ng.I += ng.vector(mode=self.value) * ng.network.dt
			ng.I = ng.vector(mode=10)
			pass
		# if ng.network.iteration * ng.network.dt%0.01==0:
		# ng.I += ng.vector(mode="normal(0,4)")