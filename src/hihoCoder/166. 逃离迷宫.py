import sys

from StringIO import StringIO
sys.stdin = StringIO("""4 4 2 0 0 0 3
.A.B
.#..
.#..
.#..
3 0
3 3""")

# real code bellow

import sys
from collections import deque

R, C, K, a, b, c, d = map(int, sys.stdin.readline().strip().split())
locks = []

grid = []
for r in xrange(R):
	row = sys.stdin.readline().strip()
	grid.append(row)

for _ in xrange(K):
	locks.append(tuple(map(int, sys.stdin.readline().strip().split())))

beginPos, endPos = (a, b), (c, d)
keyPoses = [(a, b), (c, d)]
locked = []
for r in xrange(R):
	for c in xrange(C):
		if grid[r][c] not in '.#': # this is a locked room
			locked.append( (grid[r][c], r, c) )
locked.sort()
locked = [(r, c) for _, r, c in locked]
assert len(locked) == len(locks)

# print locks, locked
for pos in locked:
	if pos not in (beginPos, endPos): keyPoses.append(pos)

for pos in locks:
	if pos not in (beginPos, endPos): keyPoses.append(pos)


# print 'keyPoses', keyPoses
# assert len(keyPoses) == len(set(keyPoses))
keyPosToIndex = {pos: i for i, pos in enumerate(keyPoses)}
N = len(keyPoses)
INFINITY = float('inf')
Q = deque()
keyDist = [[INFINITY] * N for _ in xrange(N)]

for i in xrange(N):
	pr, pc = keyPoses[i]
	mindist = [ [INFINITY] * C for _ in xrange(R) ]
	mindist[pr][pc] = 0
	Q.append( (pr, pc) )

	while Q:
		r, c = Q.popleft()
		if (r, c) in keyPosToIndex: # this is a key pos
			keyDist[i][keyPosToIndex[(r, c)]] = mindist[r][c]

		if grid[r][c] != '.' and (r, c) != (pr, pc): # ABCD...
			continue

		if r > 0 and mindist[r-1][c] == INFINITY and grid[r-1][c] != '#':
			mindist[r-1][c] = mindist[r][c] + 1
			Q.append( (r-1, c))

		if r < R-1 and mindist[r + 1][c] == INFINITY and grid[r + 1][c] != '#':
			mindist[r + 1][c] = mindist[r][c] + 1
			Q.append((r + 1, c))

		if c > 0 and mindist[r][c-1] == INFINITY and grid[r][c-1] != '#':
			mindist[r][c-1] = mindist[r][c] + 1
			Q.append((r, c-1))

		if c < C-1 and mindist[r][c+1] == INFINITY and grid[r][c+1] != '#':
			mindist[r][c+1] = mindist[r][c] + 1
			Q.append((r, c+1))

lockedBy = [-1] * N
lockingIndex = [-1] * N
for i, pos in enumerate(locked):
	lockedIndex = keyPosToIndex[pos]
	lockIndex = keyPosToIndex[locks[i]]
	lockedBy[lockedIndex] = lockIndex
	lockingIndex[lockIndex] = lockedIndex

# print 'lockedBy', lockedBy, 'lockingIndex', lockingIndex


# now backtracking on all key poses
path = [0]
used = [False] * N
used[0] = True
pathDist = 0
minPathDist = INFINITY
keyPosLocked = [lockedBy[_] != -1 for _ in xrange(N)]
# print 'keyPosLocked', keyPosLocked
def bt():
	global minPathDist, pathDist
	#  'bt', path, keyDist
	if path[-1] == 1: # index 1 is always the end pos
		# print 'found path', path, pathDist
		if pathDist < minPathDist:
			minPathDist = pathDist
		return

	# choose among all possible key positions for the next pos in path
	lastPos = path[-1]
	for i, _used in enumerate(used):
		if _used or keyPosLocked[i] or keyDist[lastPos][i] == INFINITY: continue
		# use this not used and not locked pos
		used[i] = True
		path.append(i)
		unlockIndex = lockingIndex[i]
		if unlockIndex != -1:
			keyPosLocked[unlockIndex] = False

		pathDist += keyDist[lastPos][i]

		bt()

		pathDist -= keyDist[lastPos][i]
		if unlockIndex != -1:
			keyPosLocked[unlockIndex] = True

		path.pop()
		used[i] = False

bt()

print minPathDist if minPathDist != INFINITY else -1
