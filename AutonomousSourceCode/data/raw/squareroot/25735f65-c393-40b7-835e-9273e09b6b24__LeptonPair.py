# Name: LeptonPair.py
#
# CMS Open Data
#
# Description: sums pairs of leptons and gets their mass, energy, momentum and transverse momentum
#
# Returns: 


__author__ = "Palmerina Gonzalez Izquierdo"
__copyright__ = "Copyright (C) 2015 Palmerina G. I."
__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Palmerina Gonzalez"
__email__ = "pgi25@alumnos.unican.es"

import ROOT
import math
import numpy as np
from DataFormats.FWLite import Events, Handle

class LeptonPair(object):

	def __init__(self, l1, l2, vertex):
	 	"""
	 	l1, l2: leptons 
	 	It sums the four-momentums of l1 and l2 and gets their mass, their energy and their transverse momentum
	 	"""

		self.l1 = l1
		self.l2 = l2		
		self.vertex = vertex

 		self.px = self.l1.px()+self.l2.px() #GeV/c
 		self.py = self.l1.py()+self.l2.py()
 		self.pz = self.l1.pz()+self.l2.pz()
		self.energy = self.l1.energy() + self.l2.energy() #GeV

		self.squareEnergy = np.power(self.energy,2)			
	 	self.squareP = np.power(self.px,2) + np.power(self.py,2) + np.power(self.pz,2)
		
	 	#l.px(),l.py(),l.pz() and l.energy() are ROOT methods


	def mass(self):
	 	#invariant mass
		squareM = self.squareEnergy-self.squareP
		if squareM < 0:
			return np.sqrt(-squareM) # con un - en el codigo de TLorentzVector
		else:
			return np.sqrt(squareM) # in natural units (GeV/c**2)
		

	def pt(self):
	 	#Total transverse momentum
	 	return np.sqrt(np.power(self.px,2) + np.power(self.py,2))



	def pt1(self):
	 	# Transverse momentum of lepton 2
	 	return np.sqrt(np.power(self.l1.px(),2) + np.power(self.l1.py(),2))


	def pt2(self):
	 	# Transverse momentum of lepton 2
	 	return np.sqrt(np.power(self.l2.px(),2) + np.power(self.l2.py(),2))


	def eta1(self):
	 	return self.l1.eta()


	def eta2(self):
	 	return self.l2.eta()



	def dB1(self):
		return self.l1.dB(self.l1.PV3D)


	def dB2(self):
		return self.l2.dB(self.l2.PV3D)


	def distance1(self):
		return self.l1.vertex().z()-self.vertex.z()


	def distance2(self):
		return self.l2.vertex().z()-self.vertex.z()








