 
from math import sqrt

users ={"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, 
					"Norah Jones": 4.5, "Phoenix": 5.0, 
					"Slightly Stoopid": 1.5, 
					"The Strokes": 2.5, "Vampire Weekend": 2.0},
		"Bill": 	{"Blues Traveler": 2.0, "Broken Bells": 3.5, 
					"Deadmau5": 4.0, "Phoenix": 2.0, 
					"Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}, 
		"Chan": 	{"Blues Traveler": 5.0, "Broken Bells": 1.0, 
					"Deadmau5": 1.0, "Norah Jones": 3.0, 
					"Phoenix": 5, "Slightly Stoopid": 1.0}, 
		"Dan":		{"Blues Traveler": 3.0, "Broken Bells": 4.0, 
					"Deadmau5": 4.5, "Phoenix": 3.0, 
					"Slightly Stoopid": 4.5, "The Strokes": 4.0, 
					"Vampire Weekend": 2.0}, 
		"Hailey": 	{"Broken Bells": 4.0, "Deadmau5": 1.0, 
					"Norah Jones": 4.0, "The Strokes": 4.0, 
					"Vampire Weekend": 1.0}, 
		"Jordyn": 	{"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, 
					"Phoenix": 5.0, "Slightly Stoopid": 4.5, 
					"The Strokes": 4.0, "Vampire Weekend": 4.0}, 
		"Sam": 		{"Blues Traveler": 5.0, "Broken Bells": 2.0, 
					"Norah Jones": 3.0, "Phoenix": 5.0, 
					"Slightly Stoopid": 4.0, "The Strokes": 5.0}, 
		"Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, 
					"Phoenix": 4.0, "Slightly Stoopid": 2.5, 
					"The Strokes": 3.0}}


def manhattan(rating1, rating2):
	"""Computes the Manhattan distance. Both rating1 and rating2 are dictionaries of the form
	{'THe Strokes': 3.0, 'Slightly': 2.5 ...}"""

	distance = 0
	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key] - rating2[key])
	return distance

def computeNearestNeighbor(username, users):
	"""creates a sorted list of users based on their distance to username"""

	distances = []
	for user in users:
		if user != username:
			distance = manhattan(users[user], users[username])
			distances.append((distance, user))
	distances.sort()
	return distances

def recommend(username, users):
	"""Give list of recommendations"""
	# first find nearest neighbor
	nearest = computeNearestNeighbor(username, users) [0][1]
	recommendations = []
	# Find bands neighbor rated that user didn't
	neighborRatings = users[nearest]
	userRatings = users[username]
	for artist in neighborRatings:
		if not artist in userRatings:
			recommendations.append((artist, neighborRatings[artist]))

	return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)

def minkowski(rating1, rating2, r):
	"""Computes the Minkowski distance Both rating1 and rating2 are dictionaries"""

	distance = 0
	commonRatings = False
	for key in rating1:
		if key in rating2:
			distance += pow(abs(rating1[key] - rating2[key]), r)
			commonRatings = True
	if commonRatings:
		return pow(distance, 1/r)
	else:
		return 0 # Indicates no rating in common

""" Alter the computeNearestNeighbor functino to use Minkowski distance """
# distance = minkowski(users[user], users[username], 2)