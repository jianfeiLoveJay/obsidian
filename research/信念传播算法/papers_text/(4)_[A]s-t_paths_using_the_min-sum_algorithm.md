Forty-Sixth Annual Allerton Conference
Allerton House, UIUC, Illinois, USA
September 23-26, 2008

ThA6.4

s-t Paths Using the Min-Sum Algorithm

Nicholas Ruozzi†
Computer Science
Yale University
New Haven, CT 06520-8285, USA
Nicholas.Ruozzi@yale.edu

Sekhar Tatikonda
Electrical Engineering
Yale University
New Haven, CT 06520-8285, USA
Sekhar.Tatikonda@yale.edu

Abstract— Solving the distributed shortest path problem has
important applications in the theory of distributed systems,
most notably routing. In this paper, we provide and prove the
convergence of a min-sum algorithm to compute the shortest
path between two nodes in a graph with positive edge weights.
Unlike the standard distributed shortest path algorithms, the
rate of convergence depends on the weight of the minimal path
and not necessarily the number of nodes in the network.

I. INTRODUCTION

The use of the max-product and min-sum algorithms
to solve combinatorial optimization problems has several
advantages over the typical algorithms that are used to solve
these problems:

1) Message passing algorithms can be easily converted

into distributed algorithms.

2) These algorithms are easy to describe and implement.
The recent work on max-product and linear programming
of [1], [2], and [3] has explored the connection between
integer programs for the max-weight matching and the max-
weight independent set problems and the convergence of
max-product for these problems. These papers suggest that
starting with any integer program, one can formulate a
max-product or min-sum message passing scheme on a
factor graph where the variables are the variables of the
integer program and the factors correspond to the constraints
of the integer program. Further, they demonstrate that the
convergence of max-product depends on the solutions to the
relaxation of the integer program.

The previous results suggest suprising connections be-
tween max-product and linear programs. However,
these
problems may not be sufﬁcient to develop a general under-
standing of when message passing algorithms can be used
to solve combinatorial optimization problems:

1) Max-weight

independent set

is known to be NP-
complete which suggests that max-product is not likely
to yield an efﬁcient solution.

2) The constraints of the integer programs for these
problems are all binary which simpliﬁes max-product.
There are known easy classes of integer programming
problems. In this paper, we explore the connections between
integer programming and the min-sum algorithm by exam-
ining the behavior of min-sum on a simple optimization
problem from one such easy class of integer programs: given

† Supported by NSF grant 0534052

a directed graph G = (V, E), vertices s and t ∈ V , and
weights we > 0 for each e ∈ E, the shortest s-t path problem
is to ﬁnd the path of minimum weight in G starting at s and
ending at t. If no such path exists the shortest s-t path is
inﬁnite. This problem is related to routing and has important
applications in distributed systems.

A. Total Unimodularity

Deﬁnition 1.1: A matrix A is totally unimodular if every
square sub-matrix has determinant 0, 1, or −1. Note that
this implies that the entries of A are 0, 1, or −1.

Theorem 1.2: Let A be a totally unimodular m×n matrix
and b an integral n vector. The polyhedron P = {x|Ax ≤ b}
is integral.

The theorem implies that if an integer programming prob-
lem Ax ≤ b with A a totally unimodular matrix and b
an integral vector b has a unique solution then the linear
programming problem obtained by relaxing the requirement
that the variables in the integer program can only take integer
values also has a unique solution.

For an instance of the weighted matching problem and
the weighted independent set problems, the corresponding
integer program is not necessarily totally unimodular. In
these cases, a unique integral solution to the IP does not
guarantee a unique solution to the linear relaxation. This
complicates the proofs of convergence as evidenced in [1]
and [3]. Therefore, with the hope of producing a general
theory,
totally unimodular matrices seem an appropriate
starting point. More information on total unimodularity and
linear programming can be found in [4].

In this paper, we will show that if the shortest s-t path
problem has a unique solution then the min-sum algorithm
always converges to the correct solution in a number of
steps that depends on the weight of the shortest path and the
weight of the second shortest path. This paper is organized as
follows: in Section II we formulate the shortest path problem
for both integer programming and the min-sum algorithm
and in Section III we show that min-sum converges if the
LP relaxation has a unique solution.

II. SHORTEST S-T PATHS
The shortest s-t path problem can be formulated as an

integer program:

978-1-4244-2926-4/08/$25.00 ©2008 IEEE

918
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 10:44:10 UTC from IEEE Xplore.  Restrictions apply.

ThA6.4

minimize:

subject to:

(cid:2)

e∈E

weXe

(cid:2)

X(u,v) =

(cid:2)

(u,v)∈E

(v,u)∈E

X(v,u) for v ∈ V − {s, t}

(1)

(cid:2)

(s,u)∈E
(cid:2)

X(s,u) = 1 +

X(u,t) = 1 +

(cid:2)

(u,s)∈E
(cid:2)

X(u,s)

X(t,u)

(u,t)∈E

(t,u)∈E

Xe ∈ {0, 1} for each e ∈ E

(2)

(3)

(4)

This integer program can be relaxed into a linear program
by changing the last constraint from Xe ∈ {0, 1} to Xe ∈
[0, 1]. The matrix for this linear program is the combination
of two copies of the V × E incidence matrix for G which is
totally unimodular [4]. Hence, if there is a unique shortest
path from s to t in G then the linear program has a unique
optimal solution (by the previous theorem).

(a) The graph G

(b) A few levels of the com-
putation tree rooted at (s, a)

Fig. 1. A simple graph and computation tree.

of whether or not it is in the minimum s-t path by using the
messages that it received from ψu and ψv in the last time
step. For the shortest path problem, the min-sum algroithm
looks as follows:

A. Shortest s-t Paths via Min-Sum

Min-Sum Algorithm:

(cid:3)

The above problem can be formulated as a problem on a
factor graph and then solved using the min-sum algorithm.
Here we will have variables Xe for each e ∈ E and factors
ψv for each v ∈ V . The factor ψv is a function depending
on all edges incident to v which we will denote ∂v. ψv is an
indicator fucntion for the constraints in the integer program
at vertex v. Speciﬁcally, deﬁne ψv for v (cid:4)= s, t as follows:

1
0

ψv(X∂v) =

if equation (1) is satisﬁed at v
otherwise
Similarly, ψs and ψt indicate whether or not (2) and (3)
respectively are satisﬁed. The factor graph then has a vertex
for each of the factors and variables with an edge joining a
variable and a factor if the factor depends on that variable.
For each edge e ∈ E deﬁne a self-potential φe(Xe) =

eweXe. We then deﬁne
(cid:2)

f (XE) =

log φe(Xe) −

e∈E

(cid:2)

v∈V

log ψv(X∂v)

(cid:4)

Given an assignment of each Xe to some value in {0, 1},
e∈E weXe if the nonzero Xe’s
f (XE) is equal to the
deﬁne a directed edge disjoint path from s to t in G and
inﬁnity otherwise. Therefore, minima of f correspond to
minimal s-t paths. If no such path exists then f is inﬁnity
for all choices of XE.

We can now use the min-sum message passing procedure
in an attempt to minimize the objective function f . The
message passing procedure is iterative in that at each stage a
message m(u,v)→v is sent from each variable X(u,v) to the
factors ψv and ψu and a message mv→e is sent from each
factor ψv to each variable Xe such that e is incident to v in
G. At any point, a variable X(u,v) can compute an estimate

1) Initialize all messages to 0.
2) For e incident to v,
mn

v→e(x) =

− log ψv(x∂v)

min
x∂v:xe=x

(cid:2)

+

e(cid:2):e(cid:2)∈∂v−{e}

mn−1

e(cid:2)→v(xe(cid:2) )

3) For e incident to v and u,
mn

e→v(x) = log φe(x) + mn−1

u→e(x)

4) Compute the beliefs at step n:

bn
e (x) = φe(x) +

mn

v→e(x)

(cid:2)

v∈∂e

5) Estimate membership of e = (u, v) in the min path as

⎧
⎨

xe

n =

⎩

1
0
?

e (1) < bn
e (0) < bn

if bn
if bn
otherwise

e (0)
e (1)

We say that the message passing procedure has converged at
n(cid:2)
step n if there is no time step n(cid:4) > n such that xe
.

n (cid:4)= xe

III. CONVERGENCE OF MIN-SUM

To prove convergence of the min-sum algorithm we will
make extensive use of the notion of a computation tree. The
computation tree rooted at a node y in the factor graph is
constructed by starting at y and adding all neighbors of y as
children of y in the tree. The next level of the tree is then
generated by taking a leaf of the tree and adding all of the
leaf’s neighbors that are not its parent.

919
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 10:44:10 UTC from IEEE Xplore.  Restrictions apply.

This process is the repeated for the new leaf nodes and
so on. Notice that this computation tree has nodes for both
edges and vertices in the original graph. We will, for ease of
illustration replace the Xe nodes with a directed edge joining
e’s two endpoints. We will denote this new tree starting with
edge e and repeating the process for 2n steps as Te(n).

The resulting minimization problem on the computation
tree is different from the original s-t path problem. There
are now multiple copies of s and t making the problem
on the computation tree a multi-source/multi-sink shortest
path problem. Contrast this with the cases of max-weight
matching and max-weight independent set where the problem
on the original graph and the problem on the computation
tree are exactly the same. Speciﬁcally, a feasible solution on
the computation tree is a set of edges such that every copy
of s in the tree has a path to a copy of t or a boundary node
(allowed by the message initialization), every copy of t in
the tree has a path from a copy of s or some boundary node,
and every vertex has at least as many out edges as in edges.
A feasible solution is minimal if no feasible solution has a
smaller weight.

The computation tree models the message passing struc-
ture of the min-sum algorithm: minimal solutions on Te(n)
correspond to the beliefs of the root obtained by running the
min-sum algorithm for 2n steps.

Deﬁne w(S) =

e∈S we for S a set of edges. Let
wmin = mine∈E we and (cid:5) be the difference in weight of the
second best s-t path in G and the optimal path in G then
we have the following theorem:

(cid:4)

Theorem 3.1: If P ∗ is the unique minimum s-t path in
G then an edge e ∈ E is in P ∗ iff every minimal solution
on Te(n) contains the root for n > w(P ∗)2

w(P ∗)
wmin .

(cid:3)wmin +

Proof: (⇒) Suppose by way of contradiction that e =
(u, v) is in the min s-t path P ∗ on G but that there is some
minimal solution M on the computation tree rooted at e at
time 2n that does not contain the root.

This proof, similar to that of [1], builds an alternating set
of paths that can be swapped to improve the optimality of
the solution. Because the constraints are not binary in our
case, the construction is slightly more complicated.

Construct two subgraphs Msub−opt and Mopt of Te(n) as

follows:

1) Let P be a copy of the minimum s-t path that uses
the root edge e = (u, v). Starting at v, follow P
forward until doing so would require traversing an edge
in M . Similarly, starting at u follow the edges in P
backwards until doing so would require traversing an
edge in M . Add this sub-path of P to Mopt.

2) By construction, for each sub-path P in Mopt not
originating at a leaf, there must be at least one path
in M that either (possibly both for the edge added in
step 1)

a) leaves the head of P and terminates in a copy
of t or in a leaf of Te(n). If no such path is
in Msub−opt, choose such a path P (cid:4) in M and

ThA6.4

(a) Solution on the computation tree (dashed edges) rooted
at (c, d) with optimal path s − a − b − c − d − e − f − t

(b) Mopt (+) edges and Msub−opt (-) edges

Fig. 2.

Illustration of the construction.

follow it until t or the boundary. Add this sub-
path to Msub−opt.

b) enters the tail of P and originates in a copy
of s or in a leaf of Te(n). If no such path is
in Msub−opt, choose such a path P (cid:4) in M and
follow it backwards until s or the boundary. Add
this sub-path to Msub−opt.

3) By construction, for each sub-path P in Msub−opt not
touching the boundary, there must be a copy of P ∗
that either

a) leaves the head of P and terminates in a copy
of t or in a leaf of Te(n). If this path is not in
Mopt, follow it until t or when traversing an edge
requires traversing an edge in M . Add this sub-
path to Mopt.

b) enters the tail of P and originates in a copy of s
or in a leaf of Te(n). If this path is not in Mopt,
follow it backwards until s or when traversing an
edge requires traversing an edge in M . Add this
sub-path to Mopt

4) Repeat steps 2 through 3 until it is no longer possible

to add any more paths.

This process builds a set of paths starting at the root
that alternates between subpaths of copies of P ∗ and sub-
paths of the solution M . Figure 2 illustrates the construc-
tion for a graph G whose unique minimum s-t path is
(s, a), (a, b), (b, c), (c, d), (d, e), (e, f ), (f, t).

Let M ∗ = (M − Msub−opt) ∪ Mopt. Notice that M ∗ is a
feasible solution on Te(n) since the in degree and out degree
of every node in M is preserved and, by the construction,
sub-paths in Mopt satisfy the constraints at their heads and
tails when added to M .

Let k be the number of disjoint sub-paths in Mopt and
k(cid:4) be the number of disjoint sub-paths in Msub−opt. In the

920
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 10:44:10 UTC from IEEE Xplore.  Restrictions apply.

ThA6.4

IV. CONCLUSION AND FUTURE WORK
We have demonstrated that the shortest s-t path problem
can be solved by a min-sum procedure derived from an
integer program. If the integer program has a unique solution,
then the estimates produced by the min-sum algorithm can
w(P ∗)
be used to ﬁnd the min s-t path in G after
wmin
iterations of the algorithm. However, the above time bound
may or may not be tight. A different or more careful proof
may be able to reduce the time bound further.

w(P ∗)2
(cid:3)wmin +

Understanding the shortest path problem is an important
ﬁrst step in understanding how the max-product and min-
sum algorithms can be used to solve totally unimodular
linear programs. This problem highlights some complexities
that are not present in the max-weight matching and max-
weight independent set problems; most notably, the opti-
mization problem on the computation tree is not the same
as the original problem (recall that there were multiple s’s
and multiple t’s on the computation tree). The result here
suggests that similar techniques may have some success
when applied to more general
totally unimodular linear
optimization problems.

REFERENCES

[1] S. Sanghavi, D. Malioutov, and A. Willsky, “Linear programming anal-
ysis of loopy belief propagation for weighted matching,” in Advances in
Neural Information Processing Systems 20, J. Platt, D. Koller, Y. Singer,
and S. Roweis, Eds. Cambridge, MA: MIT Press, 2008, pp. 1273–
1280.

[2] M. Bayati, D. Shah, and M. Sharma, “Max-product for maximum
weight matching: Convergence, correctness, and lp duality,” in Infor-
mation Theory, IEEE Transactions on, 2008, pp. 1241–1251.

[3] S.

Sanghavi

Shah,
max-product
propagation,”
http://www.citebase.org/abstract?id=oai:arXiv.org:cs/0508097

and
belief

via
[Online]. Available:

“Tightness

2005.

D.

of

lp

[4] A. Schrijver, Theory of Linear and Integer Programming.

John Wiley

& Sons Ltd., 1987.

Fig. 3. Example of non-uniqueness.

worst case, k = k(cid:4) +1 due to the alternating construction. As
all other possible outcomes can be reduced to this situation,
we only illustrate the proof in this instance. There are two
cases:

k > w(P ∗)

(cid:3) + 1

Case 1:
In this case there are k − 1 disjoint sub-paths in Msub−opt
each of which cannot have a weight closer than (cid:5) to the
weight of the sub-path in Mopt that enters its tail. We have
(k − 1)(cid:5) > w(P ∗), so

w(M ∗) = w(M ) − w(Msub−opt) + w(Mopt)
< w(M ) − (k − 1)(cid:5) + w(P ∗)
< w(M )

Case 2:

k ≤ w(P ∗)

(cid:3) + 1

w(M ∗) = w(M ) − w(Msub−opt) + w(Mopt)

≤ w(M ) − (2x − k|P ∗|)wmin + w(Mopt)

kw(P ∗)
wmin

≤ w(M ) − (2x −
≤ w(M ) − 2xwmin + 2kw(P ∗)
< w(M )

)wmin + kw(P ∗)

In either case, w(M ∗) < w(M ) contradicting the

minimality of M .

(⇐) For the opposite direction, suppose by way of con-
tradiction that every minimal solution on Te(n) contains the
root edge e but that e is not in P ∗. We can then construct
Msub−opt and Mopt in an alternating fashion similar to the
above. As the details of the proof are nearly identical, we
omit them here.

A. Non-Uniqueness

If the shortest path is not unique, the min-sum algorithm
may not produce the correct answer. For example, consider
Figure 3. The s-t path is not unique, and by symmetry,
the computation tree rooted at (s, a) is isomorphic to the
computation tree rooted at (s, b). As a result, their beliefs at
any ﬁxed time will be the same.

921
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 10:44:10 UTC from IEEE Xplore.  Restrictions apply.

