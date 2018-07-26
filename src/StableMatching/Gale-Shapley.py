from collections import deque

class GaleShapley(object):
    def __init__(self, ManPref, WomenPref):
        assert len(ManPref) == len(WomenPref)
        N = self.N = len(ManPref)
        self.ManPref=  ManPref
        self.WomenPref = WomenPref
        self.Ranking = []
        for w in xrange(N):
            r = [-1] * N
            for i, m in enumerate(WomenPref[w]):
                r[m] = i
            self.Ranking.append(r)

    def stableMatch(self):
        N = self.N
        proposeIndex = [0] * N
        freeList = deque(xrange(N))
        engagedTo = [-1] * N
        Ranking = self.Ranking
        while freeList:
            m = freeList.popleft() # get a free man
            assert proposeIndex[m] < N
            w = ManPref[m][proposeIndex[m]]
            proposeIndex[m] += 1
            # let man w propose to women w
            m2 = engagedTo[w]
            assert m2 != m
            if m2 == -1 or Ranking[w][m2] > Ranking[w][m]:
                engagedTo[w] = m
                if m2 != -1:
                    freeList.append(m2)
            else:
                # propose failed, put back to free list
                freeList.append(m)

        return engagedTo

import random
random.seed(1)
N = 10
ManPref, WomenPref = [], []
for m in xrange(N):
    p = range(N)
    random.shuffle(p)
    ManPref.append(p)
    p = range(N)
    random.shuffle(p)
    WomenPref.append(p)

gs = GaleShapley(ManPref, WomenPref)
res = gs.stableMatch()
print 'stable matching result: %s' % res