# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.

def Q17_Normal(M):
	R = len(M)
	if R == 0: return
	C = len(M)

	rowHasZero = [False] * R
	colHasZero = [False] * C
	for r in xrange(R):
		for c in xrange(C):
			if M[r][c] == 0:
				rowHasZero[r] = True
				colHasZero[c] = True

	for r, hasZero in enumerate(rowHasZero):
		if hasZero:
			M[r][:] = [0] * C
	for c, hasZero in enumerate(colHasZero):
		if hasZero:
			for r in xrange(R):
				M[r][c] = 0

def Q17_NoExtraSpace(M):
	R = len(M)
	if R == 0: return
	C = len(M)

	clearFirstRow = False
	clearFirstCol = False

	for r in xrange(R):
		for c in xrange(C):
			if M[r][c] == 0:
				if r == 0:
					clearFirstRow = True
				else:
					M[r][0] = 0
				if c == 0:
					clearFirstCol = True
				else:
					M[0][c] = 0

	for r in xrange(1, R):
		if M[r][0] == 0:
			M[r][:] = [0] * C

	for c in xrange(1, C):
		if M[0][c] == 0:
			for r in xrange(R):
				M[r][c] = 0

	if clearFirstRow:
		M[0][:] = [0] * C
	if clearFirstCol:
		for r in xrange(R):
			M[r][0] = 0


M = [
	[0,2,3],
	[4,1,6],
	[6,7,3]
]
Q17_NoExtraSpace(M)
for r in M:
	print r


