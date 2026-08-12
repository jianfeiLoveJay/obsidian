IEEETRANSACTIONSONINFORMATIONTHEORY 1
Iterative Message Passing Algorithm for
Vertex-Disjoint Shortest Paths
Guowei Dai, Longkun Guo , Gregory Gutin, Xiaoyan Zhang , and Zan-Bo Zhang
Abstract—As an algorithmic framework, message passing an approximation of the dynamic programming when the
is extremely powerful and has wide applications in the con- underlying graph has no cycles [13], [21], [26]. Specifically,
text of different disciplines including communications, coding
BP algorithm provides a natural parallel iterative version of
theory, statistics, signal processing, artificial intelligence and
the dynamic programming in which variable vertices pass
combinatorial optimization. In this paper, we investigate the
performance of a message-passing algorithm called min-sum messages between each other along arcs on graphical mod-
belief propagation (BP) for the vertex-disjoint shortest k-path els. Surprisingly, even for graphs with many cycles, the BP
problem (k-VDSP) on weighted directed graphs, and derive the algorithm performs well in practice and has empirically been
iterativemessage-passingupdaterules.Asthemainresultofthis
shown to give good results [19], [22]. While BP algorithms
paper, we prove that for a weighted directed graph G of order
n, BP algorithm converges to the unique optimal solution of have been shown empirically to be effective in solving many
k-VDSP on G withinO(n2w max )iterations, provided that the instances of optimization problems, theoretical analysis of
weightw e isnonnegativeintegralforeacharce ∈ E(G),where performance of BP algorithms remains far from complete.
w
max
= max{w
e
:e ∈ E(G)}.Tothebestofourknowledge,
Someprogresshasbeenmadeinunderstandingconvergence
this is the first instance where BP algorithm is proved correct
and accuracy of BP algorithms for several optimization and
for NP-hard problems. Additionally, we establish the extensions
of k-VDSP to the case of multiple sources or sinks. decision problems, see, e.g., [3]–[5],[7], [8], [14], [23], [24].
As a major breakthrough, Bayati et al. [4] and Cheng et
Index Terms—Belief propagation, message-passing algorithm,
al. [5] independently simplified the BP algorithm to obtain
iterative algorithms, vertex-disjoint shortest path.
two essentially same algorithms for the maximum weight
matching (MWM) on a bipartite graph. They established the
I. INTRODUCTION convergence of the BP algorithm for MWM, provided that
BELIEFpropagation(BP)isadistributed,message-passing the optimal solution is unique. Bayati et al. [3] as well as
Sanghavi et al. [23] generalized the result by showing the
heuristicalgorithmforsolvingoptimizationandinference
convergence of BP algorithm for the min-cost b-matching
problems on various graphical models. Since the proposition
problem on arbitrary graphs, provided that the corresponding
of BP algorithm by Pearl in 1988 [21], the message-passing
linear programming (LP) relaxation has a unique integral
algorithm based on BP has shown its power as an algo-
optimal solution. Note that the weighted matching problem
rithmic framework and has wide applications in the context
on bipartite graphs can be viewed as a special case of the
of variety of disciplines including satisfiability in discrete
minimum cost flow (MCF) problem. Gamarnik et al. [14]
optimization [1], [9], [19], [20], error correcting code in
proved that BP algorithm for MCF converges to the optimal
informationtheory[13],[15],[18],[22],anddataclusteringin
solution if its optimal solution is unique. Recently, Even and
machine learning [10]. BP algorithm is known as essentially
Halabi [8] developed a BP algorithm for the covering and
Manuscript received December 14, 2020; revised January 15, 2022; packingproblemand established that BP algorithmconverges
accepted January18,2022.ThisworkwassupportedinpartbytheNational to the optimal solution if its LP relaxation has a unique
NaturalScienceFoundationofChinaunderGrant11871280,GrantU1811461,
integraloptimalsolution. Sanghaviet al. [24] investigatedthe
Grant61772005,Grant11971349,andGrant11971196;inpartbytheNatural
ScienceFoundationofGuangdongProvinceunderGrant2020B1515310009; performanceofBP algorithmforthe max-weightindependent
and in part by the Qinglan Project of Jiangsu Province. (Corresponding set problem and established a one-sided relation between BP
author:XiaoyanZhang.)
algorithm and its LP relaxation. Furthermore, an example
Guowei Dai and Xiaoyan Zhang are with the School of Mathematical
ScienceandtheInstituteofMathematics,NanjingNormalUniversity,Nanjing in[24]showsthatBPalgorithmisunlikelytosolvethegeneral
210023,China(e-mail: guoweidai@njnu.edu.cn; royxyzhang@gmail.com). linear programming problem.
LongkunGuoiswiththeDepartmentofComputerScience,QiluUniversity
Graph routing problems have already attracted intensive
ofTechnology, Jinan250353 China(e-mail: longkun.guo@gmail.com).
Gregory Gutin is with the Department of Computer Science, Royal research from mathematicians and computer scientists start-
Holloway University of London, Egham TW20 0EY, U.K. (e-mail: ing from early 1970s. One of the most well-known graph
gutin@cs.rhul.ac.uk).
routing problems is the travelling salesman problem (TSP),
Zan-Bo Zhang is with the School of Statistics and Mathematics and the
Institute ofArtificial Intelligence andDeepLearning,GuangdongUniversity for which Gutin and Punnen [11] provided a compendium of
ofFinanceandEconomics,Guangzhou510320,China(e-mail:zanbozhang@ results. In particular, Chapter 6 of [11] describes a somewhat
gdufe.edu.cn). unexpected result that for any number n of vertices there is
Communicated byD.Mitchell, AssociateEditorforCodingTheory.
Digital ObjectIdentifier 10.1109/TIT.2022.3145232 an infinite number of TSP instances (both asymmetric and
0018-9448©2022IEEE.Personaluseispermitted, butrepublication/redistribution requires IEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.html formoreinformation.

2 IEEETRANSACTIONSONINFORMATIONTHEORY
symmetric) such that the greedy algorithmoutputs the unique of its arcs. Several paths are said to be internally vertex-
worst possible solution. The same result holds for the TSP disjoint if for any two paths of them, there exits no vertices
nearestneighboralgorithm.These results were provedin [12] in common except at the terminals. For a given weighted
and the TSP greedy algorithm result was generalized to other directed graph G with source s ∈ V(G) and sink t ∈ V(G),
combinatorial optimization problems in [2]. the problem k-VDSP aims to find k internally vertex-disjoint
As a class of graph routing problems, the vertex-disjoint paths from s to t, denoted by P 1 ,P 2 ,...,P k, such that
shortest k-path problem (k-VDSP) was first introduced by k i=1 w(P i) is minimized. Let P = {P 1 ,P 2 ,...,P k } and
Suurballe[25].An objectiveofk-VDSPonweighteddirected E(P) = ∪k
i=1
E(P i), where E(P i) denotes the set of arcs in
graphs is to find k internally vertex-disjointpaths from given P i.Foreache∈E(G),definex e asanindicatorvariablesuch
source s to sink t, with minimum total weight. Note that that x e = 1 if e ∈ E(P), and x e = 0 else. Then those arcs
k-VDSP is strongly NP-hard when k ≥ 2 [16], and it will belongtoX ={e∈E(G):x e =1}correspondexactlytothe
be reduced to the classic shortest s-t path problem when union of k internally vertex-disjointpaths that P 1 ,P 2 ,...,P k
k =1. Vertex-disjoint paths are often used in communication in G. So, for any k internally vertex-disjoint paths from s to
networksforreliabilityoftransmissionbetweenagivensource t can be represented by x = {x e : e ∈ E(G)} where x e is
andsink.Inthispaper,wefocusprimarilyontheperformance defined as above.
oftheMin-SumBPalgorithmforfindingtheoptimalsolution Weusew e todenotetheweightoneforanyarce∈E(G).
of k-VDSP. For any vertex i ∈ V(G), denote the sets of out-neighbors
and in-neighbors of i in G by N+ = {j : ij ∈ E(G)} and
i
N i − ={j :ji∈E(G)},respectively,andletN i =N i +∪N i − .
A. Our Contributions
Throughoutthe paper, we assume there exist no in-neighbors
The contributions of this paper, in detail, are as follows. of the source vertexand out-neighborsof the sink vertex,that
First, we derivea message-passingalgorithmbased onBP for is, N s − =N t + =∅. Let x e be the 0-1 value assigned to each
finding the optimal solution of k-VDSP. Then we establish arce∈E(G).Thenthek-VDSPongraphG=(V,E,w) can
that for any weighted directed graph G with n vertices, as also be formulated as the follows:
longastheoptimalsolutionisunique,ouralgorithmconverges 
to the optimal solution x∗ within ( U +1)n iterations, min w e x e (1)
2o(x∗)
where U and o(x∗) are the maximum weight of a simple  e∈E(G) 
directed path and minimum weight of a directed cycle in the s.t. x sj = x jt =k, (2)
residualnetworkG x∗, respectively.Note thatwe developnew j∈N+ j∈N−
s t
and more complex rules in our proof since the constraints
of k-VDSP are more complex than those of the previous x ij − x ji =0, ∀ i∈V (3)
problems in [4], [8], [14], [23], [24]. Next, we show that j∈  N i + j∈  N i −
the Min-Sum BP algorithm converges to the unique optimal x ij + x ji ∈{0,2}, ∀ i∈V (4)
solution in O(n2w max) iterations, provided that the weight
j∈N+ j∈N−
w w e ma i x s = non m n a e x g { a w tiv e e : i e nt ∈ egr E al (G fo )} r . e A ac d h dit a i r o c na e lly ∈ , w E e ( e G x ) t , en w d h o e u re r x e ∈ i {0,1}, ∀ i e∈E(G), (5)
analysisto establishtheextensionsofk-VDSPto theversions where V = V(G) \ {s,t}. Constraints (2) and (3) state
of multiple sources or sinks. that there are exactly k paths from s to t. The third type of
IthasbeenshownthatBPalgorithmisunlikelytosolvethe constraints (4) state that these k paths are internally vertex-
generallinearprogrammingproblembymeansofacounterex- disjoint.Notethatonthepremisethat(3)and(5)aresatisfied,
ample[24].Thus,ourresultsextendthescopeoftheproblems the type of constraints (4) hold if and only if
thatare provablysolvableby the BP algorithm.To the bestof  
our knowledge, this is the first instance where BP algorithm x ij + x ji ≤2, ∀ i∈V(G)\{s,t}.
is proved correct for NP-hard problems. We believe that our j∈N+ j∈N−
i i
methodscan help to analyse the convergenceand accuracy of
BPalgorithmsforotherNP-hardproblemswithmorecomplex Define a vertex demand function f :V(G) →Z that f s =
constraints. k,f t = −k and f i = 0 for any i ∈ V(G) \ {s,t}. Then
the k-VDSP on G can be formulated as the following integer
II. PRELIMINARIES programming problem (IP):

A. Problem Statement min w e x e
The input to the vertex-disjoint shortest k-path problem  e∈E(G) 
(k-VDSP) is a weighteddirectedgraphG=(V,E,w), where s.t. x ij − x ji =f i , ∀ i∈V(G);
V(G),E(G) denote the set of vertices and arcs (i.e., directed
j∈N+ j∈N−
edges) in G, respectively, and w : E → R+ is a weight i i
function. A path a connected subgraph where each vertex is x ij + x ji ≤2, ∀ i∈V(G)\{s,t};
of degree 2 and each vertex in the subgraph is distinct. The j∈N+ j∈N−
i i
weightw(P) ofa pathP isdefinedasthesumof theweights x e ∈{0,1}, ∀ e∈E(G).

DAIetal.: ITERATIVEMESSAGEPASSINGALGORITHMFORVERTEX-DISJOINTSHORTESTPATHS 3
Let x be the feasible solution of the integer programming We definetheinducedk-VDSPproblem,denotedbyVDSPQ,
r
problem(IP)above.Thentheoptimalsolutionofk-VDSPcan oncomputationtreeTQ.Givenarootr,letVo(TQ)⊂V(TQ)
r r r
be defined as: denote the set of all the vertices but the leaves of TQ. Let
r
 V o (TQ)=:Vo(TQ)\{s,t}. Then the problemVDSPQ can
x∗ =argm x in w e x e . be for r mulated as f r ollows: r
e∈E(G) 
min w e y e
B. Computation Tree
e∈E(TQ)
r 
Nowweintroducetheconceptsofrootedtreeandcomputa- s.t. y ij − y ji=f γ(i) , ∀ i ∈Vo (T r Q )
tiontree,whichhasbeenusedwidelyinthepreviousliterature
j∈N+(TQ) j∈N−(TQ)
[3], [4], [6], [13], [14], [23]. A connected acyclic graph (i.e., i r i r
containing no cycles) is called a tree. Any nontrivial tree y ij + y ji ≤2, ∀ i ∈V o (T r Q )
contains a vertex which has exactly one neighbor. Such a j∈N+(TQ) j∈N−(TQ)
vertex is called a leaf. Throughout of the paper, we define
i r i r
a rooted tree T r as a tree T with a specified arc r, called the y e ∈{0,1}, ∀ e∈E(T r Q )
root of T. It should be noted that the definition of the root where γ(s)=s,γ(t)=t.
of a tree sometimes refers to a specified vertex, in contrast Remark: The computation tree is locally equivalent to the
to a specified arc. In a tree, any two vertices are connected originalgraph,whichmeansonecanviewtheiterativeprocess
by exactly one path. We denote the unique path connecting of BP algorithm as sending the messages along the way from
vertices i and j in a tree T by iTj. For a rooted tree T r with leafverticestotherootinthecomputationtree.Allthevertices
root r, the level of a vertex j in T r is the length of the path oncomputationtreewillsendmessagestotheirparentsateach
rTj, and each vertex on the path rTj is called an ancestor iteration, and the direction of message-passing is independent
of j. For two adjacent vertices i,j in T, if i is an ancestor of of the direction of those arcs. One can guess that the BP
j, then i is also called a parent of j, and j is a child of i. algorithm for VDSPQ works quite similar as BP algorithm
r
We use T r Q to denote the Q-level computation tree asso- for k-VDSP on the original graph, and the reasoning will be
ciated with arc r as the root. Denote the set of vertices and formalized in the Lemma 3.
arcs in TQ by V(TQ) and E(TQ), respectively. Each vertex
r r r
or arc of T r Q is a duplicate of some vertex or arc of the III. MIN-SUMBP ALGORITHMFOR k-VDSP
original graph G. Define a mapping γQ : V(TQ) → V(G)
r r A. Factorized Optimization Problem and Factor Graph
such that if i ∈ V(TQ) is a duplicate of i ∈ V(G), then
r
γQ(i) = i. Denote by L(TQ) the set of leaves of TQ. For Consider the optimization problem (P) as following:
r r r  
any i ∈V(T r Q), denote by P(i) the parent of i in T r Q. It is min φ i(x i)+ ψ D(x D)
essentially a breadth-first search tree of G (with repetition of
i∈V D∈D
vertices allowed) starting from r up to depth Q. In detail, s.t. x i ∈R, ∀i∈V,
we inductively define TQ a follows.
r
• r Le = t u u v v ∈ , c E on (G sis ) t . s T o h f e t n wo the ve c rt o i m ce p s u u ta , ti v o  n a t n r d ee an T r 0 a , rc w u h  e v r  e , w of h s e u re bs V ets is o a f fi V nit r e ep s r e e t s o e f nt v i a n r g ia c b o l n e s s tr a a n i d nt D s. H is e a re fi φ ni i te : R col → lec R tio ∪ n
such that γ0(u) = u and γ0(v) = v. The arc r = uv {∞} and ψ D :R|D| →R∪{∞},∀D∈D are extended real-
is the rooto r f T0, and vertice r s u,v are considered to be valued functions, where each φ i is called a variable function
at 0-level of T0 r . and each ψ D is called a factor function. We also call the
• Inductively, th r e computation tree T r Q can be obtained optimization problem (P) a factorized optimization problem.
from TQ−1 by adding vertices to V(TQ−1) and arcs to Next, we introduce the concept of a factor graph of a
r r
E(TQ−1)asfollows.Foreachleafvertexi ∈L(TQ−1), factorizedoptimizationproblem,whichcanbereferredto[17].
addv r ertexj toexpandV(TQ−1)andaddarcij o r rji A factorgraphF P of(P)is a bipartitegraphwith oneparti-
to expand E(TQ−1) if there r is a vertex j ∈ V(G) such tion containing variables V and the other partition containing
that ij ∈ E(G) r or ji ∈ E(G) with γQ−1(i) = i, and factor vertices D corresponding to the constraints, and there
γQ−1(P(i)) = j. In this case, define r P(j) = i, the is an edge (i,D)∈V ×D if and only if i∈D.
r
map γQ(j) = j, and level of j as Q. Indeed, γQ is
r r
identical to γQ−1 for vertices in V(TQ−1)⊆V(TQ). B. Algorithm
r r r
• For any e = ij ∈ E(G), the arc from i to j in T r Q is It is well-known that BP algorithms are always viewed
alsodenotedbyeforsimplicityandisassignedthesame
as heuristic algorithms for factorized optimization problems
weightw easthatinG,whereγ
r
Q(i)=iandγ
r
Q(j)=j.
and operate by passing messages iteratively with variables
An example of a computation tree can be seen in Fig. 1. and factors. Next, we will represent k-VDSP as a factorized
In what follows, we shall drop reference to r,Q in notation optimization problem. Let E i be the set of arcs incident to
of γ r Q when it is clear from context what r,Q are and abuse i and x Ei = {x e : e ∈ E i }, where x e ∈ {0,1} and x
notation by denoting γ(ij)=γ(i)γ(j). is a solution of k-VDSP. Recall that f s = k,f t = −k and
Now assume there is a k-VDSP problemstated for a graph f i = 0 for any i ∈ V(G) \ {s,t}. We define the factor
G = (V(G),E(G),w) with given source s and sink t. and variable functions φ,ψ for each e ∈ E(G),i ∈ V(G),

4 IEEETRANSACTIONSONINFORMATIONTHEORY
Fig.1. Thefigureontheleftisanoriginal graph,andtherightoneisa2-level computation treeofit,denoted byT v 2 1v2 withrootv 1 v 2.
respectively as follows: φ e(x e) = w e x e if x e ∈ {0,1}, which is also known as the belief of the root arc. Finally,
otherwise φ e(x e)=+∞; and we describe the Min-Sum BP algorithm for solving k-VDSP
⎧
in detail as Algorithm 1.
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ 0 i
j
f
∈

N
i
i +
∈
x
{
i
s
j
,
−
t}
j
a
∈

n
N
d
i −
x ji =

f i Al
1
g
:
ori
I
t
n
h
it
m
ial
1
ize
Min
q
-Sum
=
BP
0,
Alg
m
o
e
r
s
it
s
h
a
m
ge
for
m
k
0 i→
-V
e
D
(x
S
e
P
) = 0,
ψ i(x Ei )= ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ 0 i
a
f
n
i
d
∈
j∈
 V
N
,
i
j
x
∈
i
N
j
i +
≤
x i
2
j = j∈N i − x ji , ∀ 2
3:
: e f = o
F
r i
o
j q
r
∈ =
ea
E
c
1
h
, ( 2 G
e
, ) .
=
. ..
i
,
j
Q
∈
d
E
o
(G), update messages as follows:
+∞ otherwise, m

q
e→j
(x e)=φ e(x e)+mq
i→
−1
e
(x
e
),

w
to
h
s
e
o
re
lv
V
ing
=
t
:
h
V
e
(
f
G
ol
)
lo
\
w
{

s
in
,
g
t}
f
.
a
T
c
h
to
e
r
n
iz
,
e
so
d
lv
o
i

p
n
t
g
im
k
i
-
z
V
at
D
io
S
n
P
p
is
ro
e
b
q
l
u
e
i
m
va
:
lent mq i→e (x e)=
x
m
Ei
i
\
n
e
ψ i(x Ei )+
e∈Ei\e
mq e→i (x e) .
min φ e(x e)+ ψ i(x Ei ) 4: q :=q+1
e∈E(G) i∈V(G) 5: end for
s.t. x e ∈{0,1}, ∀e∈E(G). 6: For each e=ij ∈E(G), set the belief function as
Let T =: T r Q be a computation tree. For each arc e = ij bQ e (x e)=mQ e→i (x e)+mQ e→j (x e)−φ e(x e)
on the computation tree, T −e has two components, the one
of which containing i denoted by T 1. We define a message 7: Calculate the belief estimate by finding
f s u u n b c tr t e io e n T m 1 e ∪ → { j( e x } e , ) a a n s d th d e efi o n p e tim m u i m →e ( ( m x i e n ) -s a u s m th w e ei o g p h t t i s m ) u o m nt o h n e x 8 : Q e R ∈ et a u r rn g x x e Q m ∈{ i = 0 n ,1 { } x b Q Q e ( : x e e) ∈ fo E r ( e G a ) c } h . e∈E(G).
e
the subtree T 1. Due to the nature of tree structure, these two
message functions can be recursively defined as follows: for
C. Results
any arc e=ij,
Before formally stating our results, we need to define the
m e→j(x e)=φ e(x e)+m i→e(x e ), (6) residual network first with a feasible solution x of k-VDSP.
m i→e(x e)= x min ψ i(x Ei )+  m e→i(x e) . (7) D fe e a fi si n b e le G s x olu to tio b n e x the as re fo si l d lo u w al r n u e le tw s: ork of G with respect to a
Ei\e
e∈Ei\e
• G x has the same vertex set as G, i.e., V(G)=V(G x);
Using (6)-(7), starting from leaves, the message functions • Foreache=ij ∈E(G),ifx e =0,thene=ij ∈E(G x)
m e→j(x e) and m i→e(x e) can be computed for all e ∈ with weight w
i
x
j
=w ij;
E(G),i ∈ V(G). Then, the update messages for each vertex • For each e = ij ∈ E(G), if x e = 1, then e = ji ∈
and arc are as follows: E(G x) with weight w
j
x
i
=−w ij.
m

q
e→j
(x e)=φ e(x e)+mq
i→
−1
e
(x
e
), Let
 

mq i→e (x e)= x m Ei i \ n e ψ i(x Ei )+
e∈Ei\e
mq e→i (x e) . o(x)= C m ∈ i C n wx (C)= e∈C w e x ,
At the root arc r = uv, combine the messages m r→u(x r)
w
th
h
e
e
u
re
ni
C
qu
i
e
s
o
th
p
e
tim
se
a
t
l
o
s
f
o
d
lu
ir
t
e
io
c
n
ted
of
cy
k
c
-V
le
D
s
S
in
P
G
in
x.
d
N
ir
o
e
t
c
e
te
t
d
ha
g
t
r
i
a
f
p
x
h
∗
G
is
,
a it n e d rat m io r n → Q v( o x n r) t , h w e e co c m an pu d ta e t r i i o v n e t t r h e e e T es Q tim as ation at the end of then o(x∗) > 0 must hold in G x∗, or else we can change x∗
r along the minimum weight cycle in o(x∗) without increasing
bQ
r
(x r)=mQ
r→u
(x r)+mQ
r→v
(x r)−φ r(x r), its weight.

DAIetal.: ITERATIVEMESSAGEPASSINGALGORITHMFORVERTEX-DISJOINTSHORTESTPATHS 5
Theorem 1: For any directed graph G of order n, if the Q = 1, the statement can be checked to be true trivially.
k-VDSPonGhasauniqueoptimalsolutionx∗,thenMin-Sum Denote by E u(T
r
Q) the set of arcs incident to u in T
r
Q. For
BPalgorithmconvergestox∗within(
2o(
U
x∗)
+1)niterations, Q>1andeacha∈E u(T
r
Q)\rwitha=pu(orup),letT
a
Q
→
−
u
1
where U is the maximum weight of a simple directed path be the subtree of TQ that includes everything in TQ but
r→v r→v
in G x∗. That is to say x Q =x∗ when Q≥(
2o(
U
x∗)
+1)n. u,vandr.Considerthesub-problemVDSPQ
a→
−
u
1(z)asfollows.
Let w max =max{w e :e ∈E(G)}. Then by the definition 
of U, we have that U ≤ nw max since simple directed path min w e y e
has at most n − 1 arcs in G x∗. If w e is integral for each e∈  E(T a Q → − u 1) 
e∈E(G), then o(x∗) is also positive integral. It follows that s.t. y ij − y ji =f γ(i) ,

2o(
U
x∗)
 ≤ nw max. Combine this with Theorem 1, we have
j∈N+(TQ) j∈N−(TQ)
the corollary as follows. i r i r
Corollary 2: For any directed graph G of size n, if the ∀ i  ∈Vo (T a Q → − u 1 ); 
problemk-VDSPonGhasauniqueoptimalsolutionx∗,then y ij + y ji ≤2,
Min-Sum BP algorithm converges to x∗ within O(n2w max) j∈N+(TQ) j∈N−(TQ)
i r i r
iterations,providedthattheweightoneacharcisnonnegative ∀ i∈Vo (TQ−1 )\{s,t};
a→u
integral.
y
a
=z,
IV. PROOF OF CORRECTNESS AND CONVERGENCE
y
e
∈{0,1}, ∀ e∈E(T
a
Q
→
−
u
1 ).
Inthissection,weestablishtheconvergenceofMin-SumBP By induction hypothesis, it must be that the value
algorithm to the optimal solution of k-VDSP. Before proving of mQ−1 (z) equals the weight of the solution of
a→γ(u)
Theorem1,wewillshowthefollowingtwoimportantlemmas. VDSPQ−1(z). Due to the hypothesis and the relation of
L co o m os p e u ly tat s io p n ea t k re in e g T , r Q V : D th S e P r Q r e a i r s e e s s im se i n la ti r al c l o y ns a tra k i - n V ts D f S o P r a o n n y a th rc e s th u a b t tr t e h e a e → T p u a r Q o → − b u l 1 em for V a D ll SP a Q ∈ E (z u ) (T is r Q e ) q \ u r iv w al i e t n h t T to r Q →v , it follows
e∈E(T r Q) and any vertex, except for those at the Q-level.  r→v
Lemma 3: Let x Q r be the value of the output of the BP min w r z+ mQ a→ − γ 1 (u) (x a)
a
th
lg
er
o
e
ri
e
th
x
m
ists
at
an
th
o
e
p
e
ti
n
m
d
a
o
l
f
so
it
l
e
u
r
t
a
io
ti
n
on
y∗
Q
of
o
V
n
D
ar
S
c
PQ
r ∈
suc
E
h
(G
th
)
a
.
t
T
y∗
he
=
n

a∈Eu(T
r
Q)\r

x Q where r is the root of computation tree r TQ. r s.t. y uv − y vu =f γ(u)
r r
Proof: Let r = uv be the root arc of computation tree v∈  N u +(T r Q) v∈  N u −(T r Q)
T r Q.Bydefinition,T r Qhastwocomponents,denotedbyC and y uv+ y vu ≤2,if u∈/ {s,t}
C, which are connected via the root arc r. Without loss of
v∈N+(TQ) v∈N−(TQ)
generality, we assume C is the component containing u. Let y r = u z r u r
T
N
r
e
Q →
xt
v
,
d
le
e
t
no
V
te
0(
C
TQ
∪r,
)
w
b
h
e
ic
t
h
he
ca
s
n
et
be
of
vi
a
e
l
w
l
e
th
d
e
as
ve
a
rt
s
i
u
c
b
es
tre
o
e
f
o
T
f
Q
T r Q.
,
y
a
∈{0,1},∀ a∈E u(T
r
Q )\r.
r→v r→v
excluding those at the Q-level. Recall that γ(s) = s and This is exactly the same as the relation between mQ (z)
r→γ(v)
γ
D
(
e
t
n
)
ot
=
e b
t,
y
w
E
h
(
e
T
re
Q
s,t
)
i
t
s
h
t
e
he
se
g
t
iv
o
e
f
n
ar
s
c
o
s
ur
i
c
n
e
T
a
Q
nds
.
in
T
k
h
,
e
r
n
es
w
pe
e
c
d
ti
e
v
fi
e
n
ly
e
. and message function mQ
a→
−
γ
1
(u)
(·) for a∈E u(T
r
Q)\r as
r→v r→v 
VDSPQ r→v (z) as follo

ws. mQ
r→γ(v)
(z)=w
r
z+ mQ
a→
−
γ
1
(u)
(x a).
min w e y e a∈Eu(T r Q)\r
e∈  E(T r Q →v )  That is, mQ (z) is exactly the same as the weight of
r→γ(v)
s.t. y ij − y ji =f γ(i) , optimal assignment of VDSPQ (z). Using this equivalence,
r→v
j∈N+(TQ) j∈N−(TQ) we will complete the proof of Lemma 3.
i r i r
∀ i  ∈Vo (T r Q →v );  Finally, for given r = uv, the problem VDSPQ r (z) is
equivalent to
y ij + y ji ≤2,  
j∈N i +(T r Q) j∈N i −(T r Q) min −w r z+ w e y e+ w e y e
∀ i∈Vo (T r Q →v )\{s,t};  e∈E(T r Q →u ) e∈E(T r Q →v )
y r =z, s.t. y ij − y ji =f γ(i) , ∀ i∈Vo (T r Q )
y e ∈{0,1}, ∀ e∈E(T r Q →v ), j∈N i +(T r Q)  j∈N i −(T r Q)
where N i + (T r Q),N i − (T r Q) denote the sets of out-neighbors y ij + y ji ≤2, ∀ i∈Vo (T r Q )\{s,t}
and in-neighbors of i in T r Q, respectively. j∈N i +(T r Q) j∈N i −(T r Q)
(ru
N
nn
o
i
w
n
,
g
w
on
e
G
sh
)
ow
the
th
v
a
a
t
lu
u
e
n
o
d
f
er
m
t
e
h
s
e
sa
M
ge
in
f
-
u
S
n
u
c
m
tion
BP
mQ
algorit
(
h
z
m
)
y
e
∈{0,1}, ∀ e∈E(T
r
Q
→i
)∪E(T
r
Q
→j
).
r→γ(v)
is the same as the weight of the optimal assignment for That means the min-sum weights of an optimal
VDSPQ (z). This can be established by induction. When solution of the problem VDSPQ(z) equals
r→v r

6 IEEETRANSACTIONSONINFORMATIONTHEORY
Fig.2. Anexample ofthepathP onacomputation treeT v 2 1v2 withdashedarcs.
mQ r→γ(u) (z) + mQ r→γ(v) (z) − w r z for any z ∈ {0,1}. such that for −Q≤l ≤Q,
Now the claim of Lemma 3 follows immediately. (cid:2) r
l
∈Ω ∗−Λ ∗
Lemma 3 exhibits the relation between BP algorithm and ⇔ both r l and r 0 have the same orientation;
computation tree. Next, we prove our main technical lemma
which is a key to the proof of Theorem 1.
r
l
∈Ω ∗−Λ ∗
Lemma 4: Let x∗ be the unique optimal solution of ⇔ both r l and r 0 have the opposite orientation.
k-VDSP on G. If y∗ is the optimal solution of VDSPQ r and Figure 2 demonstrates this path P with dashed arcs.
Q≥( 2o( U x∗) +1)n, then we have y r ∗ = x∗ r where r is the Now,we can modifyy∗ to obtaina new feasible solutiony
root of T
r
Q. ofVDSPQ
r
asfollowing.LetΩ =(Ω∗−Ω∗∩P)∪(Λ∗∩P)and
Proof: Suppose on the contrary that there is an arc r 0 = y bethesolutionofVDSPQcorrespondingtoΩ.Furthermore,
r
u x g T Ω e ∗ e v h ∗ n e − = e n ∈ r , a Λ 1 l E b i ∗ } t y . ( y G a , I t f n h w ) d a e e s f Ω u d e a c ∗ e a s h fi s s = i u n b t m i h l t e { i a e o e t s n y o ∈ y r ∗ l r ∗ u o 0 0 E t f i > o ( = Λ n T x ∗ r Q o x ∗ e 0 0 f a ) ∗ r , 0 n V : . d i. D y e L e Ω ∗ . S e , P ∗ t = x Q , Λ ∗ r0 w 1 ∗ c } = e a . = n h W 0 b a { i e v a t e e h n o o d b ∈ t u h t y a t a E r i ∗ t l n 0 o ( e r s G = d 0 s ) b o 1 ∈ y f : . f i v n o e c r r • i t d e a x i e n f n y i r t  v o t e o n a r n t P i e d x , a r n  i  d  o h n b av e P e lo , t n h g l e et t s o a r m  P e a . n o T d ri h e r e n  n  ta b w ti e o e n th h a e a s v a e r r 0 c t , s h t a h w t e h n f i o c r h a a n r y e
modifying y∗ such that its total weight r s 0 trictly less than that y ij − y ji
of y∗, then a contradiction to the optimality of y∗ arises and j∈N i +(T r Q) j∈N i −(T r Q) 
Lemma 4 is established. = (−1+ y ij)−(−1+ y ji)
abo
L
v
e
e
t
.
r
W
0
e
=
wi
u
ll
v
ch
b
o
e
o
t
s
h
e
e
an
ro
a
o
r
t
c
o
r
f
1
t
=
he
r
c
0
o
i
m
nc
p
i
u
d
t
e
a
n
ti
t
o
t
n
o
t
u
re
i
e
n
T
T
r
r
Q Q0
0
a
a
s
s = f γ(i) ,
j∈N i +(T r Q) j∈N i −(T r Q)
the following rules:
 and  
• If x ju =0, then there exists an in-arc r 1 for u y ij + y ji
• s O u t c h j h ∈ e N r t w h u a i ( s T t e r Q y , 0 r ∗ ) 1 th = er 1 e ; exists an out-arc r 1 for u such = j ( ∈ − N 1 i + + (T r Q) j∈ y N ij i − ) ( + T r Q (− ) 1+  y ji)
that x∗ r1 =1. j∈N i +(T r Q) j∈N i −(T r Q)
Similarly,we canchooseanarc r −1 =r 0 incidenttov in T r Q 0 = (−1+1)+(−1+1)=0≤2.
as the follo  wing rules: • if r and r h  ave the oppos  ite orientation as r 0, then
• If x jv =0, then there exists an out-arcr −1 for y ij − y ji
v s
j
u
∈
c
N
h
v(
t
T
h r a
Q
0 t
)
y∗ =1; j∈N i +(T r Q ) j∈N i − 
• Otherwise, th r e − r 1 e exists an in-arc r −1 for v such that = (1+ y ij)−(1+ y ji)
x∗ =1. j∈N+(TQ) j∈N−(TQ)
Let u 1 r , − v 1 1 be the other ends of r 1 ,r −1, respectively. Then we = f γ(i) , i r i r
can apply recursively the similar reasoning for u 1 and v 1 so and  
that the feasibility condition of x∗,y∗ and the inequalities y ij + y ji
between the value of components of x∗,y∗ at arcs r 1 ,r −1 j∈N+(TQ) j∈N−(TQ)
lead to the existence of arcs r 2 ,r −2 incident to u 1 ,v 1, i r i r 
respectively. Continuing this manner all the way down to
= (1+ y ij)+(1+ y ji)
the leaves, we will find a path starting and ending in leaves j∈N i +(T r Q) j∈N i −(T r Q)
of T r Q 0 , denoted by P = {r −Q ,...,r −1 ,r 0 ,r 1 ,...,r Q }, = (1+0)+(1+0)=2≤2.

DAIetal.: ITERATIVEMESSAGEPASSINGALGORITHMFORVERTEX-DISJOINTSHORTESTPATHS 7
• if r has the same orientation and r has the opposite where w(P ),w(D),w(C i) denote the sum of weights of all
orientation as r 0, then both r and r are in-arcs or out- the arcs in w(P ),w(D),w(C i), respectively.
arcs for i. Finally, for any Q≥( U +1)n, we have
2o(x∗)
(1) If both r and r are in-arcs for i, then  
y − y w y∗− w y
ij ji e e e e
j∈N i +(T r Q) j∈N i −(T r Q)  e∈E  (T r Q) e∈E(T r Q)
= y ij −(−1+1+ y ji) = w e(y e ∗−y e)
j∈N+(TQ) j∈N−(TQ) e∈E(TQ)
i r i r r 
= f γ(i) , = w e − w e
and   e∈Ω∗∩P e∈Λ∗∩P
y ij + y ji =
j∈N+(TQ) j∈N−(TQ) e∈ i r i r 
= y ij +(−1+1+ y ji)
j∈N+(TQ) j∈N−(TQ)
i r i r
≤ 2.
(2) If both r and r are out-arcs for i, then
y − y
ij ji
j∈N+(TQ) j∈N−(TQ)
i r  i r 
= (−1+1+ y ij) − y ji
j∈N+(TQ) j∈N−(TQ) i r i r = f γ(i) ,
and
 
y ij + y ji
j∈N+(TQ) j∈N−(TQ) i r  i r 
= (−1+1+ y ij)+ y ji
j∈N+(TQ) j∈N−(TQ)
i r i r
≤ 2.
This implies y satisfies all the other equality constraints of
VDSPQ, since only the values of the arcs in P are changed.
r
Therefore, y is a feasible solution of VDSPQ.
r
Recall that P = {r −Q ,...,r −1 ,r 0 ,r 1 ,...,r Q }. For any
r l = ij ∈ P, we define r l = ij if x∗ r = 0, and
r l = ji if x∗ r = 1, where −Q ≤ l ≤ Q l . Let P =
{r −Q ,...,r −1 , l r 0 ,r 1 ,...,r Q }. Given the value of x∗ and
definition of r l, it can be checked that r l is an arc in the
residualnetworkG x∗, and P is a directed walk in G x∗. Then
P can be decomposed into a simple directed path D and a
collectionofsimpledirectedcyclesC 1 ,...,C d.Notethateach
simpledirectedcycleorpathonG x∗ canhaveatmostn arcs.
Since there are 2Q+1 arcs in P and Q ≥ ( U +1)n,
2o(x∗)
we have
d>
2Q+1
≥
2(
2o(
U
x∗)
+1)n+1
>
U
.
n n o(x∗)
Then we can obtain that the weight of P is strictly positive:
m
w(P ) = w(D)+ w(C i)
i=1
≥ −U +d·o(x∗ )
U
> −U + o(x∗ ) o(x∗)
= 0,
(cid:0)
w e
P
= w(P )
> 0.
Thelast inequalityleadsa contradictionthat y∗ isthe optimal
solution of VDSPQ which completes the proof. (cid:2)
r
NowwecancompletetheproofofTheorem1andestablish
the correctnessand convergenceof Min-Sum BP for k-VDSP
as follows.
ProofofTheorem1:Supposetothecontrarythatthereexists
r ∈ E(G) and Q ≥ ( U  +1)n such that x Q = x∗. 2o(X∗) r r According to the relation between BP and computation tree
TQ as Lemma 3, there is an optimal solution y∗ of VDSPQ r r
such that y∗ = x Q when r is the root of TQ. Then we
r r r have y∗ = x∗ which contradicts Lemma 4. Therefore, the
r r
assumption that x Q = x∗ does not hold. This completes the r r
proof of Theorem 1.
V. EXTENSIONS
We now establish the extensions of k-VDSP to the ver-
sions of multiple sources or sinks. The main ideas remain
unchanged,andthusthe proofsare omittedhere.The keydif-
ferences in mathematical programming between the problem
k-VDSP and its versions are the definition of vertex demand
function f :V(G)→Z for some i∈V(G).
A. The Version of Multiple Sources
For k given sources S := {s 1 ,s 2 ,...,s k } ⊆ V(G) and a
sink t ∈ V(G), it aims to compute k vertex-disjoint (besides
t)pathsP 1 ,P 2 ,...,P k inG,suchthat k i=1 w(P i)attainsthe
minimum. Define the function f : V(G) → Z that f t = −k,
f i = 1 for any i ∈ S and f i = 0 for any i ∈ V(G)\({t}∪
S). The version of multiple sources is given by the following
integer program:

min w e x e
e∈E(G)  
s.t. x ij − x ji =f i , ∀i∈V(G)
j∈N+ j∈N−
i i
x ij + x ji ≤2,∀i∈V(G)\({t}∪S)
j∈N+ j∈N−
i i
x e ∈{0,1}, ∀ e∈E(G).

8 IEEETRANSACTIONSONINFORMATIONTHEORY
B. The Version of Multiple Sinks REFERENCES
For a given a source s ∈ V(G) and k sinks T :=
[1] D.Achlioptas andF.Ricci-Tersenghi, “Onthesolution-space geometry
{t 1 ,t 2 ,...,t k } ⊆ V(G), it aims to compute k vertex- ofrandom constraint satisfaction problems,” inProc. 38thAnnu. ACM
disjoint (besides s) paths P 1 ,P 2 ,...,P k in G, such that Symp.TheoryComput.(STOC),2006,pp.130–139.
i=1,2,...,k
w(P i) attains the minimum. Define the function [2] J
fa
.
il
B
s,
a
”
n
D
g-
i
J
s
e
c
n
r
s
e
e
te
n,
O
G
pt
.
im
G
.,
ut
v
in
o
,
l.
a
1
n
,
d
no
A
.
.
2,
Y
p
eo
p
,
.1 “
2
W
1
h
–
e
1
n
27
t
,
h
N
e
o
g
v
r
.
e
2
ed
0
y
04
a
.
lgorithm
f : V(G) → Z that f s = k, f i = −1 for any i ∈ T and [3] M. Bayati, C. Borgs, J. Chayes, and R. Zecchina, “Belief propagation
f i =0 for any i∈V(G)\({s}∪T). The version of multiple for weighted b-matchings on arbitrary graphs and its relation to linear
programswithintegersolutions,”SIAMJ.DiscreteMath.,vol.25,no.2,
sinks is given by the following integer program:
 pp.989–1011,Jan.2011.
min w e x e [4] M ma . t B ch a i y n a g t : i, C D o . n S v h e a r h g , en a c n e d , M co . r S re h c a t r n m es a s , , “M an a d x- L p P ro d d u u a c l t it f y o ,” rm IE a E xi E mu T m ran w s e . i I g n h f t .
e∈E(G) Theory,vol.54,no.3,pp.1241–1251,Mar.2008.
 
[5] Y.-S. Cheng, M. Neely, and K. M. Chugg, “Iterative message passing
s.t. x ij − x ji =f i , ∀i∈V(G) algorithm for bipartite maximum weighted matching,” in Proc. IEEE
j∈N+ j∈N− Int.Symp.Inf.Theory,Jul.2006,pp.1934–1938.
i i [6] G.Dai,L.Guo,G.Gutin,X.Zhang,andZ.-B.Zhang,“Convergenceand
x ij + x ji ≤2, ∀i∈V(G)\({s}∪T) correctnessofbeliefpropagationforweightedmin–maxflow,”Discrete
Appl.Math.,tobepublished, doi: 10.1016/j.dam.2021.12.025.
j∈N+ j∈N−
i i [7] G. Dai, F. Li, Y. Sun, D. Xu, and X. Zhang, “Convergence and
x e ∈{0,1}, ∀ e∈E(G). correctness of belief propagation for the Chinese postman problem,”
J.GlobalOptim.,vol.75,no.3,pp.813–831,Nov.2019.
[8] G.EvenandN.Halabi,“Analysisofthemin-sumalgorithmforpacking
C. The Version of Multiple Sources and Multiple Sinks and covering problems via linear programming,” IEEE Trans. Inf.
Theory,vol.61,no.10,pp.5295–5305,Oct.2015.
For k given sources {s 1 ,s 2 ,...,s k } ⊆ V(G) and k sinks [9] U. Feige, E. Mossel, and D. Vilenchik, “Complete convergence of
{t 1 ,t 2 ,...,t k }⊆V(G), it aims to compute k vertex-disjoint messagepassingalgorithmsforsomesatisfiabilityproblems,”inApprox-
paths P 1 ,P 2 ,...,P k in G, such that k i=1 w(P i) attains the i a m n a d ti T o e n c , hn R i a q n u d e o s, m 2 iz 0 a 0 t 6 io , n p , p. an 3 d 39 C –3 o 5 m 0 b . inatorial Optimization. Algorithms
minimum. Let S := {s 1 ,s 2 ,...,s k }, T := {t 1 ,t 2 ,...,t k }. [10] B.J.FreyandD.Dueck,“Clusteringbypassingmessagesbetweendata
Define the function f :V(G)→Z that f i =1 for any i∈S, points,”Science, vol.315,no.5814,pp.972–976,Feb.2007.
f
i
=−1foranyi∈T andf
i
=0foranyi∈V(G)\(S∪T). [11] G
Va
.
ri
G
at
u
i
t
o
i
n
n
s.
a
N
nd
orw
A
e
.
ll
P
,
u
M
nn
A
e
,
n,
US
T
A
he
:K
Tr
lu
a
w
ve
e
l
r
i
,
ng
20
S
0
a
2
l
.
esman Problem and its
Theversionofk sourcesandk sinksisgivenbythefollowing [12] G. Gutin, A. Yeo, and A. Zverovich, “Traveling salesman should not
integer program: begreedy: Domination analysis ofgreedy-type heuristics fortheTSP,”
 DiscreteAppl.Math.,vol.117,nos.1–3,pp.81–86,Mar.2002.
min w e x e [13] R. G. Gallager, Low Density Parity Check Codes. Cambridge, U.K.,
1963,pp.21–28.
e∈E(G)
  [14] D. Gamarnik, D. Shah, and Y. Wei, “Belief propagation for min-cost
s.t. x ij − x ji =f i , ∀i∈V(G) networkflow:Convergenceandcorrectness,”Oper.Res.,vol.60,no.2,
pp.410–428,Apr.2012.
j  ∈N i + j  ∈N i − [15] G.B.Horn,“Iterative decoding andpseudocodewords,” Ph.D.disserta-
tion, Dept. Elect. Eng.,California Inst. Technol., Pasadena, CA, USA,
x ij + x ji ≤2, ∀i∈V(G)\(S∪T) 1999.
j∈N+ j∈N− [16] A. Itai, Y. Perl, and Y. Shiloach, “The complexity of finding maxi-
i i mum disjoint paths with length constraints,” Networks, vol. 12, no. 3,
x
e
∈{0,1}, ∀ e∈E(G).
pp.277–286,Sep.1982.
[17] F. R. Kschischang, B. J. Frey, and H.-A. Loeliger, “Factor graphs and
the sum-product algorithm,” IEEE Trans. Inf. Theory, vol. 47, no. 2,
VI. CONCLUSION
pp.498–519,Feb.2001.
In this paper, we formulated the Min-Sum BP algorithm [18] M.Mézard,“Passingmessagesbetweendisciplines,” Science, vol.301,
for the vertex-disjoint shortest k-path problem (k-VDSP) and no.5640,pp.1685–1686,Sep.2003.
[19] M. Mézard, G. Parisi, and R. Zecchina, “Analytic and algorithmic
analyzedthecorrectnessandconvergenceofthealgorithmpre- solutionofrandomsatisfiabilityproblems,”Science,vol.297,no.5582,
sented. We established thatthe Min-SumBP algorithmsolves pp.812–815,Aug.2002.
k-VDSP exactly in O(n2w max) iterations, provided that the [20] M.Mézard and R.Zecchina, “Random K-satisfiability problem: From
ananalyticsolutiontoanefficientalgorithm,” Phys.Rev.E,Stat.Phys.
optimalsolutionisuniqueandtheweightparameterisnonneg- Plasmas Fluids Relat. Interdiscip. Top., vol. 66, no. 5, pp.249–264,
ative integral. Althoughthe runningtime of our algorithmfor Nov.2002.
k-VDSPisnotbetterthanthatofotherexistingalgorithmsfor [21] J. Pearl, Probabilistic Reasoning in Intelligent Systems: Networks of
PlausibleReasoning.SanMateo, CA,USA:MorganKaufmann, 1988.
k-VDSP, the advantage of message-passing algorithms based
[22] T.J.RichardsonandR.L.Urbanke,“Thecapacityoflow-densityparity-
on BP is that it is widely applicable and easy to implement checkcodesundermessage-passingdecoding,”IEEETrans.Inf.Theory,
for a broad class of constrained optimization problems. Due vol.47,no.2,pp.599–618,Feb.2001.
[23] S.Sanghavi,D.Malioutov,andA.Willsky,“BeliefpropagationandLP
to its distributed nature, the BP algorithm and its variants
relaxation for weighted matching in general graphs,” IEEE Trans. Inf.
can also run fast on a large data network in synchronous Theory,vol.57,no.4,pp.2203–2212,Apr.2011.
circumstances. [24] S.Sanghavi,D.Shah,andA.S.Willsky,“Messagepassingformaximum
weight independent set,” IEEE Trans. Inf. Theory, vol. 55, no. 11,
pp.4822–4834,Nov.2009.
ACKNOWLEDGMENT
[25] J.W.Suurballe, “Disjointpaths inanetwork,”Networks, vol.4,no.2,
The authors would like to thank the anonymous pp.125–145,Jan.1974.
[26] J.S.Yedidia,W.T.Freeman,andY.Weiss,“Understandingbeliefprop-
referees for their invaluable suggestions and
agationanditsgeneralizations,”ExploringArtif.Intell.NewMillennium,
comments. vol.8,pp.236–239,Jan.2003.

DAIetal.: ITERATIVEMESSAGEPASSINGALGORITHMFORVERTEX-DISJOINTSHORTESTPATHS 9
GuoweiDaireceivedthePh.D.degreeinoperationalresearchandcybernetics Xiaoyan Zhang receivedthefirstPh.D.degreeinappliedmathematics from
fromCentralChinaNormalUniversity,Wuhan,China,in2020.Heiscurrently NankaiUniversity in2006andthesecondPh.D.degreeincomputerscience
aPost-DoctoralResearcherinstatisticsattheSchoolofMathematicalScience from the University of Twente in 2014. He is currently a Full Professor
andtheInstituteofMathematics,NanjingNormalUniversity,China.Hismajor with the School of Mathematical Science and the Institute of Mathematics,
researchinterests include optimization andalgorithms, andtheirapplications NanjingNormalUniversity.Hehaspublishedmorethan50academicpapers
to networks, communication, and statistical inference and learning, particu- in reputable journals, such as SIAM Journal on Computing (SICOMP),
larlyformessagepassingalgorithms onnetworks. SIAM Journal on Scientific Computing (SISC), SIAM Journal on Discrete
|                     |                     |              |                 |              |             |            | Mathematics            |           | Journal       | of Graph      | Theory.           |                  |                |
| ------------------- | ------------------- | ------------ | --------------- | ------------ | ----------- | ---------- | ---------------------- | --------- | ------------- | ------------- | ----------------- | ---------------- | -------------- |
|                     |                     |              |                 |              |             |            |                        | (SIDMA),  | and           |               |                   | His              | major research |
|                     |                     |              |                 |              |             |            | interests include      | efficient | algorithm     | design        | and computational |                  | complexity     |
|                     |                     |              |                 |              |             |            | analysis, particularly | for       | combinatorial | optimization, |                   | graph algorithms | and            |
| Longkun             | Guo received        | the B.S.     | and Ph.D.       | degrees      | in computer | science    | networks,andVLSI.      |           |               |               |                   |                  |                |
| from the University | of Science          | and          | Technology      | of China     | (USTC),     | China,     |                        |           |               |               |                   |                  |                |
| in 2005 and         | 2011, respectively. |              | From 2015       | to 2016,     | he was      | a Research |                        |           |               |               |                   |                  |                |
| Associate           | at The University   | of Adelaide. | He              | is currently | a Full      | Professor  |                        |           |               |               |                   |                  |                |
| with the School     | of Computer         | Science      | and Technology, |              | Qilu        | University | of                     |           |               |               |                   |                  |                |
Technology,Jinan,China.Hehaspublishedmorethan80academicpapersin
| reputablejournals/conferences, |           | suchasAlgorithmica, |                             | IEEETRANSACTIONS   |            |           |     |     |     |     |     |     |     |
| ------------------------------ | --------- | ------------------- | --------------------------- | ------------------ | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| ONMOBILECOMPUTING              |           | (TMC),              | IEEETRANSACTIONSONCOMPUTERS |                    |            |           |     |     |     |     |     |     |     |
| (TC), IEEETRANSACTIONSON       |           |                     | PARALLELAND                 | DISTRIBUTEDSYSTEMS |            |           |     |     |     |     |     |     |     |
| (TPDS), IEEE                   | ICDCS,    | IJCAI, and          | SPAA.                       | His major          | research   | interests |     |     |     |     |     |     |     |
| include efficient              | algorithm | design              | and computational           |                    | complexity | analysis, |     |     |     |     |     |     |     |
particularlyforoptimizationproblemsinhighperformancecomputingsystems
| andnetworks | andVLSI. |     |     |     |     |     |              |          |     |             |           |          |            |
| ----------- | -------- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ----------- | --------- | -------- | ---------- |
|             |          |     |     |     |     |     | Zan-Bo Zhang | received | the | first Ph.D. | degree in | computer | science in |
Gregory Gutin received the Ph.D. degree in mathematics from Tel Aviv 2008 from Sun Yat-sen University, China, and the second Ph.D. degree in
appliedmathematicsfromtheUniversityofTwente,TheNetherlands,in2017.
University(supervisedbyNogaAlon)in1993.SinceSeptember2000,hehas
|                                     |     |     |                              |     |     |     | He is currently | a Professor | with | the School | of Statistics | and | Mathematics, |
| ----------------------------------- | --- | --- | ---------------------------- | --- | --- | --- | --------------- | ----------- | ---- | ---------- | ------------- | --- | ------------ |
| beenaFullProfessorofcomputerscience |     |     | attheRoyalHollowayUniversity |     |     |     |                 |             |      |            |               |     |              |
ofLondon.Hehasover260publications,whichwerecitedover11300times. Guangdong University of Finance and Economics. He has published more
Hismajorresearchinterestsincludegraphtheory,algorithmsandcomplexity, than 30 academic papers in reputable journals, such as SIAM Journal on
combinatorial optimization, information security, and theoretical economics. Discrete Mathematics and Journal of Graph Theory. His research interests
|     |     |     |     |     |     |     | include factors, | cycles, | and paths | in graphs | and digraphs, | graph | partition, |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | --------- | --------- | ------------- | ----- | ---------- |
HereceivedtheRoyalSocietyWolfsonResearchMeritAwardin2014.Hehas
|             |                           |     |     |     |     |     | graphconnectivity, | andrelated |     | algorithms. |     |     |     |
| ----------- | ------------------------- | --- | --- | --- | --- | --- | ------------------ | ---------- | --- | ----------- | --- | --- | --- |
| alsoelected | toAcademiaEuropaeain2017. |     |     |     |     |     |                    |            |     |             |     |     |     |