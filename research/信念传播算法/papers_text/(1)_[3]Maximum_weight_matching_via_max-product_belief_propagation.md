| Maximum |     |     | Weight |     | Matching |     |     |     | via | Max-Product |     |     |     | Belief |     |
| ------- | --- | --- | ------ | --- | -------- | --- | --- | --- | --- | ----------- | --- | --- | --- | ------ | --- |
Propagation
|     | Mohsen     | Bayati     |       |     |             | Devavrat |     | Shah     |       |     | Mayank     |     | Sharma     |     |     |
| --- | ---------- | ---------- | ----- | --- | ----------- | -------- | --- | -------- | ----- | --- | ---------- | --- | ---------- | --- | --- |
|     | Department |            | of EE |     | Departments |          | of  | EECS     | & ESD |     | Department |     | of         | EE  |     |
|     | Stanford   | University |       |     |             |          | MIT |          |       |     | Stanford   |     | University |     |     |
|     | Stanford,  | CA         | 94305 |     |             | Boston,  |     | MA 02139 |       |     | Stanford,  |     | CA 94305   |     |     |
Email: bayati@stanford.edu Email: devavrat@mit.edu Email: msharma@stanford.edu
|              |             |     |         |              |     |           |     | BP  | is  | known to | converge | to the | correct | marginal/MAP |     |
| ------------ | ----------- | --- | ------- | ------------ | --- | --------- | --- | --- | --- | -------- | -------- | ------ | ------- | ------------ | --- |
| Abstract—The | max-product |     | “belief | propagation” |     | algorithm |     |     |     |          |          |        |         |              |     |
is an iterative, local, message passing algorithm for finding probabilities on tree-like graphs [11] or graphs with a single
the maximum a posteriori (MAP) assignment of a discrete loop [2], [16]. For graphicalmodels with arbitraryunderlying
| probability | distribution | specified | by  | a graphical |     | model. | Despite |         |        |          |       |     |             |     |             |
| ----------- | ------------ | --------- | --- | ----------- | --- | ------ | ------- | ------- | ------ | -------- | ----- | --- | ----------- | --- | ----------- |
|             |              |           |     |             |     |        |         | graphs, | little | is known | about | the | correctness | of  | BP. Partial |
thespectacularsuccessofthealgorithminmanyapplicationareas
progressconsistsof[17]wherecorrectnessofBPforGaussian
| such as | iterative decoding |     | and computer |     | vision | which | involve |     |     |             |       |               |     |              |     |
| ------- | ------------------ | --- | ------------ | --- | ------ | ----- | ------- | --- | --- | ----------- | ----- | ------------- | --- | ------------ | --- |
|         |                    |     |              |     |        |       |         | GMs | is  | proved, [5] | where | an attenuated |     | modification | of  |
graphswithmanycycles,theoreticalconvergenceresultsareonly
known for graphs which are tree-like or have a single cycle. BP is shown to work, and [12] where the iterative turbo
Inthispaper,weconsideraweightedcompletebipartitegraph decoding algorithm based on BP is shown to work in the
anddefineaprobabilitydistributiononitwhoseMAPassignment
asymptoticregimewithprobabilisticguarantees.Tothebestof
| corresponds | to the | maximum | weight | matching | (MWM) |     | in that |     |     |     |     |     |     |     |     |
| ----------- | ------ | ------- | ------ | -------- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ourknowledge,littletheoreticalprogresshasbeeninresolving
graph.Weanalyzethefixedpointsofthemax-productalgorithm
|     |     |     |     |     |     |     |     | the | question: | Why does | BP work | on  | arbitrary | graphs? |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------- | --- | --------- | ------- | --- |
whenrunonthisgraphandprovethesurprisingresultthateven
though the underlying graph has many short cycles, the max- Motivatedbythe objectiveof providingjustification forthe
product assignment converges to the correct MAP assignment. successofBPonarbitrarygraphs,wefocusontheapplication
| We also | provide a | bound on | the number |     | of iterations | required |     |     |       |                |               |     |              |     |         |
| ------- | --------- | -------- | ---------- | --- | ------------- | -------- | --- | --- | ----- | -------------- | ------------- | --- | ------------ | --- | ------- |
|         |           |          |            |     |               |          |     | of  | BP to | the well-known | combinatorial |     | optimization |     | problem |
by the algorithm.
|     |     |                 |     |     |     |     |     | of          | finding | the Maximum  | Weight        |     | Matching     | (MWM) | in a         |
| --- | --- | --------------- | --- | --- | --- | --- | --- | ----------- | ------- | ------------ | ------------- | --- | ------------ | ----- | ------------ |
|     |     |                 |     |     |     |     |     | bipartite   |         | graph, also  | known as      | the | “Assignment  |       | Problem”. It |
|     |     | I. INTRODUCTION |     |     |     |     |     |             |         |              |               |     |              |       |              |
|     |     |                 |     |     |     |     |     | is standard |         | to represent | combinatorial |     | optimization |       | problems,    |
Graphical models (GM) are a powerful method for repre- likefindingtheMWM, ascalculatingtheMAPprobabilityon
| senting | and manipulating | joint | probability |     | distributions. |     | They |                     |     |     |                                   |     |     |     |     |
| ------- | ---------------- | ----- | ----------- | --- | -------------- | --- | ---- | ------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- |
|         |                  |       |             |     |                |     |      | a suitablydefinedGM |     |     | whichencodesthedataandconstraints |     |     |     |     |
have found major applications in several different research oftheoptimizationproblem.Thus,themax-productalgorithm
communities such as artificial intelligence [11], statistics [8], can be viewed at least as a heuristic for solving the problem.
error-control coding [6] and neural networks. Two central In this paper, we study the performance of the max-product
problems in probabilistic inference over graphical models are algorithm as a method for finding the MWM on a weighted
those of evaluating the marginal and maximum a posteriori complete bipartite graph.
(MAP) probabilities, respectively. In general, calculating the Additionally,usingthemax-productalgorithmforproblems
marginal or MAP probabilities for an ensemble of random like finding the MWM has the potential of being an exciting
| variables | would require | a   | complete | specification |     | of the | joint |               |     |           |              |     |                     |     |     |
| --------- | ------------- | --- | -------- | ------------- | --- | ------ | ----- | ------------- | --- | --------- | ------------ | --- | ------------------- | --- | --- |
|           |               |     |          |               |     |        |       | applicationof |     | BP in its | ownright.The |     | assignmentproblemis |     |     |
probability distribution. Further, the complexity of a brute extremelywell-studiedalgorithmically.Attemptstofindbetter
force calculation would be exponential in the size of the MWM algorithms contributed to the development of the rich
ensemble. GMs assist in exploiting the dependency structure theory of network flow algorithms [4], [9]. The assignment
between the random variables, allowing for the design of problem has been studied in various contexts such as job-
| efficient | inference | algorithms. |     |     |     |     |     |            |     |                  |     |         |      |        |            |
| --------- | --------- | ----------- | --- | --- | --- | --- | --- | ---------- | --- | ---------------- | --- | ------- | ---- | ------ | ---------- |
|           |           |             |     |     |     |     |     | assignment |     | in manufacturing |     | systems | [4], | switch | scheduling |
The belief propagation (BP) and max-product algorithms algorithms [10] and auction algorithms [3]. We believe that
[11] were proposed in order to compute, respectively, the the max-product algorithm can be effectively used in high-
marginal and MAP probabilities efficiently. Comprehensive speed switch scheduling where the distributed nature of the
surveys of various formulations of BP and its generalization, algorithm and its simplicity can be very attractive.
thejunctiontreealgorithm,canbefoundin[1],[20],[14].BP- The main result of this paper is to show that the max-
based message-passing algorithms have been very successful product algorithm for finding the MWM always finds the
in the context of, for example, iterative decoding for turbo correct solution, as long as the solution is unique. Our proof
codes and in computer vision. The simplicity, wide scope of is purely combinatorial and depends on the graph structure.
applicationandexperimentalsuccessofbeliefpropagationhas We think that this result may lead to further insights in
attracted a lot of attention recently [1], [7], [12], [19]. understandinghowBPalgorithmsworkwhenappliedtoother
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:10:02 UTC from IEEE Xplore.  Restrictions apply.

optimization problems. The rest of the paper is organized The following claims are a direct consequence of these
as follows: In Section II, we provide the setup, define the definitions.
assignment problem and describe the max-product algorithm Claim(cid:2) 1: For the GM as defined above(cid:3), the joint den-
for finding the MWM. Section III states and proves the main sity p X =(x1,...,xn),Y =(y1,...,yn) is nonzero if
result of this paper. Finally, we discuss some implications of and only if πα(X) = {(α1,βx1 ),(α2,βx2 ),...,(αn,βxn )}
our results in Section IV. and πβ(Y) = {(αy1 ,β1),(αy2 ,β2),...,(αyn ,βn)} are both
matchings and παP (X)=πβ(Y). Further, when nonzero, they
II. SETUPAND PROBLEM STATEMENT are equal to Z 1e2 i wixi.
∗ ∗
Claim 2: Let (X ,Y ) be such that
In this section, we first define the problem of finding
(cid:2) (cid:3)
the MWM in a weighted complete bipartite graph and then (X ∗ ,Y ∗ )=argmax{p X,Y }.
describe the max-productBP algorithm for solving it.
∗ ∗
Then, the corresponding πα(X ) = πβ(Y ) is the MWM in
A. MAXIMUM WEIGHT MATCHING
Kn,n.
Claim 2 implies that finding the MWM is equivalent to
Consider an undirected weighted complete bipartite graph
Kn,n = (V1,V2,E), where V1 = {α1,...,αn }, V2 = finding the maximum a posteriori (MAP) assignment on the
{β1,...,βn } and (αi,βj) ∈ E for 1 ≤ i,j ≤ n. Let each GM defined above.Thus, the standardmax-productalgorithm
edge (αi,βj) have weight wij ∈R. can be used as an iterative strategy for finding the MWM. In
If π = {π(1),...,π(n)} is a permutation of {1,...,n} factwe show thatthisstrategyyieldsthe correctanswer. Next
then the collection of n edges {(α1,β π(1) ),...,(αn,β π(n) )} we describe the max-product algorithm (and the equivalent
iscalleda matchingofKn,n.We denoteboththepermutation min-sum algorithm) for the GM defined above.
andthecorrespondingmatchingbyπ.Theweightofmatching
π, denoted by Wπ, is defined as B. MAX-PRODUCT ALGORITHM FOR Kn,n
(cid:1)
Wπ = w
iπ(i)
. We need some definitions and notations before we can
describe the max-productalgorithm. Consider the following.
1≤i≤n
Definition 1: Let D ∈ Rn×n and X,Y,Z ∈ Rn×1. Then
Then, the Maximum Weight Matching (MWM), π∗, is the
the operations ∗,(cid:6) are defined as follows:
matching such that
π∗ =argmax π Wπ. D∗X =Z ⇐⇒zi =m j axdijxj, ∀i, (2)
Note 1. In this paper, we always assume that the weights are X (cid:6)Y =Z ⇐⇒zi =xiyi, ∀i. (3)
such that the MWM is unique. In particular, if the weights of For X1,...,Xm ∈Rn×1,
the edges are independent,continuous random variables, then
(cid:8)m
with probability 1, the MWM is unique.
Xi =X1 (cid:6)X2 (cid:6)...(cid:6)Xn. (4)
Next, we model the problem of finding MWM as find-
i=1
ing a MAP assignment in a graphical model where the Define the compatibility matrix Ψαiβj ∈ Rn×n such that
joint probability distribution can be completely specified in its (r,s) entry is ψαiβj (r,s), for 1 ≤ i,j ≤ n. Also, let
terms of the product of functions that depend on at most Φαi ,Φβj ∈Rn×1 be the following:
two variables (nodes). For details about GMs, we urge the
reader to see [8]. Now, consider the following GM defined
Φαi =[φαi (1),...,φαi (n)]t, Φβj =[φβj (1),...,φβj (n)]t.
on Kn,n: LetX 1,...,Xn,Y1,...,Yn be random variables
Max-Product Algorithm.
corresponding to the vertices of Kn,n and taking values
fr(cid:2)om {1,2,...,n}. Let their joint pr(cid:3)obability distribution,
(1) LetMk =[mk (1),mk (2),...,mk (n)]t ∈
p X =(x1,...,xn);Y =(y1,...,yn) , be of the form: αi→βj αi→βj αi→βj αi→βj
(cid:2) (cid:3) (cid:4) (cid:4) Rn×1 denote the messages passed from αi to βj in the
p X,Y = Z 1 i,j ψαiβj (xi,yj) i φαi (xi)φβi (yi), (1) i m te e r s a s t a io g n e k ve ≥ cto 0 r , p fo a r ss 1 ed ≤ fr i o ,j m ≤ βj n. to Si α m i il i a n rl t y h , e M ite β k r j a α t i io i n s t k h . e
(2) Initially k = 0 and set the messages as follows. Let
where the pairwise compatibility functions, ψ··(·,·), are de- M0 =[m0 (1)...m0 (n)]t andM0 =
fined as
αi→βj αi→βj αi→βj βj→αi
 [m0 (1)...m0 (n)]t where
 0 r =j and s(cid:3)=i
βj→αi βj→αi
(cid:9)
ψαiβj (r,s)=  0 r (cid:3)=j and s=i m0 (r)= ewij if r =i (5)
1 Otherwise αi→βj 1 otherwise
(cid:9)
and the potentials at the nodes, φ·(·), are defined as m0 (r)= ewji if r =i (6)
φαi (r)=ewir, φβj (r)=ewrj, ∀ 1≤ i,j,r,s ≤ n. βi→αj 1 otherwise
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:10:02 UTC from IEEE Xplore. Restrictions apply.

(3) For k ≥ 1, messages in iteration k are obtained from (c) Replace (8) by the following.
|     | messages | of iteration |      | k−1 recursively |            | as follows:       |          |     |     |     | (cid:1)  |         |       |     |      |
| --- | -------- | ------------ | ---- | --------------- | ---------- | ----------------- | -------- | --- | --- | --- | -------- | ------- | ----- | --- | ---- |
|     |          |              |      |                 |            |                   |          |     |     | bk  |          | k       |       |     |      |
|     |          |              |      | (cid:10)        | (cid:8)    |                   | (cid:11) |     |     |     | = (      | M       | )+Φαi |     |      |
|     |          |              |      |                 |            |                   |          |     |     | αi  |          | β l →αi |       |     |      |
|     | k        |              | Ψt   | ∗               |            | k − 1 )(cid:6)Φαi |          |     |     |     | (cid:1)l |         |       |     |      |
|     | M α      | i→βj         | =    | αiβj (          | M          | β → αi            |          |     |     |     |          |         |       |     |      |
|     |          |              |      |                 |            | l                 |          |     |     | bk  |          | k       |       |     |      |
|     |          |              |      |                 | l(cid:4)=j |                   |          |     |     |     | = (      | M       | )+Φβi |     | (12) |
|     |          |              |      | (cid:10)        | (cid:8)    |                   | (cid:11) |     |     | βj  |          | α l →βi |       |     |      |
|     | M k      |              | = Ψt | ∗ (             | M          | k − 1 )(cid:6)Φβi | (7)      |     |     |     |          | l       |       |     |      |
|     | β        | i→αj         |      | αiβj            |            | α → βi            |          |     |     |     |          |         |       |     |      |
l
l(cid:4)=j Note 3. The min-sum algorithm involves only summations
(4) Define the beliefs (n×1 vectors) at nodes αi and βj, and subtractions compared to max-product which involves
1≤i,j ≤n, multiplicationsanddivisions.Computationally,thismakesthe
|     |     | in  | iteration | k as | follows. |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:12) (cid:13) min-sum algorithm more efficient and hence very attractive.
(cid:8)
|     |     | bk  |     |            | k        |            |     |     |     |      |      |        |     |     |     |
| --- | --- | --- | --- | ---------- | -------- | ---------- | --- | --- | --- | ---- | ---- | ------ | --- | --- | --- |
|     |     |     | =   | M          |          | (cid:6)Φαi |     |     |     |      |      |        |     |     |     |
|     |     | αi  |     |            | b l →αi  |            |     |     |     | III. | MAIN | RESULT |     |     |     |
|     |     |     |     | (cid:12) l | (cid:13) |            |     |     |     |      |      |        |     |     |     |
(cid:8)
|     |     |     |     |     |     |            |     | Now | we state | and | prove Theorem |     | 1, which | is the | main |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- | -------- | --- | ------------- | --- | -------- | ------ | ---- |
|     |     | bk  |     |     | k   | (cid:6)Φβi |     |     |          |     |               |     |          |        |      |
βj = M α →βi (8) contributionof this paper.Before proceedingfurther,we need
l
|     |     |     |     | l   |     |     |     | the following |     | definitions. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | --- | --- | --- | --- |
estimated1 πk, Definition 2: Let (cid:6) be the difference between the weights
| (5) | The        |              | MWM        | at the       | end of      | iteration | k is   |        |     |           |             |            |         |               |     |
| --- | ---------- | ------------ | ---------- | ------------ | ----------- | --------- | ------ | ------ | --- | --------- | ----------- | ---------- | ------- | ------------- | --- |
|     |            |              |            |              |             |           |        | of the | MWM | and th e  | se co n d m | ax i m u m | w eight | matching;i.e. |     |
|     | w h e re π | k ( i ) =    | a r g m a  | x            | { b k (j)}, | for       | 1≤i≤n. |        |     |           |             |            |         |               |     |
|     |            |              |            | 1 ≤ j ≤ n    | αi          |           |        |        |     |           |             |            |         |               |     |
| (6) | R e p e at | ( 3 ) - (5 ) | t il l π k | c o n v e rg | e s .       |           |        |        |     |           | −           |            |         |               |     |
|     |            |              |            |              |             |           |        |        |     | (cid:6) = | W π ∗       | m a x ( W  | π ).    |               |     |
π(cid:4)=π∗
|      |        |               |     |            |       |                   |     | Due to          | the uniqueness |     | of the | MWM, | (cid:6) > | 0. Also, | define |
| ---- | ------ | ------------- | --- | ---------- | ----- | ----------------- | --- | --------------- | -------------- | --- | ------ | ---- | --------- | -------- | ------ |
| Note | 2. For | computational |     | stability, | it is | often recommended |     |                 |                |     |        |      |           |          |        |
|      |        |               |     |            |       |                   |     | w∗ =maxi,j(|wij |                | |). |        |      |           |          |        |
thatmessagesbenormalizedateveryiteration.However,such
|               |     |      |            |     |        |        |            | Theorem | 1:  | For any | weighted | complete |     | bipartite | graph |
| ------------- | --- | ---- | ---------- | --- | ------ | ------ | ---------- | ------- | --- | ------- | -------- | -------- | --- | --------- | ----- |
| normalization |     | does | not change | the | output | of the | algorithm. |         |     |         |          |          |     |           |       |
Kn,n
Since we are only interested in theoretically analyzing the with unique maximum weight matching, the max-
algorithm, we will ignore the normalization step. Also, the product or min-sum algorithm when applied to the corre-
spondingGMasdefinedabove,convergestothecorrectMAP
messagesareusuallyallinitializedtoone.Althoughtheresult
|     |     |     |     |     |     |     |     |     |     |     |     | (cid:10)2n w∗(cid:11) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
doesn’t depend on the initial values, setting them as defined assignment or the MWM within iterations.
(cid:4)
| above      | makes | the analysis | and | formulas | nicer | at  | the end. |            |               |           |            |             |                  |            |               |
| ---------- | ----- | ------------ | --- | -------- | ----- | --- | -------- | ---------- | ------------- | --------- | ---------- | ----------- | ---------------- | ---------- | ------------- |
|            |       |              |     |          |       |     |          | A. PROOF   | OF            | THEOREM   | 1          |             |                  |            |               |
| C. MIN-SUM |       | ALGORITHM    |     | FOR      | Kn,n  |     |          |            |               |           |            |             |                  |            |               |
|            |       |              |     |          |       |     |          | We         | first present | some      | useful     | notation    | and definitions. |            | Con-          |
|            |       |              |     |          |       |     |          | s id e r α | i, 1 ≤        | i ≤ n . L | e tT k b e | t he le v e | l- k u n ro      | l l ed t r | ee c o rr e - |
T h e m a x - p r o d u ct a n d m i n - su m al g o rit h m s c a n b e s e en α
|     |     |     |     |     |     |     |     |     |     |     | i   | k   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to b e e qu i v a l e n t b y o b se rv i n g t hat t h e l o ga rit h m f u nc t io n sp o n d in g to α i, de fi n e d as fo l lo w s: T α i s a w e i g ht e d re g u la r
i
is monotone and hence maxilog(αi) = log(maxiαi). In rootedtreeofheightk+1witheverynon-leafhavingdegreen.
|     |     |     |     |     |     |     |     |     |     |     |     | {α1,...,αn,β1,...,βn |     |     | }   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
order to describe the min-sum algorithm, we need to redefine All nodes have labels from the set
Φαi ,Φβj , 1≤i,j ≤n, as follows: according to the following recursive rule: (a) root has label
|      |                      |         |           |     |                  |          |         | αi; (b)  | the n        | children | of the root                    | αi have | labels | β1,...,βn; |     |
| ---- | -------------------- | ------- | --------- | --- | ---------------- | -------- | ------- | -------- | ------------ | -------- | ------------------------------ | ------- | ------ | ---------- | --- |
|      | Φαi =[wi1,...,win]t, |         |           | Φβj | =[w1j,...,wnj]t. |          |         |          |              |          |                                |         |        |            |     |
|      |                      |         |           |     |                  |          |         | and (c)  | the children | of       | each non-leaf                  | node    | whose  | parent     | has |
|      |                      |         |           |     |                  |          |         | label αr | (or          | βr) have | labels α1,...,αr−1,αr+1,...,αn |         |        |            | (or |
| Now, | the                  | min-sum | algorithm | is  | exactly          | the same | as max- |          |              |          |                                |         |        |            |     |
β1,...,βr−1,βr+1,...,βn).
|         |         |               |                |          |         |          |     |            |        |             | The      | edgebetween |       | nodeslabeled  |     |
| ------- | ------- | ------------- | -------------- | -------- | ------- | -------- | --- | ---------- | ------ | ----------- | -------- | ----------- | ----- | ------------- | --- |
| product | with    | the equations |                | (6), (7) | and (8) | replaced | by: |            |        |             |          |             |       | ≤             | ≤   |
|         |         |               |                |          |         |          |     | αi,βj      | in the | tree is     | assigned | weight wij  | for   | 1 i,j         | n.  |
| (a)     | Replace | (6) by        | the following. |          |         |          |     |            |        |             |          |             |       |               |     |
|         |         |               |                |          |         |          |     | Examplesof |        | such a tree | for n=3  | are         | shown | in the Figure | 1.  |
(cid:9)
w i f r = i N ot e 4 . T k is o f t en c a lle d t h e l ev el-k u n wr a p p e d g r a p h
|     |     | m0    | (r)= | ij  |     |     | (9) |     | α   |     |     |     |     |     |     |
| --- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | αi→βj |      |     |     |     |     |     | i   |     |     |     |     |     |     |
0 ot h e rw is e at n od e α i co rre s p o ndi n g t o t h e G M und e r c o n s id er a ti o n .
(cid:9) The unwrapped graph in general is constructed by replicating
|     |     | m0  |     | w ji | i   | f r = i |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(r)= (10) thepairwisecompatibilityfunctionsψαiβj (r,s)andpotentials
|     |         | βi→αj  |                | 0   | ot h | e rw is | e   |               |      |        |             |                 |       |              |          |
| --- | ------- | ------ | -------------- | --- | ---- | ------- | --- | ------------- | ---- | ------ | ----------- | --------------- | ----- | ------------ | -------- |
|     |         |        |                |     |      |         |     | φαi (r),φβj   | (s), | while  | preserving  | the             | local | connectivity | of       |
|     |         |        |                |     |      |         |     | the (possibly |      | loopy) | graph. They | are constructed |       | so           | that the |
| (b) | Replace | (7) by | the following. |     |      |         |     |               |      |        |             |                 |       |              |          |
(cid:10) (cid:1) (cid:11) messages received by node αi after k iterations in the actual
M k = Ψt ∗ ( M k − 1 )+Φαi graph are equivalent to those that would be received by the
|     | α   | i→βj |     | αiβj |     | β → αi |     |        |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | ---- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |     |      |     |      |     | l      |     | rootαi |     |     |     |     |     |     |     |
(cid:10) l(cid:4)=j (cid:11) intheunwrappedgraph,ifthemessagesarepassedup
|     |     |     |     |     | (cid:1) |     |     |     |     |     |     |     |     | k   |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k Ψt k − 1 a lo n g th e t re e f ro m th e l e av e s t o t h e r o ot . Le t t (r) b e t h e
|     | M   |     | =   | ∗ ( | M   | )+Φβi | (11) |     |     |     |     |     |     | α i |     |
| --- | --- | --- | --- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
β i→αj αiβj α l → βi w ei g ht o f m a xi m u m w ei g h t m a t ch i n g i n T k w h ic h us e s t h e
αi
l(cid:4)=j
edge(αi,βr)attheroot.Here,weconsideronlythematchings
|     |     |     |     |     |     |     |     | on the | tree under | which | all | non-leaf | nodes | of T k | are the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ----- | --- | -------- | ----- | ------ | ------- |
1Notethat,asdefined,πk neednotbeamatching. Theorem1showsthat α i
| forlargeenoughk,πk |     |             |     |                |     |           |     | endpoints | of  | exactly one | edge. |     |     |     |     |
| ------------------ | --- | ----------- | --- | -------------- | --- | --------- | --- | --------- | --- | ----------- | ----- | --- | --- | --- | --- |
|                    |     | isamatching |     | andcorresponds |     | totheMWM. |     |           |     |             |       |     |     |     |     |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:10:02 UTC from IEEE Xplore.  Restrictions apply.

α1
weight is more than Λ and which connects (αi,β π∗(i) ) at the
β
(cid:0) (cid:0)
(cid:0)
(cid:1) (cid:1)
(cid:1)
(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1)
1
(cid:0) (cid:0)
(cid:0)
(cid:1) (cid:1)
(cid:1)
(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1)
β
(cid:0) (cid:0)
(cid:0)
(cid:1) (cid:1)
(cid:1)
(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1)
2
(cid:0) (cid:0)
(cid:0)
(cid:1) (cid:1)
(cid:1)
(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0)
(cid:0)
(cid:1) (cid:1)
(cid:1)
(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1)(cid:0) (cid:0)
(cid:0)
(cid:1) (cid:1)
(cid:1) β
(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1)
3
(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1)
roo
C
t
o
i
n
n
s
s
i
t
d
e
e
a
r
d
p
o
a
f
th
(α
s
i
P
,
(cid:5)
β
,
π∗
(cid:7)
(i
≥
1) )
0
,
,
th
th
u
a
s
t
c
c
o
o
n
n
t
t
r
a
a
i
d
n
ic
e
t
d
in
g
g
es
w
f
i
r
t
o
h
m
(1
m
3)
a
.
tch-
α(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 2 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) α(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 3 α(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 2 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) α(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 3 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) α(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 2 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) α(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 3 ings2π∗ andΛalternativelyonthetreeT α k i definedasfollows.
Let α0 = root αi, i0 = i and P1 = (α0) be a single vertex
(a)
path. Let P2 = (β π∗(i0) ,α0,β π∗(i1) ), where i1 is such that
α1
α0 = αi is connected to βπ∗i1 under Λ. For r ≥ 1, define
P2r+1 and P2r+2 recursively as follows:
β1 β2 β3
α (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 2 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1)(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) α (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 3 α (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 2 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1)(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) α (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 3 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) α (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 2 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1)(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) α (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 3 P2r+2 P = 2r+ (β 1 π = ∗(i ( − α r i ) − , r P , 2 P r+ 2r 1 , , α β i π r ∗ ) ( , ir+1) )
(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) β(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 2 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) β (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 3 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) β(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 2 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) β (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 3β(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 1 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) β (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 3β(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 1 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) β (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 3 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) β(cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 1 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) β (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 2 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) β (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 1 (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) β (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) (cid:0) (cid:0) (cid:0) (cid:1) (cid:1) (cid:1) 2 whereαi−r isthenodeatlevel2r towhichtheendpointnode
(b) β π∗(i−r+1) of path P2r is connected to under Λ, and ir+1
Fig.1. Whenn=3(a)isT α 1 i and(b)isT α 2 i . i β s π∗ s ( u i c r+ h 1) th u a n t d α e i r r Λ a . t N le o v te el th 2 a r t, ( b p y ar d t e o fi f n P iti 2 o r n + , 1 s ) u i c s h c p o a n t n h e s c P te (cid:5) d fo to r
(cid:7)≤k existsincethetreeTk hask+1levelsandcansupport
αi
a path of length at most 2k as defined above.
Now, we state two important lemmas that will lead to the Now consider the path Pk of length 2k. It’s edges are
proof of Theorem 1. The first presents an important charac- alternately from Λ and π∗. Let us refer to the edges of Λ
terization of the min-sum algorithm while the second lemma as the Λ-edgesof Pk. Replacingthe Λ-edgesof Pk with their
relates the maximum weight matching over the unwrapped complement in Pk produces a new matching Λ(cid:6) in T
α
k
i
; this
tree-graph and the MWM in Kn,n. follows from the way the paths are constructed.
Lemma 1: At the end of the kth iteration of the min-sum Lemma 3: TheweightofmatchingΛ(cid:6)isstrictlyhigherthan
[ a 2 lg tk α o i r ( it 1 h ) m . , .. t 2 h t e k αi b ( e n li ) e ] f t. at node αi of Kn,n is precisely bk αi = T th h a i t s o c f o Λ mp o l n ete tr s ee th T e α k p i r . oof of Lemma 2 since Lemma 3 shows
2n
L
w
e
∗
mma 2: If π∗ is the MWM of graph Kn,n then for k > that Λ is not the maximum weight matching on T
α
k
i
, leading
we have to a contradiction.
(cid:4)
Now, we provide the proof of Lemma 3.
π∗(i)=argmax{tk (r)}.
r αi Proof:[Lemma3]Itsufficestoshowthatthetotalweight
oftheΛ-edgesislessthanthetotalweightoftheircomplement
Thatis, fork largeenough,the maximumweightmatchingin
T α k i chooses the edge (αi,β π∗(i) ) at the root. i P n (cid:6) P c k a . n C b o e n d s e id c e o r m t p h o e se p d ro i j n e t c o tio a n un P i k o (cid:6) n of of P a k s i e n t t o h f e si g m ra p p le h c K yc n l , e n s .
Proof:[Theorem1]Considerthemin-sumalgorithm.Let k
bk = [bk (1),...,bk (n)]t. Recall that πk = (πk(i)) where {C1,C2,...,Cm } and at most one even length path Q of
k π α k > i (i) 2n = w∗ α a , i r π g k m = ax π r ∗ { . b α k α i i (r)}. Then, by Lemmas 1 and 2, for l v e e n r g ti t c h es at an m d o t s h t e 2 l n en . g S t i h nc o e f P ea k ch is s 2 im k, ple cycle has at most 2n
(cid:4)
2k k
Next, we present the proofsof Lemmas1 and 2 in that order. m≥ = . (14)
Proof: [Lemma 1] It is known [15] that under the min- 2n n
t
s
h
u
e
m
c
(
o
o
r
r
re
m
ct
ax
m
-p
ar
r
g
o
i
d
n
u
a
c
l
t
s
)
f
a
o
lg
r
o
th
ri
e
th
r
m
oo
,
t
th
α
e
i
v
o
e
f
ct
t
o
h
r
e
bk
α M i A
co
P
rr
a
e
s
s
s
p
ig
o
n
n
m
ds
e
t
n
o
t ma
C
tc
o
h
n
i
s
n
i
g
de
π
r
(cid:6)
o
i
n
n
e
K
o
n
f
,
t
n
he
a
s
s
e
fo
si
l
m
lo
p
w
le
s:
c
(
y
i)
cl
F
e
o
s,
r
s
α
a
l
y
∈
C
C
s.
s,
C
s
o
e
n
l
s
e
t
c
r
t
u
e
c
d
t
g
th
e
e
s
o fu n nc th ti e on G s M fo c r o c r e re t s h p e on M di A ng P to as T si α g k i n . m T e h n e t p o a n irw th is is e c tr o e m e p t a o tib b i e lity a i p n r c o i p d e e r n ty t o o n f t α he l p th a a th t b P e k lo t n h g at to co Λ nt . ai S n u s c C h s. ed ( g ii e ) s F e o x r is α t l b ∈/ y C th s e ,
matching. Now, each edge has two endpoints and hence its connect it according to π∗, that is, add the edge (αl,β π∗(l) ).
weight is counted twice in the weight of matching. Now π(cid:6) (cid:3)= π∗ by construction. Since the MWM is unique,
Next consider the jth entry of bk , bk (j). By definition, it the definition of (cid:6) gives us
αi αi
corresponds to the MAP assignment with the value of αi at Wπ(cid:2) ≤Wπ∗ −(cid:6).
the root being j. That is, (αi,βj) edge is chosen in the tree
t
a
o
t t
2
h
t
e
k αi
r
(
o
j
o
)
t
.
. From the above discussion, bk αi (j) must be equal B
no
u
n
t,
-Λ
W
-e
π
d
∗
g
−
es
W
of
π
C
(cid:2)
s
is
m
e
i
x
n
a
u
c
s
tly
the
eq
t
u
o
a
ta
l
l
t
w
o
e
t
i
h
g
e
ht
to
o
t
f
al
th
w
e
e
Λ
ig
-
h
e
t
dg
o
e
f
s
th
o
e
f
Proof:[Lemma2]We provethelemmabycontradiction. Cs. Thus,
Assume to contrary that for some k >
2nw∗
,
(cid:4) weight of Λ-edges of C s −weight of rest of C s =
π∗(i)(cid:3)=argmaxtk (r)= (cid:5)ˆi, for some i. (13) −(Wπ∗ −Wπ(cid:2)) ≤ −(cid:6). (15)
r
αi
T w h h e o n s , e le w t e ˆi ig = ht π i ∗ s ( t i k α 1 i ) (ˆ f i o ). r W i1 e (cid:3)= w i i . ll L m et o Λ dif b y e Λ the an m d a fi tc n h d in Λ g (cid:6) o w n h T o α s k e i i tr n e 2 e K T T n h α e , k n i m . o a H r tc e t h n h i c e n e g t , re π w e ∗ h T e i n s α k i d w e d e fi e n r p e e e d f n e d r o i n t n o g K ‘ o e n n d ,n g t e h b s e u o t c f o c n a m n te a x b tc t e . hi n n a g tu π ra ∗ ll ’ y ,w pr e oj m ec e t a e n dt e o dg th e e s
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:10:02 UTC from IEEE Xplore. Restrictions apply.

α1 β1 α1 β1 arerequiredintheworstcase,forfinitew∗ and(cid:6),thealgorithm
α2 β2 α2 β2 requiresO(n3)operationsatthemost.Thisiscomparablewith
α3 β3 α3 β3 thebestknownMWM algorithm.Furthermore,thedistributed
(a) (b) nature of the max-product algorithm makes it particularly
α1 suitable for networking applications like switch scheduling
β1
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
β
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) 2(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
β3
w
fin
h
F
d
e
u
i
r
n
e
tu
g
s
r
t
c
e
h
a
e
w
la
M
o
b
r
i
W
l
k
it
M
y
wi
i
l
s
i
l
n
a
c
a
o
n
g
n
e
e
s
c
n
i
e
s
e
s
t
r
s
a
a
o
l
r
f
y
g
t
r
r
p
a
y
p
r
i
o
h
n
p
,
g
e
a
r
s
t
t
o
y
o
.
u
ex
r
t
c
e
u
n
r
d
re
o
n
u
t
r
ar
r
g
e
u
s
m
ul
e
t
n
t
t
o
s
α
β
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)2
1(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
α
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
3
2
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
1
β
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
3
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1) 3(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
α
β (cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
2
1(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
2α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
1
β
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
3
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
3
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
2α
β
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
1
1
α
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
2
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1) 3(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
1
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
α
β (cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
3
3(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
α
β
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
1
1
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1) 2(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
α
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
3
1
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
α
β (cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
3
2(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
α
β
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)
(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
1
1
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
α
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
3
2
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1) 1(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
α
β (cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
2
3α
β
1
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
1
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
α
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
2
α
α(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1) (cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
3
1
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)
(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
α
β
(cid:0)(cid:0)(cid:0)(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)(cid:1)(cid:1)(cid:1)
(cid:0)(cid:0)(cid:0) (cid:1)(cid:1)(cid:1)
2
2
d
b
s
th
t
o
o
u
a
u
d
n
n
n
ie
d
o
th
s
s
t
e
s
o
c
h
w
n
a
o
r
o
w
t
r
h
r
y
s
e
t
t
o
h
r
c
v
a
u
a
t
e
n
s
r
n
e
t
4
h
i
.
n
b
e
g
o
A
a
u
t
l
l
n
i
s
g
m
o
d
o
,
e
r
o
it
w
b
o
h
t
f
e
m
a
t
i
h
n
w
r
e
e
u
o
d
n
a
u
s
l
i
l
g
n
d
m
o
t
r
l
u
h
i
i
t
k
c
i
h
s
h
e
m
p
f
t
a
a
o
s
p
s
in
e
t
o
e
r
c
.
r
b
e
t
o
a
s
n
i
i
n
m
a
u
v
ti
l
e
g
a
r
h
t
a
i
t
o
g
e
n
e
r
End of Pk Start of Pk ACKNOWLEDGMENT
(c)
While working on this paper the first and the last author
Fig.2. Projection ofthepathP k isdecomposed to(a):pathQoflength4
and(b)cycleC 1 oflength4. were supported by Air Force grant AF F49620-01-1-0365.
REFERENCES
[1] S.M.AjiandR.J.McEliece,“TheGeneralizedDistributiveLaw,”IEEE
Since the path Q is of even length, either the first edge or the Trans.Inform.Theory,Vol.46,pp.325-343,2000.
last edge is an Λ-edge. Without loss of generality, assume it [2] S. M. Aji, G. B. Horn and R. J. McEliece, “On the Convergence of
IterativeDecodingonGraphswithaSingleCycle,”Proc.1998IEEEInt.
is the last edge. Then, let
Symp.Information Theory,Cambridge, MA,p.276,1998.
[3] D. Bertsekas and J. Tsitsiklis, “Parallel and Distributed Computation:
Q=(β
π∗(ij1 )
,αij1 ,β
π∗(ij2 )
,...,β
π∗(ijl )
,αijl ,β
π∗(ijl+1 )
).
NumericalMethods,”PrenticeHall,Englewood Cliffs,N.J.,1989.
[4] J. Edmonds and R. Karp, “Theoretical Improvements in Algorithmic
Now consider the cycle
Efficiency for Network Flow Problems,” Jour. of the ACM, Vol. 19,
pp248-264, 1972.
C =(β
π∗(ij1 )
,αij1 ,β
π∗(ij2 )
,...,β
π∗(ijl )
,αijl ,β
π∗(ij1 )
).
[5] B.J.Frey,R.Koetter,“Exactinferenceusingtheattenuated max-product
algorithm”, inAdvancedMeanFieldMethods:TheoryandPractice, ed.
AlternateedgesofC arefromthe maximumweightmatching
ManfredOpperandDavidSaad,MITPress,2000.
π∗. Hence, using the same argument as above, we obtain [6] R. G. Gallager, “Low Density Parity Check Codes,” MIT Press, Cam-
bridge,MA,1963.
w (cid:1) eight of Λ-edges of Q− (cid:1) weight of rest of Q [7] G.B.Horn,“Iterative DecodingandPseudocodewords,” Ph.D.disserta-
tion,Dept.elect. Eng.,Calif.Inst.Technol.,Pasadena, CA,1999.
= w − w
ijr π∗(ijr+1 ) ijr π∗(ijr ) [8] S.Lauritzen, “Graphical models,”OxfordUniversity Press,1996.
1≤r≤l 1≤r≤l [9] E.Lawler,“Combinatorial Optimization: NetworksandMatroids”,Holt,
≤ −(cid:6)+|w
ijl π∗(ij1 )
|+|w
ijl π∗(ijl+1 )
|
[10]
R
N
in
.
eh
M
ar
c
t
K
a
e
n
o
d
w
W
n,
in
V
st
.
on
A
,
n
N
an
ew
tha
Y
ra
o
m
rk,
a
1
n
9
d
76
J
.
. Walrand, “Achieving 100 %
≤ −(cid:6)+2w∗. (16) Throughput in an Input-Queued Switch,” Infocom, Vol. 1, pp 296-302,
1996.
From(14)-(16),weobtainthatformatchingsΛ(cid:6) andΛinTk : [11] J. Pearl, “Probabilistic Reasoning in Intelligent Systems: Networks of
αi
Plausible Inference,” SanFrancisco, CA:MorganKaufmann,1988.
weight of Λ−weight of Λ(cid:2) ≤ −(m+1)((cid:6))+2w∗ [12] T. Richardson and R. Urbanke, “The Capacity of Low-Density Parity
Check Codes under Message-Passing Decoding,” IEEE Trans. Info.
k
≤ − (cid:6)+2w∗ <0. (17) Theory,Vol.47,pp599-618,2001.
n [13] M. Wainwright, T. Jaakkola and A. Willsky, “Tree Consistency and
Bounds on the Performance of the Max-Product Algorithm and its
This completes the proof of Lemma 3.
Generalizations,” Statistics andComputing, Vol.14,pp143-166,2004.
[14] M. Wainwright, M. Jordan, “Graphical models, exponential families,
IV. DISCUSSION AND CONCLUSION
andvariationalinference,”Tech.Report,Dept.ofStat.,UniversityofCal.,
In this paper, we proved that the max-product algorithm Berkeley, 2003.
[15] Y.Weiss,“Beliefpropagationandrevisioninnetworkswithloops,”MIT
convergesto the desirable fixedpointin the contextof MWM
AILab.,Tech.Rep.1616,1997.
for bipartite graph, even in the presence of loops. This result [16] Y. Weiss, “Correctness of local probability propagation in graphical
has a twofold impact. First, it will possibly open avenues modelswithloops,”NeuralComput.,Vol.12,pp.1-42,2000.
[17] Y.WeissandW.Freeman,“Correctness ofbeliefpropagation inGaus-
fordemystificationofthe max-productalgorithm.Second,the
sian graphical models of arbitrary topology,” Neural Comput., Vol. 13,
same approach may provably work for other combinatorial Issue10,pp2173-2200, 2001
optimization problems and possibly lead to better algorithms. [18] Y. Weiss W. Freeman, “On the optimality of solutions of the max-
product belief propagation algorithm in arbitrary graphs.,” IEEE Trans.
Though, the algorithm described in the paper may seem
Info.Theory,Vol.47,pp736-744, 2001.
complicated, we have managed to simplify3 it using the [19] J.Yedidia,W.FreemanandY.Weiss,“GeneralizedBeliefPropagation,”
regularity of the structure of the problem. In the simpli- MitsubishiElect. Res.Lab.,TR-2000-26,2000.
[20] J.Yedidia,W.FreemanandY.Weiss,“UnderstandingBeliefPropagation
fied algorithm, each node needs to perform O(n) addition-
anditsGeneralizations,” MitsubishiElect.Res.Lab.,TR-2001-22,2000.
subtraction operationsin each iteration. Since O(n) iterations
4A key fact in the proof of lemma was the property that bipartite graphs
3Moredetails willappearinatechnical report donothaveoddcycles.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:10:02 UTC from IEEE Xplore. Restrictions apply.