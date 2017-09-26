def find_word(board, word):
	# write your code here
	if not word: return True
	R = len(board)
	if not R: return False

	C = len(board[0])

	visited = [[False] * C for _ in xrange(R)]
	def fit(r, c, word, idx):
		visited[r][c] = True

		if idx == len(word)-1:
			# print 'fit', r, c, word, idx
			return True
		else:
			for dr, dc in ( (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1) ):
				nr, nc = r + dr, c + dc
				if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == word[idx+1] and not visited[nr][nc] and fit(nr, nc, word, idx+1):
					return True

		visited[r][c] = False
		return False

	for r in xrange(R):
		for c in xrange(C):
			if board[r][c] == word[0]:
				if fit(r, c, word, 0):
					return True

	return False

import Test

testBoard = [
  ["E","A","R","A"],
  ["N","L","E","C"],
  ["I","A","I","S"],
  ["B","Y","O","R"]
]

Test.expect( find_word( testBoard, "C" ) == True )
Test.expect( find_word( testBoard, "EAR" ) == True )
Test.expect( find_word( testBoard, "EARS" ) == False )
Test.expect( find_word( testBoard, "BAILER" ) == True )
Test.expect( find_word( testBoard, "RSCAREIOYBAILNEA" ) == True)
Test.expect( find_word( testBoard, "CEREAL" ) == False)
Test.expect( find_word( testBoard, "ROBES" ) == False)
