def solve(board):
	R = [0x1ff] * 9

	C = [0x1ff] * 9
	B = [0x1ff] * 9
	solution = [[0] * 9 for _ in xrange(9)]
	for r in xrange(9):
		for c in xrange(9):
			v = solution[r][c] = board[r][c]

			if v == 0: continue

			R[r] &= ~(1 << (v - 1))
			C[c] &= ~(1 << (v - 1))
			b = r // 3 * 3 + c // 3

			B[b] &= ~(1 << (v - 1))
	#
	# print R
	# print C
	# print B

	def next(r, c):
		if c < 8:
			return r, c+1
		else:
			return r+1, 0

	def bt(r, c):
		if r == 9:
			# print 'SOLUTION FOUND'
			return True

		if solution[r][c] == 0:
			b = r // 3 * 3 + c // 3

			possible = R[r] & C[c] & B[b]
			if possible == 0: # bt fail to continue
				return False

			for i in xrange(9):
				m = (1 << i)
				if possible & m:
					solution[r][c] = i+1
					R[r] &= ~m
					C[c] &= ~m
					B[b] &= ~m

					if bt(*next(r, c)): # if solved
						return True

					R[r] |= m
					C[c] |= m
					B[b] |= m

			solution[r][c] = 0
		else:
			return bt(*next(r, c))

	solved = bt(0, 0)
	return solution

	# possible = [ [0] * 9 for _ in xrange(9)]
	# for r in xrange(9):
	# 	for c in xrange(9):
	# 		b = r // 3 * 3 + c // 3
	# 		possible[r][c] = R[r] & C[c] & B[b]
	#
	# print 'possible:'
	# for r in possible:
	# 	print map(lambda v: '{0:09b}'.format(v), r )

problem = [[9, 0, 0, 0, 8, 0, 0, 0, 1],
 [0, 0, 0, 4, 0, 6, 0, 0, 0],
 [0, 0, 5, 0, 7, 0, 3, 0, 0],
 [0, 6, 0, 0, 0, 0, 0, 4, 0],
 [4, 0, 1, 0, 6, 0, 5, 0, 8],
 [0, 9, 0, 0, 0, 0, 0, 2, 0],
 [0, 0, 7, 0, 3, 0, 2, 0, 0],
 [0, 0, 0, 7, 0, 5, 0, 0, 0],
 [1, 0, 0, 0, 4, 0, 0, 0, 7]]

solution = solve(problem)
print 'SOLUTION: '
for r in solution:
	print r