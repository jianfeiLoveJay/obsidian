|     | Belief | Propagation |          | for Min-cost |             | Network  | Flow: | Convergence |     | &   |
| --- | ------ | ----------- | -------- | ------------ | ----------- | -------- | ----- | ----------- | --- | --- |
|     |        |             |          |              | Correctness |          | ∗     |             |     |     |
|     |        | David       | Gamarnik |              | Devavrat    | Shah     |       | Yehua Wei   |     |     |
|     |        |             |          | †            |             |          | ‡     |             | §   |     |
|     |        |             |          | September    |             | 25, 2018 |       |             |     |     |
2102 luJ 11  ]MD.sc[  4v6851.4001:viXra
Abstract
Distributed, iterative algorithms operating with minimal data structure while performing
littlecomputationperiterationarepopularlyknownasmessage-passingintherecentliterature.
BeliefPropagation(BP),aprototypicalmessage-passingalgorithm,hasgainedalotofattention
across disciplines including communications, statistics, signal processing and machine learning
asanattractivescalable,generalpurposeheuristicforawideclassofoptimizationandstatistical
inferenceproblems. Despiteitsempiricalsuccess,thetheoreticalunderstandingofBPisfarfrom
complete.
Withthegoalofadvancingthestate-of-artofourunderstandingofBP,westudythe perfor-
mance of BP in the context of the capacitated minimum-cost network flow problem – a corner
stone in the development of theory of polynomial time algorithms for optimization problems
as well as widely used in practice of operations research. As the main result of this paper, we
prove that BP converges to the optimal solution in the pseudo-polynomial-time, provided that
theoptimalsolutionoftheunderlyingnetworkflowprobleminstanceisuniqueandtheproblem
parameters are integral. We further provide a simple modification of the BP to obtain a fully
polynomial-time randomized approximation scheme (FPRAS) without requiring uniqueness of
the optimal solution. This is the first instance where BP is proved to have fully-polynomial
running time. Our results thus provide a theoretical justification for the viability of BP as an
|     | attractive | method | to solve | an important | class | of optimization | problems. |     |     |     |
| --- | ---------- | ------ | -------- | ------------ | ----- | --------------- | --------- | --- | --- | --- |
1 Introduction
Message-passing has emerged as canonical algorithmic architecture to deal with the scale of the
optimization and inference problems arising in the context of variety of disciplines including com-
munications, networks, machine learning, image processing and computer vision, signal processing
and statistics. The Belief Propagation (BP) is a message-passing heuristic for solving optimiza-
tion and inference problems in the context of graphical model. The graphical model or a Markov
random field provides a succinct representation for capturing the dependency structure between a
∗A conference version of this paper appeared in Proceedings of the 21-st ACM-SIAM Symposium on Discrete
| Algorithms |     | [11] |     |     |     |     |     |     |     |     |
| ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
†Operations
Research Center and Sloan School of Management, MIT, Cambridge, MA, 02139, e-mail:
gamarnik@mit.edu
‡Laboratoryforinformationanddecisionsystems(LIDS)andOperationsResearchCenter,DepartmentofEECS,
| MIT, | Cambridge, | MA, | 02139, e-mail: | devavrat@mit.edu |     |     |     |     |     |     |
| ---- | ---------- | --- | -------------- | ---------------- | --- | --- | --- | --- | --- | --- |
§Operations
|     |     | Research | Center, | MIT, Cambridge, | MA, | 02139, e-mail: | y4wei@MIT.EDU |     |     |     |
| --- | --- | -------- | ------- | --------------- | --- | -------------- | ------------- | --- | --- | --- |
1

collection of random variables. In the recent years, the need for large scale statistical inference and
optimization has made graphical models the representation of choice in a variety of applications.
There are two key problems for a graphical model of interest. The firstproblem is the computation
of marginal distribution of a random variable. This problem is (computationally) equivalent to the
computation of the so-called partition function and can be thought of as a weighted combinatorial
counting problem (e.g., counting the number of independent sets of a graph is a special case of this
problem). The second problem is that of finding the mode of a distribution, i.e., an assignment
with the maximum likelihood (ML). For a constrained optimization (maximization) problem, when
the constraints are modeled through a graphical model and probability is proportional to the cost
of the assignment, an ML assignment is an optimal solution to the optimization problem. Both of
these questions, in general, are computationally hard either in the #P or NP-complete sense.
Belief Propagation (BP) is an “umbrella” message-passing heuristic designed for these two
problems. Its version for the first problem is known as the “sum-product algorithm” and for the
second problem is known as the “max-product’’ or “min-sum algorithm”. Both versions of the
BP algorithm are iterative, easy to implement and distributed in nature. When the underlying
graph is a tree, the BP algorithm essentially performs the dynamic programming recursion [10],
[33], [24], and, as a result, leads to a correct solution both for the optimization and inference
problems. Specifically, BPprovidesanaturalparalleliterative versionofthedynamicprogramming
in which variable nodes pass messages between each other along edges of the graphical model.
Somewhat surprisingly, this seemingly naive BP heuristic has become quite popular in practice
even for graphical models which do not have the tree structure [3], [14], [17], [25]. In our opinion,
there are two primary reasons for the popularity of BP. First, it is generically applicable, easy to
understand and implementation-friendly due to its iterative, simple and message-passing nature.
Second, in many practical scenarios, the performance of BP is surprisingly good [32],[33]. On one
hand, for an optimist, this unexpected success of BP provides a hope for it being a genuinely much
more powerful algorithm than what we know thus far (e.g., better than primal-dual methods).
On the other hand, a skeptic would demand a systematic understanding of the limitations (and
strengths) of BP, in order to caution a practitioner. Thus, irrespective of the perspective of an
algorithmic theorist, rigorous understanding of BP is very important.
Despite the apparent empirical success of the BP algorithm for solving a variety of problems,
theoretical understanding of BP is far from complete. In this paper, primarily our interest lies
in the correctness and convergence properties of the min-sum version of BP when applied to the
minimum-cost network flow problems (or simply min-cost flow) - an important class of linear (or
more generally convex) optimization problems. As a secondary interest, we wish to bring BP to
the attention of researchers in the Operations Research (OR) community and thereby improving
the current state in which BP has remained elusive in OR.
1.1 Contributions
As the main contribution of this paper, we establish that BP converges to the optimal solution of a
min-cost network flow problem in the pseudo-polynomial time, provided that the optimal solution
of the underlying problem is unique and the problem input is integral. At the same time, it is
known [29] that BP fails to converge for general linear programming (LP) problem by means of a
counter-example. Thus our results extend, in an important way, the scope of the problems that
are provably solvable by the BP algorithm. We also point out that identifying the broadest class
of optimization problems solvable using the BP algorithm is an interesting open problem. Indeed,
2

resolution of itwilllead to thepreciseunderstandingof the structureof optimization problemsthat
are solvable by BP.
The contributions of this paper, in detail are as follows. First, we show that an exact version
of BP can be implemented for the min-cost flow problems, by encoding each message in BP as
a piece-wise linear convex function. This is significant because the natural formulation of BP
requires maintaining a vector of real-valued functions which may require an infinite amount of
memory to store and computation to update. Then, we provide a proof to show that BP finds the
optimal solution in pseudo-polynomialtime, providedthat theoptimalsolution is unique. Next, we
present a simple modification of the BP algorithm which gives a fully polynomial-time randomized
approximation scheme (FPRAS) for the same problem, which no longer requires the uniqueness of
theoptimal solution. Thisis thefirstinstancewhereBP isproved tohave fully-polynomial running
time, except for the case when the underlying graph is a tree and BP solves the problem exactly.
The modification of BP is obtained by applying a novel lemma; it is a natural generalization of
the so-called Isolation Lemma found in [21]. Unlike the Isolation Lemma, our lemma can be used
for generic LP. In essence, we show that it is possible to perturb the cost of any LP using little
randomness so that the resulting modified LP has unique solution which is a good approximation
to the original LP, and its gap to the next optimal solution is large enough. Indeed this is a
general method and can be useful in a variety of applications including improving performance of
distributed algorithms; it is no surprise that it is already used in a subsequent work [15].
1.2 Prior work on BP
Despite compelling reasons explained earlier, only recently we have witnessed an explosion of re-
search for theoretical understanding of the performance of the BP algorithm in the context of
various combinatorial optimization problems, both tractable and intractable (NP-hard) versions.
In the earlier work, Weiss and Freeman [32] identified certain local optimality properties of the BP
(max-product) for arbitrary graphs. It implies that when graph has a single-cycle then the fixed
point of max-product corresponds to the correct answer. However they do not provide any guaran-
teeontheconvergence ofmax-product. Bayati, ShahandSharma[5]consideredtheperformanceof
BP for finding the maximum weight matching in a bipartite graph. They established that BP con-
verges in pseudo-polynomial time to the optimal solution when the optimal solution is unique [5].
Bayati et al. [4] as well as Sanghavi et al. [28] generalized this result by establishing correctness
and convergence of the BP algorithm for b-matching problem when the linear programming re-
laxation corresponding to the node constraints has a unique integral optimal solution. Note that
the LP relaxation corresponding to the node constraints is not tight in general, as inclusion of the
odd-cycleelimination constraints [30]isessential. Furthermore,[4]and[28]established thattheBP
does not converge if this LP relaxation does have a non-integral solution. Thus, for a b-matching
problem BP finds an optimal answer when the LP relaxation can find an optimal solution. In the
context of maximum weight independent set problem, a one-sided relation between LP relaxation
and BP is established [29]; if BP converges then it is correct and LP relaxation is tight. In [29], a
counter-example was produced that shows that BP does not converge to the optimal solution of an
LP. This seem to suggest that BP is unlikely to solve all forms of LP.
Beyond LP, the performance of BP for quadratic optimization problems (QP) and more gener-
ally convex optimization problems (CP) are recently studied. The conditions for correctness and
convergence of BP in the context of inference in Gaussian graphical models such as those estab-
lished by Malioutov, Johnson and Willsky [16] lead to sufficient conditions for when BP can solve
3

(a certain class of) QP. More recently, in a sequence of works, Moallemi and Van Roy [18, 19] have
identifiedsufficientconditionsunderwhichBPconverges tocorrectsolutionforconvexoptimization
problems. It is worth identifying the differences between results of this paper and that of Moallemi
and Van Roy [18, 19]. To start with, our work applies to constrained min-cost network flow LP
while that of [18, 19] applies to unconstrained convex optimization problem. While constrained
min-cost network flow LP can be seen as an unconstrained convex optimization problem (e.g. via
Lagrangian relaxation), the resulting convex optimization is not a strictly convex and hence suf-
ficient conditions (the diagonal dominance of Hessian) of [18, 19] is not applicable. Indeed, the
proof methods are different, and results of this paper provide ‘implementation’ of BP unlike results
of [18, 19]. We also take note of a work by Ruozzi and Tatikonda [27] that utilizes BP to find
source-sink paths in the network.
1.3 Prior work on min-cost network flow
The min-cost network flow problem (MCF) has been fundamental in the development of the-
ory of polynomial time algorithms for optimization problems. The first polynomial-time algo-
rithm for MCF was developed by Edmonds and Karp [8] with a running time of O(m(logU)(m+
nlogn)), where m represents the number of edges, n represents the number of nodes and U the
largest capacity of an arc. Subsequently the first strongly polynomial time algorithm was pro-
posed by Tardos [31]. Since MCF has been central to the development of algorithmic theory, a
wide variety of efficient algorithms have been proposed over years with different virtues such as
[26],[22],[23],[9],[6],[12],[13], [1]. Among these, the fastest polynomial time algorithm runs (evalu-
ated in the centralized computation model) in essentially O(n3log(nC)) time [6], [13], [1], where
C is the largest cost of an arc. On the other hand, the fastest strongly polynomial time algorithm
for MCF runs (again, evaluated in the centralized computation model) in O(mlogn(m+nlogn))
[23].
It is worth comparing the running time of the BP algorithm that we have obtained for MCF.
The basic version of BP takes (evaluated under decentralized computation model) O C3mn4logn
computation (C represents the largest cost) in total. The modified FPRAS version of BP algo-
(cid:0) (cid:1)
rithmrequiresO ε−3n8m7logn computationintotalonaverage(w.r.t. decentralizedcomputation
model) for obtaining (1+ε) approximation. It should be noted that the number of iterations re-
(cid:0) (cid:1)
quired by the algorithm scales as nL where L is the maximal cost of a directed path.
It is clear from the comparison that the bounds implied by our results for BP are not com-
petitive with respect to the best known results for MCF. BP’s performance is evaluated for the
decentralized model while the above reported computation time analysis for other algorithms is
for centralized model. Indeed, some of the known algorithms can be implemented in decentralized
model such as that of [6] and [12] (see [2, Chapters 10-12] for further details). The analysis of BP
forMCF, whenspecialized tospecificinstances of MCF like thebipartite matchingproblem, leads
to tighter performance bounds that are competitive with respect to the best known results (see
Theorem 4.14 in Section 4.2). But the important thing is that BP is a general purpose algorithm,
not specialized for the problem at hand like the best known algorithm for MCF. For this reason,
BP is highly desirable from an implementor’s perspective as it does not require specific modifica-
tions for the problem of interest. Finally, it should be noted that the BP algorithm can operate in
asynchronous decentralized environment unlike most known algorithms.
4

1.4 Organization
The rest of the paper is organized as follows. In Section 2, we introduce the BP algorithm as an
iterativeheuristicforagenericoptimizationproblem. Weprovideanintuitiveexplanationbymeans
of an example of how BP is derived as an iterative heuristic for generic problem inspired by parallel
implementation ofdynamicprogrammingontree-like problemstructure. InSection 3,wespecialize
BP for linear programming (LP). We recall a (counter-)example of an LP for which BP cannot find
its optimal solution. In Section 4, we further specialize BP algorithm for the capacitated min-
cost network flow problem (MCF). We state the main result that establishes pseudo-polynomial
time convergence of BP to the optimal solution of MCF, when the optimal solution is unique.
Specifically, Section 4.1 explains how each message function in the BP algorithm can be computed
leading to an efficient implementation of BP. In Section 4.2, we consider a subclass MCFo of
MCF that includes the problems of min-cost path as well as bipartite matching or more generally
b-matching. For this subclass of MCF, it turnsout that BP has very simple message functions and
this subsequently leads to a tighter bound on the runningtime. In Section 5, the proof of the main
result about convergence of BP for MCF is provided. Section 6 presents an extension of our result
for min-cost flow problems with piece-wise linear convex cost functions. In Section 7, we provide
MCFo.
the running time analysis of BP for MCF and From the analysis, we show that BP for
the min-cost flow problem is a pseudo-polynomial-time algorithm when the data input is integral.
In Section 8, we present a randomized approximation scheme for the min-cost flow problem which
uses the standard BP as a subroutine. We prove that for any ε∈ (0,1), the approximation scheme
finds a solution that is within 1 + ε of the optimal solution, while its expected running time is
polynomial in m, n, and 1. In doing so, we introduce a variation of the Isolation Lemma for LP in
ε
Section 8.1. Finally, Section 9 presents conclusions and directions for future work.
| 2 Belief | Propagation | for optimization |     | problem |     |
| -------- | ----------- | ---------------- | --- | ------- | --- |
Here we introducethe min-sumversion of BP as a heuristic for optimization problem in the general
form. We shallutilize thenotations similar tothoseusedin[18],[19]. Intheremainderofthepaper,
by BP we mean it’s min-sum version for solving optimization problem. To this end, consider the
| optimization | problem |          |         |        |     |
| ------------ | ------- | -------- | ------- | ------ | --- |
|              |         | minimize | φ (x )+ | ψ (x ) | (P) |
|              |         |          | i i     | C C    |     |
|              |         |          | i∈V     | C∈C    |     |
|              |         |          | X       | X      |     |
R,
|     |     | subject | to x i ∈ ∀i∈ | V,  |     |
| --- | --- | ------- | ------------ | --- | --- |
whereV isafinitesetofvariablesandC isafinitecollection ofsubsetsofV representingconstraints.
Here φ : R → R¯, ∀i ∈ V and ψ : R|C| → R¯, ∀C ∈ C are extended real-valued functions where R¯
| i   |     | C   |     |     |     |
| --- | --- | --- | --- | --- | --- |
R∪{∞}.
represents extended real-numbers We call each φ a variable function, each ψ a factor
|              |                  |              |          | i C |     |
| ------------ | ---------------- | ------------ | -------- | --- | --- |
| function and | (P) a factorized | optimization | problem. |     |     |
It is not difficult to see that essentially any constrained optimization problem of interest can be
represented asafactorized optimization problem. For example, consider thewell-known maximum-
size independent set problem on a simple undirected graph G = (V,E) which requires selecting
subset V of maximal cardinality so that no two vertices of the chosen subset are neighbor of each
5

other as per E. The factorized form of the maximum weight independent set is given by
|     |     | minimize |     |     | φ (x )+  |         | ψ   | (x ,x ) |     |     |
| --- | --- | -------- | --- | --- | -------- | ------- | --- | ------- | --- | --- |
|     |     |          |     |     | i i      |         | ij  | i j     |     |     |
|     |     |          |     | i∈V |          | (i,j)∈E |     |         |     |     |
|     |     |          |     | X   |          | X       |     |         |     |     |
|     |     | subject  | to  | x   | ∈ R, ∀i∈ | V,      |     |         |     |     |
i
where
|     |     |     |     |     | 0   | if x | = 0 |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
i
|     |     |     | φ    | (x ) = | −1   | if x      | = 1 |     |     |     |
| --- | --- | --- | ---- | ------ | ---- | --------- | --- | --- | --- | --- |
|     |     |     |      | i i    |     |           | j   |     |     |     |
|     |     |     |      |        |  ∞ | otherwise |     |     |     |     |
|     |     |     |      |        |  0 | if x      | +x  | ≤ 1 |     |     |
|     |     |     |      |        |      | i         | j   |     |     |     |
|     |     |     | ψ (x | ,x ) = |      |           |     |     |     |     |
|     |     |     | ij i | j      |      |           |     |     |     |     |
|     |     |     |      |        | (∞   | otherwise |     |     |     |     |
In above, x i = 1 if and only if node i is selected in the independent set. Finally, we introduce
the notion of factor graph of a factorized optimization problem. A factor graph F of (P) is a
P
bipartite graph with one partition containing variable nodes V and the other partition containing
factor nodes C corresponding to the constraints. There is an edge (v,C) ∈ V ×C if and only if
v ∈C. For example, the graph shown in Figure 1, is the factor graph for optimization problem:
5
| minimize |     | φ (x | ) +ψ | (x    | ,x ,x | )+ψ | (x    | ,x ,x )+ψ | (x ,x ) | (P′) |
| -------- | --- | ---- | ---- | ----- | ----- | --- | ----- | --------- | ------- | ---- |
|          |     | i    | i    | 1,2,3 | 1 2   | 3   | 1,4,5 | 1 4 5     | 1,5 1 5 |      |
i=1
|     | (cid:16)X |     | (cid:17) |     |     |     |     |     |     |     |
| --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
∈R,
| subject | to x i | ∀1≤    | i ≤5.   |            |         |      |        |       |     |     |
| ------- | ------ | ------ | ------- | ---------- | ------- | ---- | ------ | ----- | --- | --- |
|         |        |        | {1,2,3} |            | {1,4,5} |      | {1,5}  |       |     |     |
|         |        |        |         | v          | v v     | v    | v      |       |     |     |
|         |        |        |         | 1          | 2 3     | 4    | 5      |       |     |     |
|         |        | Figure | 1:      | An example |         | of a | factor | graph |     |     |
Now we introduce BP. To start with, suppose the factor graph F of P is a tree (note that
P
factor graph in Figure 1 is not a tree because there is a cycle (v ,{1,4,5},v ,{1,5},v )). In this
|     |     |     |     |     |     |     |     | 1   | 5 1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
case, let us consider the dynamic programming algorithm. The dynamic programming algorithm
would suggest computation of thevalue or assignment of a given variable nodei ∈V in the optimal
solution as follows: fix a specific value z ∈ R of variable x corresponding to the variable i ∈ V.
i
Subject to x = z compute the cost of optimal assignment for the rest of the problem, say b (z).
| i   |     |     |     |     |     |     |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Then the optimal assignment of variable node i is in argmin z∈Rb i (z). Now to compute b i (z) for all
z ∈R, the dynamic programming would recurse the same approach on the problem
|     |     | minimize | φ   | (z)+ |           | φ (x | )+    | ψ (x ), |     | (1) |
| --- | --- | -------- | --- | ---- | --------- | ---- | ----- | ------- | --- | --- |
|     |     |          | i   |      |           | j j  |       | C C     |     |     |
|     |     |          |     |      | j∈V\{i} X |      | C∈C X |         |     |     |
|     |     | subject  | to  |      | R,        |      |       |         |     |     |
|     |     |          | x i | = z, | x j ∈     | ∀j.  |       |         |     |     |
6

Now implementation of this recursion of dynamic programing in general is not straightforward
and can be computationally expensive. However, when the factor graph F P is a tree, it is quite
simplebecause theproblem decomposes into sub-problemson disconnected trees. Itis thedynamic
programming implementation for tree factor graph which leads to the derivation of BP. To that
end, given a node i consider any constraint C such that i ∈ C, i.e. (i,C) is an edge in F . Since
P
F P is a tree, F P \(i,C) has two disjoint components, say T 1 and T 2 . Without loss of generality, we
assume i is contained in T and C is contained in T . Due to this division of the problem structure,
|     |     |     | 1   |     |     |     | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
R
b (z) for z ∈ or equivalently solution of optimization problem (1), can be computed recursively
i
| as follows. | For | edge | (i,C), | define | ‘messages’ | m   | i→C  | (z) and | m C→i   | (z) as |     |     |     |
| ----------- | --- | ---- | ------ | ------ | ---------- | --- | ---- | ------- | ------- | ------ | --- | --- | --- |
|             |     |      | m      | (z) =  | minimize   |     |      | φ (x    | )+      | ψ (x   | ),  |     |     |
|             |     |      | i→C    |        |            |     |      | j j     |         | D D    |     |     |     |
|             |     |      |        |        |            | j∈  | V∩T1 |         | D∈ C∩T1 |        |     |     |     |
|             |     |      |        |        |            |     | X    |         | X       |        |     |     |     |
R,
|     |     |     |     |       | subject  | to x | = z, | x ∈  | ∀ j.    |      |     |     |     |
| --- | --- | --- | --- | ----- | -------- | ---- | ---- | ---- | ------- | ---- | --- | --- | --- |
|     |     |     |     |       |          |      | i    | j    |         |      |     |     |     |
|     |     |     | m   | (z) = | minimize |      |      | φ (x | )+      | ψ (x | ),  |     |     |
|     |     |     | C→i |       |          |      |      | j j  |         | D D  |     |     |     |
|     |     |     |     |       |          | j∈   | V∩T2 |      | D∈ C∩T2 |      |     |     |     |
|     |     |     |     |       |          |      | X    |      | X       |      |     |     |     |
∈R,
|     |     |     |     |     | subject | to x |     | ∀ j. |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | ---- | --- | ---- | --- | --- | --- | --- | --- |
j
Note that such two directional ‘messages’ can be defined for any edge in F in a similar manner
P
since it is a tree. Again, invoking the tree structure of F and definition of ‘messages’, the solution
P
| of (1) can | be  | re-written | as  |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
R,
|     |     |     |     | b (z) | = φ (z)+ |     | m   | (z), | ∀ z | ∈   |     |     | (2) |
| --- | --- | --- | --- | ----- | -------- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     |     |     |     | i     | i        |     |     | C→i  |     |     |     |     |     |
|     |     |     |     |       |          | C   | ∈Ci |      |     |     |     |     |     |
X
where C is the set of all factor nodes (or constraints) that contain i, i.e.
i
△
|     |     |     |     |     | C   | = {C | ∈ C | : i∈ C}. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | -------- | --- | --- | --- | --- | --- |
i
That is, if the graph underlying F is a tree, then in order to compute b (z) it is sufficient to have
|     |     |     |     |     | P   |     |     |     |     | i   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
knowledge of the ‘messages’ coming towards node i from the factor nodes to which it is connected
to. For the tree F P , such messages can be recursively defined as follows: for any edge (i,C) in F P ,
| for any | z ∈ R |     |     |       |       |          |     |     |          |     |     |     |     |
| ------- | ----- | --- | --- | ----- | ----- | -------- | --- | --- | -------- | --- | --- | --- | --- |
|         |       |     |     | m i→C | (z) = | φ i (z)+ |     | m   | K→i (z), |     |     |     | (3) |
K∈ X Ci\C
|     |     |     |     | m   | (z) = | min | ψ (y)+ |     | m   | (y ). |     |     | (4) |
| --- | --- | --- | --- | --- | ----- | --- | ------ | --- | --- | ----- | --- | --- | --- |
|     |     |     |     | C→i |       |     | C      |     | j→C | j     |     |     |     |
R |C |
|     |     |     |     |     |     | y y ∈ z |     | j ∈C\i |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | i =     |     | X      |     |     |     |     |     |
For tree structuredF , starting from leaf nodes using (3)-(4) the‘messages’ m (z) andm (z)
|     |     |     | P   |     |     |     |     |     |     |     | i→C |     | C→i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
for all edges (i,C) can be computed. A parallel implementation of this recursive procedure is as
follows. Initially, for t = 0 we set m0 (z) = m0 (z) = 0 for all edges (i,C) of F . For t ≥ 1,
|        |          |     |      |            | C→i |      | i→C |     |     |     |     | P   |     |
| ------ | -------- | --- | ---- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| update | messages | for | each | edge (i,C) | of  | F as |     |     |     |     |     |     |     |
P
|     |     |     |     | mt  | (z) = | φ (z)+ |     | mt−1 | (z), |     |     |     | (5) |
| --- | --- | --- | --- | --- | ----- | ------ | --- | ---- | ---- | --- | --- | --- | --- |
|     |     |     |     | i→C |       | i      |     |      | K→i  |     |     |     |     |
K∈ X Ci\C
|     |     |     |     | mt  |       |     |        |     | mt  |       |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | ------ | --- | --- | ----- | --- | --- | --- |
|     |     |     |     |     | (z) = | min | ψ (y)+ |     |     | (y ). |     |     | (6) |
|     |     |     |     | C→i |       |     | C      |     | j→C | j     |     |     |     |
y ∈ R |C |
|     |     |     |     |     |     | y = z |     | j ∈C\i |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | i     |     | X      |     |     |     |     |     |
7

R
The estimation of b (z) at the end of iteration t for each i∈ V and z ∈ is given by
i
|     |     |     |     |     | bt(z) | = φ | (z)+ | mt  | (z). |     |     |     | (7) |
| --- | --- | --- | --- | --- | ----- | --- | ---- | --- | ---- | --- | --- | --- | --- |
|     |     |     |     |     | i     | i   |      |     | C→i  |     |     |     |     |
|     |     |     |     |     |       |     | C    | ∈Ci |      |     |     |     |     |
X
It is easy to show by induction that if the graph underlying F is a tree, then for t larger than
P
the diameter of the tree, bt(·) equals to the value produced by the dynamic programming problem,
i
| therefore | resulting | in  | the optimal |     | assignment |     | of x i | .   |     |     |     |     |     |
| --------- | --------- | --- | ----------- | --- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- |
The parallelized implementation of the dynamic programming problem described by (5) and
(6) can be applied to any factor graph in general. This is precisely the BP min-sum heuristic. The
algorithm is described in detail next. For the non-tree graphs the convergence and/or correctness
| of such   | a heuristic | is,     | by no | means | guaranteed |     | in general. |     |     |     |     |     |     |
| --------- | ----------- | ------- | ----- | ----- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
| Algorithm | 1           |         |       |       |            |     |             |     |     |     |     |     |     |
|           |             | min-sum | BP    |       |            |     |             |     |     |     |     |     |     |
Given a factorized optimization problem (P), construct factor graph F .
| 1:     |         |            |     |               |     |     |     |     |     |     | P   |     |     |
| ------ | ------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2: Set | N to be | the number |     | of iterations |     | for | BP. |     |     |     |     |     |     |
R.
3: Initialize t = 0, and for each edge (i,C) in F , initialize m0 (z) = 0 = m0 (z) for all z ∈
|     |               |     |     |     |     |     | P   |     | C→i |     | i→C |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| for | t = 1,2,...,N |     | do  |     |     |     |     |     |     |     |     |     |     |
4:
R,
| 5: For | any edge | (i,C) | in  | F and | z   | ∈   | update |     |     |     |     |     |     |
| ------ | -------- | ----- | --- | ----- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
P
|     |     |     |     | mt  | (z) | = φ (z)+ |     | mt−1 | (z), |     |     |     | (8) |
| --- | --- | --- | --- | --- | --- | -------- | --- | ---- | ---- | --- | --- | --- | --- |
|     |     |     |     | i→C |     | i        |     |      | K→i  |     |     |     |     |
|     |     |     |     |     |     |          | K∈  | Ci\C |      |     |     |     |     |
X
|     |     |     |     | mt  |     |             |     |          | mt  |      |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | --- | ---- | --- | --- | --- |
|     |     |     |     |     | (z) | =           | min | ψ C (y)+ |     | (y j | ).  |     | (9) |
|     |     |     |     | C→i |     | y∈R|C|,yi=z |     |          |     | j→C  |     |     |     |
j∈C\i
X
| 6: t        | := t+1     |          |            |        |     |          |             |     |          |       |     |     |     |
| ----------- | ---------- | -------- | ---------- | ------ | --- | -------- | ----------- | --- | -------- | ----- | --- | --- | --- |
| 7: end      | for        |          |            |        |     |          |             |     |          |       |     |     |     |
|             |            |          |            | bN     |     |          |             | mN  |          |       |     |     |     |
| 8: Set      | the belief | function |            | as (z) | =   | φ i (z)+ |             |     | (z), ∀1≤ | i ≤n. |     |     |     |
|             |            |          |            | i      |     |          | C∈Ci        | C→i |          |       |     |     |     |
|             |            |          |            |        |     | xˆN      | argminbN(z) |     |          |       |     |     |     |
| 9: Estimate | the        | optimal  | assignment |        | as  |          | ∈           |     | for each | i ∈V. |     |     |     |
|             |            |          |            |        |     | i        | P           | i   |          |       |     |     |     |
| Return      | xˆN.       |          |            |        |     |          |             |     |          |       |     |     |     |
10:
| 3 BP | for | Linear |     | Programming |     |     |     |     |     |     |     |     |     |
| ---- | --- | ------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The linear programming (LP) problem in the standard form is given by
cTx
|     |       |     |     |     | minimize |     |         |      |       |     |     |     | (LP) |
| --- | ----- | --- | --- | --- | -------- | --- | ------- | ---- | ----- | --- | --- | --- | ---- |
|     |       |     |     |     | subject  |     | to Ax = | g,   |       |     |     |     |      |
|     |       |     |     |     |          |     | x ≥     | 0, x | ∈ Rn, |     |     |     |      |
|     | Rm×n, |     | Rm  |     |          | Rn. |         |      |       |     |     |     |      |
where A ∈ g ∈ and c ∈ In the notation of factorized optimization problem
introduced earlier, variable nodes are V = {1,...,n} with associated variables x , i ∈ V; rows of
i
A correspond to constraint nodes C = {C : 1 ≤ j ≤ m} where C = {i ∈ V : a 6= 0}; and
|     |     |     |     |     |     | j   |     |     |     | j   |     | ji  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
8

|     |     |     |     |     |     |     | :R|Cj| | R¯  |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
C = {C : a 6= 0}, ∀ i ∈ V. Define factor function ψ → for 1 ≤ j ≤ m as:
| i   | j ji |     |     |         |      | j    |       |     |     |
| --- | ---- | --- | --- | ------- | ---- | ---- | ----- | --- | --- |
|     |      |     |     |         | 0 if |      | a z = | g   |     |
|     |      |     |     |         |      | i∈Cj | ji i  | j   |     |
|     |      |     |     | ψ (z) = |      |      |       |     |     |
j
|     |     |     |     |     | (∞ oth | erwise. |     |     |     |
| --- | --- | --- | --- | --- | ------ | ------- | --- | --- | --- |
P
|            |          |          | :R  |     | R¯       |     |     |     |     |
| ---------- | -------- | -------- | --- | --- | -------- | --- | --- | --- | --- |
| And define | variable | function | φ   | →   | for i∈ V | as: |     |     |     |
i
|     |     |     |     |     | c z     | if z | ≥ 0 |     |     |
| --- | --- | --- | --- | --- | ------- | ---- | --- | --- | --- |
|     |     |     |     | φ   | (z) = i |      |     |     |     |
i
|     |     |     |     |     | (∞  | otherwise |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
Then, (LP) is equivalent to following the factorized optimization problem:
|     |     |     |     |          | n    | m   |      |     |      |
| --- | --- | --- | --- | -------- | ---- | --- | ---- | --- | ---- |
|     |     |     |     | minimize | φ (x | )+  | ψ (x | ),  | (P ) |
|     |     |     |     |          | i    | i   | Cj   | Cj  | LP   |
|     |     |     |     |          | i=1  | j=1 |      |     |      |
|     |     |     |     |          | X    | X   |      |     |      |
R,
|     |     |     | subject |     | to x i ∈ | ∀i∈ V. |     |     |     |
| --- | --- | --- | ------- | --- | -------- | ------ | --- | --- | --- |
Then BP for this factorized optimization problem becomes the BP heuristic for LP. BP described
earlier requires computing message functions of the form mt and mt . In general, it is not
|     |     |     |     |     |     |     | i→C | C→i |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
clear if such message functions can be stored and updated efficiently. For LP, however it can be
shown that every message function is a piece-wise linear convex function, which allows efficient
encoding of them in terms of a finite vector describing the break points and the slopes of its linear
pieces. In Section 4.1, we will do this in the context of min-cost network flow problem and we will
| explain | the associated | computation |     | procedure | in  | detail. |     |     |     |
| ------- | -------------- | ----------- | --- | --------- | --- | ------- | --- | --- | --- |
Now BP being a distributed algorithm, it is unlikely to work well when the (LP) does not
have a unique optimal solution. Yet, even with the assumption that (LP) has a unique optimal
solution, in general the estimation of BP may not converge to the unique optimal solution. One
such instance is an LP-relaxation of the maximum-weight independent set problem on a complete
| bipartite | graph [29]: |     |          |       |        |      |     |          |      |
| --------- | ----------- | --- | -------- | ----- | ------ | ---- | --- | -------- | ---- |
|           |             |     |          |       | 3      | 3    |     |          |      |
|           |             |     | minimize | −     | 2x −   | 3y   |     |          |      |
|           |             |     |          |       | i      |      | i   |          |      |
|           |             |     |          |       | i=1    | j=1  |     |          |      |
|           |             |     |          |       | X      | X    |     |          |      |
|           |             |     | subject  | to x  | +y +z  | = 1, | ∀1≤ | i,j ≤ 3, | (P ) |
|           |             |     |          |       | i j ij |      |     |          | I    |
|           |             |     |          | x,y,z | ≥ 0.   |      |     |          |      |
Although BP in [29] was stated in a somewhat different manner, it can be checked that it is
equivalent to the description presented here. It turns out that although this problem has a unique
optimal solution, the BP algorithm does not converge at all, let alone to the optimal solution.
Specifically,themessagesxˆN oscillatebetweentwodifferentvaluesvaluesasthenumberofiterations
| N oscillates | between   | odd | and even | values.  |         |     |      |         |     |
| ------------ | --------- | --- | -------- | -------- | ------- | --- | ---- | ------- | --- |
| 4 BP         | Algorithm |     | for      | Min-Cost | Network |     | Flow | Problem |     |
In this section, we formulate BP for the capacitated min-cost network flow problem (MCF), and
state our main result about the convergence of BP for MCF. As mentioned earlier, each message
9

of BP for MCF is a function, and we describe how these messages can be efficiently updated and
storedas vectors inSection 4.1. InSection 4.2, weconsiderasubclassof MCF, itincludesbipartite
matching, for which BP can take advantage of its special structure to obtain much faster running
time.
Let us define the capacitated min-cost network flow problem (MCF). Given a directed graph
G = (V,E), let V, E denote the set of vertices and arcs or directed edges respectively with |V|= n
and |E| = m. For any vertex v ∈ V, let E be the set of arcs incident to v, and for any e∈ E , let
|     |     |     | v   |     |     |     | v   |
| --- | --- | --- | --- | --- | --- | --- | --- |
∆(v,e) = 1 if e is an out-arc of v (i.e. arc e = (v,w), for some w ∈ V), and ∆(v,e) = −1 if e is an
in-arc of v (i.e. arc e= (w,v), for some w ∈V). The MCF on G is formulated as follows [2, 7]:
|     | minimize | c e x | e   |     |     |     | (MCF) |
| --- | -------- | ----- | --- | --- | --- | --- | ----- |
e∈E
X
|     | subject | to ∆(v,e)x | = f , | ∀ v ∈ V (demand/supply |     | constraints) |     |
| --- | ------- | ---------- | ----- | ---------------------- | --- | ------------ | --- |
e v
e ∈Ev
X
|     |     | 0 ≤ x e | ≤ u e , ∀ e∈ E | (flow constraints) |     |     |     |
| --- | --- | ------- | -------------- | ------------------ | --- | --- | --- |
|     |     | R,      | R¯,            |                    | R   |     |     |
where c e ≥ 0, u e ≥ 0, c e ∈ u e ∈ for each e ∈ E, and f v ∈ for each v ∈ V. The variables
x represent flow value assigned to each arc e ∈ E; the first type of constraints state that the
e
difference of in-flow and out-flow at each node v ∈ V equals the node demand f (could be positive
v
or negative); and the second type of constraints state that flow on each arc e ∈ E is non-negative
and can not belarger than its capacity u e . We shall assumethe instance of network flow is feasible.
Without loss of generality, let each node v ∈ V be such that |E | ≥ 2; or else either E = ∅ in
|     |     |     |     |     | v   |     | v   |
| --- | --- | --- | --- | --- | --- | --- | --- |
which case we ignore such v or |E |= 1 in which case the flow on e∈ E is determined by f . For
|     |     |     | v   |     |     | v   | v   |
| --- | --- | --- | --- | --- | --- | --- | --- |
the MCF, define factor and variable functions ψ, φ as follows: for v ∈ V, e ∈E
|     |     |     | 0 if  | ∆(v,e)z | e = f v | ,   |     |
| --- | --- | --- | ----- | ------- | ------- | --- | --- |
|     |     | ψ   | (z) = | e∈Ev    |         |     |     |
v
|     |     |     | (∞ oth | erwise, |     |     |     |
| --- | --- | --- | ------ | ------- | --- | --- | --- |
P
|     |     |     | c z       | if 0≤ z ≤ u , |     |     |     |
| --- | --- | --- | --------- | ------------- | --- | --- | --- |
|     |     |     | e         | e             |     |     |     |
|     |     |     | φ e (z) = |               |     |     |     |
|     |     |     | (∞        | otherwise.    |     |     |     |
Then, solving MCF is equivalent to solving min { ψ (x )+ φ (x )}. Therefore,
|     |     |     |     | x∈R|E| v∈V | v Ev | e∈E e e |     |
| --- | --- | --- | --- | ---------- | ---- | ------- | --- |
the BP algorithm can be applied for MCF in this standard form. Because of the special structure
|     |     |     |     | P   |     | P   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
of MCF that each variable node is adjacent to exactly two factor nodes, it is indeed possible to
skip the message update step mt and resulting into a simplified Algorithm 2 stated next.
v→e
Intuitively, in Algorithm 2 each arc can be thought of as an agent, who is trying to figure
out its own flow while meeting the conservation constraints at its endpoints. Each link maintains
an estimate of its “local cost” as a function of its flow (thus this estimate is a function, not a
single number). At each time step an arc updates its function as follows: the cost of assigning
x units of flow to link e is the cost of pushing x units of flow through e plus the minimum-cost
way of assigning flow to neighboring edges (with respect to the functions computed at the previous
| iteration) | to restore | flow conservation | at the | endpoints of e. |     |     |     |
| ---------- | ---------- | ----------------- | ------ | --------------- | --- | --- | --- |
Similar to BP for LP, the message functions in BP for MCF, mt for suitable pairs of e and
e→v
v, are also piece-wise linear convex functions. In Section 4.1, we establish this fact and present
an explicit procedure for computing mt . Hence, Algorithm 2 is indeed a procedure that can be
e→v
10

Algorithm 2 BP for MCF
1: Initialize t = 0, messages m0 (z) = 0, m0 (z) = 0, ∀z ∈ R for each e = (v,w) ∈ E.
e→v e→w
2: for t = 1,2,3,...,N do
3: For each e = (v,w) ∈ E update messages as follows:
mt (z) = φ (z)+ min ψ (z¯)+ mt−1 (z¯ ) , ∀z ∈ R
e→v e z¯∈R|Ew|,z¯e=z 

w
e˜∈ X Ew\e
e˜→w e˜ 

 
mt (z) = φ (z)+ min ψ (z¯)+ mt−1 (z¯ ) , ∀z ∈R
e→w e z¯∈R|Ev|,z¯e=z 

v
e˜∈ X Ev\e
e˜→v e˜ 

4: t := t+1  
5: end for
6: For each e = (v,w) ∈ E, set the belief function as
bN(z) = φ (z)+ mN−1(z)+ mN−1(z)
e e e˜→v e˜→w
e˜∈
X
Ev\e e˜∈
X
Ew\e
7: Calculate the belief estimate by finding xˆN ∈ argminbN(z) for each e ∈ E.
e e
8: Return xˆN as an estimation of the optimal solution of MCF.
implemented on a computer. Next, we state conditions under which the estimates of BP converge
to the optimal solution of MCF. Before formally stating the result, we first give the definition of a
residual network [2]. Define G(x) to be the residual network of G with respect to flow x as follows:
G(x) has the same vertex set as G, ∀e = (v,w) ∈ E if x < u then e is an arc in G(x) with cost
e e
cx = c . Finally, if x > 0 then there is an arc e′ = (w,v) in G(x) with cost cx = −c . Let
e e e e′ e
δ(x) = min{cx(C) = cx}, (10)
e
C∈C
e∈C
X
where C is the set of directed cycles in G(x). Note that if x∗ is the unique optimal solution of
MCF with directed graph G, then it must be that δ(x∗) > 0 in G(x∗) or else we can change flow
x∗ along the minimal cost cycle in (10) without increasing its cost.
Theorem 4.1. Suppose MCF has a unique optimal solution x∗. Define L to be the maximum cost
of a simple directed path in G(x∗). Then for any N ≥ (⌊ L ⌋+1)n, xˆN =x∗.
2δ(x∗)
The proof of Theorem 4.1 is presented in Section 5. The above stated theorem claims that
the BP algorithm finds the unique optimal solution of MCF in at most (⌊ L ⌋+1)n iterations:
2δ(x∗)
this convergence is exact in the sense that BP finds the optimal solution exactly in finite number
of iterations. This is in contrast with the asymptotic convergence established for many iterative
algorithms in the theory of continuous optimization. We note that this result is similar in flavor
to those established in the context of BP’s convergence for combinatorial optimization [5, 4, 29].
However, it differs from the convergence results in [18, 19] where the estimates converge to the
optimal solution with an exponential rate, but are not established to reach exact optimal in finitely
11

many steps. Next we state the total computation performed by Algorithm 2 to find the optimal
solution when the parameters (capacities and costs) are integral in the MCF.
Theorem 4.2. Given an MCF with a unique optimal solution x∗ and integral data, BP algorithm
finds the unique optimal solution of MCF in O c3 mn4logn operations, where cmax = max c .
|     |     |     |     |     |     |     | max |     |     |     | e e |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Theorem 4.2 follows by utilizing Theorem 4(cid:0).1 to bound th(cid:1)e number of iterations along with
a bound on the number of operations required for updating message functions mt up to those
e→v
many iterations. The formal proof of this statement is presented in Section 7.
| 4.1 | Computing/encoding |     |     | message |     | functions |     |     |     |     |     |
| --- | ------------------ | --- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- |
mt
Here we provide a procedure for constructing message function in BP for MCF. This con-
e→v
struction procedure shows that each message function mt is a piece-wise linear convex function.
e→v
Moreover, we provide a bound for the number of operations required for this construction pro-
cedure, which will help in bounding the running time of Algorithm 2. First, we formally define
| piece-wise | linear | convex | function: |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Definition 4.3. A function f is called piece-wise linear convex if for some finite set of reals,
| a < a | < ... | < a , (allowing |        | a = −∞ | and   | a = | ∞),  |              |        |     |     |
| ----- | ----- | --------------- | ------ | ------ | ----- | --- | ---- | ------------ | ------ | --- | --- |
| 0     | 1     | n               |        | 0      |       | n   |      |              |        |     |     |
|       |       |                 |        | c (z−a | )+f(a | )   | if z | ∈ [a ,a ]    |        |     |     |
|       |       |                 |        | 1      | 1     | 1   |      | 0 1          |        |     |     |
|       |       |                 | f(z) = | c (z−a | )+f(a | )   | if z | ∈ (a ,a ], 1 | ≤ i ≤n |     |     |
|       |       |                 |        |  i+1  | i     | i   |      | i i+1        |        |     |     |

|     |     |     |     | ∞   |     |     | otherwise |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --------- | --- | --- | --- | --- |
|     |     | R   |     |  < |     |     |           |     |     |     |     |
where f(a 1 )∈ and c 1 < c 2 ... < c n satisfy c i+1 (a i+1 −a i )+f(a i ) = f(a i+1 ) for 1 ≤ i≤ n−1.
We definea ,a ,...,a as thevertices of f. Wedefinen tobethenumberof pieces of f,denoted
|     |     | 0 1 | n   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by p(f). We call c i (z −a i−1 )+f(a i−1 ) for z ∈ [a i−1 ,a i ] as the ith linear piece of f. Clearly, if f
is a piece-wise linear convex function, then all relevant information about f can be stored using
a finite vector of size O(p(f)). We make the following observation that will be useful for efficient
| update | of messages | of  | BP. |     |     |     |     |     |     |     |     |
| ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Observation 4.4. Suppose f , f are piece-wise linear convexfunctions. Then, f (ax+b), cf (x)+
|     |     |     |     | 1 2 |     |     |     |     |     | 1   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
df (x) are also convex piecewise-linear functions, for any real numbers a, b, c and d, where c ≥
2
0,d ≥ 0.
Definition 4.5. Let S = {f ,f ,...,f } be a set of piece-wise linear convex functions, and let
|     |     |     |     | 1 2 | k   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| :Rk | R   |     |     |     |     |     |     |     |     |     |     |
| Ψ   | →   | be  |     |     |     |     |     |     |     |     |     |
t
k
|     |     |     |     |     |         | 0   | if         | x = t |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | ---------- | ----- | --- | --- | --- |
|     |     |     |     |     |         |     | i=1        | i     |     |     |     |
|     |     |     |     | Ψ   | t (x) = |     |            |       |     |     |     |
|     |     |     |     |     |         | (∞  | oth erwise |       |     |     |     |
P
Then the interpolation of f ,...,f or S, denoted by I (·) is defined as
|     |     |     |     | 1 k |     |     | S   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k
|     |     |     |     | I (t) = min | ψ   | (x)+ | f (x | ) , ∀ t ∈R. |     |     |     |
| --- | --- | --- | --- | ----------- | --- | ---- | ---- | ----------- | --- | --- | --- |
|     |     |     |     | S           |     | t    | i    | i           |     |     |     |
x∈Rk
i=1
|     |     |     |     |     | n   |     | X   | o   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
12

Lemma 4.6. Suppose f , f are piece-wise linear convex functions. Then for S = {f ,f } the
|     |     |     | 1   | 2   |     |     |     |     |     |     | 1 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
I S (t) is a piece-wise linear convex function and it can be computed in O(p(f 1 )+p(f 2 )) operations.
Proof. We shall provide a constructive proof of this result by describing a procedure to construct
I (t). Theidea behindconstruction of I (t) isessentially to “stitch” together thelinear pieces of f
| S   |     |     |     |     | S   |     |     |     |     |     |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | z∗, | z∗  |     |     |     | z∗  |     | z∗  |     |     |
and f 2 . To this end, let be vertices of f 1 , f 2 such that = argminf 1 (z), = argminf 2 (z).
|     |     |     | 1   | 2   |     |     |     | 1   |     | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Let S = {f ,f }. In case the case of ties, we select z∗ to be the smallest point in the argmin set.
|     |     | 1 2 |     |     |     |     | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Let g(t) be the function that is defined only at z∗ + z∗ with g(z∗ + z∗) = f (z∗)+ f (z∗). Let
|     |     |     |     |     |     |     | 1   | 2   | 1   | 2 1 1 | 2 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
|     |     | z∗  |     | z∗. |     |     |     |     |     | R     |     |     |
L 1 = U 1 = and L 2 = U 2 = We shall construct g iteratively for all t ∈ so that we shall end
|     |     | 1   |     | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
up with g(t) = I (t). The construction is described as follows. At every iteration, let X (and X )
|     |     | S   |     |     |     |     |     |     |     |     | 1   | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
be the linear piece of f (and f ) at the left side of L (and L ). Choose the linear piece with the
|     |     |     | 1   | 2   |     |     | 1   |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
larger slope from {X ,X }, and “stitch” this piece onto the left side of the left endpoints of g. If
|     |     |     | 1 2 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
piece, say P i , of function f i is chosen then update L i to the vertex which is on the left end of P i
for i= 1,2. As an example, consider f and f shown in the Figure 2. Here z∗ = 1 and z∗ = 0 are
|     |     |     |     |     | 1   | 2   |     |     |     | 1   | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vertices of f and f such that z∗ = argminf (z), z∗ = argminf (z). Note that the linear piece
|     |     | 1   | 2   | 1   |     | 1   | 2   |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X 1 in the procedure is labeled as P1 on the graph, while X 2 does not exist (since there is no linear
piece for f on the right side of z ). Hence, we “stitch” P1 to the left side of g, and update L
|     | 2   |     |     |     | 2   |     |     |     |     |     |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to 0. In a similar manner, let Y (Y ) be the linear piece of f (f ) to the right side of U (U ).
|     |     |     |     | 1   | 2   |     |     |     | 1 2 |     | 1   | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Then choose the linear piece with the smaller slope and “stitch” this piece onto the right side of
the right endpoint of g. If Q i is the chosen piece, update U i to the vertex which is on the right
side of Q for i = 1,2. Again, we use f and f in Figure 2 as an illustration. The linear piece Y
|     | i   |     |     |     | 1   | 2   |     |     |     |     |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in the procedure is labeled as P2, while Y is labeled as P3. As P2 has a lower slope than P3, we
2
| “stitch” | P2  | to the right | side | of g and | update | U 1 | to 2. |     |     |     |     |     |
| -------- | --- | ------------ | ---- | -------- | ------ | --- | ----- | --- | --- | --- | --- | --- |
Repeat this procedure until both L (and L ) and U (and U ) are the left most (and right
|     |     |     |     |     | 1   |     | 2   | 1   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
most) endpoints of f (and f ), or both endpoints of g are infinity. See Figure 2 and Figure 3 as
|                 |     |              | 1   | 2             |     |         |            |     |     |     |     |     |
| --------------- | --- | ------------ | --- | ------------- | --- | ------- | ---------- | --- | --- | --- | --- | --- |
| an illustration |     | of resulting |     | interpolation | of  | the two | functions. |     |     |     |     |     |
Note that the total number of iterations is bounded by O(p(f ) + p(f )) and each iteration
|     |     |     |     |     |     |     |     |     | 1   | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
takes at most constant number of operations. Thus total computation performed to obtain g
is O(p(f ) + p(f )). By construction, it is clear that g is a piece-wise linear convex function.
1 2
|     | g(z∗ | z∗) | (z∗)+ | (z∗) |     |     |     |     |     |     |     |     |
| --- | ---- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Also + = f 1 f 2 and by the way we have constructed g, we must have g(t) ≤
|     | 1   | 2   | 1   | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{Ψ (x)+f (x )+f (x )} for any t ∈ R. Therefore, it follows that g = I . This completes the
| t     |          | 1 1  | 2 2 |     |     |     |     |     |     | S   |     |     |
| ----- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| proof | of Lemma | 4.6. |     |     |     |     |     |     |     |     |     |     |
Theorem 4.7. Given a set S{f ,...,f } of piece-wise linear convex functions, I (t) is also a
|     |     |     |     | 1   | k   |     |     |     |     |     | S   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
piece-wise linear convex function. Let P = p(f). Then I (t) can be computed in O(P logk)
|     |     |     |     |     |     | f∈S |     |     | S   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
operations.
P
Proof. Withoutthelossofgeneralitywemayassumethatkisdivisibleby2. LetS = {f ,f },S =
|     |     |     |     |     |     |     |     |     |     | 1   | 1 2 | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{f ,f },...,S = {f ,f } and S′ = {I ,I ,...,I }. Then one can observe that I = I by
| 3   | 4   | k   | k−1 | k   | S1  | S2  | Sk  |     |     |     | S′  | S   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 2   |     |     |     |     | 2   |     |     |     |     |     |
the definition of I . By Lemma 4.6 each function in S′ is piece-wise linear convex and S′ can be
S
computed in O(P) operations. Consider changing S to S′ as a procedure of decreasing the number
of piece-wise linear convex functions. This procedurereduces the number by a factor of 2 each time
whileitconsumesO(P)operations. Hence, ittakes O(logk)procedurestoreducesetS intoasingle
piece-wise linear convex function. And hence computing I (t) takes O(P logk) operations.
S
13

Figure 2: Functions f and f
1 2
Definition 4.8. Let S = {f ,f ,...,f } be a set of convex piecewise-linear functions, a ∈ Rk, and
1 2 k
let Ψ : Rk → R be:
t
k
0 if a x = t
Ψ (x) = i=1 i i , ∀v ∈ V
t
∞ otherwise
(cid:26) P
We call I S a(t) = min x∈Rk {ψ t (x)+ k i=1 f i (x i )} the scaled interpolation of S.
Theorem 4.9. Given a set of piePce-wise linear convex functions S = {f ,...,f }, Ia(t) is also a
1 k S
piece-wise linear convex function. Let P = p(f). Then I (t) can be computed in O(P logk)
f∈S S
operations.
P
Proof. Let S = {f ,...,f } and S′ = {f′,...,f′} with f′(x) = f (a x) for 1 ≤ i ≤ k. If f is
1 k 1 k i i i i
a piece-wise linear convex function, then it can be easily checked that so is f′ for 1 ≤ i ≤ k.
i
Therefore, Theorem 4.9 follows immediately by an application of Theorem 4.7 to S′.
Nowrecallthatforanyt ≥ 1,themessageupdateintheBPforMCF problemhasthefollowing
form:
mt (z) = φ (z)+ min ψ (z¯)+ mt−1 (z¯ ) for z ∈ R.
e→v e z¯∈R|Ew|,z¯e=z 

w
e˜∈ X Ew\e
e˜→w e˜ 

Therefore, the message update can be performed using the scaled interpolation. Specifically, we
make the following observation.
Observation 4.10. Let S = {mt−1 , e˜∈ E \e} and a = ∆(w,e˜) for any e˜∈ E \e. Then the
e˜→w w e˜ w
function m˜t (z) = mt (z)−φ (z) is equal to Ia(−∆(w,e)z +f ).
e→v e→v e S w
From above Observation 4.10, the following Corollaries are immediate.
Corollary 4.11. For t ≥ 1 and e ∈ E with e = (v,w), the message functions mt ,mt of BP
e→v e→w
algorithm for MCF are piece-wise linear convex functions.
14

Figure 3: Interpolation of f and f
1 2
Proof. The proof follows by induction on t. Initially, t = 0 and m0 is constant function (equal
e→v
to 0). Therefore, it is a piece-wise linear convex function by definition. For t ≥ 1, by Corollary 4.9
and Observation4.10, mt (z)−φ (z) is a piece-wise linear convex. Now φ is a piece-wise linear
e→v e e
convex function. Therefore, mt is a summation of two piece-wise linear convex functions which
e→v
is piece-wise linear convex as well.
Corollary 4.12. Suppose the components of cost vector c in MCF are integers. At iteration t, for
piece-wise linear convex message function mt (z) of BP algorithm for MCF , let {s ,s ,...,s }
e→v 1 2 k
be the slopes of its pieces. Then −tc ≤ s ≤ tc and s is integral for each 1 ≤ i ≤ k, where
max i max i
c = max c .
max e e
Proof. The proof follows by induction on t. Initially, t = 0 and the statement is immediate. For
t ≥ 1, since ∆(w,e) = ±1 for any e ∈ E , by Observation 4.10 it follows that the absolute values
w
of the slopes for the linear pieces of mt −φ is the same as the absolute values of the slopes for
e→v e
the linear pieces of message functions mt−1 . By induction hypothesis, the absolute values of the
e˜→w
slopes of mt −φ are integral and bounded by (t−1)c . The slope of pieces in φ is c and
e→v e max e e
therefore, the absolute values of slopes of mt are integral and bounded by tc .
e→v max
Corollary 4.13. Suppose components of vectors f and u take integer values in MCF. Then at
iteration t ≥ 1, for any message function mt , the vertices of mt are integral as well.
e→v e→v
Proof. Again, the proof is by induction on t. Initially, t = 0 and the statement trivially holds. For
t ≥ 1, firstobserve that since u has integral components, all of its vertices of φ are integral as well.
e
By Observation 4.10 and induction hypothesis, all vertices of mt −φ are integral. Therefore,
e→v e
all vertices of mt are integral.
e→v
Corollaries 4.9 and 4.11 shows that at every iteration, each message function can be encoded
in terms of a finite vector describing the corners and slopes of its linear pieces in finite number of
15

iterations. These arguments extend easily to the form of linear program considered earlier. That
| is, BP for | LP can | be truly | implemented |     | on a | computer. |     |     |     |     |
| ---------- | ------ | -------- | ----------- | --- | ---- | --------- | --- | --- | --- | --- |
The Corollary 4.12 provides a bound for the number of linear pieces in mt . This bound
e→v
will help us bound the running time of BP algorithm for MCF . We shall discuss this in detail in
functionsmt
Section 7. Finally, wewould like tonote that theresultthatmessage are piece-wise
e→v
linear convex functions can be also shown by sensitivity analysis of LP, cf. [7, Chapter 5].
| 4.2 BP | for a | sub-class | of  | MCF |     |     |     |     |     |     |
| ------ | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
The Section 4.1 established that each message function is a piece-wise linear convex function.
However, as per the bounds established, the number of pieces increase linearly with iterations and
thisrequiresmorecomputationformessageupdateasiterationsgrow. NowforaninstanceofMCF
withintegral componentsofvector bandu, themessagefunctionmt is apiece-wise linearconvex
e→v
function with integral vertices as per Corollary 4.13. Therefore, it has at most u linear pieces.
e
Thus, if u is bounded by some constant for all e, the message functions at every iteration is piece-
e
wise linear convex function with a bounded number of pieces. This results in a computationally
efficient update of messages. Next, we present a sub-class of MCF, denoted by MCFo, for which
such property holds and which contains important classes of network flow problems.
To this end, given a directed graph G = (V,E), consider the following sub-class of problem:
| with notation | in(v) | = {(u,v) | ∈ E} |     |     |     |     |     |     |     |
| ------------- | ----- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
(MCFo)
|     | minimize |     | c e x e |     |     |     |     |     |     |     |
| --- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
e∈E
X
subject to ∆(v,e)x e = f v , ∀v ∈ V (demand/supply constraints)
e ∈Ev
X
|     |     |     | x ≤ u˜ | ,   |     | ∀v ∈ V |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | ------ | --- | --- | --- | --- |
|     |     |     | e      | v   |     |        |     |     |     |     |
e∈in(v)
X
|     |     | 0 ≤ | x ≤ u . |     |     | ∀e∈ E | (flow | constraints) |     |     |
| --- | --- | --- | ------- | --- | --- | ----- | ----- | ------------ | --- | --- |
|     |     |     | e e     |     |     |       |       |              |     |     |
In above, c, u, and u˜ are all integral. To see MCFo is indeed an instance of MCF consider the
following. Split each v ∈ V into two vertices v and v , where v is incident to all in-arcs of v
|     |     |     |     |     |     | in out |     | in  |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
with f vin = 0 and v out is incident to all out-arcs of v with f vout = f v . Create an arc from v in to
v with capacity u˜ and cost equal to 0. Denote thus created new graph as Go. Then the MCF
| out |     | v   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
on Go is equivalent to MCFo. Instead of using the Algorithm 2 to solve the MCF on Go, we shall
| use it on | G with | the following | functions |         | ψ, φ: |         |         |     |      |      |
| --------- | ------ | ------------- | --------- | ------- | ----- | ------- | ------- | --- | ---- | ---- |
|           |        | 0             | if        | ∆(v,e)x |       | = f and |         | x   | ≤ u˜ |      |
|           | ψ (x)  | =             | e∈Ev      |         |       | e v     | e∈in(v) | e   | v ∀v | ∈ V, |
v
|     |       | (∞  | oth erwise |       |     |        |     |     |     |     |
| --- | ----- | --- | ---------- | ----- | --- | ------ | --- | --- | --- | --- |
|     |       |     | P          |       |     |        | P   |     |     |     |
|     |       | c   | x if 0≤    | x ≤ u |     |        |     |     |     |     |
|     |       |     | e          |       | e   |        |     |     |     |     |
|     | φ (x) | =   |            |       |     | ∀e ∈E. |     |     |     |     |
e
(∞ otherwise
mt
Now to update message functions for all e ∈ E w , the inequality e∈in(w) x e ≤ u˜ w implies
e→v
mt−1
that it is sufficient to check u˜ linear pieces from message functions for all but constant
|     |     |     | w   |     |     |     |     |     | Pe˜→w |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
MCFo.
number of e ∈ E w . This leads to efficient implementation of BP for Specifically, we state
| the following | result. |     |     |     |     |     |     |     |     |     |
| ------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
16

MCFo
Theorem 4.14. Suppose the as described above has a unique optimal solution with
|     |     |     |     | max | u˜ ,u    | ,|f | | ≤ K,     | maxc ≤ | K.  |     |     |     |
| --- | --- | --- | --- | --- | -------- | ----- | -------- | ------ | --- | --- | --- | --- |
|     |     |     |     |     | v        | v v   |          | e      |     |     |     |     |
|     |     |     |     | v   |          |       |          | e      |     |     |     |     |
|     |     |     |     |     | (cid:16) |       | (cid:17) |        |     |     |     |     |
Then Algorithm 2 for MCFo finds the unique optimal solution using O(K2mn2logn), which is
O(K2n4logn),
operations in total. As a result, Algorithm 2 is polynomial time when K is a
constant.
The proof of Theorem 4.14 is presented in Section 7.1. It is worth taking note of the fact that
both the shortest-path problem and maximum weight matching in a bipartite graph belong to the
MCFo class of problems with all components of f, u being bounded by 2. For these two classes
of problems we do not need the extra constraint x ≤ u˜ , but we do need this constraint
|     |     |     |     |     |     |     | e∈in(v) | e   | v   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
to make a general statement of the theorem. We see that under the uniqueness assumptions, BP
P
solves these problems in polynomial (as opposed to just pseudo-polynomial) time.
| 5   | Convergence |     | of  | BP  | for MCF |     |     |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
This section is devoted to establishing the convergence of BP to the optimal solution of the MCF
under the assumption of the uniqueness of the optimal solution, namely we shall prove Theorem
TN
4.1. The outline of the proof is as follows. First, we define the notion of a computation tree
e
that is associated with each variable node x of MCF for iteration N. We show that in fact the
e
estimation xˆN under BP is the optimal solution of an appropriately defined MCF problem on TN
|     |     | e   |     |     |     |     |     |     |     |     |     | e   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(Lemma 5.1). Next, we show that the optimal assignment to x under the min-cost flow problem
e
on the computation tree TN is the same as the optimal assignment to x under the original MCF
|     |     |     | e   |     |     |     |     |     | e   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as long as N is large enough (see Section 5.2). This immediately implies that BP finds the correct
optimal solution for MCF for large enough N leading to Theorem 4.1. We note that this strategy
is similar to that of [5]. However, the technical details are quite different.
| 5.1 | Computation |     | Tree | and | BP  |     |     |     |     |     |     |     |
| --- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We start with the definition of computation tree. The N-level computation tree associated with
arc e = (v,w) ∈ E is denoted by TN. It is essentially the breadth first search tree of G (with
e
repetition of nodes allowed) starting from e up to depth N. Formally, computation tree TN is
e
|     |     |     |     | T0  |     | T0  | T0  |     |     |     | T0  | {v′,w′} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- |
defined inductively as follows. = V ,E is a tree with vertex set V =
|     |     |     |     | e   |     | e   | e   |     |     |     | e   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and arc set E T0 = {e′ = (v′,w′)}. The v′,w′ are considered replicas of v,w ∈ V and this
e
|     |     |     |     |     | (cid:0) (cid:0) | (cid:1) | (cid:0) (cid:1)(cid:1) |     |     |     | (cid:0) (cid:1) |     |
| --- | --- | --- | --- | --- | --------------- | ------- | ---------------------- | --- | --- | --- | --------------- | --- |
is represented by a mapping Γ0 : V T0 → V with Γ0(v′) = v and Γ0(w′) = w. The arc e′ is
|     |     |         |            | e   | e     |     |     | e   | e   |     |     |     |
| --- | --- | ------- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (cid:0) | (cid:1) T0 |     | v′,w′ |     |     |     |     |     | w′  | v′) |
considered the “root” of and vertices are considered to be at level 0. Define (resp.
|     |     |     | e   |     | (cid:0) (cid:1) |     |     |       |      |     |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | ----- | ---- | --- | --- | --- |
|     |     | v′  | w′) |     | P(v′)           |     | w′  | P(w′) | v′). |     |     |     |
as parent of (resp. denoted as = (resp. = Inductively, let us suppose
that tree TN = V TN ,E TN is defined with corresponding ΓN : V TN → V such that for
|     |     | e   | e   | e   |     |     |     |     | e   | e   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
u′,u′ ∈ V TN , (u′,u′) ∈ E TN only if (ΓN(u′),ΓN(u′)) ∈ E. Let P : V TN → V TN
1 2 e (cid:0) (cid:0)1 2(cid:1) (cid:0) (cid:1)(cid:1)e e 1 e 2 (cid:0) (cid:1) e e
|     |     |     |     |     | TN. |     | TN  |     | leaves1 | TN. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
represent the parent relation in Let L be the set of of Now we shall
(cid:0) (cid:1) (cid:0) e(cid:1) e e (cid:0) (cid:1) (cid:0) (cid:1)
define TN+1 = V TN+1 ,E TN+1 which contains TN as a sub-tree. Specifically, V TN+1 and
|     | e   |     | e   | e   |     |         |         | e   |     |     | e   |     |
| --- | --- | --- | --- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | (cid:0) | (cid:1) |     |     |     |     |     |
E TN+1 are obtained by adding vertices to V TN and arcs to E TN as follows. For each leaf
|     | e   |     |     |     |     |     | e   |     | e   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nodeu′ TN (cid:0) (cid:0) nodeu˜′ (cid:1) (cid:0) (cid:1)(cid:1) TN arc(u′,u˜′)or (u˜′,u′)to (cid:0) TN (cid:1)
|         | ∈       | L   | , add | to expandV |     |     | andadd          |     |                 |     | expandE | if  |
| ------- | ------- | --- | ----- | ---------- | --- | --- | --------------- | --- | --------------- | --- | ------- | --- |
| (cid:0) | (cid:1) | e   |       |            |     | e   | (cid:0) (cid:1) |     | (cid:0) (cid:1) |     |         | e   |
1A vertex v(cid:0)′ is c(cid:1)alled leaf if it is connected to ex(cid:0)actly(cid:1)one other vertex. (cid:0) (cid:1)
17

|     |     |     |     | Figure 4: | Computation |     | tree of G | rooted at | e = (1,3) |     |     |     |
| --- | --- | --- | --- | --------- | ----------- | --- | --------- | --------- | --------- | --- | --- | --- |
3
|                   |     |     |     |                               |     |     | withΓN(u′)= |     | and(b)ΓN(P(u′)) |     |     |           |
| ----------------- | --- | --- | --- | ----------------------------- | --- | --- | ----------- | --- | --------------- | --- | --- | --------- |
| (a)thereisanodeu˜ |     |     |     | ∈ V sothat(u,u˜)or(u˜,u)isinE |     |     |             |     | u,              |     |     | 6= u˜. In |
|                   |     |     |     |                               |     |     |             | e   |                 | e   |     |           |
thiscase,defineP(u˜′)= u′,themapΓN+1(u˜′) = u˜andlevelofu˜′ asN+1. Indeed,ΓN+1 isidentical
|     |     |     |     |     | e   |     |     |     |     | e   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to ΓN for nodes V TN ⊂ V TN+1 . In what follows, we shall drop reference to e,N in notation
|     | e   |     |     | e   | e   |     |     |      |          |                |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | -------------- | --- | --- |
|     | ΓN  |     |     |     |     |     |     | Γ(e′ | (u′,u′)) | (Γ(u′),Γ(u′)). |     |     |
of when clear from context and abuse notation by denoting = =
|     | e   |     | (cid:0) | (cid:1) (cid:0) | (cid:1) |     |     |     | 1 2 |     | 1   | 2   |
| --- | --- | --- | ------- | --------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Sometimes TN is also called ‘unwrapped tree” of G rooted at e. Figure 4 gives an example of a
e
computation tree. It should be noted that the definition of computation tree may appear slightly
different compared to that in related works such as [4], [5], [28] (arc is root here in contrast to a
vertex as root). However, the utility of the computation trees is very similar.
Now we are ready to relate the computation tree with the BP. Let Vo(TN) ⊂ V(TN) denote
|     |     |     |     |     |     |     |     |     | e   |     | e   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the set of all the vertices which are not on the N-th level of TN. Consider the problem
e
|     |     |     |     | minimize |     | c     | x   |     |     |     | (MCFN) |     |
| --- | --- | --- | --- | -------- | --- | ----- | --- | --- | --- | --- | ------ | --- |
|     |     |     |     |          |     | Γ(e˜) | e˜  |     |     |     |        | e   |
e˜∈E X(T N)
e
|     |     |     |     |         |     | ∆(u′,e˜)x |              | u′    | Vo(TN) |     |     |     |
| --- | --- | --- | --- | ------- | --- | --------- | ------------ | ----- | ------ | --- | --- | --- |
|     |     |     |     | subject | to  |           | e˜ = f Γ(u′) | , ∀ ∈ |        |     |     |     |
e
e˜ ∈E u′
X
∈E(TN).
|     |     |     |     |     | 0≤  | x ≤ u | , ∀ f |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | e˜    | Γ(f)  | e   |     |     |     |     |
In above, E ⊂ E(TN) is the set of arcs incident on u′ ∈ Vo(TN) in TN and ∆(u′,e˜) for e˜∈ E is
|     |     | u′  |     | e   |     |     |     | e   | e   |     |     | u′  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
defined as −1 or +1 depending upon whether e′ is in-arc or out-arc for node u′. Loosely speaking,
| MCFN |     |     |     |     | TN: |     |     |     |     |     | E(TN) |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
is essentially an MCF on there is a flow constraint for every arc e˜ ∈ and a
|     | e   |     |     |     | e   |     |     |     |     |     | e   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
demand/supply constraint for every node, except for the nodes on the Nth level. Now, we state
the following well known result which exhibits the connection between BP and the computation
trees.
18

Lemma 5.1. Let xˆN be the value produced by BP at the end of iteration N for the flow value on
e
edge e ∈E. Then there exists an optimal solution y∗ of MCFN such that y∗ = xˆN where e′ is the
e e′ e
root of TN (and Γ(e′)= e).
e
Proof. Let e′ = (v′,w′) be the root arc of computation tree TN with e = (v,w) such that Γ(e′) =
e
e,Γ(v′) = v and Γ(w′) = w. By definition, TN has two components connected via the root arc e′.
e
Let C be the component containing w′ and TN denote the C with edge e′; indeed TN is a
e′→v′ e′→v′
tree. As before, let Vo(TN ) be the set of all nodes excluding those at the Nth level. Define
e′→v′
minimize c x (MCFN (z))
Γ(e˜) e˜ e′→v′
e˜∈E(XT
e
N
′→v′
)
subject to ∆(q′,e˜)x = f , ∀ q′ ∈ Vo(TN )
e˜ Γ(q′) e′→v′
e˜ X ∈E q′
x = z,
e′
0 ≤ x ≤ u , ∀ e˜∈ E(TN ).
e˜ Γ(e˜) e′→v′
Now, we shall establish that under the BP algorithm (running on G) the value of message function
from e → v evaluated at z, that is mN (z), is the same as the cost of the optimal assignment for
e→v
MCFN (z). This can be established inductively. To start with, for N = 1, the statement can be
e′→v′
checked to be true trivially. For N > 1, let E denote the edges incident on w′ in TN where recall
w′ e
e′ = (v′,w′) is it’s root arc. Then for each g′ ∈E \e′ with g′ = (u′,w′) (or (w′,u′)), let TN−1 be
w′ g′→w′
the subtree of TN that includes g′ and everything in TN that is part of it’s component that
e′→v′ e′→v′
does not include w′. Define optimization problem
minimize c x (MCFN−1 (z))
Γ(e˜) e˜ g′→w′
e˜∈E(XT
g
N
′→
−1
w′
)
subject to ∆(q′,e˜)x = f , ∀ q′ ∈ Vo(TN−1 )
e˜ Γ(q′) g′→w′
e˜ X ∈E q′
x = z,
g′
0 ≤ x ≤ u , ∀ e˜∈ E(TN−1 ).
e˜ Γ(e˜) g′→w′
Byinductionhypothesis,itmustbethatmN−1 (z)equalsthecostofthesolutionofMCFN−1 (z).
g′→w′ g′→w′
Given this hypothesis and the relation of sub-tree TN−1 for all g′ ∈ E \e′ with TN , it follows
g′→w′ w′ e′→v′
that the optimization problem MCFN (z) is equivalent to
e′→v′
minimize c z+ mN−1 (x )
e Γ(g′)→Γ(w′) g′
g′∈
X
E w′\e′
subject to ∆(w′,e′)z+ ∆(w′,g′)x = f
g′ Γ(w′)
g′∈
X
E w′\e′
0 ≤ x ≤ u , ∀ g′ ∈ E \e′.
g′ Γ(g′) w′
This is exactly the same as the relation between mN (z) and message function mN−1(·) for g ∈
e→v g→w
E \e as defined by BP. That is, mN (z) is exactly the same as the cost of optimal assignment of
w e→v
MCFN . We shall use this equivalence, to complete the proof of Lemma 5.1.
e′→v′
19

To that end, for given e = (v,w) with 0 ≤ z ≤ u , the optimization problem MCFN(z) is
e e
equivalent to
minimize c z+ c x + c x
e Γ(e˜) e˜ Γ(e˜) e˜
e˜∈E(XT
e
N
′→v′
) e˜∈E(XT
e
N
′→w′
)
subject to ∆(q′,e˜)x = f , ∀ q′ ∈ Vo(TN)∩ V(TN )∪V(TN )
e˜ Γ(q′) e e′→v′ e′→w′
e˜ X ∈E q′ (cid:16) (cid:17)
0≤ x ≤u , e˜∈ E(TN )∪E(TN ).
e˜ Γ(e˜) e′→v′ e′→w′
That is, the cost of an optimal assignment of MCFN(z) equals mN (z)+mN (z)+c z for any
e e→u e→v e
0 ≤ z ≤ u . Now the claim of Lemma 5.1 follows immediately.
e
5.2 Proof of theorem 4.1
Now we are ready to establish Theorem 4.1. Suppose to the contrary that there exists e =
0
(v ,v )∈ E and N ≥ L +1 n such that xˆN 6=x∗ . By Lemma 5.1, there exists an optimal
α β 2δ(x∗) e0 e0
solution y∗ of MCFN such that y∗ = xˆN. Without loss of generality, assume y∗ > x∗ . Using
e0 (cid:0)(cid:4) (cid:5) e(cid:1)′
0
e0 e′
0
e0
the optimality of x∗, we will show that it is possible to modify y∗ to obtain a feasible solution of
MCFN with cost strictly lower than that of y∗. This will lead to contradiction to the assumption
e0
that xˆN 6= x∗ and establish the result.
e0 e0
To that end, let e′ = (v′ ,v′ ) be the root edge of the computation tree TN as discussed earlier.
0 α β e0
Because y∗ is a feasible solution of MCFN and x∗ is a feasible solution of MCF,
e0
f = ∆(v′ ,e˜)y∗ = y∗ + ∆(v′ ,e˜)y∗ (constraint at v′ in MCFN)
Γ(v
α
′) α e˜ e′
0
α e˜ α e0
e˜∈ X E vα ′ e˜∈E Xvα ′ \e′ 0
f = ∆(Γ(v′ ),e˜)x∗ = x∗ + ∆(Γ(v′ ),e˜)x∗ (constraint at Γ(v′ ) in MCF).
Γ(v α ′) α e˜ e0 α e˜ α
e˜∈E XΓ(vα ′) e˜∈E ΓX(vα ′) \e0
Note that the edges in E in the computation tree TN are copies of edges in E in G where v =
v α ′ e0 vα α
Γ(v′ ). Therefore, ∆(v′ ,e˜) = ∆(Γ(v ),Γ(e˜)) for e˜ ∈ E . Therefore, from above inequalities, it
α α α v α ′
followsthatsincey∗ > x∗ ,thereexistsarce′ 6= e′ incidentonv′ inTN suchthat∆(v′ ,e′)(x∗ −
e′
0
e0 1 0 α e0 α 1 Γ(e′
1
)
y∗ ) is strictly positive. Therefore, if ∆(v′ ,e′) = 1 then x∗ > y∗ else x∗ < y∗ . That is,
e′ α 1 Γ(e′) e′ Γ(e′) e′
1 1 1 1 1
if edge e′ has the opposite orientation with respect to e′ at node v′ (both are outgoing from v′
1 0 α α
and hence opposite orientation), then x∗ > y∗ else x∗ < y∗ . The Figure 5 explains this by
Γ(e′) e′ Γ(e′) e′
1 1 1 1
means of a simple example.
More generally, using similar argument we can find arc e′ 6= e′ incident to v′ satisfying similar
−1 0 β
condition. Let v′ , v′ be the other end points of e′, e′ respectively. A recursive application of
α1 α−1 1 −1
similar argument utilizing the feasibility condition of x∗ and y∗ and the inequalities between value
of components of x∗ and y∗ at edges e′ and e′ , leads to existence of arcs e′, e′ incident on v′ ,
1 −1 2 −2 α1
v′ respectively so that x∗ 6= y∗ and x∗ 6= y∗ with inequalities being < or > depending upon
α−1 e′
2
e′
2
e′
−2
e′
−2
the orientation of the edges with respect to e . Continuing further in this manner all the way down
0
to the leaves, it is possible to find arcs {e′ ,e′ ,...,e′ ,,e′,...,e′ } such that for −N ≤ i ≤ N,
−N −N+1 −1 1 N
y∗ > x∗ ⇐⇒ e′ has the same orientation as e ,
e′ Γ(e′) i 0
i i
y∗ < x∗ ⇐⇒ e′ has the opposite orientation as e .
e′ Γ(e′) i 0
i i
20

Figure 5: An example of Augmenting path between the flow assignment on computation tree T2
e3
and the flow assignment on G. The dashed edges represent the edges belonging to the augmenting
| path. | Root edge and edge | from v 4 | to v 1 have | same | orientation. |     |     |     |     |
| ----- | ------------------ | -------- | ----------- | ---- | ------------ | --- | --- | --- | --- |
Let us denote the path containing these edges as X = {e′ ,e′ ,...,e′ ,e′,e′,...,e′ }. For any
|     |     |     |     |     | −N  | −N+1 | −1 0 | 1 N |     |
| --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- |
e′ = (v′,v′) ∈ X, define Aug(e′) = (v′,v′) if y∗ > x∗ , and Aug(e′) = (v′,v′) if y∗ < x∗ .
|     | p q |     | p   | q e′ | Γ(e′) |     |     | q p e′ | Γ(e′) |
| --- | --- | --- | --- | ---- | ----- | --- | --- | ------ | ----- |
Given the feasibility conditions of y∗ and definition of Aug(e′), it can be checked that Γ(Aug(e′)) is
an arc in theresidualgraph G(x∗). Thedirected path W = (Aug(e′ ),...,Aug(e′),...,Aug(e′ ))
|     |     |     |     |     |     | −N  |     | 0   | N   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | TN  |     |     | y∗  |     | x∗. |     |     |     |
on will be called the augmenting path of with respect to Also, Γ(W) is a directed walk
e0
on G(x∗). Now we can decompose Γ(W) into a simple directed path P and a collection of simple
directed cycles C ,...,C . Now each simple directed cycle or path on G(x∗) can have at most n
1 k
|     |     |     |     | L   |     |     |     | L   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
edges. Since W has 2N +1 arcs and N ≥ +1 n, it follows that k > . Now the cost
|     |     |        |     | 2δ(x∗) |     |       |     | δ(x∗) |     |
| --- | --- | ------ | --- | ------ | --- | ----- | --- | ----- | --- |
|     |     | c∗(P), |     |        |     | G(x∗) |     |       |     |
of path P, denoted by with respect to the residual graph is at least −L (and at most
|     |     |     |     | (cid:0)(cid:4) | (cid:5) (cid:1) |     |     |     |     |
| --- | --- | --- | --- | -------------- | --------------- | --- | --- | --- | --- |
G(x∗),
L) by definition of L. Since each C i is a simple cycle in by definition it’s cost, denoted by
c∗(C ) with respect to G(x∗) is at least δ(x∗); δ(x∗) > 0 since x∗ is the unique optimal solution.
i
Therefore, as explained below we obtain that the cost of W is strictly positive:
N
c∗ c∗(W)
Γ(e′) =
i
i=−N X
k
|     |     |     |     | = c∗(P)+ | c∗(C | )   |     |     |     |
| --- | --- | --- | --- | -------- | ---- | --- | --- | --- | --- |
j
j=1
X
≥ −L+kδ(x∗)
L
δ(x∗)
|     |     |     |     | > −L+ |     | = 0. |     |     |     |
| --- | --- | --- | --- | ----- | --- | ---- | --- | --- | --- |
δ(x∗)
|     |     | y∗ x∗ |     |     | y∗ x∗ |     |     |     |     |
| --- | --- | ----- | --- | --- | ----- | --- | --- | --- | --- |
Let FWD = {e ∈ X : > }, BCK = {e ∈ X : < }. Since both FWD and BCK are
|     |     | e Γ(e) |     |     | e   | Γ(e) |     |     |     |
| --- | --- | ------ | --- | --- | --- | ---- | --- | --- | --- |
finite, there exists λ > 0 such that y∗−λ ≥ x∗ , ∀e∈ FWD and y∗+λ ≤ x∗ , ∀e∈ BCK. Define
|     |     |     | e   | Γ(e) |     | e   | Γ(e) |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- |
21

N
| y˜∈ R|E(T | e )| as |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|     |     |     |     |     | y∗−λ |     | e ∈FWD |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ------ | --- | --- | --- | --- | --- |
e
|     |     |     |     |     | y˜ = y∗+λ |     | e ∈BCK |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     |     | e        | e   |        |     |     |     |     |     |

|     |     |     |     |     | 0  |     | otherwise. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
The y˜ can be thought of as flow that is obtained  by pushing λ units of additional flow along path
W over the existing flow y∗ in TN. Since for each e ∈ FWD, y∗ − λ ≥ x∗ ≥ 0 and for each
|     |     |     |     | e0  |     |     |     |     | e   | Γ(e) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
e ∈BCK, y∗+λ ≤ x∗ ≤ u , y˜satisfies all the flow constraints. Further since all edges in FWD
|     | e   | Γ(e) | Γ(e) |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
have the same orientation as e 0 and those in BCK have the opposite orientation compared to e 0 ,
| we have | that for | any | v′ ∈ Vo(TN), |     |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e0
|     |     |     |     |     | ∆(v′,e′)y˜ |     |     | ∆(v′,e′)y∗ |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | ---------- | --- | --- | --- | --- |
e′ =
e′
|     |     |     |     | e′ ∈E v′ |     |     | e′ ∈E v′ |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | -------- | --- | --- | --- | --- | --- |
|     |     |     |     | X        |     |     | X        |     |     |     |     |     |
|     |     |     |     |          |     | =   | f Γ(e′)  | ,   |     |     |     |     |
which implies that y˜satisfies all the demand/supply constraints. Therefore, y˜is a feasible solution
| of MCFN. | Now |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e0
|     |     |          | y∗         |      |         |             |        |         | y∗         |           |     |     |
| --- | --- | -------- | ---------- | ---- | ------- | ----------- | ------ | ------- | ---------- | --------- | --- | --- |
|     |     |          | c Γ(e′) e′ | −    | c       | Γ(e′) y˜ e′ | =      |         | c Γ(e′) e′ | −y˜ e′    |     |     |
|     |     | e′∈X E(T | N )        | e′∈X | E(T N ) |             | e′∈X   | E(T N ) |            |           |     |     |
|     |     |          | e 0        |      | e 0     |             |        | e 0     | (cid:0)    | (cid:1)   |     |     |
|     |     |          |            |      |         |             | =      | c       | Γ(e′) λ−   | c Γ(e′) λ |     |     |
|     |     |          |            |      |         |             | e′∈FWD | X       | e′∈BCK     | X         |     |     |
= c∗(W)λ
> 0.
|     |     |     |     |     | c∗  |     | e′  |     | c∗  |     | e′  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In above we have used the fact that = c Γ(e′) for ∈ FWD and = −c Γ(e′) for ∈ BCK.
|     |     |     |     |     | Γ(e′) |     |     |     | Γ(e′) |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | ----- | --- | --- | --- |
The above contradicts the optimality of y∗. Therefore, the assumption about BP estimate not
| converging    | is false. | This | completes  | the | proof      | of Theorem |          | 4.1. |          |     |     |     |
| ------------- | --------- | ---- | ---------- | --- | ---------- | ---------- | -------- | ---- | -------- | --- | --- | --- |
| 5.3 Detection |           | of   | uniqueness |     | of optimal |            | solution |      | using BP |     |     |     |
Inthissection,weestablishanunusualpropertyofBPintermsofitsabilitytodetecttheuniqueness
of optimal solution in the MCF in distributed manner as long as the input parameters c, f and u
| are integral. | We  | state | this as the | following | Corollary |     | of  | Theorem | 4.1. |     |     |     |
| ------------- | --- | ----- | ----------- | --------- | --------- | --- | --- | ------- | ---- | --- | --- | --- |
Corollary 5.2. Consider an instance of MCF with integral c, f and u. Suppose c = max c .
|     |     |     |     |     |     |     |     |     |     | max           |     | e∈E e |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- |
|     |     |     |     |     | n2c |     |     |     | z∗  | ∈argminbN(z). |     |       |
Suppose the BP Algorithm 2 runs for N = max +n iterations. Let Then
|             |        |     |          |           |          |           |     |          |         | e e |     |      |
| ----------- | ------ | --- | -------- | --------- | -------- | --------- | --- | -------- | ------- | --- | --- | ---- |
|             |        |     |          | bN(z∗−1), |          | bN(z∗+1)  |     |          | +bN(z∗) |     |     |      |
|             |        | ∀   | e∈ E,    | min       |          |           |     | >        | nc      |     |     | (11) |
|             |        |     |          |           | e e      | e         | e   |          | max     | e e |     |      |
|             |        |     |          | (cid:16)  |          |           |     | (cid:17) |         |     |     |      |
| if and only | if the | MCF | instance | has       | a unique | solution. |     |          |         |     |     |      |
Proof. We first establish the implication that if MCF has a unique optimal solution then (11)
holds. To that end, let us suppose that the instance of MCF of interest has a unique solution.
22

Consider any edge e ∈ E and its computation tree TN. Then from Lemma 5.1 it follows that z∗
|     |     |     |     |     |     |     |     | e   |     |     |     | e   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | e′  | TN  |     |     |     |     |
is an optimal assignment of the root edge of with respect to the associated optimization
e
problem MCFN. Now suppose y is an optimal solution of MCFN with the additional constraint
|     |     | e   |     |     |     |     |     |     |     | e   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that flow on the root edge e′ of TN, denoted by y is fixed to value z∗−1. Then, using arguments
|     |     |     |     |     | e   |     |     | e′  |     | e   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
similar to those used in the proof of Theorem 4.1, it can be shown that there exists an augmenting
|     |     |     |     |     | z∗  |     | 2n2c | TN. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
path W of y with respect to of length max in e0 As before, W can be decomposed into
at least 2nc disjoint simple cycles and a simple path. Now each cycle has a cost of at least
max
MCFN
δ(x∗), which is at least 1 as MCF has integral data. Since the MCF and have integral
e
x∗
parameters, the y and can be restricted to be integral. Therefore, the augmenting path W must
allow for pushing at least unit amount of flow to modify y to result in the decrease of its cost by
at least nc . This is because (a) the increase, due to pushing unit amount of flow on the simple
max
path, could be at most nc max , and (b) decrease along (at least) 2nc cycles is at least 2nc . In
|     |     |     |     |     |     |     |     |     |     | max |     | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
summary, the modified solution is feasible for MCFN on TN with cost decreased by at least nc .
|     |     |     |     |     |     |     |     | e   | e   |     |     | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Therefore, it would follow that the optimal cost bN(z∗) for MCFN is less than bN(z∗−1)−nc .
|     |     |     |     |     |     |     |     | e e    |             | e   | e e | max |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | --- | --- |
|     |     |     |     |     |     |     |     | bN(z∗) | bN(z∗+1)−nc |     |     |     |
In a very similar manner, it can be argued that < . This concludes that
|     |       |              |     |     |             |           |     | e e   | e e | max |     |     |
| --- | ----- | ------------ | --- | --- | ----------- | --------- | --- | ----- | --- | --- | --- | --- |
|     | bN(z∗ | +1),bN(z∗−1) |     |     |             | bN(z∗)+nc |     |       |     |     |     |     |
| min |       |              |     |     | is at least |           |     | max . |     |     |     |     |
|     | e     | e            | e e |     |             | e         | e   |       |     |     |     |     |
To e(cid:0)stablish the other side(cid:1) of the equivalence, suppose MCF does not have a unique optimal
solution. Consider any arc e ∈ E, corresponding computation tree TN and optimization problem
e
| MCFN. |     |     |     |     |     |     |     |     |     |     | MCFN |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
Let e′ be the root arc of TN as before. Let y be the optimal assignment of with
|     | e   |     |     |     | e   |     |     |     |     |     |     | e   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | e′  |     |     | z∗. |     |     |     |     |     |
the assignment for root arc being y e′ = Now since MCF has multiple optimal solution, there
e
exists another optimal assignment x∗ of MCF so thatx∗ 6= z∗. Indeed given thatboth MCFN and
|     |     |     |     |     |     |     |     | e   | e   |     |     | e   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MCF are integral, we can restrict our attention to z∗, x∗ and y having integral components. Since
x∗ z∗,
6= using arguments similar to those used in the proof of Theorem 4.1, it is indeed possible
e e
to find an augmenting path W, of length 2N, on TN with respect to y and x∗. This augmenting
e
path decomposes into one simple path P of length at most n−1 and at least 2nc simple cycles.
max
Since x∗ is an optimal solution, the cost of each of the cycles with respect to the residual graph
| G(x∗) |     |     |     |     |     |     |     |     |     |     |     | x∗  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is non-positive (it is not strictly negative like the proof of Theorem 4.1 since the is not
unique). The cost of the path, however is between −(n−1)c and (n−1)c . Therefore, by
|     |     |     |     |     |     |     |     |     | max |     | max |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pushing unit amount of flow (which is possible along this augmenting path W due to integrality of
| x∗  |     |     |     |     | TN  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and y), the resulting flow y˜ on is such that its total cost is at most (n−1)c more than
|     |     |     |     |     | e   |     |     |     |     |     | max |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the cost of y. Now either y˜ = z∗ −1 or z∗ +1. Suppose y˜ = z∗ −1. In that case, the y˜ is a
|     |     |     |     | e′  | e   |     | e   |     | e′  | e   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
feasible solution of MCFN with additional constraint that the root arc e′ has flow z∗ −1. This
|     |     |     |     | e   |     |     |     |     |     |     | e   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MCFN
cost is no less than the cost of an optimal solution of with additional constraint that the
e
|     |     | e′  | z∗−1, |     |     |     |     | bN(z∗ |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
root arc has flow which is defined as −1). Putting all together, we obtain
|     |           |         | e   |         |          |     |       | e e       |      |     |     |     |
| --- | --------- | ------- | --- | ------- | -------- | --- | ----- | --------- | ---- | --- | --- | --- |
|     |           |         |     |         | bN(z∗−1) |     | ≤     | bN(z∗)+nc | .    |     |     |     |
|     |           |         |     |         | e        | e   |       | e e       | max  |     |     |     |
| In  | a similar | manner, |     | if y˜ = | z∗+1 the | we  | would | conclude  | that |     |     |     |
|     |           |         |     | e′      | e        |     |       |           |      |     |     |     |
|     |           |         |     |         | bN(z∗+1) |     | ≤     | bN(z∗)+nc | .    |     |     |     |
|     |           |         |     |         | e        | e   |       | e e       | max  |     |     |     |
That is, we have established that if MCF does not have a unique optimal solution then
|     |     |     |     |     | bN(z∗−1),bN(z∗ |     |     |          | bN(z∗)+nc |       |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | -------- | --------- | ----- | --- | --- |
|     |     |     |     | min | e e            |     | e e | +1) ≤    | e e       | max . |     |     |
|     |     |     |     |     | (cid:16)       |     |     | (cid:17) |           |       |     |     |
This completes the proof of the other side of equivalence and hence the proof of Corollary 5.2.
23

| 6   | Network |     | Flow: | Piece-wise |     |     | Linear | Convex |     | Objective |     |     |
| --- | ------- | --- | ----- | ---------- | --- | --- | ------ | ------ | --- | --------- | --- | --- |
Thissection describestheextension of Theorem 4.1 for network flow problemwith piece-wise linear
convex objective or cost function. Specifically, given a graph G = (V,E) as before, consider
|     |     | minimize |     | c (x | )   |     |     |     |     |     |     | (CP) |
| --- | --- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | ---- |
e e
e∈E
X
|     |     | subject | to  | ∆(v,e)x |     | = f | , ∀ v | ∈V (demand/supply |     |     | constraints) |     |
| --- | --- | ------- | --- | ------- | --- | --- | ----- | ----------------- | --- | --- | ------------ | --- |
e v
e ∈Ev
X
|     |     |     |     | 0≤ x ≤ | u , | ∀ e∈ | E (non-negativity |     |     | constraints), |     |     |
| --- | --- | --- | --- | ------ | --- | ---- | ----------------- | --- | --- | ------------- | --- | --- |
e e
where c : R → R is a piece-wise linear convex function for each e ∈E. As before, we shall assume
e
| that | the CP | is feasible. |     | Let ψ be | the   | same | as before | and    | define |     |     |     |
| ---- | ------ | ------------ | --- | -------- | ----- | ---- | --------- | ------ | ------ | --- | --- | --- |
|      |        |              |     |          |       |      | c (z)     | if 0 ≤ | z ≤    | u   |     |     |
|      |        |              |     |          |       |      | e         |        |        | e   |     |     |
|      |        |              |     |          | φ (z) | =    |           |        |        |     |     |     |
e
|     |     |     |     |     |     | (∞  |     | otherwise. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
The Algorithm 2 on G with functions ψ and φ thus defined is the BP for this problem instance.
Before we state our result, we need to define the corresponding residual graph. Suppose x is
a feasible solution for CP. Define the residual graph of G and x, denoted by G(x) as follows:
∀ e= (v ,v )∈ E, if x < u , then e is an arc in G(x) with cost cx = lim c(xe+t)−c(xe) ; if x > 0,
|     | α   | β   | e   | e   |     |     |     |     |     | e   | t↓0 | e   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
|     |     |     | e′  |     |     |     |     | cx  |     | c(xe)−c(xe−t) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- |
then there is an arc = (v β ,v α ) in G(x) with cost = lim t↓0 . Finally, let
|     |     |     |     |     |     |      |       | e′  |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | ---- | ----- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | δ(x) | = min | cx  | ,   |     |     |     |
e
|     |     |     |     |     |     |     | C∈C | (   | )   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e∈C
X
whereC is theset of all directed simplecycles in G(x). We state resultaboutconvergence property
of BP.
Theorem 6.1. Suppose x∗ is the unique optimal solution for CP and hence δ(x∗) > 0. Let L to be
|     |     |     |     |     |     |     | G(x∗). |     |     |     | L   | xˆN x∗. |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ------- |
the maximum cost of a simple directed path in Then, for any N ≥ +1 n, =
2δ(x∗)
The proof of Theorem 6.1 is identical to that of Theorem 4.1 with th(cid:0)e(cid:4)above(cid:5)defi(cid:1)ned notions.
| Therefore, |          | we shall | skip | it.      |     |     |          |     |     |     |     |     |
| ---------- | -------- | -------- | ---- | -------- | --- | --- | -------- | --- | --- | --- | --- | --- |
| 7          | Integral |          | MCF: | Run-time |     |     | analysis | of  | BP  |     |     |     |
In the next two sections, we shall consider MCF with integral components for c, u and f. Our
| goal | is to | analyze | the run-time | of  | BP  | for such | integral | MCF. |     |     |     |     |
| ---- | ----- | ------- | ------------ | --- | --- | -------- | -------- | ---- | --- | --- | --- | --- |
Lemma 7.1. For an integral MCF, the total number of operations performed by Algorithm 2 to
| update | all | the messages |     | at iteration | t   | is O | tc max mlogn |     | .   |     |     |     |
| ------ | --- | ------------ | --- | ------------ | --- | ---- | ------------ | --- | --- | --- | --- | --- |
Proof. Recall that, for edge e ∈ E with v(cid:0)as one of its(cid:1)end point (and w at the other), message
| function | is  | updated | as  |         |      |     |     |         |     |      |           |     |
| -------- | --- | ------- | --- | ------- | ---- | --- | --- | ------- | --- | ---- | --------- | --- |
|          |     |         | mt  |         |      |     |     |         |     | mt−1 |           |     |
|          |     |         |     | (z) = φ | (z)+ | min |     | ψ (z¯)+ |     |      | (z¯ ) .   |     |
|          |     |         | e→v | e       |      |     |     |  w     |     |      | e˜→w e˜  |     |
z¯∈R|Ew|,z¯e=z
|     |     |     |     |     |     |     |     |    | e˜∈ | Ew\e |    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
X
|     |     |     |     |     |     |     |     |    |     |     |    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
24

v
2
e
2
|     |     |     |     |     | e 1 |     |     | v   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3
e
3
v
1
|     |     |     |     |     |     | Figure | 6:  |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
From Corollary 4.12, all the message functions have integral slopes for an instance of MCF with
integral components. The absolute values of these slopes are bounded by (t−1)c max . This implies
that each (convex piece-wise linear) message (function) has at most 2(t−1)c linear pieces. By
max
Corollary4.9andObservation4.10itfollows thatg(z)canbecomputedinO(tc |E |log|E |) =
max w w
| O tc max | |E w |logn | total   | operations |     | since          | |E w | | ≤ n.    | Here |         |
| -------- | ---------- | ------- | ---------- | --- | -------------- | ------ | ------- | ---- | ------- |
| (cid:0)  |            | (cid:1) |            |     |                |        |         |      |         |
|          |            |         | g(z)       | =   | min            |        | ψ (z¯)+ | mt−1 | (z¯ ) . |
|          |            |         |            |     |                |        | w       | e˜→w | e˜      |
|          |            |         |            |     | z¯∈R|Ew|,z¯e=z |       |         |      |        |
e˜∈ Ew\e
|     |     |     |     |     |     |    |     | X   |    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Now computing g(z) +φ e (z) is a simple procedure which requires increasing the slopes of linear
piecesofg(z)byaconstant. Sinceg(·)hasatmost2tc linearpieces,computingg(z)+φ (z)takes
max e
further O(tc ) operations. In summary, it follows that all message updates can be performed in
max
| total of | O tc            | mlogn | operations   |            | since |       | |E | =Θ(m). |     |     |
| -------- | --------------- | ----- | ------------ | ---------- | ----- | ----- | ----------- | --- | --- |
|          | max             |       |              |            |       | w     | w           |     |     |
| We now   | co(cid:0)mplete | the   | p(cid:1)roof | of Theorem |       | 4.P2. |             |     |     |
δ(x∗)≥
Proof of Theorem 4.2. The integral instance of MCF with unique optimal solution has 1.
Therefore by Theorem 4.1, the BP Algorithm 2 converges after at most O(nL) iterations. By
Lemma 7.1, the total computation performed up to iteration t is O mlognc t2 . Therefore, the
max
total computation performed till convergence is O mlognc n2L2 . The L can be bounded as
|     |     |     |     |     |     |     |     | max | (cid:0) (cid:1) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |
mn4c3
L = O(nc max ). Therefore, it follows that the overall cost is at most O logn .
|     |     |     |     |     |     |     | (cid:0) |     | (cid:1) max |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------- |
The bound of Theorem 4.2 is pseudo-polynomial time. In fact q(cid:0)ualitatively th(cid:1)is is the best
bound one can hope for. To see this, consider an example of MCF defined on a directed graph G
as shown in Figure 6. Given large integer D, set the costs of edges as c e1 = c e2 = D, c e3 = 2D−1;
demands as b = 1, b = 0 and b = −1. It can be checked that xˆN alternates between 1 and
|     | v1  |     | v2  |     | v3  |     |     |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−1 when 2N +1< 2D. This means that BP algorithm takes at least Ω(D) iterations to converge.
3
Since the input size is Θ(logD), we have that Algorithm 2 for MCF does not converge to the
| unique      | optimal | solution | in     | polynomial-time |     | in   | the size | of the input. |     |
| ----------- | ------- | -------- | ------ | --------------- | --- | ---- | -------- | ------------- | --- |
| 7.1 Runtime |         | of       | BP for | integral        |     | MCFo |          |               |     |
Here we analyze the run time of BP for integral MCFo, the subclass of MCF defined in Section
| 4.2 and | prove | Theorem | 4.14. |     |     |     |     |     |     |
| ------- | ----- | ------- | ----- | --- | --- | --- | --- | --- | --- |
MCFo
Proof of Theorem 4.14. Since is an instance of MCF with integral components and unique
optimal solution, Theorem 4.1 it follows that the BP Algorithm 2 converges to the optimal solution
within O(Ln) iterations. To bound computation performed in each iteration and subsequently
25

bound overall computation cost, without loss of generality we shall assume that the piece-wise
linear convex message function is such that each linear piece is of unit length. This assumption is
without loss of generality, as each linear piece has integral vertices from Corollary 4.13 and hence
assumption of each piece being unit length only leads to upper bound on computation. Now each
message function is defined on a uniformly bounded interval due to uniform bound K on capacity
of each edge in MCFo. Therefore, the number of pieces in each piece-wise linear convex message
function is bounded by K +1. Recall that for t ≥ 1,
mt (z) = φ (z)+ min ψ (z¯)+ mt−1 (z¯ ) .
e→v e z¯∈R|Ew|,z¯e=z 

w
e˜∈ X Ew\e
e˜→w e˜ 

As explained in detail in Section 4.1, specificallyLemma 4.6 and Theorem 4.9, computing mt
e→v
takesatmostO Klog|E | whichisO Klogn as|E | ≤ nforallw. SincethereareatmostO(m)
w w
messages, total computation per iteration is O(Kmlogn). As discussed earlier, it takes O(Ln)
(cid:0) (cid:1) (cid:0) (cid:1)
iterations for the algorithm to converge. Therefore, overall computation scales O(KLmnlogn).
Finally, due to uniform bound of K on cost of edges, L = O(nc ) = O(nK). In summary, the
max
total computation cost is bounded above by O K2mn2logn .
(cid:0) (cid:1)
8 FPRAS for MCF using BP
Inthis section, we providea fully polynomial-time randomized approximation scheme(FPRAS) for
MCF using BP as a subroutine. As mentioned earlier, we shall assume integral MCF. We start
by describing the insights behind the algorithm followed by precise description in Section 8.2. To
this end, recall that the key hurdles in making BP fully polynomial-time as indicated by Theorem
4.2 are the following:
1. The convergence of BP requires MCF to have a unique optimal solution.
2. The running time of BP is polynomial in m, n and c .
max
Therefore, to find FPRAS for any given instance of MCF we need to overcome the requirement
of uniqueness and dependence over c of running time. To do so, we shall utilize appropriate
max
randomized modification of cost vector so that the resulting problem with modified cost vector c¯
has the following properties:
1. The modified problem has a unique optimal solution with high probability.
2. The modified cost vector has c¯ polynomial in m, n and 1.
max ε
3. The optimal solution of the modified problem provides 1+ε multiplicative approximation to
the optimal solution of MCF .
It seems intuitive that by adding enough randomness to cost vector, the modified problem will
have unique solution with high probability. However, requiring the resulting cost vector to be
polynomially small in m,n and 1/ε as well as having small approximation error is challenging and
a priori not clear if it is even feasible. The so called Isolation Lemma introduced in [21] helps to
address precisely this question for a specific class of combinatorial problems including matching. It
26

is not directly applicable to our setup primarily because the Isolation Lemma requires the feasible
{0,1}M
set of optimization problem to be a monotone subset of (for appropriate M) while the
feasible set of interest here is a polytope derived from a linear programming problem. For this
reason we state and prove a variation of Isolation Lemma for our setup next.
| 8.1 | Variation | of  | the Isolation |     | Lemma |     |     |     |     |     |
| --- | --------- | --- | ------------- | --- | ----- | --- | --- | --- | --- | --- |
Theorem 8.1. Let MCF be an instance of min-cost flow problem with underlying graph G =
(V,E), demand vector b, constraint vector u. Let its cost vector c¯be generated as follows: for each
e ∈E, c¯ is chosen independently and uniformly over N , where N is a discrete set of 4m positive
|     | e   |     |     |     |     |     | e   | e   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
numbers (m =|E|). Then, the probability that MCF has a unique optimal solution is at least 1.
2
Proof. Fix an arc e ∈ E and fix c¯ for all e ∈ E\e . First suppose there exists a value α ≥ 0 such
|     |     | 1   |     | e   |     | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that when c¯ = α, MCF has two optimal solutions x∗, x∗∗ and, moreover, x∗ = 0 and x∗∗ > 0.
|       | e1         |         |          |          |          |        |     |      | e1  | e1  |
| ----- | ---------- | ------- | -------- | -------- | -------- | ------ | --- | ---- | --- | --- |
| Then, | if c¯ > α, | for any | feasible | solution | x of MCF | with   | x   | > 0, |     |     |
|       | e1         |         |          |          |          |        | e1  |      |     |     |
|       |            |         |          |          | x∗       | x∗     |     |      |     |     |
|       |            |         |          | c¯       | =        | c¯     |     |      |     |     |
|       |            |         |          |          | e e      | e      | e   |      |     |     |
|       |            |         |          | e ∈E     | e∈E      | ,e6=e1 |     |      |     |     |
|       |            |         |          | X        | X        |        |     |      |     |     |
(a)
|     |     |     |     |     | ≤   | c¯  | x +x | α   |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
|     |     |     |     |     |     | e   | e e1 |     |     |     |
e∈E ,e6=e1
X
(b)
|     |     |     |     |     | <   | c¯ e x e . |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
e∈E X
In above, (a) follows from the fact that x∗ is optimal with c¯ = α; (b) follows c¯ > α and x > 0.
|     |     |     |     |     |     |     | e1  |     | e1  | e1  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
On the other hand, if c¯ < α, then for any feasible solution x of MCF where x = 0, we have
|     |     |     | e1  |     |     |     |     |     | e1  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(a)
|     |     |     |     | c¯   | x∗∗ < | c¯     | x∗∗+αx∗∗ |     |     |     |
| --- | --- | --- | --- | ---- | ----- | ------ | -------- | --- | --- | --- |
|     |     |     |     | e    | e     | e      | e        | e1  |     |     |
|     |     |     |     | e ∈E | e∈E   | ,e6=e1 |          |     |     |     |
|     |     |     |     | X    |       | X      |          |     |     |     |
(b)
|     |     |     |     |     | ≤   | c¯  | x +αx |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
|     |     |     |     |     |     | e   | e     | e1  |     |     |
e∈E X ,e6=e1
|     |     |     |     |     | =   | c¯ x . |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
|     |     |     |     |     |     | e e    |     |     |     |     |
e∈E
X
|     |     |     | x∗∗ |     |     |     |     | x∗∗ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In above (a) follows from e1 > 0 and c¯ e1 <α; (b) follows from being an optimal solution with
c¯ = α. In summary, there exists at most one value for α such that when c¯ = α, MCF has two
| e1  |     |     |     |     |     |     |     |     | e1  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
solutions x∗, x∗∗ with x∗ = 0 and x∗∗ > 0. In a similar manner, it can be established that there
|     |     |     | e1  | e1  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | x∗, | x∗∗ |
exists at most one value β such that with c¯ e1 = β, MCF has two optimal solutions with
| x∗ < | u and x∗∗ | = u | .   |     |     |     |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| e1   | e1        | e1  | e1  |     |     |     |     |     |     |     |
Let O be the set of all optimal solutions of MCF. From above discussion, it follows that for
a given arc e, if c¯ is chosen uniformly at random from 4m distinct positive integers, then the
e
|     |     |     |     |     | x∗, | x∗∗ |     |     | x∗ 0,x∗∗ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
probability that there exists two solutions in O that satisfy either e = e > 0 or
x∗ < u ,x∗∗ = u is at most 1/(2m). Therefore, with probability at least 1−1/(2m) all solutions x
| e   | e e | e   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in O satisfy either x = 0 or 0 < x < u or x = u . Denote this event by D(e). By union bound
|     |     | e   |     | e   | e e | e   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∩ e∈E D(e) holds with probability at least 1/2. Now to conclude the proof of Theorem 8.1, we state
| the following | Lemma. |     |     |     |     |     |     |     |     |     |
| ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
27

Lemma 8.2. Under event ∩ D(e), the MCF has a unique optimal solution.
e∈E
Proof. Supposetothecontrarythatunderevent∩ D(e),MCF hastwodistinctoptimalsolutions
e∈E
x∗ and x∗∗. Let d = x∗∗−x∗, then x∗+λd is an optimal solution of MCF iff 0 ≤ (x∗+λd) ≤ u ,
e e
|     |     |     |     |     | c¯Td |     | c¯Tx∗∗ | −c¯Tx∗ |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ------ | ------ | --- | --- | --- |
∀e ∈ E. Since c¯ > 0 for any e ∈ E and = = 0, there exists some e′ ∈ E such
e
| that d e′ | < 0. Let |     |         |     |         |     |            |          |     |       |     |
| --------- | -------- | --- | ------- | --- | ------- | --- | ---------- | -------- | --- | ----- | --- |
|           |          | λ∗  | = sup{λ | ≥ 0 | : x∗+λd | is  | a feasible | solution | of  | MCF}. |     |
Since d < 0, λ∗ is bounded and since x∗+d= x∗∗, λ∗ ≥ 1. Further, the supremum λ∗ is achieved,
e′
that is x∗+λ∗d is a feasible solution of MCF since the feasible space of MCF is a closed set. By
|     | λ∗, |     |     |     | e′′ |     | x∗  | x∗∗ |     | (x∗+λ∗d) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
definition of there must exists some such that 6= and either e′′ = 0 or u e′′ .
|         |     |          |     |     |     |     | e′′ | e′′ |     |            |     |
| ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| Sinceλ∗ | x∗  | (x∗+λ∗d) |     |     |     |     |     |     | x∗  | x∗+λ∗dthat |     |
> 0, e′′ 6= e′′ . Thatis, we have two solutions and do notsatisfy
D(e′′). This contradicts the hypothesis and hence MCF must have a unique optimal solution.
We note that Theorem 8.1 can be easily modified for LP in the standard form.
Corollary 8.3. Let LP be an LP problem with constraint Ax = b, where A is a m×n matrix,
b ∈ Rm. The cost vector c¯of LP is generated as follows: for each e∈ E, c¯ is chosen independently
e
and uniformly over N , where N is a discrete set of 2n elements. Then, the probability that LP
|     |     |     | e   | e   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.
| has a unique | optimal |     | solution | is at least |     |     |     |     |     |     |     |
| ------------ | ------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
2
c¯
| 8.2 Finding |     | the | correct | modified |     | cost vector |     |     |     |     |     |
| ----------- | --- | --- | ------- | -------- | --- | ----------- | --- | --- | --- | --- | --- |
Next, we construct a randomly generated cost vector c¯ with the desired properties stated in the
beginning of this section. Let X : E → {1,2,...,4m} be a random function where for each e ∈ E,
X(e) ischosen independentlyanduniformlyover therange. Lett = cmaxε andgenerate c¯as follows:
4mn
ce
for each e ∈E, let c¯ = 4m +X(e). Then, c¯ is polynomial in m, n and 1. By Theorem 8.1,
|     |     | e   |     | t   |     | max |     |     |     | ε   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.
the probability of MCF having a unique optimal solution is greater than
|     |     |     | (cid:4) | (cid:5) |     |     |     |     |     | 2   |     |
| --- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Now, we introduce algorithm APRXMT(MCF,ε) as follows. Select a random c¯; try to solve
MCF using BP. If BP discovers that MCF has no unique optimal solution (using Corollary 5.2),
then restart the procedure by selecting another c¯at random, otherwise, return the unique optimal
solution found by BP. Formally, we present APRXMT(MCF,ε) as Algorithm 3.
Corollary 8.4. The APRXMT(MCF,ε) runs in O n8m7logn expected time.
ε3
Proof. Theorem 8.1 implies that on average O(1) ins(cid:0)tances of(cid:1)MCF are required to be solved by
n2c¯
the BP. Each such instance requires running Algorithm 2 for O iterations. Therefore,
max
m2n),
the total cost scales as O c¯3 mn4logn on average by Lemma 7.1. Since c¯ = O it is
|     |     |     |     | max |     |     |     |     | (cid:0) | (cid:1) max | ε   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- |
ε−3m7n7logn
| bounded | as O |     |         | .   |         |     |     |     |     |     |         |
| ------- | ---- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | ------- |
|         |      |     | (cid:0) |     | (cid:1) |     |     |     |     |     | (cid:0) |
Now let c¯b(cid:0)e the randomly(cid:1) chosen vector as per above described procedure such that MCF has
a unique optimal solution, say x(2). Next, we show that x(2) is a “near optimal” solution of MCF .
28

| Algorithm |     | 3   | APRXMT(MCF,ε) |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1: Let t = c m ax ε, for any e ∈ E, assign c¯ = 4m·⌊c e⌋+p , where p is an integer chosen indepen-
|     |         | 4 m       | n      |         |      |              | e   |      | t   | e   | e   |     |     |
| --- | ------- | --------- | ------ | ------- | ---- | ------------ | --- | ---- | --- | --- | --- | --- | --- |
|     | dently, | uniformly |        | random  | from | {1,2,...,4m} |     |      |     |     |     |     |     |
|     | Let MCF |           | be the | problem | with | modified     |     | cost | c¯. |     |     |     |     |
2:
| 3:  | Run | Algorithm |     | 2 on | MCF | for N | = 2c¯ | n2 iterations. |     |     |     |     |     |
| --- | --- | --------- | --- | ---- | --- | ----- | ----- | -------------- | --- | --- | --- | --- | --- |
max
| 4:  | Use Corollary |      | 5.2           | to   | determine      | if       | MCF | has a | unique | solution. |     |     |     |
| --- | ------------- | ---- | ------------- | ---- | -------------- | -------- | --- | ----- | ------ | --------- | --- | --- | --- |
|     | if            |      |               |      |                |          |     | then  |        |           |     |     |     |
| 5:  | MCF           | does | not           | have | a unique       | solution |     |       |        |           |     |     |     |
|     | Restart       |      | the procedure |      | APRXMT(MCF,ε). |          |     |       |        |           |     |     |     |
6:
7: else
|     |     |     |     |     | x(2) | xˆN, | wherexˆN |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | ---- | -------- | --- | --- | --- | --- | --- | --- |
8: Terminate and return = is the estimate of optimal flow assignments found
|     | in  | Algorithm |     | 2.  |     |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9:  | end | if        |     |     |     |     |     |     |     |     |     |     |     |
To accomplish this, let e′ = argmaxc , ties broken arbitrarily, and define a new optimization
e
| problem |     | MCF      | as follows: |     |       |     |     |     |     |     |     |     |       |
| ------- | --- | -------- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | ----- |
|         |     | minimize |             | c   | e x e |     |     |     |     |     |     |     | (MCF) |
e∈E
X
|     |     | subject | to  |       | ∆(v,e)x | =b  | ,   |     | ∀v ∈ V | (demand/supply |     | constraints) |     |
| --- | --- | ------- | --- | ----- | ------- | --- | --- | --- | ------ | -------------- | --- | ------------ | --- |
|     |     |         |     |       |         | e   | v   |     |        |                |     |              |     |
|     |     |         |     | e ∈Ev |         |     |     |     |        |                |     |              |     |
X
(2)
|       |     |      |     | x =x  |     |     |     |     |       |       |               |     |     |
| ----- | --- | ---- | --- | ----- | --- | --- | --- | --- | ----- | ----- | ------------- | --- | --- |
|       |     |      |     | e′    | e′  |     |     |     |       |       |               |     |     |
|       |     |      |     | 0 ≤ x | ≤ u | ,   |     |     | ∀e∈ E | (flow | constraints). |     |     |
|       |     |      |     |       | e e |     |     |     |       |       |               |     |     |
| Lemma |     | 8.5. |     | x(3)  |     |     |     |     |       |       | x(1)          |     |     |
Suppose is an optimal solution for (MCF) and is an optimal solution of
MCF. Then
|     |     |     |            |     |     |             |         |             | (2)                 | (1) |     |     |     |
| --- | --- | --- | ---------- | --- | --- | ----------- | ------- | ----------- | ------------------- | --- | --- | --- | --- |
|     |     |     |            |     |     | cTx(3)      | −cTx(1) | ≤           | x −x                |     | nt. |     |     |
|     |     |     |            |     |     |             |         |             | e′                  | e′  |     |     |     |
|     |     |     | x(2)−x(1). |     |     | {−1,0,1}|E| |         | as(cid:12)a | synchrono(cid:12)us |     |     |     |     |
Proof. Let d = Call γ ∈ (cid:12) (cid:12) cycle vector of d if for any e ∈E,
γ = 1 only if d > 0, γ = −1 only if d < 0 and the set {e ∈ E : γ = 1 or γ = −1} forms exactly
| e   |     |     | e   | e   |     |     | e   |     |     |     | e   | e   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
one directed cycle in G. Now d is an integral vector of circulation (i.e., d send 0 unit amount of
flow to every vertex v ∈ V) since it is difference of two feasible solution of the same network flow
problem. Therefore, d can be decomposed as γ = d with K′ ⊂ K and K being a finite set
γ∈K′
|     |     |     |     |     |     |     |     |     |     | K′, |     | x(2) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
of synchronous cycle vectors of G (cf. see [2]). For any γ ∈ observe that −γ is a feasible
P
solution for MCF. Now since x(2) is an optimal solution for MCF, it follows that c¯Tγ ≤ 0. Now
| for | any e∈ | E,  |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
c e
|     |     |     |     |     |     | c¯ = 4m |     | +p , | 1≤ p | ≤ 4m, |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | ---- | ---- | ----- | --- | --- | --- |
|     |     |     |     |     |     | e       |     | e    | e    |       |     |     |     |
t
|     |     |     |     |     |     | 4mc  | j k    | c   |     | c   |      |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------ | --- | --- | --- | ---- | --- | --- |
|     |     |     |     |     | =⇒  | c¯ , | e ∈ 4m | e   | ,4m | e   | +1 , |     |     |
e
|     |     |     |     |     |     | t    |       | t   |             | t   |           |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ----- | --- | ----------- | --- | --------- | --- | --- |
|     |     |     |     |     |     |      | 4mc h | j   | k (cid:16)j | k   | (cid:17)i |     |     |
|     |     |     |     |     | =⇒  | c¯ − | e ≤   | 4m, |             |     |           |     |     |
e
t
|     |     |     |     |     |     | (cid:12) 4mc | (cid:12)    |          |      |     |          |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | ----------- | -------- | ---- | --- | -------- | --- | --- |
|     |     |     |     |     |     | (cid:12)     | e −(cid:12) |          |      |     |          |     |     |
|     |     |     |     |     | =⇒  | (cid:12)     | (cid:12)    | c¯ e γ e | ≤ 4m | γ   | e ≤ 4mn. |     |     |
t
|     |     |     |     |     |     | X e (cid:12) |     | (cid:12)(cid:12) | (cid:12) | X e      |          |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ---------------- | -------- | -------- | -------- | --- | --- |
|     |     |     |     |     |     | (cid:12)     |     | (cid:12)(cid:12) | (cid:12) | (cid:12) | (cid:12) |     |     |
|     |     |     |     |     |     |              |     |                  |          | (cid:12) | (cid:12) |     |     |
|     |     |     |     |     |     | (cid:12)     |     | (cid:12)(cid:12) | (cid:12) |          |          |     |     |
29

| Using | this | and fact | that | c¯Tγ | ≤ 0, we | have |     |     |       |     |     |     |
| ----- | ---- | -------- | ---- | ---- | ------- | ---- | --- | --- | ----- | --- | --- | --- |
|       |      |          |      |      |         | 4m   | 4m  |     |       |     |     |     |
|       |      |          |      |      |         | cTγ  | ≤   | cTγ | −c¯Tγ |     |     |     |
|       |      |          |      |      |         | t    | t   |     |       |     |     |     |
4mc
|     |     |     |     |     |     |     | ≤   |     | e −c¯ | γ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |       | e e |     |     |
t
e
|     |     |     |     |     |     |     | X      | (cid:12) |       | (cid:12)(cid:12) (cid:12) |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ----- | ------------------------- | --- | --- |
|     |     |     |     |     |     |     |        | (cid:12) |       | (cid:12)(cid:12) (cid:12) |     |     |
|     |     |     |     |     |     |     | ≤ 4mn. | (cid:12) |       | (cid:12)(cid:12) (cid:12) |     |     |
|     |     |     | cTγ |     |     |     | K′,    | x(2)     | x(1)+ |                           |     |     |
Therefore, we have ≤ nt. By definition of = γ∈K′ γ. Therefore, for all e∈ E
|     |     |     |     | min{x(1),x(2)} |     |     | x(1)+ |     |     | P    | x(1),x(2)}. |     |
| --- | --- | --- | --- | -------------- | --- | --- | ----- | --- | --- | ---- | ----------- | --- |
|     |     |     |     |                |     | ≤   |       | γ   | e ≤ | max{ |             |     |
|     |     |     |     |                | e   | e   | e     |     |     |      | e e         |     |
γ∈K′
X
Therefore, it follows that x(1) + γ is a feasible solution for MCF. Since x(3) is the optimal
γ∈K′
| solution |     | of MCF, |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P
|     |     |     |     |     |     | cTx(3) | ≤ cTx(1)+ |     |     | cTγ |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --------- | --- | --- | --- | --- | --- |
γ∈K′
X
|     |     |     |     |     |     |     | cTx(1)+ |     | K′  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | ≤       |     | nt. |     |     |     |
(cid:12) (cid:12)
|           | K′       | (2)               |         | (1)          |               |      |     |          | (cid:12) (cid:12) |          |     |     |
| --------- | -------- | ----------------- | ------- | ------------ | ------------- | ---- | --- | -------- | ----------------- | -------- | --- | --- |
| Since     |          | ≤ x               | −x      | , it follows |               | that |     |          | (cid:12) (cid:12) |          |     |     |
|           |          | e′                |         | e′           |               |      |     |          |                   |          |     |     |
|           | (cid:12) | (cid:12) (cid:12) |         | (cid:12)     | cTx(3)−cTx(1) |      |     | (2)      |                   | (1)      |     |     |
|           | (cid:12) | (cid:12) (cid:12) |         | (cid:12)     |               |      |     | ≤ x      | −x                | nt.      |     |     |
|           |          |                   |         |              |               |      |     | e′       |                   | e′       |     |     |
|           |          |                   |         |              |               |      |     | (cid:12) |                   | (cid:12) |     |     |
|           |          |                   |         |              |               |      |     | (cid:12) |                   | (cid:12) |     |     |
|           |          |                   |         |              |               |      |     | (cid:12) |                   | (cid:12) |     |     |
| Corollary |          | 8.6.              | For any | ε∈           | (0,1),        |      |     |          |                   |          |     |     |
ε
|     |     |     |     |     |     | cTx(3) | ≤ 1+ |     | cTx(1). |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | ---- | --- | ------- | --- | --- | --- |
2m
|     |     |     |     |     |     |     | (cid:16) |     | (cid:17) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- |
(2) (1)
Proof. By Lemma 8.5 we may assume without the loss of generality that x 6= x . Also by
e′ e′
Lemma 8.5,
|     |     |     |     | cTx(3) |     | −cTx(1) |     | x (2) −x | (1) | nt  |     |     |
| --- | --- | --- | --- | ------ | --- | ------- | --- | -------- | --- | --- | --- | --- |
|     |     |     |     |        |     |         |     | e′       | e′  |     |     |     |
≤
|     |     |     |     |     | cTx(3) |     |          | cTx(3)   |             |             |      |      |
| --- | --- | --- | --- | --- | ------ | --- | -------- | -------- | ----------- | ----------- | ---- | ---- |
|     |     |     |     |     |        |     | (cid:12) |          |             | (cid:12)    |      |      |
|     |     |     |     |     |        |     | (cid:12) | (2)      | (1)(cid:12) |             |      |      |
|     |     |     |     |     |        |     |          | x −x     |             | nt          | nt   |      |
|     |     |     |     |     |        |     | ≤        | e′       | e′          | =           | ,    | (12) |
|     |     |     |     |     |        |     |          | x (2) −x | (1)         | c           | c e′ |      |
|     |     |     |     |     |        |     | (cid:12) | e′       | e′          | (cid:12) e′ |      |      |
|     |     |     |     |     |        |     | (cid:12) |          |             | (cid:12)    |      |      |
|     |     |     |     |     |        |     | (cid:12) |          |             | (cid:12)    |      |      |
where the last inequality follows because of c Tx(3) ≥ |x ( 2 ) − x ( 1 ) |c justified as follows: using
|     |     |     |     |     |     |     | (cid:12) |     |     | (cid:12) e ′ | e ′ e′ |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ------------ | ------ | --- |
(3) (2)
| x   | =x  | by definition, |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e′ e′
|     |     |     |     |     | cTx(3) |     | (2)  |      | (2) | (1) |      |     |
| --- | --- | --- | --- | --- | ------ | --- | ---- | ---- | --- | --- | ---- | --- |
|     |     |     |     |     |        | ≥x  | c e′ | ≥ (x | −x  | )c  | e′ ; |     |
|     |     |     |     |     |        |     | e′   |      | e′  | e′  |      |     |
the optimal solution x(3) of MCF is a feasible solution for MCF, x(1) is optimal solution for MCF
and therefore
|     |     |     |     | cTx(3) |     | cTx(1) |     | (1)  |      | (1) | (2)     |     |
| --- | --- | --- | --- | ------ | --- | ------ | --- | ---- | ---- | --- | ------- | --- |
|     |     |     |     |        | ≥   |        | ≥ x | c e′ | ≥ (x | −x  | )c e′ . |     |
|     |     |     |     |        |     |        |     | e′   |      | e′  | e′      |     |
30

|      |     |             | (2) | (1)   |     |     |     |
| ---- | --- | ----------- | --- | ----- | --- | --- | --- |
| That | is, | cTx(3) ≥ |x | −x  | |c    | .   |     |     |
|      |     |             | e′  | e′ e′ |     |     |     |
c e′ε
| Using | t = | , from | (12) | it follows | that |     |     |
| ----- | --- | ------ | ---- | ---------- | ---- | --- | --- |
4mn
|     |     |     |     |     | cTx(3) | −cTx(1) | ε   |
| --- | --- | --- | --- | --- | ------ | ------- | --- |
≤ .
|     |     |     |     |     |     | cTx(3) | 4m  |
| --- | --- | --- | --- | --- | --- | ------ | --- |
Therefore
|       |     |                 |        |       |          | ε −1      | ε                 |
| ----- | --- | --------------- | ------ | ----- | -------- | --------- | ----------------- |
|       |     |                 | cTx(3) |       | ≤ 1−     | cTx(1)    | ≤ 1+ cTx(1),      |
|       |     |                 |        |       |          | 4m        | 2m                |
|       |     |                 |        |       | (cid:16) | (cid:17)  | (cid:16) (cid:17) |
| where | the | last inequality |        | holds | because  | ε∈ (0,1). |                   |
| 8.3   | The | FPRAS           |        |       |          |           |                   |
|       |     |                 |        |       |          | x(2)      | e′                |
Loosely speaking, Corollary 8.6 shows that at arc is “near optimal”, since fixing the flow
|     | e′  | (2) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
at arc to x helps us in finding a feasible solution of MCF which is close to optimal. This
e′
leads ustoan approximation algorithm AS(MCF, ε) (Algorithm 4)below. Thisalgorithm atevery
iteration uses APRXMT (Algorithm 3), and iteratively fixes the flow values at the arc with the
largest cost. Theorem 8.7 establishes that this algorithm AS(MCF, ε) is indeed an FPRAS.
| Algorithm |     | 4 AS(MCF, |     | ε)  |     |     |     |
| --------- | --- | --------- | --- | --- | --- | --- | --- |
1: Let G = (V,E) be the underlying directed graph of MCF with m = |E|, n = |V|.
| 2:  | while | MCF flows | for      | all arcs | are      | not assigned    | do        |
| --- | ----- | --------- | -------- | -------- | -------- | --------------- | --------- |
|     | Run   | APRXMT    | (MCF,ε), |          | let x(2) | be the solution | returned. |
3:
Find e′ = argmax c and modify MCF by fixing the flow on arc e′ by x ( 2 ) ; change the
| 4:  |     |     |     | e∈E e |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- |
e ′
|     | demands/supply |       | on  | node | v′,w′ with | e′ = (v′,w′). |     |
| --- | -------------- | ----- | --- | ---- | ---------- | ------------- | --- |
| 5:  | end            | while |     |      |            |               |     |
Theorem 8.7. Given ε ∈ (0,1), algorithm AS(MCF, ε) takes O ε−3n7m8logn operations on
| average. |     | Let x∗ be | the solution |     | produced | by AS(MCF, | ε). Then |
| -------- | --- | --------- | ------------ | --- | -------- | ---------- | -------- |
(cid:0) (cid:1)
|     |     |     |     |     |     | cTx∗ (1+ε)cTx(1). |     |
| --- | --- | --- | --- | --- | --- | ----------------- | --- |
≤
ε−3n7m7logn
Proof. By Corollary 8.4, APRXMT(MCF,ε) takes O operations on average. Since
AS(MCF, ε) invokes the method APRXMT(MCF,ε) m times, AS(MCF, ε) performs on average
(cid:0) (cid:1)
total operations bounded as O ε−3n7m8logn . By successive application of Corollary 8.6,
|     |     |     |     | (cid:0) |      | (cid:1) ε | m      |
| --- | --- | --- | --- | ------- | ---- | --------- | ------ |
|     |     |     |     |         | cTx∗ |           | cTx(1) |
|     |     |     |     |         |      | ≤ 1+      |        |
2m
(cid:16) ε cTx(1)(cid:17)
|     |     |     |     |     |     | ≤ e2 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
(1+ε)cTx(1)
≤
| where | the | last two | inequalities |     | follows | for ε∈ (0,1) | and m ≥ 1. |
| ----- | --- | -------- | ------------ | --- | ------- | ------------ | ---------- |
31

9 Conclusions
Inthispaper,weformulatedandanalyzedtheBeliefPropagation(BP)algorithmforthecapacitated
min-cost network flow problem MCF. We proved that the BP solves MCF exactly in pseudo-
polynomial time when the optimal solution is unique. This result generalizes an earlier result
from [5], and provides new insights for understanding BP as an optimization solver. Although the
running time of BP for MCF is slower than other existing algorithms for MCF, the advantage
of BP is that it is a general purpose distributed heuristic which is widely applicable and which is
easy to formulate and implement for a broad class of constrained optimization problems. We also
showed that a similar result holds for the network flow problem with the piece-wise linear convex
cost function. A salient feature of the BP established in this work is ability to detect uniqueness
| of the optimal |     | solution | in an entirely |     | distributed |     | manner. |     |     |     |
| -------------- | --- | -------- | -------------- | --- | ----------- | --- | ------- | --- | --- | --- |
We showed that the BP algorithm, in its original form, at best leads to a pseudo-polynomial
time algorithmic complexity. To address this problem we have introduced a randomized variant
of BP and showed that this variant provides FPRAS. This is the first FPRAS result for the BP
type algorithms. Our variant of BP is based on fixing the values of flow variables one-by-one in a
sequential manner. Such methodology, used commonly in practice, is known as the “decimation”
procedure (see [20]). To the best of our knowledge, this is the first disciplined, provable instance
| of the decimation |     | procedure | in  | the context |     | of BP | algorithms. |     |     |     |
| ----------------- | --- | --------- | --- | ----------- | --- | ----- | ----------- | --- | --- | --- |
Acknowledgments
Whileworkingonthispaper,D.GamarnikwaspartiallysupportedbyNSFProjectCMMI-0726733;
D. Shah was supported in parts by NSF EMT Project CCF 0829893 and NSF CAREER Project
CNS 0546590; and Y. Wei was partially supportedby a Natural Sciences and Engineering Research
Council of Canada (NSERC) Postgraduate Scholarship. The authors would also like to thank the
| anonymous | referees |     | for the helpful | comments. |     |     |     |     |     |     |
| --------- | -------- | --- | --------------- | --------- | --- | --- | --- | --- | --- | --- |
References
| R.     | Ahuja,   | A.  | Goldberg,    | J.           | Orlin, | and | R. Tarjan, |     |                      |          |
| ------ | -------- | --- | ------------ | ------------ | ------ | --- | ---------- | --- | -------------------- | -------- |
| [1]    |          |     |              |              |        |     |            |     | Finding minimum-cost | flows by |
| double | scaling, |     | Mathematical | Programming, |        |     | 53 (1992), | pp. | 243–266.             |          |
[2] R. K. Ahuja, T. L. Magnanti, and J. B. Orlin, Network Flows., Prentice-Hall Inc., 1993.
[3] S. M. Aji and R. J. McEliece, The generalized distributive law, IEEE Transaction on
| Information |     | Theory, | 46 (2000), |     | pp. 325–343. |     |     |     |     |     |
| ----------- | --- | ------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- |
[4] M. Bayati, C. Borgs, J. Chayes, and R. Zecchina,On the exactness of the cavity method
for weighted b-matchings on arbitrary graphs and its relation to linear programs, Journal of
| Statistical |     | Mechanics: | Theory | and | Experiment, |     | 2008 | (2008). |     |     |
| ----------- | --- | ---------- | ------ | --- | ----------- | --- | ---- | ------- | --- | --- |
[5] M. Bayati, D. Shah, and M. Sharma, Max-product for maximum weight matching: Con-
vergence, correctness, and lp duality, IEEE Transaction on Information Theory, 54 (2008),
| pp. | 1241–1251. |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
32

[6] D. P. Bertsekas, Distributed relaxation methods for linear network flow problems, in Pro-
ceedings of 25th IEEE Conference on Decision and Control, Athens, Greece, 1986, pp. 2101–
2106.
[7] D. Bertsimas and J. Tsitsiklis, Introduction to Linear Optimization, Athena Scientific,
| third ed., | 1997, | pp. 289–290. |     |     |     |     |     |     |     |     |
| ---------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[8] J. Edmonds and R. M. Karp, Theoretical improvements in algorithmic efficiency for net-
| work flow | problems, | J.  | ACM, | 19  | (1972), | pp. 248–264. |     |     |     |     |
| --------- | --------- | --- | ---- | --- | ------- | ------------ | --- | --- | --- | --- |
[9] S. Fujishige, A capacity-rounding algorithm for the minimum-cost circulation problem: A
dual framework of the tardos algorithm, Mathematical Programming, 35 (1986), pp. 298–308.
R. Gallager,Low
[10] Density Parity Check Codes, PhDthesis, Massachusetts Institute of Tech-
| nology, Cambridge, |     | MA, | 1963. |     |     |     |     |     |     |     |
| ------------------ | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
[11] D. Gamarnik, D. Shah, and Y. Wei, Belief propagation for min-cost network flow: con-
vergence & correctness, in Proceedings of the Twenty-First Annual ACM-SIAM Symposium
on Discrete Algorithms, Society for Industrial and Applied Mathematics, 2010, pp. 279–292.
[12] A. Goldberg and R. Tarjan, Solving minimum-cost flow problems by successive approxi-
mation, in STOC ’87: Proceedings of the nineteenth annual ACM symposium on Theory of
| computing,     | New | York, | NY,        | USA,       | 1987,        | ACM, pp. | 7–18.        |              |              |      |
| -------------- | --- | ----- | ---------- | ---------- | ------------ | -------- | ------------ | ------------ | ------------ | ---- |
| A. V. Goldberg |     | and   | R.         | E. Tarjan, |              |          |              |              |              |      |
| [13]           |     |       |            |            |              | Finding  | minimum-cost | circulations | by canceling | neg- |
| ative cycles,  | J.  | ACM,  | 36 (1989), |            | pp. 873–886. |          |              |              |              |      |
[14] G. B. Horn, Iterative Decoding and Pseudocodewords, PhD thesis, California Institute of
| Technology, | Pasadena, |     | CA, | 1999. |     |     |     |     |     |     |
| ----------- | --------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
[15] Y. Kanoria, M. Bayati, C. Borgs, J. T. Chayes, and A. Montanari,Fast convergence
of natural bargaining dynamics in exchange networks, CoRR, abs/1004.2079 (2010).
[16] D. M. Malioutov, J. K. Johnson, and A. S. Willsky,Walk-sums and belief propagation
in gaussian graphical models, J. Mach. Learn. Res., 7 (2006), pp. 2031–2064.
[17] M. Mezard, G. Parisi, and R. Zecchina, Analytic and algorithmic solution of random
| satisfiability | problems, |     | Science, | 297 | (2002), | p. 812. |     |     |     |     |
| -------------- | --------- | --- | -------- | --- | ------- | ------- | --- | --- | --- | --- |
[18] C. Moallemi and B. V. Roy, Convergence of min-sum message passing for convex opti-
mization, in 45th Allerton Conference on Communication, Control and Computing, 2008.
[19] C. C. Moallemi and B. V. Roy, Convergence of the min-sum message passing algorithm
| for quadratic | optimization, |     |     | CoRR, | abs/cs/0603058 |     | (2006). |     |     |     |
| ------------- | ------------- | --- | --- | ----- | -------------- | --- | ------- | --- | --- | --- |
[20] A. Montanari, F. Ricci-Tersenghi, and G. Semerjian, Solving constraint satisfaction
problems through belief propagation-guided decimation, in 45th Allerton, 2007.
[21] K. Mulmuley, U. Vazirani, and V. Vazirani, Matching is as easy as matrix inversion,
| Combinatorica, |     | 7 (1987), | pp. | 105–113. |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- |
33

[22] J. Orlin, A faster strongly polynomial minimum cost flow algorithm, in Proceedings of the
twentieth annual ACM symposium on Theory of computing, ACM, 1988, pp. 377–387.
[23] J. B. Orlin, A faster strongly polynomial minimum cost flow algorithm, in Operations Re-
| search, 1988, | pp. 377–387. |     |     |     |     |
| ------------- | ------------ | --- | --- | --- | --- |
[24] J. Pearl, Probabilistic reasoning in intelligent systems: networks of plausible inference, Mor-
| gan Kaufmann, | 1988.  |          |                         |              |             |
| ------------- | ------ | -------- | ----------------------- | ------------ | ----------- |
| T. Richardson | and R. | Urbanke, |                         |              |             |
| [25]          |        | The      | capacity of low-density | parity check | codes under |
message-passing decoding, IEEE Transaction on Information Theory, 47 (2001), pp. 599–618.
Ro¨ck,
[26] H. Scaling techniques for minimal cost flow problems, Discrete Structures and Algo-
| rithms, (1980), | pp. 181–191. |     |     |     |     |
| --------------- | ------------ | --- | --- | --- | --- |
[27] N. Ruozzi and S. Tatikonda, s-t paths using the min-sum algorithm, in Forty-Sixth Annual
Allerton Conference on Communication, Control, and Computing, September 2008, pp. 918
–921.
[28] S. Sanghavi, D. Malioutov, and A. Willsky,Linear programming analysis of loopy belief
propagation for weighted matching, in Proc. NIPS Conf, Vancouver, Canada, 2007.
[29] S. Sanghavi, D. Shah, and A. Willsky,Message-passing for maximum weight independent
set, IEEE Transaction on Information Theory, 51 (2009), pp. 4822–4834.
| [30] A. Schrijver, | Combinatorial | Optimization, | Springer, 2003. |     |     |
| ------------------ | ------------- | ------------- | --------------- | --- | --- |
[31] E. Tardos, A strongly polynomial minimum cost circulation algorithm, Combinatorica, 5
| (1985), pp. 247–255. |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- |
[32] Y. Weiss and W. Freeman, On the optimality of solutions of the max-product belief-
propagation algorithm in arbitrary graphs, IEEE Transactions on Information Theory, 47
(2001).
[33] J. Yedidia, W. Freeman, and Y. Weiss, Understanding belief propagation and its gener-
alizations, Tech. Rep. TR-2001-22, Mitsubishi Electric Research Lab, 2002.
34