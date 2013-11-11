#!/usr/bin/python

class Trip(object):
	def __init__(self, milePerGallon, distance, pricePerGallon, askName):
		self.milePerGallon = milePerGallon
		self.distance = distance
		self.pricePerGallon = pricePerGallon
		self.askName = askName

	def calculated_price_per_gallon(self):
		return (self.pricePerGallon * self.distance)

	def round_trip(self):
		return (self.distance * 2)

	def say_hi(self):
		self.askName = raw_input("What is your name?")

	def read_float(self):
	#def read_float(self, mpg_text):
		#mpg_text = "Vehicles Advertised Miles Per Gallon: "
		value = float(raw_input("Please enter: "))
		print ('is %f') % (value)

	def mass_multiply(self):
		return (self.distance * self.milePerGallon * self.pricePerGallon)

if __name__ == "__main__":
	#Creating new object
	newTrip = Trip(22, 13.5, 3.27, "Bob")
	newTrip.read_float()
	print newTrip.askName
	print newTrip.pricePerGallon
	print newTrip.milePerGallon
	print newTrip.distance
	print newTrip.mass_multiply()
