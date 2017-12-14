#S = (N,E,D,R)
#S == social domain
#N == nodes, ipnode, Information Nodes
#E ==edges, information elements on R
#R == invterval, such that [0,r]
#D == decision function

#Trust Network T = (S,V,alpha)
#V = value function = []
#alpha , maximum trust value in T, alpha>0

#V(n,n')=0, means no direct trust relation

#Bayesian Network B = (X,A)
#X (state variables) is a set of logical relation in the network, in boolean e.i. True,False
#A set of arcs
#If there is an arcx→x'  in A,suchthatx,x' ∈X,thenthismeans that the truth value of x'  depends on the truth value of x
#e.g. B(X,A) = B({a,b,c,d},{[a,b],[b,c]} ) then truth value of b depends on a. similar for c
#Parents(x) 
# each x has CPT with given its parent

#Confidence categories, average_phi, extreme_phi, max_phi
# 1>gamma>-1 if gamma (n,n')> 0 belife, else none belief
# if phi > 1std gamma -1, phi < 1std gamma 1, else gamma = Pearson correlation