#!/usr/bin/env python

import sys
import os
import string
import math
import random

infinity = 1000000000.0


class theobj:
    def printit():
        print


def mymax(a, b):
   if a > b:
      return a
   else:
      return b

# C++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++C
# C                                                            C
# C  HIERARCHICAL CLUSTERING using (user-specified) criterion. C
# C                                                            C
# C  Parameters:                                               C
# C                                                            C
# C  DATA(N,M)         input data matrix,                      C
# C  DISS(LEN)         dissimilarities in lower half diagonal  C
# C                    storage; LEN = N.N-1/2,                 C
# C  IOPT              clustering criterion to be used,        C
# C  IA, IB, CRIT      history of agglomerations; dimensions   C
# C                    N, first N-1 locations only used,       C
# C  MEMBR, NN, DISNN  vectors of length N, used to store      C
# C                    cluster cardinalities, current nearest  C
# C                    neighbour, and the dissimilarity assoc. C
# C                    with the latter.                        C
# C  FLAG              boolean indicator of agglomerable obj./ C
# C                    clusters.                               C
# C                                                            C
# C  F. Murtagh, ESA/ESO/STECF, Garching, February 1986.       C
# C                                                            C
# C------------------------------------------------------------C


def hc(n, diss):
    mergelist = ''
   # n is the number of objects to be clustered
#       SUBROUTINE HC(N,M,LEN,IOPT,DATA,IA,IB,CRIT,MEMBR,NN,DISNN,
#      X                FLAG,DISS)
#       REAL DATA(N,M),MEMBR(N),DISS(LEN)
#       INTEGER IA(N),IB(N)
#       REAL CRIT(N)
#       DIMENSION NN(N),DISNN(N)
#       LOGICAL FLAG(N)
#       REAL INF
#       DATA INF/1.E+20/
# C
# C  Initializations
# C
#       DO I=1,N
#          MEMBR(I)=1.
#          FLAG(I)=.TRUE.
#       ENDDO
#       NCL=N
    membr = {}
    flag = {}
    for i in range(n):
       membr[i] = 1
       flag[i] = 1
# C
# C  Construct dissimilarity matrix
# C
#       DO I=1,N-1
#          DO J=I+1,N
#             IND=IOFFSET(N,I,J)
#             DISS(IND)=0.
#             DO K=1,M
#                DISS(IND)=DISS(IND)+(DATA(I,K)-DATA(J,K))**2
#             ENDDO
#             IF (IOPT.EQ.1) DISS(IND)=DISS(IND)/2.
# C           (Above is done for the case of the min. var. method
# C            where merging criteria are defined in terms of variances
# C            rather than distances.)
#           ENDDO
#        ENDDO
# C
# C  Carry out an agglomeration - first create list of NNs
# C
#       DO I=1,N-1
#          DMIN=INF
#          DO J=I+1,N
#             IND=IOFFSET(N,I,J)
#             IF (DISS(IND).GE.DMIN) GOTO 500
#                DMIN=DISS(IND)
#                JM=J
#   500    CONTINUE
#          ENDDO
#          NN(I)=JM
#          DISNN(I)=DMIN
#       ENDDO

    nn = {}
    disnn = {}
    for i in range(n):
       dmin = infinity
       for j in range(n):
          if i == j:
             continue
          if diss[i][j] >= dmin:
             continue
          dmin = diss[i][j]
          jm = j
       nn[i] = jm
       disnn[i] = dmin

# C
#   400 CONTINUE
# C     Next, determine least diss. using list of NNs
#       DMIN=INF
#       DO I=1,N-1
#          IF (.NOT.FLAG(I)) GOTO 600
#          IF (DISNN(I).GE.DMIN) GOTO 600
#             DMIN=DISNN(I)
#             IM=I
#             JM=NN(I)
#   600    CONTINUE
#       ENDDO
#       NCL=NCL-1

    for ncl in range(n-1):
       #print 'ncl',ncl
       dmin = infinity
       for i in range(n):
          if flag[i] == 0:
             continue
          if disnn[i] >= dmin:
             continue
          dmin = disnn[i]
          im = i
          jm = nn[i]

# C
# C  This allows an agglomeration to be carried out.
# C
#       I2=MIN0(IM,JM)
#       J2=MAX0(IM,JM)
#       IA(N-NCL)=I2
#       IB(N-NCL)=J2
#       CRIT(N-NCL)=DMIN

       if jm < im:
          i2 = im
          j2 = jm
       else:
          i2 = jm
          j2 = im

       mergelist += `j2`+ ':' +`i2`+ ' '

# C
# C  Update dissimilarities from new cluster.
# C
#       FLAG(J2)=.FALSE.
#       DMIN=INF
#       DO K=1,N
#          IF (.NOT.FLAG(K)) GOTO 800
#          IF (K.EQ.I2) GOTO 800
#          X=MEMBR(I2)+MEMBR(J2)+MEMBR(K)
#          IF (I2.LT.K) THEN
#                            IND1=IOFFSET(N,I2,K)
#                       ELSE
#                            IND1=IOFFSET(N,K,I2)
#          ENDIF
#          IF (J2.LT.K) THEN
#                            IND2=IOFFSET(N,J2,K)
#                       ELSE
#                            IND2=IOFFSET(N,K,J2)
#          ENDIF
#          IND3=IOFFSET(N,I2,J2)
#          XX=DISS(IND3)

# non complete link methods deleted here

# C
# C  COMPLETE LINK METHOD - IOPT=3.
# C
#          IF (IOPT.EQ.3) THEN
#             DISS(IND1)=MAX(DISS(IND1),DISS(IND2))
#          ENDIF

# non complete link methods deleted here

# C
#          IF (I2.GT.K) GOTO 800
#          IF (DISS(IND1).GE.DMIN) GOTO 800
#             DMIN=DISS(IND1)
#             JJ=K
#   800    CONTINUE
#       ENDDO

       flag[j2] = 0
       dmin = infinity
       for k in range(n):
          if flag[k] == 0:
             continue
          if k == i2:
             continue
          diss[i2][k] = mymax(diss[i2][k], diss[j2][k])
          diss[k][i2] = diss[i2][k]
          if diss[i2][k] >= dmin:
             continue
          dmin = diss[i2][k]
          jj = k

#       MEMBR(I2)=MEMBR(I2)+MEMBR(J2)
#       DISNN(I2)=DMIN
#       NN(I2)=JJ

       disnn[i2] = dmin
       nn[i2] = jj

# C
# C  Update list of NNs insofar as this is required.
# C
#       DO I=1,N-1
#          IF (.NOT.FLAG(I)) GOTO 900
#          IF (NN(I).EQ.I2) GOTO 850
#          IF (NN(I).EQ.J2) GOTO 850
#          GOTO 900
#   850    CONTINUE
# C        (Redetermine NN of I:)
#          DMIN=INF
#          DO J=I+1,N
#             IND=IOFFSET(N,I,J)
#             IF (.NOT.FLAG(J)) GOTO 870
#             IF (I.EQ.J) GOTO 870
#             IF (DISS(IND).GE.DMIN) GOTO 870
#                DMIN=DISS(IND)
#                JJ=J
#   870       CONTINUE
#          ENDDO
#          NN(I)=JJ
#          DISNN(I)=DMIN
#   900    CONTINUE
#       ENDDO

       for i in range(n):
          if flag[i] == 0:
             continue
          if nn[i] != i2 and nn[i] != j2:
             continue
          dmin = infinity
          for j in range(n):
             global innerloopcounter
             innerloopcounter += 1
             #print ncl,i,j
             if flag[j] == 0:
                continue
             if i == j:
                continue
             if diss[i][j] >= dmin:
                continue
             dmin = diss[i][j]
             jj = j
          nn[i] = jj
          disnn[i] = dmin

    return mergelist

# C
# C  Repeat previous steps until N-1 agglomerations carried out.
# C
#       IF (NCL.GT.1) GOTO 400
# C
# C
#       RETURN
#       END


def mycmp(obj1, obj2):
  if obj1.sim > obj2.sim:
    return -1
  else:
    if obj1.sim < obj2.sim:
      return 1
    else:
      return 0


def n2logn(hashobj, sim):
   mergelist = ''
   nextbest = {}
   # this loop takes O(n^2logn):
   #   for each object, we do an O(nlogn) sorting
   for n in range(hashobj):
      nextbest[n] = []
      for i in range(hashobj):
         if n == i:
            continue
         myobj = theobj()
         myobj.partner = i
         myobj.sim = sim[n][i]
         nextbest[n].append(myobj)
      nextbest[n].sort(mycmp)
   #for n in range(hashobj):
   #   for i in range(hashobj-1):
   #      myobj = nextbest[n][i]
   #      print 'original',n,myobj.partner,myobj.sim
   #for n in range(hashobj):
   #   for i in range(hashobj-1):
   #      myobj = nextbest[n][i]
   #      print n,myobj.partner,myobj.sim
   nbpointer = {}
   for n in range(hashobj):
      nbpointer[n] = 0
   assign = {}
   for n in range(hashobj):
      assign[n] = n
   eliminated = {}
   for n in range(hashobj):
      eliminated[n] = 0
   # the following loop is O(n^2)
   for k in range(hashobj-1):
      #for i in range(hashobj):
      #   if eliminated[i]:
      #      continue
      #   for j in range(hashobj):
      #      if eliminated[j]:
      #         continue
      #      print i,j,sim[i][j]
      #for n in range(hashobj):
      #   if eliminated[n]:
      #      continue
      #   if nbpointer[n]>=hashobj-1:
      #      continue
      #   myobj = nextbest[n][nbpointer[n]]
      #   print 'pre-candidate',n,myobj.partner,myobj.sim

      # the following loop will traverse each element
      # in the nextbest array. so the overall
      # complexity of this loop per call of
      # n2logn is O(n^2)
      for i in range(hashobj):
         while 1:
            if nbpointer[i] >= hashobj-1:
               break
            myobj = nextbest[i][nbpointer[i]]
            #print 'main cluster',i,assign[i]
            #print 'second cluster',myobj.partner,assign[myobj.partner]
            if assign[myobj.partner] == assign[i]:
               # this similarity is not relevant if
               # the two objects are already in the
               # same cluster
               #print 'skipping (same cluster)',i,myobj.partner,myobj.sim
               #print 'skipping (same cluster)',assign[i],assign[myobj.partner],myobj.sim
               nbpointer[i] += 1
               continue
            mysim = sim[assign[i]][assign[myobj.partner]]
            if mysim < myobj.sim:
               # this similarity is not relevant if
               # the two objects are in two clusters that
               # if merged will have a smaller minimum
               # similarity than the similarity between
               # i and myobj.partner
               #print 'skipping (worse sim)',i,myobj.partner,myobj.sim
               #print 'skipping (worse sim)',assign[i],assign[myobj.partner],myobj.sim
               #print 'current sim',mysim
               nbpointer[i] += 1
               continue
            break
      maxsim = -1
      for n in range(hashobj):
         if nbpointer[n] >= hashobj-1:
            continue
         myobj = nextbest[n][nbpointer[n]]
         #print 'candidate',n,myobj.partner,myobj.sim,'pos',nbpointer[n]
         if myobj.sim > maxsim:
            maxsim = myobj.sim
            c1 = n
            c2 = myobj.partner
      assert maxsim >= 0
      #print 'selected candidates',c1,c2
      c1 = assign[c1]
      c2 = assign[c2]
      assert c1 != c2
      if c2 < c1:
         tmp = c1
         c1 = c2
         c2 = tmp
      for n in range(hashobj):
         if assign[n] == c1:
            assign[n] = c2
      # update the similarity matrix
      # the row corresponding to cl2
      #   is updated with similarity of cl1
      #   if similarity of cl1 is smaller
      for n in range(hashobj):
         if eliminated[n]:
            continue
         if n == c1 or n == c2:
            continue
         if sim[c1][n] < sim[c2][n]:
            smallersim = sim[c1][n]
            sim[c2][n] = smallersim
            sim[n][c2] = smallersim
      eliminated[c1] = 1
      mergelist += `c1`+ ':' +`c2`+ ' '
      #print 'mergelist',mergelist
      #print 'end'
   return mergelist

# cubic complete link


def runcubic(hashobj, sim):
    mergelist = ''
    assign = {}
    eliminated = {}
    for n in range(hashobj):
       assign[n] = n
       eliminated[n] = 0
    for k in range(hashobj-1):
        max = -1
        cl1 = -1
        cl2 = -1
        for n in range(hashobj):
           if eliminated[n]:
              continue
           for i in range(n):
              if eliminated[i]:
                 continue
              if sim[n][i] > max:
                 max = sim[n][i]
                 cl1 = i
                 cl2 = n
        assert cl1 >= 0 and cl2 >= 0
        eliminated[cl1] = 1
        mergelist += `cl1`+ ':' +`cl2`+ ' '
        for n in range(hashobj):
           if assign[n] == cl1:
              assign[n] = cl2
        # update the similarity matrix
        # the row corresponding to cl2
        #   is updated with similarity of cl1
        #   if similarity of cl1 is smaller
        for n in range(hashobj):
           if eliminated[n]:
              continue
           if sim[cl1][n] < sim[cl2][n]:
              smallersim = sim[cl1][n]
              sim[cl2][n] = smallersim
              sim[n][cl2] = smallersim
    return mergelist


def computesourcedata(hashobj, mode):
   assert mode == 'random' or mode == 'pathological'
   sourcedata = {}
   for n in range(hashobj):
      sourcedata[n] = {}
   for n in range(hashobj):
      sourcedata[n][n] = 1.0
   max = 0
   for n in range(hashobj):
      for i in range(n+1, hashobj):
         if mode == 'random':
            sim = random.random()
         else:
            sim = n/(1.0*hashobj) + i/(1.0*hashobj*hashobj)
         if sim > max:
            max = sim
         sourcedata[n][i] = sim
         sourcedata[i][n] = sim
   assert max <= 1
   return sourcedata


def simtodis(hashobj, oldmatrix):
   newmatrix = {}
   for n in range(hashobj):
      newmatrix[n] = {}
      for i in range(hashobj):
         newmatrix[n][i] = -oldmatrix[n][i]
   return newmatrix


def simtosim(hashobj, oldmatrix):
   newmatrix = {}
   for n in range(hashobj):
      newmatrix[n] = {}
      for i in range(hashobj):
         newmatrix[n][i] = oldmatrix[n][i]
   return newmatrix


def distribution(hashiteration, increment, datamode):
   hashobj = 0
   outfile = open('timing.xls', "w")
   for n in range(hashiteration):
      hashobj += increment
      global innerloopcounter
      innerloopcounter = 0
      sourcedata = computesourcedata(hashobj, datamode)
      dismatrix = simtodis(hashobj, sourcedata)
      hc(hashobj, dismatrix)
      cubicroot = math.log(innerloopcounter)/3
      cubicroot = math.exp(cubicroot)
      mystring = ''
      mystring += `hashobj`+ '\t'
      mystring += `innerloopcounter`+ '\t'
      mystring += `math.sqrt(innerloopcounter)`+ '\t'
      mystring += `cubicroot`+ '\t'
      outfile.write(mystring+'\n')


print '1 mode: c(ompare output)/t(iming of murtaghs algorithm)'
print '2 data: r(andom)/h(ard)'
assert len(sys.argv) == 3
algorithm = sys.argv[1]
data = sys.argv[2]

if data[0] == 'r':
   datamode = 'random'
else:
   datamode = 'pathological'

if algorithm[0] == 'c':

   hashobj = 20
   innerloopcounter = 0

   sourcedata = computesourcedata(hashobj, datamode)

   simmatrix = simtosim(hashobj, sourcedata)
   mergerscubic = runcubic(hashobj, simmatrix)
   print 'cubic', mergerscubic

   simmatrix = simtosim(hashobj, sourcedata)
   mergersn2logn = n2logn(hashobj, simmatrix)
   if mergerscubic == mergersn2logn:
      print 'n2logn algorithm is correct'
   else:
      print 'n2logn algorithm is not correct:', mergerscubic

   dismatrix = simtodis(hashobj, sourcedata)
   mergersmurtagh = hc(hashobj, dismatrix)
   if mergerscubic == mergersmurtagh:
      print 'murtaghs algorithm is correct'
   else:
      print 'murtagh s algorithm is not correct', mergersmurtagh

else:
   assert algorithm[0] == 't'
   hashiteration = 10
   increment = 20
   distribution(hashiteration, increment, datamode)
