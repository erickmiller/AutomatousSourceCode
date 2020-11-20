import numpy as _np

class Rectangle(object):
	def __init__(self,rect=None):
		self._rect = rect

	def _get_sorted_x(self):
		x_a = self._rect.get_y()
		x_b = x_a + self._rect.get_height()
		return _np.sort([x_a,x_b])

	_sorted_x = property(_get_sorted_x)

	def _get_x0(self):
		return self._sorted_x[0]

	def _get_x1(self):
		return self._sorted_x[1]
	
	x0 = property(_get_x0,doc='The smaller x coordinate.')
	x1 = property(_get_x1,doc='The larger x coordinate.')

	def _get_sorted_y(self):
		y_a = self._rect.get_x()
		y_b = y_a + self._rect.get_width()
		return _np.sort([y_a,y_b])

	_sorted_y = property(_get_sorted_y)

	def _get_y0(self):
		return self._sorted_y[0]

	def _get_y1(self):
		return self._sorted_y[1]
	
	y0 = property(_get_y0,doc='The smaller y coordinate.')
	y1 = property(_get_y1,doc='The larger y coordinate.')
