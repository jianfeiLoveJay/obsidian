8
1
0
2

y
a
M
6
1

]
S
D
.
s
c
[

1
v
2
8
2
6
0
.
5
0
8
1
:
v
i
X
r
a

Max-Product for Maximum Weight Matching –
Revisited

Mario Holldack
Institut f¨ur Informatik
Goethe-Universit¨at
Frankfurt am Main, Germany
holldack@thi.cs.uni-frankfurt.de

Abstract—We focus on belief propagation for the assignment
problem, also known as the maximum weight bipartite matching
problem. We provide a constructive proof that the well-known
upper bound on the number of iterations (Bayati, Shah, Sharma
2008) is tight up to a factor of four. Furthermore, we investigate
the behavior of belief propagation when convergence is not
required. We show that the number of iterations required for a
sharp approximation consumes a large portion of the convergence
time. Finally, we propose an “approximate belief propagation”
algorithm for the assignment problem.

Index Terms—Belief Propagation, Max-Sum Algorithm, As-

signment Problem, Matching, Approximations

I. INTRODUCTION

Since Pearl’s introduction of the belief propagation algo-
rithm (BP) in [1], applications of BP have been extensively
covered in the literature, ranging from artiﬁcial intelligence,
computer vision, communication, and combinatorial optimiza-
tion to statistical physics; see [2] for an introductory survey.
The same algorithm is also known as the max-product, max-
sum, or sum-product algorithm among others Here we address
the application of BP – that is the max-sum algorithm – to the
assignment problem in a weighted complete bipartite graph
Kn,n, i.e., the problem of assigning n jobs to n employees
such that every job is assigned exactly once and the proﬁt
is maximized. The assignment problem is also known as the
maximum weight matching problem in a weighted complete
bipartite graph. Here it is sufﬁcient to know that BP is an
iterative graph algorithm where each node outputs a local
solution (a so-called belief ) in every iteration. More precisely,
a local solution of a node u is an edge
that u believes
to be in a maximum weight matching (MWM). The algorithm
local solutions converge, that is when the
stops when all
outputs no longer change. In [3] Bayati, Shah, and Sharma
show that BP converges to the MWM within 2n
wmax/ε
iterations, where wmax := max
and ε is the
uniqueness gap, i.e., the difference between the sum of the
weights of the best and the second best perfect matching. In
total their BP implementation takes
wmax/ε) operations
for ﬁnding the unique MWM which is comparable with the
best known sequential algorithms – given that wmax and ε
are ﬁxed parameters. As shown by Salez and Shah in [4], BP
is an optimal algorithm for the MWM problem in complete
bipartite graphs with randomly weighted edges, i.e., with high

we|

(n3

u, v

: e

O

{|

E

∈

{

}

}

·

·

probability BP ﬁnds the maximum weight matching within a
constant number of iterations.

the upper bound [3] of
In Theorem 2 we show that
wmax/ε iterations for the convergence time is is tight up to
2n
·
a factor of four. Based on this result we construct weights for
the Kn,n such that BP does not ﬁnd any good approximate
MWM, even when the number of iterations is close to the
convergence time. What is the reason behind this surprisingly
poor approximation behavior? One possible explanation is that
the BP matching, i.e., the set of edges for which the beliefs of
the endpoints agree, consists only of few edges. We show in
Theorem 3 that any completion of a BP matching computed
in an early iteration has a poor approximation factor.

The rest of this paper is organized as follows: Section II de-
scribes our main results. Section III and Section IV cover the
proofs of Theorem 2 and Theorem 3, respectively. Section V
presents an approximate BP algorithm and Section VI con-
cludes the paper.

II. BP FOR THE ASSIGNMENT PROBLEM

Let Kn,n be the complete bipartite graph with n nodes
in each layer. In [3] Bayati, Shah, and Sharma implement
and analyze BP for the assignment problem on Kn,n where
edges receive real-valued weights. Their result is one of most
important success stories of Loopy BP, i.e., BP on graphs with
cycles. In the following wmax is the maximum absolute value
of any edge weight and ε is the difference (uniqueness gap)
between the sum of the weights of the best and the second
best perfect matching.

Theorem 1 (Bayati, Shah, Sharma, [3]). For any edge weights
for the Kn,n, the BP algorithm converges to the maximum
weight matching within 2n·wmax
iterations, provided the max-
imum weight matching is unique.

ε

How tight is their analysis?

3, wmax > 0, and 0 < ε < wmax
Theorem 2. For any n
4(n–2)
there are edge weights for the Kn,n such that the maximum
weight matching is unique and BP converges to the maximum
weight matching only after n·wmax

iterations.

≥

2ε

Thus, the bound of Theorem 1 cannot be improved. Since
the ratio wmax
can be exponentially large in the number of in-
put bits, Theorem 2 implies that BP has an exponential worst-

ε

α1

α2

α3

β1

β2

β3

α1

α2

α3

β1

β2

β3

α1

α2

α3

β1

β2

β3

Fig. 1. left: the cycle C2n (for n = 3); middle and right: the
optimal and suboptimal matching drawn with double and solid
edges, respectively.

case convergence time. However, demanding convergence may
be too harsh since the algorithm may have found an approxi-
mate MWM (or even the MWM itself) already after relatively
few iterations. Observe that in each iteration BP produces a
partial matching consisting of all edges
where both
α, β
endpoints believe that
belongs to the MWM. Hence,
it is important to determine whether those partial matchings
already constitute good approximations of the MWM. Maybe
such a partial matching is not good enough, but can be
completed into a good perfect matching with little additional
resources. However, in the worst case, a sharp approximation
cannot be achieved much earlier than convergence.

α, β

{

}

{

}

Theorem 3. For sufﬁciently large n, for all wmax > 0 and
0 < ε < wmax
4(n−2) , there are edge weights for the Kn,n such that
every completion of a partial BP matching computed during
the ﬁrst

wmax

Θ

√n/ log(n)
(cid:0)

(cid:1)

, Θ

min

√n3/ log(n)·ε (cid:17)(cid:27)

n log(n)
(cid:26)
(cid:1)
(cid:0)
iterations is

(cid:16)
-approximative.
1–Θ(1/√n log(n))
(cid:1)
(cid:0)
We construct weights such that the partial BP matchings are
almost perfect, but none of the few completions are capable of
improving the matching considerably. Observe that the sharp
lower bound n·wmax
for the convergence time and the time
(see Theorem 2 and Theorem 3,
Θ
·
respectively) are closely related: tight approximations require
a large portion of the convergence time, if wmax
dominates n.

wmax/
(cid:0)

n3/ log(n)

(cid:0)p

(cid:1)(cid:1)

2ε

ε

ε

III. PROOF OF THEOREM 2

We start by motivating some of the key ideas. We ﬁrst
investigate the behavior of BP on the cycle C2n for carefully
selected weights. Subsequently we embed C2n into Kn,n and
complete the argument for Theorem 2. The cycle C2n on 2n
nodes (see Fig. 1 for n = 3) has two perfect matchings, one
of which is optimal, provided that the MWM is unique. Since
these two matchings are edge-disjoint, the edges of C2n may
be partitioned into optimal and suboptimal edges. Now assume
that there is a heavy suboptimal edge (see the thick edge
in Fig. 1) which is at least twice as heavy as any
α1, β3}
{
other edge. It turns out that this heavy edge acts as an attractor
of suboptimal beliefs. In particular, we show in the Nibbling
Lemma (Lemma 1) that many iterations are required to rule
out the heavy edge.

Now deﬁne the edge weights of the cycle graph C2n as
, and 0 < ε < wmax
follows. Let n
4(n–2) .
Denote the layers of the bipartite cycle C2n := (An, Bn, En)

3, [n] :=

1, . . . , n

≥

{

}

α1

α2

β1

α2

β2

α3

l
i
a
t

β3

α3

β2

α2

β1

α1

β3

α3

l
i
a
t

β2

α3

β3

α1

wopt

wsub

wmax

Fig. 2. computation trees T (4)
wopt = wmax

, wsub = wmax

2

wmax
2(n–1) −

2 −

α1 and T (4)

α2 with edge weights
ε
n–1 , and wmax.

and Bn :=

by An :=
β1, . . . , βn}
α1, . . . , αn}
{
is En := Eopt
αi, βi} |
{
∪
Esub :=
α1, βn}
i
αi+1, βi} |
(cid:8)
{
optimal and suboptimal edges, respectively.
(cid:9)

{
Esub, where Eopt :=

[n–1]

{
(cid:8)

∪

∈

(cid:8)

(cid:9)
From now on, whenever we refer to C2n, its edges are

. Its edge set
and
[n]
i
are the sets of

∈

(cid:9)

weighted as follows, where wmax > 0 is the largest weight:

we:= 


wmax
2
wmax

2 – wmax

2(n–1) – ε

n–1 ,

wmax

if e
∈
if e =
if e =

Esub,

(1)

{

Eopt,
αi+1, βi}∈
α1, βn}∈
{
2(n–1) – ε

Esub.

≥

wmax

2 −

n–1 ≥

implies wmax


Note that ε < wmax
0 for
4(n–2)
3. Let W (M ) :=
e∈M we denote the weight
all n
edge
the
a matching M . A simple
of
weights shows that W (Eopt) = n
and W (Esub) =
( wmax
2(n–1) – ε
the
(n–1)
·
maximum weight matching is indeed the set Eopt of optimal
edges, the set Esub of suboptimal edges is the second best
matching, and ε is the uniqueness gap.

·
n–1 ) + wmax = W (Eopt)–ε,

addition of
wmax
2

2 – wmax

i.e.,

P

v

For the remaining analysis of BP on C2n, we need some
of the concepts and arguments from the proof of Theorem 1
in [3]. Given an arbitrary graph G=(V, E) – such as C2n or
Kn,n – the computation tree (or unwrapped network) T (t)
v of v
at iteration t is constructed as follows: First, let v be the root
of T (t)
at depth t′ < t, make
all neighbors of u in G children of u except for its parent in
the tree. Note that the depth of T (t)
is exactly t. This might
differ from other literature where the iteration counter of the
BP algorithm starts with t = 0.

v . Then for any node u of T (t)

Now let T (t)
E′ is a partial
v = (V ′, E′). A T-matching T ′
matching in T (t)
v where every inner node is an endpoint of an
edge in T ′. One can show that the belief of v in G at iteration t
is the same as the belief of v in T (t)
(cf. the unwrapped
network lemma in [5]) and that the belief of v in T (t)
is the
edge incident with v in a maximum weight T-matching (cf.
Lemma 1 in [3]). Thus, for the analysis of BP in G, it sufﬁces
to only consider maximum weight T-matchings.

⊆

v

v

v

For G = C2n the situation is simple since every compu-
tation tree is a path. Consider the computation tree T (t)
for
n–1.
0 and 0
some iteration t = kn + ℓ where k
Beginning with a leaf, T (t)
is partitioned into k copies of C2n
and an incomplete copy, called a tail, of 2ℓ edges (see Fig. 2).

≤

≤

≥

ℓ

v

v

Example 1. Let n = 3. Consider the cycle C6 and its
computation trees T (4)
α2 as depicted in Fig. 2. The
maximum weight T-matching in T (4)
wmax
2

α1 has the weight 4

α1 and T (4)

·

2 ).
compared to the suboptimal weight of wmax + 3
As a consequence the root α1 of T (4)
α1 correctly believes that
belongs to the MWM in C6. On the other hand, the
α1, β1}
{
root α2 of T (4)
is an edge of
α2
the MWM in C6 since the heavy edge in the tail outweighs
the ε-advantage of the optimal edges in the copy of C6.

falsely believes that

α2, β1}

( wmax

4 – ε

{

·

α1

β1

β2

α2

α3

α2

α3

α2

β3

α3

The following lemma generalizes this observation.

β2

β3

β2

β3

β1

β3

β1

β3

β1

β2

β1

β2

≥

0 and 1

Lemma 1 (Nibbling Lemma). For every iteration t = kn + ℓ
with k
n–1, there is a node v such that the
ℓ
≤
computation tree T (t)
consists of k copies of the cycle C2n
and a tail of length 2ℓ, where the tail contains the heavy edge
v ) and Wsub(T (t)
v ) be the weights of the
α1, βn}
{
optimal and suboptimal edges in T (t)

v , respectively. Then

. Let Wopt(T (t)

≤
v

Fig. 3.
the augmenting path argument from Proposition 1
where light edges are depicted with dotted edges; suppose a
at the root; then
T-matching contained the light edge
ﬂipping the edges along the path increases the weight of the
T-matching.

α1, β2}

{

Wsub(T (t)

v )–Wopt(T (t)

v ) = –kε + ∆ℓ,

(2)

where wmax

2 = ∆1 >

> ∆n–1 > wmax

4(n−1) .

· · ·

We interpret the Nibbling Lemma as follows. Whenever the
= 0, and the tail contains the heavy
tail is nonempty, i.e., ℓ
edge, the suboptimal edges have an advantage of ∆ℓ > 0 in the
tail. On the other hand, the higher the number t of iterations,
the larger the number k of copies of C2n in T (t)
v . Since the
weight difference is –kε + ∆ℓ, each of the k copies “nibbles
off” an ε from ∆ℓ. Hence, if k is large enough, kε > ∆ℓ
follows for all ℓ

[n–1], and therefore BP converges.

For the proof of Theorem 2, it sufﬁces to consider the case
when the tail consists only of the heavy edge and an optimal
edge (ℓ = 1). However, a general version of the Nibbling
Lemma is required in the proof of Theorem 3.

∈

Proof of Lemma 1. Let v be some node such that T (t)
con-
the
tains the heavy edge in its tail. Since t = kn + ℓ,
computation tree consists of k copies of C2n and a tail of
length 2ℓ. The optimal matching on C2n has an advantage
of ε over the suboptimal matching for each copy. However,
restricted to the tail, the suboptimal matching wins by

v

wmax
2

–ℓ

·

(cid:17)

(3)

(4)

+ wmax

n–1

∆ℓ

wmax

2 – wmax
2(n–1) – ε
ℓ–1
n–1 .

(1)
:=
(ℓ–1)
·(cid:16)
(cid:16)
n–ℓ
= wmax ·
2(n–1) –ε
Now observe that ∆1 >
sequence which is bounded by ∆1 = wmax
due to ε < wmax

3, by

4(n–2) and n

· · ·

(cid:17)

2

·

> ∆n–1 is a strictly decreasing
from above and,

≥
n–1 > wmax
n–2

2(n–1) – wmax

4(n–1) = wmax
4(n−1)

(5)

∆n–1 = wmax

2(n–1) –ε

·

from below.

holds. Observe that for t = kn + 1 there is a node v such
that the computation tree T (t)
contains k copies of the cycle
each.
C2n and a tail with one copy of
and
α1, β1}
{
Then v has a suboptimal belief since k < wmax
and (2) from
2ε
the Nibbling Lemma imply

α1, βn}

{

v

Wsub(T (t)

v )–Wopt(T (t)

v ) = –kε + ∆1 > – wmax
2ε ·

ε + wmax

2 = 0.
(7)

On the other hand, for k > wmax

2ε , BP converges since

Wsub(T (t)

v )–Wopt(T (t)

v ) = –kε + ∆1 < – wmax
2ε

ε + wmax

2 = 0.
(8)

·

Hence, Theorem 2 holds for the graph C2n.

In order to prove the original version of the theorem, we
embed C2n into the complete bipartite graph Kn,n, where
every cycle edge is weighted as in (1) and (in a slight abuse
of the notation for wmax) every noncycle edge e receives the
weight we = –2wmax. We call any such edge a light edge.

Proposition 1. In every iteration of BP, every node v in C2n
has exactly the same belief as v in Kn,n.

Note that the argument holds for non-negative weights as

well when 2wmax is added to the weight of each edge.

Proof of Proposition 1 (sketch). We show that for every com-
putation tree, every maximum weight T-matching does not
contain a light edge. Otherwise the weight of this T-matching
could be increased using an augmenting path argument (see
Fig. 3) where the path contains the light edge, as well as
suboptimal and optimal edges alternately. Hence, maximum
weight T-matchings only contain cycle edges.

Proposition 1

Lemma 1

Now the claim follows for Kn,n.

Theorem 2

We now show that the weights as deﬁned in (1) force the

upper bound in Theorem 1 to be tight.

Proof of Theorem 2. We start our analysis with the graph C2n
and explain how the lower bound of n·wmax
for the number
of iterations follows from Lemma 1. Consider the largest
integer k such that

2ε

kn + 1 < n·wmax

2ε

(6)

IV. PROOF OF THEOREM 3

Theorem 2, in conjunction with the upper bound of Bayati,
Shah, Sharma (Theorem 1), characterizes the worst-case con-
vergence time. However, BP already computes the maximum
weight matching in C2n after performing t = n iterations
since every computation tree at time n does not have a tail.
Instead of using a single cycle, we build a graph using multiple
node-disjoint cycles of length 2ni where n1 <
< nc

· · ·

6
are prime numbers with the same order of magnitude. The
convergence time for cycle C2ni coincides with 2niwmax
, but
the construction prevents BP from ﬁnding a perfect matching
in unions of cycles as an intermediate solution. Based on
this observation, we will see that even partial intermediate
solutions cannot be completed to give matchings with a weight
close to the weight of the MWM.

ε

Proof of Theorem 3. We begin our investigation on the cycle
construction with the following lemma.

Lemma 2 (Dusart, [6]). For every n
of prime numbers less than or equal n is bounded by

599, the number π(n)

≥

n
log(n)

1 + 1

log(n)

(cid:16)

π(n)

n
log(n)

≤

(cid:16)

(cid:17) ≤

1 + 1.2762
log(n)

(cid:17)

(9)

1
2

p
= π( n

For the rest of the proof let n be sufﬁciently large and
n/log(n). Let Pn,c denote the set of prime numbers
c
≤
in the open interval ( n
c ). We apply Lemma 2, obtain
c )–π( n
c follows.
4c log(n) , and
Pn,c| ≥
2c ) >
Pn,c|
|
|
< nc from Pn,c and
Now select c prime numbers n1 <
· · ·
let C2n1 , . . . , C2nc be node-disjoint cycles with weights as
described in (1).

2c , n

n

The next lemma states that BP fails for many cycles within

a large number of iterations.

⌊

{

c/2

6≡

≤

⌋}

min

( n
2c )

wmax
8cε ,

2c )c/2
( n

ni·wmax
2ε

, there are at least c

Pn,c. If t
≤
, then Lemma 1 implies that BP does not ﬁnd a perfect

Lemma 3. For the cycles Cn1 , . . . , Cnc the following holds:
If t
2 cycles such
that BP does not ﬁnd a perfect matching for any of these
cycles.
Proof of Lemma 3. Let ni ∈
matching for C2ni at iteration t. Now note that for every t
≤
wmax
, the prime factorization of t contains at
8cε ,
min
⌊
⌋}
{
most c
2 distinct prime numbers from Pn,c. Hence, there is a set
Pn,c of at least c
2 prime numbers such that t
0 mod nj
Q
for all nj ∈
Lemma 3

Q. Now the claim follows.

0 mod ni and t

By embedding

c
i=1 C2ni into the Kn,n such that the argu-
ments from Lemma 3 still hold, we reach another important
c
i=1 ni;
milestone in our reasoning. W.l.o.g. we assume n =
c
otherwise extend Kn′,n′ , where n′ =
i=1 ni, with a match-
ing on 2(n–n′) new nodes and let each new matching edge
e receive the weight we = wmax
. Finally, weight every other
edge e′ in Kn,n with we′ = –2wmax.

P

P

S

⊆

6≡

2

Proposition 2. In every iteration of BP, every node v in

c
i=1 C2ni has exactly the same belief as v in Kn,n.

S
Proof of Proposition 2. The proof is analogous to the proof
of Proposition 1.

Proposition 1

Hence, Lemma 3 implies that BP fails to ﬁnd perfect
matchings for at least c
2 node-disjoint cycles in Kn,n. In
order to gain a better understanding of completing partial BP
matchings, the next example illustrates the exact behavior of
BP for our constructed weights.

Example 2. Consider the cycle C10. The beliefs at iteration
t = 1, . . . , 6 are shown in Fig. 4 where each undirected

α1

α2

α3

α4

α5

α1

α2

α3

α4

α5

β1

β2

β3

β4

β5

α1

α2

α3

α4

α5

β1

β2

β3

β4

β5

α1

α2

α3

α4

α5

(a) t = 1

(b) t = 2

(c) t = 3

β1

β2

β3

β4

β5

α1

α2

α3

α4

α5

β1

β2

β3

β4

β5

α1

α2

α3

α4

α5

β1

β2

β3

β4

β5

β1

β2

β3

β4

β5

(d) t = 4

(e) t = 5

(f) t = 6

Fig. 4. beliefs in C10 for iteration t = 1, . . . , 6; see Example 2.

{

}

{

u, v

u, v

u, v

indicates that both endpoints believe in

edge
}
belonging to the MWM; and where each directed edge (u, v)
indicates that u believes in
belonging to the MWM,
{
but v does not. With increasing t, the number of optimal
edges in the partial BP matching decreases and the number
of suboptimal edges increases. However, in each iteration
t = 1, . . . , 4, there are only two nodes that are not endpoints
of a partial matching. Finally, BP ﬁnds the optimal matching
at iteration t = 5. For larger t, the beliefs repeat periodically
until the process converges.

}

Lemma 4. For every iteration t
and
every completion of a partial BP matching, its weight is at
1–Θ( c
is the weight of
most
n )
the MWM for Kn,n.
(cid:1)
(cid:0)

Wopt, where Wopt = n

wmax
2

min

⌋}

≤

{

⌊

·

·

wmax
8cε ,

( n
2c )

c/2

Proof of Lemma 4. As a consequence of Lemma 3 and the
observation we made in Example 2, there is a set Q
Pn,c
⊆
of at least c
Q, the
2 prime numbers such that for each ni ∈
partial BP matching for C2ni consists of ni–1 edges. In order
to complete the partial BP matching for one of those cycles,
we are forced to add a light edge, i.e., an edge e (between two
black nodes in Fig. 4) with weight we = –2wmax. In iteration
1 mod ni, the completion has the highest weight, namely
t
. Thus the
2 +wmax = –2wmax+ni·
–2wmax+(ni–2)
W (i)
completion for C2ni has a weight of at most
opt ,
ni )
where W (i)
wmax
(cid:1)
is the weight of the MWM restricted
opt = ni ·
2
to C2ni . In total, completing partial BP matchings for Kn,n
is at most 1–Θ( c
Lemma 4

wmax
2
1–Θ( 1
(cid:0)

n )-approximative.

wmax

≡

·

·

A worst-case analysis of Lemma 4 concludes the proof of
( n
2c )c
as close as possible to
Theorem 3. In order to push
⌊
the convergence bound, we are interested in the largest c such
2(c+1) )c+1
holds. Observe that the
that
left-hand and right-hand side of this inequation differ at most
wmax
( n
2c )c
by the factor n. Hence,
8ncε , i.e., we lose the
⌋ ≥
16n2c of the Bayati-Shah-Sharma convergence bound.
factor

wmax
8cε ≤ ⌊

( n
2c )c

⌋ ≤

⌋

⌊

⌋

⌊

(

n

1

α1
α2
α3
α4
α5
α6

β1
β2
β3
β4
β5
β6

α1
α2
α3
α4

α6

β1
β2
β3
β4

β6

Fig. 5. graphical representation of beliefs and their conﬂict
graph; the edge
belongs the partial BP matching and
hence, both endpoints do not occur in the conﬂict graph.

α5, β5}

{

Now Theorem 3 follows by plugging in c = 1
2
into Lemma 4.

n/ log(n)

p

Theorem 3

V. APPROXIMATE BELIEF PROPAGATION

Finally, we present a linear-time algorithm for the comple-
tion of partial matchings which “respects” the beliefs of the
nodes and only adds edges. However, since the analysis in the
proof of Theorem 3 is not restricted to any speciﬁc algorithm,
the algorithm described here cannot improve its approximation
factor.

We call a pair (α, β) a conﬂict if exactly one of the two
belongs to the MWM. For each
nodes believes that
BP-iteration t for the Kn,n = (An, Bn, En), let CBP(t) :=
(A, B, Et) be the bipartite conﬂict graph with

α, β

{

}

.
(cid:9)

A :=
B :=
Et :=

|
|
α, β

α
β

{
{

{
(cid:8)

} |

α is not covered by the partial BP matching
,
}
β is not covered by the partial BP matching
,
}

(α, β) is a conﬂict

Fig. 5 shows the transformation of beliefs into a conﬂict
graph. Note that every connected component of a conﬂict
graph for the assignment problem has at most one cycle.

W.l.o.g. let the conﬂict graph be connected and have a cycle.
For every iteration t, let Mt be the approximate MWM in Kn,n
initialized with the partial BP matching. For an arbitrary cycle
edge e consider the following two a-posteriori cases:
(a) e belongs to Mt; then remove e and its incident edges

from the conﬂict graph;

(b) e does not belong to Mt; then remove e as well.
In either case the resulting graph is a forest (or even a tree).
We execute BP for both forests and obtain maximum weight
T-matchings Ma and Mb since BP is correct for trees (see [7,
Theorem 14.1] for a detailed proof). If W (Ma) > W (Mb),
then set Mt := Mt ∪
Mb.
}
Now remove the edges in Mt and their endpoints from the
conﬂict graph.

, otherwise set Mt := Mt ∪

Ma ∪ {

e

We still have to worry about matching the remaining leafs,
denoted by the subsets A′ and B′. Observe that
B′
|
and that the set of edges between A′ and B′ in the conﬂict
graph is empty. Compute an arbitrary matching M ′ between
A′ and B′ with edges from Kn,n, e.g., by using a greedy
:= Mt ∪
the
algorithm, and set Mt
approximate MWM Mt.

M ′. Finally, output

A′

=

|

|

|

For the weights that we used in the proofs of Theorem 2
and Theorem 3, this algorithm is trivial since the conﬂict
graph consists of isolated nodes only. However, even though
approximate BP cannot improve upon the 1–Θ( c
n ) barrier from
Lemma 4, we suggest that similar algorithms should also be
of interest for the application of BP to other combinatorial
optimization problems.

VI. CONCLUSIONS

·

We established lower bounds on the running time of the BP
algorithm for the assignment problem. With respect to conver-
gence, Theorem 2 states that the upper bound of 2n
wmax/ε
on the number of iterations (see Theorem 1) is tight up to a
factor of four. Theorem 3 considers the behavior of BP when
convergence is not required. There are edge weights for com-
plete bipartite graphs such that tight BP-based approximations
consume a large portion of the convergence time. The exact
number of iterations for a 1
1/√n/ log(n)-approximate solution
−
wmax
belongs to the interval Θ(
.
ε
We have to leave its exact value open. Possibly, a tight analysis
of the approximation time requires a construction different
from our cycle construction.

log(n)/n3

), . . . , 2n

wmax
ε

p

·

·

We proposed an approximate BP algorithm which has
the advantage of outputting a (suboptimal) solution in every
iteration. Also, similar lower bounds for other applications of
BP to combinatorial optimization problems remain an open
research question. An upper bound for the convergence time
for the MWM problem for non-bipartite graphs – under certain
restrictions – is shown in [8]. Our methods can be utilized
to provide a tight runtime analysis in this case too. Finally
we pose the question, under which circumstances can the
proposed approximate BP algorithm be used as a tool when BP
does not converge or when the underlying decision problem
is computationally hard?

REFERENCES

[1] J. Pearl, “Reverend bayes on inference engines: A distributed hierarchical
approach,” in Proceedings of the Second National Conference on Artiﬁcial
Intelligence, 1982, pp. 133–136. 1

[2] F. R. Kschischang, B.

J.

Frey,

and H. Loeliger,

graphs and the sum-product algorithm,” IEEE Trans.
Theory, vol. 47, no. 2, pp. 498–519, 2001.
https://doi.org/10.1109/18.910572 1

“Factor
Information
[Online]. Available:

[3] M. Bayati, D. Shah, and M. Sharma, “Max-product for maximum weight
matching: Convergence, correctness, and LP duality,” IEEE Transactions
on Information Theory, vol. 54, no. 3, pp. 1241–1251, 2008. 1, 2

[4] J. Salez

and D. Shah,

“Belief propagation: An asymptotically
optimal algorithm for the random assignment problem,” Math. Oper.
Res., vol. 34, no. 2, pp. 468–480, 2009.
[Online]. Available:
https://doi.org/10.1287/moor.1090.0380 1

[5] Y. Weiss, “Correctness of local probability propagation in graphical
models with loops,” Neural Computation, vol. 12, no. 1, pp. 1–41, 2000.
[Online]. Available: https://doi.org/10.1162/089976600300015880 2
[6] P. Dusart, “Autour de la fonction qui compte le nombre de nombres

premiers,” Th`ese, Universit´e de Limoges, 1998. 4

[7] M. Mezard and A. Montanari, Information, Physics, and Computation.

Oxford University Press, 2009. 5

[8] S. Ahn, M. Chertkov, A. E. Gelfand, S. Park,

and J. Shin,
“Maximum weight matching using odd-sized cycles: Max-product
Information
belief propagation and half-integrality,”
Theory, vol. 64, no. 3, pp. 1471–1480, 2018.
[Online]. Available:
https://doi.org/10.1109/TIT.2017.2788038 5

IEEE Trans.

