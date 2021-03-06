class Path(object):
	"""
	From a array of initial positions and a model, predicts the path of an objet
	"""

	pos_y = None

	def __init__(self, pos_y):
		"""
		params:
			- pos_y : a function that give the y coordinate in function of the x coordinate
		"""

		self.pos_y = pos_y

	def falling_point(self, window, x_0=0, h_limit=0, precision=0.01):
		"""
		Returns the x value of the falling point (when y == h_limit) or None
		if it does no fall within the view of the camera
		
		Uses  a bisect method assuming that there only one zero (or none) in 
		the	function (studied models are free falling objects so it is 
		justified)
		"""

		left, right = x_0, window['width']
		middle = (left + right) / 2

		while abs(right - left) >= precision:

			if (self.pos_y(left) - h_limit)*(self.pos_y(middle) - h_limit) < 0:
				right = middle
			else:
				left = middle

			middle = (left + right) / 2

		return middle