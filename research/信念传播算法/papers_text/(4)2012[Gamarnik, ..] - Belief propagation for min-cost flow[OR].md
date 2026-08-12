| O         |     | R       |     |     |     |     |     |     |     |     |     |
| --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PERATIONS |     | ESEARCH |     |     |     |     |     |     |     |     |     |
Vol.60,No.2,March–April2012,pp.410–428
ISSN0030-364X(print)(cid:151)ISSN1526-5463(online)
http://dx.doi.org/10.1287/opre.1110.1025
©2012INFORMS
|     | Belief |     | Propagation |     |     | for | Min-Cost    | Network |     | Flow: |     |
| --- | ------ | --- | ----------- | --- | --- | --- | ----------- | ------- | --- | ----- | --- |
|     |        |     | Convergence |     |     | and | Correctness |         |     |       |     |
 .devreser sthgir lla ,ylno esu lanosrep roF . 65:71 ta ,5202 lirpA 61 no ]91.112.052.121[ yb gro.smrofni morf dedaolnwoD
|     |     |     |     |     |     | David Gamarnik |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
OperationsResearchCenterandSloanSchoolofManagement,MassachusettsInstituteofTechnology,
Cambridge,Massachusetts02139,gamarnik@mit.edu
|     |     |     |     |     |     | Devavrat | Shah |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ---- | --- | --- | --- | --- |
LaboratoryforInformationandDecisionSystems(LIDS)andOperationsResearchCenter,DepartmentofEECS,
MassachusettsInstituteofTechnology,Cambridge,Massachusetts02139,devavrat@mit.edu
|     |     |     |     |     |     | Yehua | Wei |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
OperationsResearchCenter,MassachusettsInstituteofTechnology,Cambridge,Massachusetts02139,
y4wei@mit.edu
Distributed, iterative algorithms operating with minimal data structure while performing little computation per iteration
are popularly known as message passing in the recent literature. Belief propagation (BP), a prototypical message-passing
algorithm, has gained a lot of attention across disciplines, including communications, statistics, signal processing, and
machinelearningasanattractive,scalable,general-purposeheuristicforawideclassofoptimizationandstatisticalinference
problems.Despiteitsempiricalsuccess,thetheoreticalunderstandingofBPisfarfromcomplete.
WiththegoalofadvancingthestateofartofourunderstandingofBP,westudytheperformanceofBPinthecontextof
the capacitated minimum-cost network flow problem—a cornerstone in the development of the theory of polynomial-time
algorithms for optimization problems and widely used in the practice of operations research. As the main result of this
paper, we prove that BP converges to the optimal solution in pseudopolynomial time, provided that the optimal solution
of the underlying network flow problem instance is unique and the problem parameters are integral. We further provide
a simple modification of the BP to obtain a fully polynomial-time randomized approximation scheme (FPRAS) without
requiringuniquenessoftheoptimalsolution.ThisisthefirstinstancewhereBPisprovedtohavefullypolynomialrunning
time.OurresultsthusprovideatheoreticaljustificationfortheviabilityofBPasanattractivemethodtosolveanimportant
classofoptimizationproblems.
|     | Subjectclassifications: |     | beliefpropagation;networkflow;graphicalmodel. |     |     |     |     |     |     |     |     |
| --- | ----------------------- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Areaofreview:           |     | Optimization.                                 |     |     |     |     |     |     |     |     |
History: ReceivedDecember2009;revisionsreceivedAugust2010,June2011;acceptedAugust2011.
1. Introduction thought of as a weighted combinatorial counting problem
Message passing has emerged as canonical algorithmic (e.g., counting the number of independent sets of a graph
|              |     |              |     |              |              |     | is a special | case of | this problem). | The second problem | is  |
| ------------ | --- | ------------ | --- | ------------ | ------------ | --- | ------------ | ------- | -------------- | ------------------ | --- |
| architecture |     | to deal with | the | scale of the | optimization | and |              |         |                |                    |     |
thatoffindingthemodeofadistribution,i.e.,anassignment
| inference | problems |     | arising | in the context | of  | variety of |     |     |     |     |     |
| --------- | -------- | --- | ------- | -------------- | --- | ---------- | --- | --- | --- | --- | --- |
withthemaximumlikelihood(ML).Foraconstrainedopti-
| disciplines, | including |             | communications, | networks,    |         | machine |                        |     |          |                        |     |
| ------------ | --------- | ----------- | --------------- | ------------ | ------- | ------- | ---------------------- | --- | -------- | ---------------------- | --- |
|              |           |             |                 |              |         |         | mization(maximization) |     | problem, | whenthe constraintsare |     |
| learning,    | image     | processing, |                 | and computer | vision, | signal  |                        |     |          |                        |     |
processing, and statistics. The Belief Propagation (BP) is modeled through a graphical model and probability is pro-
|                   |     |           |     |             |              |     | portional | to the cost | of the assignment, | an ML assignment |     |
| ----------------- | --- | --------- | --- | ----------- | ------------ | --- | --------- | ----------- | ------------------ | ---------------- | --- |
| a message-passing |     | heuristic |     | for solving | optimization | and |           |             |                    |                  |     |
inference problems in the context of the graphical model. isanoptimalsolutiontotheoptimizationproblem.Bothof
The graphical model or a Markov random field provides a these questions, in general, are computationally hard either
inthe#PorNP-completesense.
| succinct | representation |     | for capturing | the | dependency | struc- |     |     |     |     |     |
| -------- | -------------- | --- | ------------- | --- | ---------- | ------ | --- | --- | --- | --- | --- |
ture between a collection of random variables. In recent Belief Propagation (BP) is an “umbrella” message-pass-
ingheuristicdesignedforthesetwoproblems.Itsversionfor
years,theneedforlarge-scalestatisticalinferenceandopti-
mization has made graphical models the representation of the first problem is known as the “sum-product algorithm”
choiceinavarietyofapplications.Therearetwokeyprob- andforthesecondproblemisknownasthe“max-product”
lems for a graphical model of interest. The first problem is or“min-sumalgorithm.”BothversionsoftheBPalgorithm
the computation of marginal distribution of a random vari- are iterative, easy to implement, and distributed in nature.
able. This problem is (computationally) equivalent to the When the underlying graph is a tree, the BP algorithm
computation of the so-called partition function and can be essentially performs the dynamic programming recursion
410

| Gamarnik,Shah,andWei: |     |     | BeliefPropagationforMin-CostNetworkFlow |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
411
OperationsResearch60(2),pp.410–428,©2012INFORMS
(Gallager 1963, Yedidia et al. 2002, Pearl 1988) and, as a requires maintaining a vector of real-valued functions that
result, leads to a correct solution both for the optimization may require an infinite amount of memory to store and
and inference problems. Specifically, BP provides a natu- computation to update. Then we provide a proof to show
ral parallel iterative version of the dynamic programming that BP finds the optimal solution in pseudopolynomial
in which variable nodes pass messages between each other time,providedthattheoptimalsolutionisunique.Next,we
alongedgesofthegraphicalmodel.Somewhatsurprisingly, presentasimplemodificationoftheBPalgorithmthatgives
thisseeminglynaiveBPheuristichasbecomequitepopular afullypolynomial-timerandomizedapproximationscheme
 .devreser sthgir lla ,ylno esu lanosrep roF . 65:71 ta ,5202 lirpA 61 no ]91.112.052.121[ yb gro.smrofni morf dedaolnwoD
in practice, even for graphical models that do not have the (FPRAS) for the same problem, which no longer requires
tree structure (Aji and McEliece 2000, Horn 1999, Mezard the uniqueness of the optimal solution. This is the first ins-
et al. 2002, Richardson and Urbanke 2001). In our opin- tancewhereBPisprovedtohavefullypolynomialrunning
ion, there are two primary reasons for the popularity of time, except for the case when the underlying graph is a
BP. First, it is generically applicable, easy to understand, tree and BP solves the problem exactly. The modification
andimplementationfriendlyduetoitsiterative,simple,and of BP is obtained by applying a novel lemma; it is a nat-
message-passing nature. Second, in many practical scenar- ural generalization of the so-called Isolation Lemma found
ios,theperformanceofBPissurprisinglygood(Weissand inMulmuleyetal.(1987).UnliketheIsolationLemma,our
Freeman 2001, Yedidia et al. 2002). On one hand, for an lemma can be used for generic LP. In essence, we show
optimistthisunexpectedsuccessofBPprovidesahopefor that it is possible to perturb the cost of any LP using little
it being a genuinely much more powerful algorithm than randomness so that the resulting modified LP has a unique
what we know thus far (e.g., better than primal-dual meth- solutionthatisagoodapproximationtotheoriginalLP,and
ods).Ontheotherhand,askepticwoulddemandasystem- itsgaptothenextoptimalsolutionislargeenough.Indeed,
atic understanding of the limitations (and strengths) of BP this is a general method and can be useful in a variety
in order to caution a practitioner. Thus, irrespective of the of applications, including improving performance of dis-
perspectiveofanalgorithmictheorist,rigorousunderstand- tributedalgorithms;itisnosurprisethatithasalreadybeen
ing of BP is very important. used in a subsequent work (Kanoria et al. 2011).
| Despite | the | apparent | empirical | success |     | of the | BP algo- |     |     |     |     |     |     |     |
| ------- | --- | -------- | --------- | ------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
rithm for solving a variety of problems, theoretical under- 1.2. Prior Work on BP
| standing | of BP          | is far | from   | complete.   | In  | this            | paper, our |         |                |     |         |           |          |      |
| -------- | -------------- | ------ | ------ | ----------- | --- | --------------- | ---------- | ------- | -------------- | --- | ------- | --------- | -------- | ---- |
|          |                |        |        |             |     |                 |            | Despite | the compelling |     | reasons | explained | earlier, | only |
| interest | lies primarily |        | in the | correctness |     | and convergence |            |         |                |     |         |           |          |      |
recentlywehavewitnessedanexplosionofresearchforthe-
| properties       | of the | min-sum | version |          | of BP | when       | applied to |          |               |            |                 |     |              |       |
| ---------------- | ------ | ------- | ------- | -------- | ----- | ---------- | ---------- | -------- | ------------- | ---------- | --------------- | --- | ------------ | ----- |
|                  |        |         |         |          |       |            |            | oretical | understanding | of         | the performance |     | of the BP    | algo- |
| the minimum-cost |        | network | flow    | problems |       | (or simply | min-       |          |               |            |                 |     |              |       |
|                  |        |         |         |          |       |            |            | rithm in | the context   | of various | combinatorial   |     | optimization |       |
cost flow)—an important class of linear (or more generally problems,bothtractableandintractable(NP-hard)versions.
| convex) | optimization |     | problems. | As        | a secondary    |     | interest, |            |             |     |         |        |            |      |
| ------- | ------------ | --- | --------- | --------- | -------------- | --- | --------- | ---------- | ----------- | --- | ------- | ------ | ---------- | ---- |
|         |              |     |           |           |                |     |           | In earlier | work, Weiss | and | Freeman | (2001) | identified | cer- |
| we wish | to bring     | BP  | to the    | attention | of researchers |     | in the    |            |             |     |         |        |            |      |
tainlocaloptimalitypropertiesoftheBP(max-product)for
| operations  | research | (OR)     | community, |              | thereby |         | improving |                |            |             |      |             |             |        |
| ----------- | -------- | -------- | ---------- | ------------ | ------- | ------- | --------- | -------------- | ---------- | ----------- | ---- | ----------- | ----------- | ------ |
|             |          |          |            |              |         |         |           | arbitrary      | graphs. It | implies     | that | when a      | graph has   | a sin- |
| the current | state    | in which | BP         | has remained |         | elusive | in OR.    |                |            |             |      |             |             |        |
|             |          |          |            |              |         |         |           | gle cycle,     | then the   | fixed point | of   | max-product | corresponds |        |
|             |          |          |            |              |         |         |           | to the correct | answer.    | However,    |      | they do     | not provide | any    |
1.1. Contributions
|     |     |     |     |     |     |     |     | guarantee | onthe convergence |     | ofmax-product. |     | Bayatiet | al. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------------- | --- | -------------- | --- | -------- | --- |
As the main contribution of this paper, we establish that (2008a) considered the performance of BP for finding the
BPconvergestotheoptimalsolutionofamin-costnetwork maximumweightmatchinginabipartitegraph.Theyestab-
flow problem in pseudopolynomial time, provided that the lished that BP converges in pseudo polynomial time to the
optimal solution of the underlying problem is unique and optimalsolutionwhentheoptimalsolutionisunique(Bayati
theprobleminputisintegral.Atthesametime,itisknown et al. 2008a). Bayati et al. (2008b), as well as Sanghavi
(Sanghavietal.2009)thatBPfailstoconvergeforthegen- et al. (2007), generalized this result by establishing the
erallinearprogramming(LP)problembymeansofacoun- correctness and convergence of the BP algorithm for the
terexample. Thus, our results extend, in an important way, b-matching problem when the linear programming relax-
thescopeoftheproblemsthatareprovablysolvablebythe ation corresponding to the node constraints has a unique
BPalgorithm.Wealsopointoutthatidentifyingthebroad- integral optimal solution. Note that the LP relaxation cor-
est class of optimization problems solvable using the BP responding to the node constraints is not tight in general,
algorithmisaninterestingopenproblem.Indeed,resolution because inclusion of the odd-cycle elimination constraints
of it will lead to the precise understanding of the structure (Schrijver 2003) is essential. Furthermore, Bayati et al.
of optimization problems that are solvable by BP. (2008b) and Sanghavi et al. (2007) established that the BP
The contributions of this paper, in detail, are as fol- doesnotconvergeifthisLPrelaxationdoeshaveanoninte-
lows. First, we show that an exact version of BP can be gral solution. Thus, for a b-matching problem, BP finds an
implemented for the min-cost flow problems by encoding optimalanswerwhentheLPrelaxationcanfindanoptimal
each message in BP as a piecewise-linear convex function. solution.Inthecontextofthemaximumweightindependent
This is significant because the natural formulation of BP setproblem,aone-sidedrelationbetweenLPrelaxationand

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
412 OperationsResearch60(2),pp.410–428,©2012INFORMS
BP is established (Sanghavi et al. 2009); if BP converges, It is worth comparing the running time of the BP
then it is correct, and LP relaxation is tight. In Sanghavi algorithm that we have obtained for (cid:77)(cid:67)(cid:70). The basic ver-
et al. (2009), a counterexample was produced that shows sion of BP takes (evaluated under decentralized compu-
thatBPdoesnotconvergetotheoptimalsolutionofanLP. tation model) O(cid:52)C3mn4logn(cid:53) computation (C represents
This seem to suggest that BP is unlikely to solve all forms the largest cost) in total. The modified FPRAS version
ofLP. of BP algorithm requires O(cid:52)(cid:152)−3n8m7logn(cid:53) computation in
Beyond LP, the performance of BP for quadratic optimi- total on average (w.r.t. decentralized computation model)
zation problems (QP) and, more generally, convex optimi- forobtaining(cid:52)1+(cid:152)(cid:53)approximation.Itshouldbenotedthat
zation problems (CP) have recently been studied. The the number of iterations required by the algorithm scales
conditionsforcorrectnessandconvergenceofBPinthecon- as nL where L is the maximal cost of a directed path.
textofinferenceinGaussiangraphicalmodelssuchasthose It is clear from the comparison that the bounds implied
establishedbyMalioutovetal.(2006)leadtosufficientcon- by our results for BP are not competitive with respect
ditionsforwhenBPcansolve(acertainclassof)QP.More to the best known results for (cid:77)(cid:67)(cid:70). BP’s performance is
recently, in a sequence of works, Moallemi and Van Roy evaluated for the decentralized model, whereas the above
(2007, 2009) have identified sufficient conditions under reported computation time analysis for other algorithms
whichBPconvergestocorrectsolutionforconvexoptimiza- is for the centralized model. Indeed, some of the known
tion problems. It is worth identifying the differences bet- algorithmscanbeimplementedinthedecentralizedmodel,
weenresultsofthispaperandthatofMoallemiandVanRoy such as that of Bertsekas (1986) and Goldberg and Tarjan
(2007, 2009). To start with, our work applies to the cons- (1987) (see Ahuja et al. 1993, Chapters 10–12 for further
trainedmin-costnetworkflowLP,whereasthatofMoallemi details). The analysis of BP for (cid:77)(cid:67)(cid:70), when specialized
and Van Roy (2007, 2009) applies to the unconstrained to specific instances of (cid:77)(cid:67)(cid:70) like the bipartite matching
convexoptimizationproblem.Whereastheconstrainedmin- problem,leadstotighterperformanceboundsthatarecom-
costnetworkflowLPcanbeseenasanunconstrainedcon- petitive with respect to the best known results (see §4.2,
vex optimization problem (e.g., via Lagrangian relaxation), Theorem4.14).However,theimportantthingisthatBPisa
the resulting convex optimization is not strictly convex, general-purpose algorithm, not specialized for the problem
and hence sufficient conditions (the diagonal dominance at hand like the best known algorithm for (cid:77)(cid:67)(cid:70). For this
of Hessian) of Moallemi and Van Roy (2007, 2009) are reason, BP is highly desirable from an implementor’s per-
notapplicable.Indeed,theproofmethodsaredifferent,and spective because it does not require specific modifications
resultsofthispaperprovide“implementation”ofBP,unlike for the problem of interest. Finally, it should be noted that
theresultsofMoallemiandVanRoy(2007,2009).Wealso the BP algorithm can operate in an asynchronous decen-
take note of a work by Ruozzi and Tatikonda (2008) that tralized environment, unlike most known algorithms.
utilizesBPtofindsource-sinkpathsinthenetwork.
1.4. Organization
1.3. Prior Work on Min-Cost Network Flow
The rest of the paper is organized as follows. In §2,
The min-cost network flow problem ((cid:77)(cid:67)(cid:70)) has been we introduce the BP algorithm as an iterative heuristic for
fundamental in the development of the theory of poly- a generic optimization problem. We provide an intuitive
nomial-time algorithms for optimization problems. The explanation by means of an example of how BP is derived
first polynomial-time algorithm for (cid:77)(cid:67)(cid:70) was developed asaniterativeheuristicforthegenericprobleminspiredby
by Edmonds and Karp (1972) with a running time of parallelimplementationofdynamicprogrammingonatree-
O(cid:52)m(cid:52)logU(cid:53)(cid:52)m+nlogn(cid:53)(cid:53), where m represents the num- likeproblemstructure.In§3,wespecializetheBPforlinear
ber of edges, n represents the number of nodes, and U the programming(LP).Werecalla(counter-)exampleofanLP
largest capacity of an arc. Subsequently, the first strongly forwhichBPcannotfinditsoptimalsolution.In§4,wefur-
polynomial-timealgorithmwasproposedbyTardos(1985). therspecializetheBPalgorithmforthecapacitatedmin-cost
Because(cid:77)(cid:67)(cid:70)hasbeencentraltothedevelopmentofalgo- networkflowproblem((cid:77)(cid:67)(cid:70)).Westatethemainresultthat
rithmic theory, a wide variety of efficient algorithms have establishes pseudopolynomial time convergence of BP to
beenproposedoveryearswithdifferentvirtuessuchasRöck theoptimalsolutionof(cid:77)(cid:67)(cid:70),whentheoptimalsolutionis
(1980), Orlin (1993), Fujishige (1986), Bertsekas (1986), unique.Specifically,§4.1explainshoweachmessagefunc-
Goldberg and Tarjan (1987, 1989), Ahuja et al. (1992). tion in the BP algorithm can be computed, leading to an
Among these, the fastest polynomial-time algorithm runs efficient implementation of BP. In §4.2, we consider a sub-
(evaluated in the centralized computation model) in essen- class (cid:77)(cid:67)(cid:70)o of (cid:77)(cid:67)(cid:70) that includes the problems of min-
tially O(cid:52)n3log(cid:52)nC(cid:53)(cid:53) time (Bertsekas 1986, Goldberg and cost path, as well as bipartite matching or, more generally,
Tarjan 1989, Ahuja et al. 1992), where C is the largest b-matching.Forthissubclassof(cid:77)(cid:67)(cid:70),itturnsoutthatBP
cost of an arc. On the other hand, the fastest strongly has very simple message functions, and this subsequently
polynomial-timealgorithmfor(cid:77)(cid:67)(cid:70)runs(again,evaluated leads to a tighter bound on the running time. In §5, the
in the centralized computation model) in O(cid:52)mlogn(cid:52)m+ proofofthemainresultaboutconvergenceofBPfor(cid:77)(cid:67)(cid:70)
nlogn(cid:53)(cid:53) (Orlin 1993). isprovided.Section6presentsanextensionofourresultfor
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
65:71
ta
,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
OperationsResearch60(2),pp.410–428,©2012INFORMS 413
min-cost flow problems with piecewise-linear convex cost In the above, x =1 if and only if node i is selected in the
i
functions. In §7, we provide the running time analysis of independentset.Finally,weintroducethenotionofafactor
BPfor(cid:77)(cid:67)(cid:70)and(cid:77)(cid:67)(cid:70)o.Fromtheanalysis,weshowthat graph of a factorized optimization problem. A factor graph
BP for the min-cost flow problem is a pseudopolynomial- F of ((cid:80)) is a bipartite graph with one partition containing
(cid:80)
time algorithm when the data input is integral. In §8, we variable nodes V and the other partition containing factor
present a randomized approximation scheme for the min- nodes (cid:67) corresponding to the constraints. There is an edge
cost flow problem that uses the standard BP as a subrou- (cid:52)v(cid:49)C(cid:53)∈V×(cid:67)ifandonlyifv∈C.Forexample,thegraph
tine. We prove that for any (cid:152)∈(cid:52)0(cid:49)1(cid:53), the approximation shown in Figure 1 is the factor graph for the optimization
scheme finds a solution that is within 1+(cid:152) of the optimal problem
solution, whereas its expected running time is polynomial
in m, n, and 1/(cid:152). In doing so, we introduce a variation of (cid:18) 5 (cid:19) (cid:88)
minimize (cid:148)(cid:52)x(cid:53) +(cid:150) (cid:52)x (cid:49)x (cid:49)x (cid:53)
the Isolation Lemma for LP in §8.1. Finally, §9 presents i i 1(cid:49)2(cid:49)3 1 2 3
conclusions and directions for future work. i=1 ((cid:80)(cid:48))
+(cid:150) (cid:52)x (cid:49)x (cid:49)x (cid:53)+(cid:150) (cid:52)x (cid:49)x (cid:53)
1(cid:49)4(cid:49)5 1 4 5 1(cid:49)5 1 5
2. Belief Propagation for subject to x ∈(cid:18)(cid:49) ∀1(cid:182)i(cid:182)5(cid:48)
i
Optimization Problem
Now we introduce BP. To start with, suppose the factor
Hereweintroducethemin-sumversionofBPasaheuristic
graph F of (cid:80) is a tree (note that the factor graph in Fig-
for the optimization problem in the general form. We shall (cid:80)
ure 1 is not a tree because there is a cycle (cid:52)v (cid:49)(cid:56)1(cid:49)4(cid:49)5(cid:57)(cid:49)
utilize the notations similar to those used in Moallemi and 1
v (cid:49)(cid:56)1(cid:49)5(cid:57)(cid:49)v (cid:53)).Inthiscase,letusconsiderthedynamicpro-
Van Roy (2007, 2009). In the remainder of the paper, by 5 1
grammingalgorithm.Thedynamicprogrammingalgorithm
BP we mean its min-sum version for solving optimization
wouldsuggestcomputationofthevalueorassignmentofa
problem. To this end, consider the optimization problem
givenvariablenodei∈V intheoptimalsolutionasfollows:
minimize (cid:88) (cid:148) i (cid:52)x i (cid:53)+ (cid:88) (cid:150) C (cid:52)x C (cid:53) fixaspecificvaluez∈(cid:18)ofvariablex i correspondingtothe
variablei∈V.Subjecttox =z,computethecostofoptimal
i∈V C∈(cid:67) ((cid:80)) i
assignment for the rest of the problem, say b(cid:52)z(cid:53). Then the
subject to x ∈(cid:18)(cid:49) ∀i∈V(cid:49) i
i optimalassignmentofvariablenodeiisinargmin b(cid:52)z(cid:53).
z∈(cid:18) i
where V is a finite set of variables and (cid:67) is a finite Now to compute b(cid:52)z(cid:53) for all z∈(cid:18), the dynamic program-
i
collection of subsets of V representing constraints. Here ming would recurse the same approach on the problem
(cid:148)(cid:50)(cid:18)→(cid:18) ¯,∀i∈V and(cid:150) (cid:50)(cid:18)(cid:151)C(cid:151)→(cid:18) ¯,∀C∈(cid:67)areextended
re i al-valued functions wh C ere (cid:18) ¯ represents extended real minimize (cid:148)(cid:52)z(cid:53)+ (cid:88) (cid:148) (cid:52)x (cid:53)+ (cid:88) (cid:150) (cid:52)x (cid:53)(cid:49)
i j j C C
numbers (cid:18)∪(cid:56)(cid:136)(cid:57). We call each (cid:148)
i
a variable function, j∈V\(cid:56)i(cid:57) C∈(cid:67) (1)
each(cid:150)
C
afactorfunction,and((cid:80))afactorizedoptimization
subject to x =z(cid:49)x ∈(cid:18)(cid:49) ∀j(cid:48)
i j
problem.
It is not difficult to see that essentially any constrained Now, implementation of this recursion of dynamic pro-
optimization problem of interest can be represented as a gramingisgenerallynotstraightforwardandcanbecompu-
factorizedoptimizationproblem.Forexample,considerthe tationally expensive. However, when the factor graph F is
(cid:80)
well-known maximum-size independent set problem on a a tree, it is quite simple because the problem decomposes
simpleundirectedgraphG=(cid:52)V(cid:49)E(cid:53),whichrequiresselect- into subproblems on disconnected trees. It is the dynamic
ingsubsetV ofmaximalcardinalitysothatnotwovertices programming implementation for the tree factor graph that
of the chosen subset are neighbors of each other as per E. leads to the derivation of BP. To that end, given a node i
The factorized form of the maximum weight independent consider any constraint C such that i∈C, i.e., (cid:52)i(cid:49)C(cid:53) is an
set is given by edge in F . Because F is a tree, F \(cid:52)i(cid:49)C(cid:53) has two dis-
(cid:80) (cid:80) (cid:80)
(cid:88) (cid:88) jointcomponents,sayT andT .Withoutlossofgenerality,
minimize (cid:148)(cid:52)x(cid:53)+ (cid:150) (cid:52)x(cid:49)x (cid:53) 1 2
i i ij i j
i∈V (cid:52)i(cid:49)j(cid:53)∈E
subject to x ∈(cid:18)(cid:49) ∀i∈V(cid:49) Figure 1. An example of a factor graph.
i
{1,2,3} {1,4,5} {1,5}
where

0 if x =0
 i
(cid:148)(cid:52)x(cid:53)= −1 if x =1
i i j
(cid:136)
otherwise(cid:49)
(cid:40)
0 if x +x (cid:182)1
(cid:150) (cid:52)x(cid:49)x (cid:53)= i j
ij i j (cid:136) otherwise(cid:48) v 1 v 2 v 3 v 4 v 5
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
65:71
ta
,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
414 OperationsResearch60(2),pp.410–428,©2012INFORMS
we assume that i is contained in T and C is contained in It is easy to show by induction that if the graph underlying
1
T . Due to this division of the problem structure, b(cid:52)z(cid:53) for F is a tree, then for t larger than the diameter of the tree,
2 i (cid:80)
z∈(cid:18)or,equivalently,solutionofoptimizationproblem(1), bt(cid:52)·(cid:53) equals the value produced by the dynamic program-
i
can be computed recursively as follows. For edge (cid:52)i(cid:49)C(cid:53), mingproblem,thereforeresultingintheoptimalassignment
define “messages” m (cid:52)z(cid:53) and m (cid:52)z(cid:53) as ofx.
i→C C→i i
The parallelized implementation of the dynamic pro-
(cid:88) (cid:88)
m (cid:52)z(cid:53)= minimize (cid:148) (cid:52)x (cid:53)+ (cid:150) (cid:52)x (cid:53)(cid:49) grammingproblemdescribedby(5)and (6)canbeapplied
i→C j j D D
j∈V∩T1 D∈(cid:67)∩T1 toanyfactorgraphingeneral.ThisispreciselytheBPmin-
subject to x =z(cid:49)x ∈(cid:18)(cid:49) ∀j(cid:48) sum heuristic. The algorithm is described in detail next.
i j
For the nontree graphs the convergence and/or correctness
(cid:88) (cid:88)
m (cid:52)z(cid:53)= minimize (cid:148) (cid:52)x (cid:53)+ (cid:150) (cid:52)x (cid:53)(cid:49)
C→i j j D D of such a heuristic is by no means guaranteed in general.
j∈V∩T2 D∈(cid:67)∩T2
Algorithm 1 min-sum BP
subject to x =z(cid:49)x ∈(cid:18)(cid:49) ∀j(cid:48) i j
1: Given a factorized optimization problem ((cid:80)),
Note that two such directional “messages” can be defined construct factor graph F .
(cid:80)
for any edge in F in a similar manner because it is a tree. 2: Set N to be the number of iterations for BP.
(cid:80)
Again, invoking the tree structure of F and definition of 3: Initialize t=0, and for each edge (cid:52)i(cid:49)C(cid:53) in F ,
(cid:80) (cid:80)
“messages,” the solution of (1) can be rewritten as initialize m0 (cid:52)z(cid:53)=0=m0 (cid:52)z(cid:53) for all z∈(cid:18).
C→i i→C
4: for t=1(cid:49)2(cid:49)(cid:48)(cid:48)(cid:48)(cid:49)N do
(cid:88)
b(cid:52)z(cid:53)=(cid:148)(cid:52)z(cid:53)+ m (cid:52)z(cid:53)(cid:49) ∀z∈(cid:18)(cid:49) (2) 5: For any edge (cid:52)i(cid:49)C(cid:53) in F and z∈(cid:18), update
i i C→i (cid:80)
C∈(cid:67)i
where (cid:67) i is the set of all factor nodes (or constraints) that mt (cid:52)z(cid:53)=(cid:148)(cid:52)z(cid:53)+ (cid:88) mt−1 (cid:52)z(cid:53)(cid:49) (8)
contain i, i.e., i→C i K→i
K∈(cid:67)i\C
(cid:67) (cid:172)(cid:56)C∈(cid:67)(cid:50) i∈C(cid:57)(cid:48) mt C→i (cid:52)z(cid:53)= min (cid:150) C (cid:52)y(cid:53)+ (cid:88) mt j→C (cid:52)y j (cid:53)(cid:48) (9)
i y∈(cid:18)(cid:151)C(cid:151)(cid:49)yi=z
j∈C\i
That is, if the graph underlying F is a tree, then in order
(cid:80) 6: t(cid:50)=t+1
to compute b(cid:52)z(cid:53) it is sufficient to have knowledge of the
i 7: end for
“messages” coming towards node i from the factor nodes
8: Set the belief function as
to which it is connected. For the tree F (cid:80) , such messages bN(cid:52)z(cid:53)=(cid:148)(cid:52)z(cid:53)+ (cid:80) mN (cid:52)z(cid:53), ∀1(cid:182)i(cid:182)n.
can be recursively defined as follows: for any edge (cid:52)i(cid:49)C(cid:53) i i C∈(cid:67)i C→i
9: Estimate the optimal assignment as
in F , for any z∈(cid:18),
(cid:80) xˆN ∈argminbN(cid:52)z(cid:53) for each i∈V.
i i
(cid:88) 10: Return xˆN.
m (cid:52)z(cid:53)=(cid:148)(cid:52)z(cid:53)+ m (cid:52)z(cid:53)(cid:49) (3)
i→C i K→i
K∈(cid:67)i\C
(cid:88) 3. BP for Linear Programming
m (cid:52)z(cid:53)= min (cid:150) (cid:52)y(cid:53)+ m (cid:52)y (cid:53)(cid:48) (4) C→i C j→C j
y y ∈ i (cid:18) = (cid:151) z C(cid:151) j∈C\i Thelinearprogramming(LP)probleminthestandardform
is given by
For tree-structured F , starting from leaf nodes using
(cid:80)
(3)–(4) the “messages” m (cid:52)z(cid:53) and m (cid:52)z(cid:53) for all edges minimize cTx
i→C C→i
(cid:52)i(cid:49)C(cid:53) can be computed. A parallel implementation of this
subject to Ax=g(cid:49) ((cid:76)(cid:80))
recursive procedure is as follows. Initially, for t =0 we
set m0 (cid:52)z(cid:53)=m0 (cid:52)z(cid:53)=0 for all edges (cid:52)i(cid:49)C(cid:53) of F . For x(cid:190)0(cid:49)x∈(cid:18)n(cid:49)
C→i i→C (cid:80)
t(cid:190)1, update messages for each edge (cid:52)i(cid:49)C(cid:53) of F as
(cid:80)
where A ∈ (cid:18)m×n, g ∈ (cid:18)m, and c ∈ (cid:18)n. In the notation
mt (cid:52)z(cid:53)=(cid:148)(cid:52)z(cid:53)+ (cid:88) mt−1 (cid:52)z(cid:53)(cid:49) (5) of the factorized optimization problem introduced earlier,
i→C i K→i
K∈(cid:67)i\C variable nodes are V = (cid:56)1(cid:49)(cid:48)(cid:48)(cid:48)(cid:49)n(cid:57) with associated vari-
mt (cid:52)z(cid:53)= min (cid:150) (cid:52)y(cid:53)+ (cid:88) mt (cid:52)y (cid:53)(cid:48) (6) ables x i , i∈V; rows of A correspond to constraint nodes
C→i y y ∈ i (cid:18) = (cid:151) z C(cid:151) C j∈C\i j→C j (cid:67) (cid:56)C = (cid:50) (cid:56) a C j (cid:54)= (cid:50)1 0 (cid:182) (cid:57), j ∀ (cid:182) i∈ m V (cid:57) . w D h e e fi re ne C j fa = ct (cid:56) o i r ∈ fu V n (cid:50) ct a io ji n (cid:54)= (cid:150) 0(cid:57) (cid:50) ; (cid:18) a (cid:151) n C d j(cid:151) (cid:67) → i = (cid:18) ¯
j ji j
for 1(cid:182)j(cid:182)m as
The estimation of b(cid:52)z(cid:53) at the end of iteration t for each
i
i∈V and z∈(cid:18) is given by
 (cid:88)
0 if a z =g
 ji i j
bt(cid:52)z(cid:53)=(cid:148)(cid:52)z(cid:53)+ (cid:88) mt (cid:52)z(cid:53)(cid:48) (7) (cid:150) j (cid:52)z(cid:53)= i∈Cj
i i C→i (cid:136) otherwise(cid:48)
C∈(cid:67)i
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
65:71
ta
,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
OperationsResearch60(2),pp.410–428,©2012INFORMS 415
And define variable function (cid:148)(cid:50) (cid:18)→(cid:18) ¯ for i∈V as of (cid:77)(cid:67)(cid:70); it includes bipartite matching, for which BP can
i
takeadvantageofitsspecialstructuretoobtainmuchfaster
(cid:40)
cz if z(cid:190)0 running time.
(cid:148)(cid:52)z(cid:53)= i
i (cid:136) otherwise(cid:48) Let us define the capacitated min-cost network flow
problem ((cid:77)(cid:67)(cid:70)). Given a directed graph G=(cid:52)V(cid:49)E(cid:53), let
Then, ((cid:76)(cid:80)) is equivalent to following the factorized opti- V, E denote the set of vertices and arcs or directed edges,
mization problem: respectively, with (cid:151)V(cid:151) = n and (cid:151)E(cid:151) = m. For any vertex
v∈V, let E be the set of arcs incident to v, and for any
v
(cid:88) n (cid:88) m e∈E , let (cid:227)(cid:52)v(cid:49)e(cid:53)=1 if e is an out-arc of v (i.e., arc e=
minimize (cid:148)(cid:52)x(cid:53)+ (cid:150) (cid:52)x (cid:53)(cid:49) v
i=1
i i
j=1
Cj Cj
((cid:80) )
(cid:52)v(cid:49)w(cid:53),forsomew∈V),and(cid:227)(cid:52)v(cid:49)e(cid:53)=−1ife isanin-arc
(cid:76)(cid:80) of v (i.e., arc e=(cid:52)w(cid:49)v(cid:53), for some w∈V). The (cid:77)(cid:67)(cid:70) on
subject to x i ∈(cid:18)(cid:49) ∀i∈V(cid:48) G is formulated as follows (Ahuja et al. 1993, Bertsimas
and Tsitsiklis 1997):
Then BP for this factorized optimization problem becomes
the BP heuristic for LP. Note that the BP described earlier minimize (cid:88) c x
requirescomputingmessagefunctionsoftheformmt and e e
i→C e∈E mt . In general, it is not clear if such message functions (cid:88)
C→i subject to (cid:227)(cid:52)v(cid:49)e(cid:53)x =f (cid:49) ∀v∈V
can be stored and updated efficiently. For LP, however, it e v ((cid:77)(cid:67)(cid:70))
can be shown that every message function is a piecewise-
e∈Ev
(demand/supply constraints)
linear convex function, which allows efficient encoding of
them in terms of a finite vector describing the break points 0(cid:182)x e (cid:182)u e (cid:49) ∀e∈E (flow constraints)
andtheslopesofitslinearpieces.In§4.1,wewilldothisin
the context of the min-cost network flow problem, and we where c e (cid:190)0, u e (cid:190)0, c e ∈(cid:18), u e ∈(cid:18) ¯, for each e∈E, and
willexplaintheassociatedcomputationprocedureindetail.
f
v
∈(cid:18)foreachv∈V.Thevariablesx
e
representflowvalue
assigned to each arc e ∈E; the first type of constraints
Now, BP being a distributed algorithm, it is unlikely to
state that the difference of inflow and outflow at each node work well when the ((cid:76)(cid:80)) does not have a unique opti-
v∈V equalsthenodedemandf (couldbepositiveorneg-
malsolution.However,evenwiththeassumptionthat((cid:76)(cid:80)) v
ative), and the second type of constraints state that flow on
has a unique optimal solution, in general the estimation
each arc e∈E is nonnegative and cannot be larger than
of BP may not converge to the unique optimal solution.
its capacity u . We shall assume that the instance of net-
One such instance is an LP-relaxation of the maximum e
work flow is feasible. Without loss of generality, let each
weight independent set problem on a complete bipartite
node v∈V be such that (cid:151)E (cid:151)(cid:190)2, or else either E =(cid:153), in
graph(Sanghavietal.2009): v v
which case we ignore such v, or (cid:151)E (cid:151)=1, in which case
v
3 3 the flow on e ∈E is determined by f . For the (cid:77)(cid:67)(cid:70),
(cid:88) (cid:88) v v
minimize − 2x i − 3y i define factor and variable functions (cid:150), (cid:148) as follows: for
i=1 j=1 v∈V, e∈E
((cid:80) )
subject to x i +y j +z ij =1(cid:49) ∀1(cid:182)i(cid:49)j(cid:182)3(cid:49) (cid:73)  (cid:88)
0 if (cid:227)(cid:52)v(cid:49)e(cid:53)z =f (cid:49)
x(cid:49)y(cid:49)z(cid:190)0(cid:48)
(cid:150)
v
(cid:52)z(cid:53)=

e∈Ev
e v
(cid:136) otherwise(cid:49)
Although BP in Sanghavi et al. (2009) was stated in a
(cid:40)
somewhat different manner, it can be checked that it is c z if 0(cid:182)z(cid:182)u (cid:49)
(cid:148) (cid:52)z(cid:53)= e e
equivalent to the description presented here. It turns out e (cid:136) otherwise(cid:48)
that although this problem has a unique optimal solution,
t
t
h
h
e
eo
B
p
P
tim
a
a
lg
l
o
s
r
o
i
l
t
u
h
t
m
ion
d
.
o
S
e
p
s
ec
n
i
o
fi
t
ca
c
l
o
ly
n
,
v
t
e
h
r
e
ge
me
a
s
t
sa
a
g
ll
e
,
s
l
x
e
ˆ
t
N
a
o
l
s
o
c
n
i
e
lla
t
t
o
e (cid:56)
T
(cid:80)
hen,
(cid:150)
sol
(cid:52)
v
x
ing
(cid:53) +
(cid:77)(cid:67)
(cid:80)
(cid:70) i
(cid:148)
s e
(cid:52)
q
x
u
(cid:53)
iv
(cid:57)
a
.
le
T
n
h
t
er
t
e
o
fo
s
r
o
e
l
,
vi
t
n
h
g
e
m
BP
in x
a
∈(cid:18)
lg
(cid:151)E
o
(cid:151)
-
·
between two different values as the number of iterations N rith v m ∈V ca v n E b v e applie e∈ d E fo e r (cid:77) e (cid:67)(cid:70) in this standard form.
oscillates between odd and even values. Becauseofthespecialstructureof(cid:77)(cid:67)(cid:70)thateachvariable
node is adjacent to exactly two factor nodes, it is indeed
4. BP Algorithm for Min-Cost possibletoskipthemessageupdatestepmt ,resultingin
v→e
Network Flow Problem a simplified Algorithm 2, stated next.
In this section, we formulate BP for the capacitated min- Algorithm 2 BP for (cid:77)(cid:67)(cid:70)
costnetworkflowproblem((cid:77)(cid:67)(cid:70))andstateourmainresult 1: Initialize t=0, messages m0 (cid:52)z(cid:53)=0, m0 (cid:52)z(cid:53)=0,
e→v e→w
about the convergence of BP for (cid:77)(cid:67)(cid:70). As mentioned ear- ∀z∈(cid:18) for each e=(cid:52)v(cid:49)w(cid:53)∈E.
lier, each message of BP for (cid:77)(cid:67)(cid:70) is a function, and we 2: for t=1(cid:49)2(cid:49)3(cid:49)(cid:48)(cid:48)(cid:48)(cid:49)N do
describehowthesemessagescanbeefficientlyupdatedand 3: For each e=(cid:52)v(cid:49)w(cid:53)∈E, update messages as
stored as vectors in §4.1. In §4.2, we consider a subclass follows:
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
. 65:71
ta
,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
416 OperationsResearch60(2),pp.410–428,©2012INFORMS
mt (cid:52)z(cid:53) Theorem 4.1. Suppose (cid:77)(cid:67)(cid:70) has a unique optimal solu-
e→v
(cid:26) (cid:27) tion x∗. Define L to be the maximum cost of a simple di-
=(cid:148) (cid:52)z(cid:53)+ min (cid:150) (cid:52)z¯(cid:53)+ (cid:88) mt−1 (cid:52)z¯ (cid:53) (cid:49) rectedpathinG(cid:52)x∗(cid:53).Then,foranyN(cid:190)(cid:52)(cid:143)L/(cid:52)2(cid:132)(cid:52)x∗(cid:53)(cid:53)(cid:144)+1(cid:53)n,
e w e˜→w e˜
z¯∈(cid:18)(cid:151)Ew(cid:151)(cid:49)z¯e=z
e˜∈Ew\e xˆN =x∗.
∀z∈(cid:18)
The proof of Theorem 4.1 is presented in §5. The above
mt (cid:52)z(cid:53) statedtheoremclaimsthattheBPalgorithmfindstheunique
e→w
(cid:26) (cid:27) optimal solution of (cid:77)(cid:67)(cid:70) in at most (cid:52)(cid:143)L/(cid:52)2(cid:132)(cid:52)x∗(cid:53)(cid:53)(cid:144)+1(cid:53)n
=(cid:148) (cid:52)z(cid:53)+ min (cid:150) (cid:52)z¯(cid:53)+ (cid:88) mt−1 (cid:52)z¯ (cid:53) (cid:49)
e v e˜→v e˜ iterations: this convergence is exact in the sense that BP
z¯∈(cid:18)(cid:151)Ev(cid:151)(cid:49)z¯e=z
e˜∈Ev\e findstheoptimalsolutionexactlyinafinitenumberofiter-
∀z∈(cid:18) ations. This is in contrast with the asymptotic convergence
established for many iterative algorithms in the theory of
4: t(cid:50)=t+1
continuous optimization. We note that this result is sim-
5: end for
ilar in flavor to those established in the context of BP’s
6: For each e=(cid:52)v(cid:49)w(cid:53)∈E, set the belief function as
convergence for combinatorial optimization (Bayati et al.
bN(cid:52)z(cid:53)=(cid:148) (cid:52)z(cid:53)+ (cid:88) mN−1(cid:52)z(cid:53)+ (cid:88) mN−1(cid:52)z(cid:53)(cid:48) 2008a, b; Sanghavi et al. 2009). However, it differs from
e e e˜→v e˜→w the convergence results in Moallemi and Van Roy (2007,
e˜∈Ev\e e˜∈Ew\e
2009)wheretheestimates convergetotheoptimalsolution
7: Calculate the belief estimate by finding with an exponential rate, but are not established to reach
xˆN ∈argminbN(cid:52)z(cid:53) for each e∈E. an exact optimal in finitely many steps. Next we state the
e e
8: Return xˆN as an estimation of the optimal total computation performed by Algorithm 2 to find the
solution of (cid:77)(cid:67)(cid:70). optimalsolutionwhentheparameters(capacitiesandcosts)
are integral in the (cid:77)(cid:67)(cid:70).
Intuitively, in Algorithm 2 each arc can be thought of
as an agent who is trying to figure out its own flow while Theorem 4.2. Givenan(cid:77)(cid:67)(cid:70)withauniqueoptimalsolu-
meeting the conservation constraints at its endpoints. Each
tionx∗ andintegraldata,theBPalgorithmfindstheunique
link maintains an estimate of its “local cost” as a function
optimal solution of (cid:77)(cid:67)(cid:70) in O(cid:52)c3 mn4logn(cid:53) operations,
of its flow (thus, this estimate is a function, not a single max
where c =max c .
number). At each time step an arc updates its function as max e e
follows: the cost of assigning x units of flow to link e Theorem 4.2 follows by utilizing Theorem 4.1 to bound
is the cost of pushing x units of flow through e plus the the number of iterations along with a bound on the num-
minimum-cost way of assigning flow to neighboring edges ber of operations required for updating message functions
(withrespecttothefunctionscomputedatthepreviousiter- mt up to those many iterations. The formal proof of this
e→v
ation) to restore flow conservation at the endpoints of e. statement is presented in §7.
Similar to BP for LP, the message functions in BP for
(cid:77)(cid:67)(cid:70), mt for suitable pairs of e and v, are also piece-
e→v 4.1. Computing/Encoding Message Functions
wise-linear convex functions. In §4.1, we establish this
factandpresentanexplicitprocedureforcomputingmt . Hereweprovideaprocedureforconstructingmessagefunc-
e→v
Hence,Algorithm2isindeedaprocedurethatcanbeimple- tion mt in BP for (cid:77)(cid:67)(cid:70). This construction procedure
e→v
mented on a computer. Next, we state conditions under shows that each message function mt is a piecewise-
e→v
whichtheestimatesofBPconvergetotheoptimalsolution linear convex function. Moreover, we provide a bound for
of(cid:77)(cid:67)(cid:70).Beforeformallystatingtheresult,wefirstgivethe thenumberofoperationsrequiredforthisconstructionpro-
definition of a residual network (Ahuja et al. 1993). Define cedure, which will help in bounding the running time of
G(cid:52)x(cid:53) to be the residual network of G with respect to flow Algorithm2.First,weformallydefinepiecewise-linearcon-
x as follows: G(cid:52)x(cid:53) has the same vertex set as G, ∀e= vexfunction:
(cid:52)v(cid:49)w(cid:53)∈E if x <u , then e is an arc in G(cid:52)x(cid:53) with cost
e e
cx=c . Finally, if x >0, then there is an arc e(cid:48)=(cid:52)w(cid:49)v(cid:53) Definition 4.3. A function f is called piecewise-linear
e e e
in G(cid:52)x(cid:53) with cost cx =−c . Let convex if for some finite set of reals, a <a <···<a ,
e(cid:48) e 0 1 n
(allowing a =−(cid:136) and a =(cid:136)),
(cid:26) (cid:27) 0 n
(cid:132)(cid:52)x(cid:53)=min cx(cid:52)C(cid:53)= (cid:88) cx (cid:49) (10)
e 
C∈(cid:67) e∈C  c 1 (cid:52)z−a 1 (cid:53)+f(cid:52)a 1 (cid:53) if z∈(cid:54)a 0 (cid:49)a 1 (cid:55)
f(cid:52)z(cid:53)= c (cid:52)z−a(cid:53)+f(cid:52)a(cid:53) if z∈(cid:52)a(cid:49)a (cid:55)(cid:49) 1(cid:182)i(cid:182)n
where (cid:67) is the set of directed cycles in G(cid:52)x(cid:53). Note that i+1 i i i i+1
if x∗ is the unique optimal solution of (cid:77)(cid:67)(cid:70) with directed
(cid:136)
otherwise
graph G, then it must be that (cid:132)(cid:52)x∗(cid:53)>0 in G(cid:52)x∗(cid:53), or else
wecanchangeflowx∗ alongtheminimalcostcyclein(10) wheref(cid:52)a (cid:53)∈(cid:18)andc <c <···<c satisfyc (cid:52)a −a(cid:53)
1 1 2 n i+1 i+1 i
without increasing its cost. +f(cid:52)a(cid:53)=f(cid:52)a (cid:53) for 1(cid:182)i(cid:182)n−1.
i i+1
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
. 65:71
ta
,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

| Gamarnik,Shah,andWei: |     |     | BeliefPropagationforMin-CostNetworkFlow |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
417
OperationsResearch60(2),pp.410–428,©2012INFORMS
Wedefinea (cid:49)a (cid:49)(cid:48)(cid:48)(cid:48)(cid:49)a astheverticesoff.Wedefinen thefunctionthatisdefinedonlyatz∗+z∗ withg(cid:52)z∗+z∗(cid:53)=
|     |     | 0 1 | n   |     |     |     |     |     |     |     |     | 1   | 2   | 1   | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to be the number of pieces of f, denoted by p(cid:52)f(cid:53). We call f (cid:52)z∗(cid:53)+f (cid:52)z∗(cid:53). Let L =U =z∗ and L =U =z∗. We
|     |     |     |     |     |     |     | 1   | 1   | 2 2 | 1   | 1   | 1   | 2   | 2   | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
c(cid:52)z−a (cid:53)+f(cid:52)a (cid:53) for z∈(cid:54)a (cid:49)a(cid:55) as the ith linear shall construct g iteratively for all t∈(cid:18) so that we shall
| i     | i−1 | i−1 |     | i−1 i |     |     |     |     |                      |                    |     |     |     |     |     |
| ----- | --- | --- | --- | ----- | --- | --- | --- | --- | -------------------- | ------------------ | --- | --- | --- | --- | --- |
| piece | f.  |     | f   |       |     |     |     |     | g(cid:52)t(cid:53)=I | (cid:52)t(cid:53). |     |     |     |     |     |
of Clearly, if is a piecewise-linear convex func- end up with The construction is described as
S
tion, then all relevant information about f can be stored follows. At every iteration, let X (and X ) be the linear
|     |     |     |     |     |     |     |     |     |     |     |     | 1   |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
using a finite vector of size O(cid:52)p(cid:52)f(cid:53)(cid:53). We make the follow- piece of f (and f ) at the left side of L (and L ). Choose
|     |     |     |     |     |     |     |     |     | 1   | 2   |     |     | 1   | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ing observation, which will be useful for efficient update the linear piece with the larger slope from (cid:56)X (cid:49)X (cid:57), and
 .devreser sthgir lla ,ylno esu lanosrep roF . 65:71 ta ,5202 lirpA 61 no ]91.112.052.121[ yb gro.smrofni morf dedaolnwoD 1 2
of messages of BP. “stitch” this piece onto the left side of the left endpoints
|             |     |          |     |                            |     |     | of  | g. If piece, | say, | P, of | function | f   | is chosen, | then | update |
| ----------- | --- | -------- | --- | -------------------------- | --- | --- | --- | ------------ | ---- | ----- | -------- | --- | ---------- | ---- | ------ |
| Observation |     | 4.4.     |     |                            |     |     |     |              |      | i     |          | i   |            |      |        |
|             |     | Supposef |     | ,f arepiecewise-linearcon- |     |     |     |              |      |       |          |     |            |      |        |
1 2 L to the vertex that is on the left end of P for i=1(cid:49)2.
vex functions. Then, f (cid:52)ax+b(cid:53), cf (cid:52)x(cid:53)+df (cid:52)x(cid:53) are also i i
|     |     |     | 1   | 1   | 2   |     | As  | an example, |     | consider | f and | f shown |     | in the Figure | 2.  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ----- | ------- | --- | ------------- | --- |
convex piecewise-linear functions, for any real numbers a, 1 2
|     |     |     |     |     |     |     |     | z∗=1 |     | z∗=0 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- |
c(cid:190)0, d(cid:190)0. Here, and are vertices of f and f such that
| b, c, | and d, where |     |     |     |     |     |            | 1   |                    | 2          |     |                    | 1    | 2        |        |
| ----- | ------------ | --- | --- | --- | --- | --- | ---------- | --- | ------------------ | ---------- | --- | ------------------ | ---- | -------- | ------ |
|       |              |     |     |     |     |     | z∗=argminf |     | (cid:52)z(cid:53), | z∗=argminf |     | (cid:52)z(cid:53). | Note | that the | linear |
|       |              |     |     |     |     |     | 1          |     | 1                  | 2          |     | 2                  |      |          |        |
Definition 4.5. Let S = (cid:56)f (cid:49)f (cid:49)(cid:48)(cid:48)(cid:48)(cid:49)f (cid:57) be a set of piece X in the procedure is labeled as P1 on the graph,
|     |     |     |     | 1 2 k |     |     |     | 1   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
piecewise-linear convex functions, and let (cid:235)(cid:50) (cid:18)k→(cid:18) be whereas X does not exist (because there is no linear piece
|     |     |     |     |     | t   |     |     |      | 2        |         |      |        |             |     |        |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ------- | ---- | ------ | ----------- | --- | ------ |
|     |     |     |     |     |     |     | for | f on | the left | side of | z∗). | Hence, | we “stitch” | P1  | to the |
|     |    |     |     |     |     |     |     | 2    |          |         | 2    |        |             |     |        |
k
0 (cid:88) left side of g, and update L to 0. In a similar manner,
|     |     | if  | x =t |     |     |     |     |     |     |     |     | 1   |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:235)(cid:52)x(cid:53)= i let Y (Y ) be the linear piece of f (f ) to the right side
| t   |     | i=1 |     |     |     |     |     | 1   | 2   |     |     | 1   | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:136) of U (U ). Then choose the linear piece with the smaller
|     |     | otherwise(cid:48) |     |     |     |     |          | 1   | 2        |            |            |        |        |         |           |
| --- | --- | ----------------- | --- | --- | --- | --- | -------- | --- | -------- | ---------- | ---------- | ------ | ------ | ------- | --------- |
|     |     |                   |     |     |     |     | slope    | and | “stitch” | this piece | onto       | the    | right  | side of | the right |
|     |     |                   |     |     |     |     | endpoint |     | of g. If | Q is       | the chosen | piece, | update | U       | to the    |
Thentheinterpolationoff (cid:49)(cid:48)(cid:48)(cid:48)(cid:49)f orS,denotedbyI (cid:52)·(cid:53), i i
|     |     |     | 1   | k   |     | S   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is defined as vertex that is on the right side of Q for i=1(cid:49)2. Again,
i
|     |     |     |     |     |     |     | we  | use f | and f | in Figure | 2   | as an | illustration. | The | linear |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --------- | --- | ----- | ------------- | --- | ------ |
|     |     |     |     |     |     |     |     |       | 1     | 2         |     |       |               |     |        |
(cid:26) k (cid:27) piece Y in the procedure is labeled as P2, whereas Y is
|                         |                             |     | (cid:88)           |                              |     |     |     | 1   |     |     |     |     |     |     | 2   |
| ----------------------- | --------------------------- | --- | ------------------ | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I (cid:52)t(cid:53)=min | (cid:235)(cid:52)x(cid:53)+ |     | f(cid:52)x(cid:53) | (cid:49) ∀t∈(cid:18)(cid:48) |     |     |     |     |     |     |     |     |     |     |     |
S x∈(cid:18)k t i i labeled as P3. Because P2 has a lower slope than P3, we
i=1
|     |     |     |     |     |     |     | “stitch” | P2  | to the | right | side of | g and | update | U to | 2.  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------ | ----- | ------- | ----- | ------ | ---- | --- |
1
| Lemma | 4.6. |     |     |     |     |     |     |     |     |     |     |     | L   | L   |     |
| ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Suppose f , f are piecewise-linear con- Repeat this procedure until both (and ) and
|     |     |     | 1   | 2   |     |     |     |     |     |     |     |     | 1   |     | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vex functions. Then, for S = (cid:56)f (cid:49)f (cid:57), the I (cid:52)t(cid:53) is a U (and U ) are the leftmost (and rightmost) endpoints of
|     |     |     |     | 1 2 | S   |     | 1   |     | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
piecewise-linear convex function, and it can be computed f (and f ), or both endpoints of g are infinity. See Fig-
|     |     |     |     |     |     |     | 1   |     | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in O(cid:52)p(cid:52)f (cid:53)+p(cid:52)f (cid:53)(cid:53) operations. ures 2 and 3 as an illustration of resulting interpolation of
|     | 1   | 2   |     |     |     |     |     |                |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | the | two functions. |     |     |     |     |     |     |     |
Proof. We shall provide a constructive proof of this Note that the total number of iterations is bounded by
result by describing a procedure to construct I (cid:52)t(cid:53). The O(cid:52)p(cid:52)f (cid:53)+p(cid:52)f (cid:53)(cid:53) and each iteration takes at most con-
|     |     |     |     |     | S   |     |     | 1   | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
idea behind construction of I (cid:52)t(cid:53) is essentially to “stitch” stant number of operations. Thus, total computation per-
S
z∗,
together the linear pieces of f and f . To this end, let formed to obtain g is O(cid:52)p(cid:52)f (cid:53)+p(cid:52)f (cid:53)(cid:53). By construction,
|     |     |     |     | 1 2 |     | 1   |     |     |     |     |     | 1   | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
z∗ be vertices of f , f such that z∗=argminf (cid:52)z(cid:53), z∗= it is clear that g is a piecewise-linear convex function.
| 2   |     | 1   | 2   | 1   | 1   | 2   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
argminf (cid:52)z(cid:53).LetS=(cid:56)f (cid:49)f (cid:57).Inthecaseofties,weselect Also, g(cid:52)z∗ +z∗(cid:53) = f (cid:52)z∗(cid:53)+f (cid:52)z∗(cid:53), and by the way we
|     | 2   |     | 1   | 2   |     |     |                                                                                            |     |     | 1   |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | haveconstructedg,wemusthaveg(cid:52)t(cid:53)(cid:182)(cid:56)(cid:235)(cid:52)x(cid:53)+f |     | 1 2 |     | 1   | 2   |     |     |     |
z∗ to be the smallest point in the argmin set. Let g(cid:52)t(cid:53) be (cid:52)x (cid:53)+
| i      |     |           |     |         |     |     |     |     |     |     |     |     |     | t   | 1 1 |
| ------ | --- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Figure | 2.  | Functions | f   | and f . |     |     |     |     |     |     |     |     |     |     |     |
|        |     |           | 1   | 2       |     |     |     |     |     |     |     |     |     |     |     |
|        | 6   |           |     |         |     |     | 6.0 |     |     |     |     |     |     |     |     |
5.5
5
5.0
P6
4.5
4
4.0
|     | 3   |     |     |     |     |     | 3.5 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3.0
2
|     |     |     |     |     |     |     | 2.5 |     |     |     | P4  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P5
2.0
1 P1
|     |     |     |     | P2  |     |     |     |     | P3  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.5
0
1.0
0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
418 OperationsResearch60(2),pp.410–428,©2012INFORMS
Figure 3. Interpolation of f and f . convex function, then it can be easily checked that so is f(cid:48)
1 2 i
for 1(cid:182)i(cid:182)k. Therefore, Theorem 4.9 follows immediately
8 by an application of Theorem 4.7 to S(cid:48). (cid:131)
7 Now recall that for any t(cid:190)1, the message update in the
P6 BP for (cid:77)(cid:67)(cid:70) problem has the following form:
6
(cid:26) (cid:27)
mt (cid:52)z(cid:53)=(cid:148) (cid:52)z(cid:53)+ min (cid:150) (cid:52)z¯(cid:53)+ (cid:88) mt−1 (cid:52)z¯ (cid:53)
e→v e w e˜→w e˜
5 z¯∈(cid:18)(cid:151)Ew(cid:151)(cid:49)z¯e=z
e˜∈Ew\e
P5 for z∈(cid:18)(cid:48)
4
P4 Therefore, the message update can be performed using the
3
scaled interpolation. Specifically, we make the following
P3 observation.
2 P1
P2 Observation 4.10. Let S =(cid:56)mt−1 (cid:49)e˜∈E \e(cid:57) and a =
e˜→w w e˜
1 (cid:227)(cid:52)w(cid:49)e˜(cid:53) for any e˜∈E w \e. Then the function m˜t e→v (cid:52)z(cid:53)=
0 1 2 3 4 5 6 7 mt (cid:52)z(cid:53)−(cid:148) (cid:52)z(cid:53) is equal to Ia(cid:52)−(cid:227)(cid:52)w(cid:49)e(cid:53)z+f (cid:53). e→v e S w
From Observation 4.10 above, the following corollaries
f (cid:52)x (cid:53)(cid:57)foranyt∈(cid:18).Therefore,itfollowsthatg=I .This
co 2 mp 2 letes the proof of Lemma 4.6. (cid:131) S are immediate.
Corollary 4.11. Any message function mt of the BP
e→v Theorem 4.7. Given a set S(cid:56)f (cid:49)(cid:48)(cid:48)(cid:48)(cid:49)f (cid:57) of piecewise- algorithm for (cid:77)(cid:67)(cid:70) is piecewise linear convex for any t(cid:190)
1 k
linear convex functions, I (cid:52)t(cid:53) is also a piecewise-linear 0 and any arc e, vertex v, where e is incident to v.
S
(cid:80)
convex function. Let P = p(cid:52)f(cid:53). Then I (cid:52)t(cid:53) can be f∈S S Proof. The proof follows by induction on t. For t =0,
computed in O(cid:52)Plogk(cid:53) operations.
m0 is a constant (and hence piecewise linear) function
e→v
Proof. Without the loss of generality, we may assume equal to 0 for any e and v where e is incident to v. For
that k is divisible by 2. Let S =(cid:56)f (cid:49)f (cid:57), S =(cid:56)f (cid:49)f (cid:57)(cid:49) t(cid:190)1, by induction hypothesis, assume message functions
1 1 2 2 3 4
(cid:48)(cid:48)(cid:48)(cid:49)S = (cid:56)f (cid:49)f (cid:57), and S(cid:48) = (cid:56)I (cid:49)I (cid:49)(cid:48)(cid:48)(cid:48)(cid:49)I (cid:57). Then in the form of mt−1 are piecewise linear. By Theorem 4.9
k/2 k−1 k S1 S2 Sk/2 e→v
one can observe that I =I by the definition of I . By and Observation 4.10, for any e and v where e is incident
S(cid:48) S S Lemma 4.6, each function in S(cid:48) is piecewise-linear con- to v, mt (cid:52)z(cid:53)−(cid:148) (cid:52)z(cid:53) is piecewise linear convex. As (cid:148) is
e→v e e
vex and S(cid:48) can be computed in O(cid:52)P(cid:53) operations. Consider also piecewise linear convex, mt is a summation of two
e→v
changing S to S(cid:48) as a procedure of decreasing the num- piecewiselinearconvexfunctionswhichispiecewiselinear
ber of piecewise-linear convex functions. This procedure convex as well. (cid:131)
reduces the number by a factor of 2 each time while it
Corollary 4.12. Supposethecomponentsofcostvectorc
consumes O(cid:52)P(cid:53) operations. Hence, it takes O(cid:52)logk(cid:53) pro-
in (cid:77)(cid:67)(cid:70) are integers. At iteration t, for piecewise-linear
cedures to reduce set S into a single piecewise-linear con-
convex message function mt (cid:52)z(cid:53) of the BP algorithm for
vex function; and hence, computing I (cid:52)t(cid:53) takes O(cid:52)Plogk(cid:53) e→v
S (cid:77)(cid:67)(cid:70), let (cid:56)s (cid:49)s (cid:49)(cid:48)(cid:48)(cid:48)(cid:49)s (cid:57) be the slopes of its pieces. Then
operations. (cid:131) −tc (cid:182)s (cid:182) 1 tc 2 and k s is integral for each 1(cid:182)i(cid:182)k,
max i max i
Definition 4.8. LetS=(cid:56)f (cid:49)f (cid:49)(cid:48)(cid:48)(cid:48)(cid:49)f (cid:57)beasetofconvex where c =max c .
1 2 k max e e
piecewise-linear functions, a∈(cid:18)k, and let (cid:235) t (cid:50) (cid:18)k→(cid:18) be Proof. The proof follows by induction on t. Initially, t=
0 and the statement is immediate. For t (cid:190) 1, because
 k
0 if (cid:88) a i x i =t (cid:227)(cid:52)w(cid:49)e(cid:53)=±1 for any e∈E w , by Observation 4.10 it fol- (cid:235)(cid:52)x(cid:53)= ∀v∈V(cid:49) lows that the absolute values of the slopes for the linear
t i=1
 pieces of mt −(cid:148) is the same as the absolute values
(cid:136) otherwise(cid:48) e→v e
of the slopes for the linear pieces of message functions
We call Ia(cid:52)t(cid:53) = min (cid:56)(cid:235)(cid:52)x(cid:53)+ (cid:80)k f(cid:52)x(cid:53)(cid:57) the scaled mt e˜ − → 1 w . By the induction hypothesis, the absolute values
S x∈(cid:18)k t i=1 i i of the slopes of mt −(cid:148) are integral and bounded by
interpolation of S. e→v e
(cid:52)t −1(cid:53)c . The slope of pieces in (cid:148) is c , and there-
max e e
Theorem 4.9. Givenasetofpiecewise-linearconvexfunc- fore,theabsolutevaluesofslopesofmt areintegraland
e→v
tions S = (cid:56)f (cid:49)(cid:48)(cid:48)(cid:48)(cid:49)f (cid:57), Ia(cid:52)t(cid:53) is also a piecewise-linear bounded by tc . (cid:131)
1 k S max
(cid:80)
convex function. Let P = p(cid:52)f(cid:53). Then I (cid:52)t(cid:53) can be
f∈S S Corollary 4.13. Suppose components of vectors f and
computed in O(cid:52)Plogk(cid:53) operations.
u take integer values in (cid:77)(cid:67)(cid:70). Then at iteration t (cid:190)1,
Proof. Let S = (cid:56)f (cid:49)(cid:48)(cid:48)(cid:48)(cid:49)f (cid:57) and S(cid:48) = (cid:56)f(cid:48)(cid:49)(cid:48)(cid:48)(cid:48)(cid:49)f(cid:48)(cid:57) with for any message function mt , the vertices of mt are
1 k 1 k e→v e→v
f(cid:48)(cid:52)x(cid:53)=f(cid:52)ax(cid:53) for 1(cid:182)i(cid:182)k. If f is a piecewise linear integral as well.
i i i i
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
. 65:71
ta
,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
OperationsResearch60(2),pp.410–428,©2012INFORMS 419
Proof. Again, the proof is by induction on t. Initially, withcapacityu˜ andcostequalto0.Denotethisnewlycre-
v
t=0, and the statement trivially holds. For t (cid:190) 1, first ated graph by Go. Then the (cid:77)(cid:67)(cid:70) on Go is equivalent to
observe that because u has integral components, all of its (cid:77)(cid:67)(cid:70) o.InsteadofusingAlgorithm2tosolvethe(cid:77)(cid:67)(cid:70)on
verticesof(cid:148) areintegralaswell.ByObservation4.10and Go,weshalluseitonGwiththefollowingfunctions(cid:150),(cid:148):
e
inductionhypothesis,allverticesofmt −(cid:148) areintegral.
Therefore, all vertices of mt are int e e → g v ral. e (cid:131)  0 if (cid:88) (cid:227)(cid:52)v(cid:49)e(cid:53)x =f and
Theorem 4.9 and Corolla
e
r
→
y
v
4.11 show that at every iter-

e∈
(cid:88)
Ev
x (cid:182)u˜
e v
ation, each message function can be encoded in terms of (cid:150) v (cid:52)x(cid:53)= e v ∀v∈V(cid:49)
a
ea
fi
r
n
p
i
i
t
e
e
ce
v
s
ec
in
tor
a
d
fi
e
n
s
i
c
te
rib
n
i
u
n
m
g
b
t
e
h
r
e
o
c
f
o
i
r
t
n
er
e
a
r
t
s
io
a
n
n
s
d
.T
sl
h
o
e
p
s
e
e
s
a
o
rg
f
u
it
m
s
e
l
n
in
ts
-
(cid:136)
oth
e
e
∈i
r
n
w
(cid:52)v
i
(cid:53)
se(cid:49)
extendeasilytotheformoflinearprogramconsideredear-

lier; that is, BP for LP can be truly implemented on a  c e x if 0(cid:182)x(cid:182)u e
(cid:148) (cid:52)x(cid:53)= ∀e∈E(cid:48)
computer. e
(cid:136) otherwise(cid:49)
Corollary4.12providesaboundforthenumberoflinear
piecesin mt . Thisboundwill helpus boundtherunning
e→v Now, to update message functions mt for all e∈E , the
time of BP algorithm for (cid:77)(cid:67)(cid:70). We shall discuss this in e→v w
inequality (cid:80) x (cid:182)u˜ implies that it is sufficient to
detail in §7. Finally, we would like to note that the result e∈in(cid:52)w(cid:53) e w
check u˜ linear pieces from message functions mt−1 for
that message functions mt are piecewise-linear convex w e˜→w
e→v all but a constant number of e∈E . This leads to efficient
functions can be also shown by sensitivity analysis of LP, w
cf. Bertsimas and Tsitsiklis (1997, Chapter 5).
implementationofBPfor(cid:77)(cid:67)(cid:70) o.Specifically,westatethe
following result.
4.2. BP for a Subclass of (cid:77)(cid:67)(cid:70) Theorem 4.14. Suppose the (cid:77)(cid:67)(cid:70) o as described above
Section 4.1 established that each message function is has a unique optimal solution with
a piecewise-linear convex function. However, as per the
boundsestablished,thenumberofpiecesincreaseslinearly max(cid:52)u˜ v (cid:49)u v (cid:49)(cid:151)f v (cid:151)(cid:53)(cid:182)K(cid:49) maxc e (cid:182)K(cid:48)
v e
withiterations,andthisrequiresmorecomputationformes-
sage update as iterations grow. Now, for an instance of ThenAlgorithm2for(cid:77)(cid:67)(cid:70) o findstheuniqueoptimalsolu-
(cid:77)(cid:67)(cid:70)withintegralcomponentsofvectorbandu,themes- tion using O(cid:52)K2mn2logn(cid:53), which is O(cid:52)K2n4logn(cid:53) opera-
sage function mt is a piecewise-linear convex function tions in total. As a result, Algorithm 2 is polynomial time
e→v
with integral vertices as per Corollary 4.13. Therefore, it when K is a constant.
hasatmostu linearpieces.Thus,ifu isboundedbysome
e e The proof of Theorem 4.14 is presented in §7.1. It is
constant for all e, the message functions at every iteration
worth taking note of the fact that both the shortest-path
arepiecewise-linearconvexfunctionswithaboundednum-
problem and maximum weight matching in a bipartite
ber of pieces. This results in a computationally efficient
graph belong to the (cid:77)(cid:67)(cid:70) o class of problems with all
update of messages. Next we present a subclass of (cid:77)(cid:67)(cid:70),
components of f, u being bounded by 2. For these two
denoted by (cid:77)(cid:67)(cid:70) o, for which such a property holds and
classes of problems we do not need the extra constraint
whichcontainsimportantclassesofnetworkflowproblems. (cid:80) x (cid:182)u˜ , but we do need this constraint to make a
Tothisend,givenadirectedgraphG=(cid:52)V(cid:49)E(cid:53),consider e∈in(cid:52)v(cid:53) e v
general statement of the theorem. We see that under the
the following subclass of problem: with notation in(cid:52)v(cid:53)=
uniquenessassumptions,BPsolvestheseproblemsinpoly-
(cid:56)(cid:52)u(cid:49)v(cid:53)∈E(cid:57)
nomial (as opposed to just pseudopolynomial) time.
(cid:88) minimize c x
e e
e∈E 5. Convergence of BP for (cid:77)(cid:67)(cid:70)
(cid:88)
subject to (cid:227)(cid:52)v(cid:49)e(cid:53)x =f (cid:49) ∀v∈V This section is devoted to establishing the convergence of
e v
e∈Ev BP to the optimal solution of the (cid:77)(cid:67)(cid:70) under the assump-
(demand/supply constraints) tion of the uniqueness of the optimal solution; namely, we
(cid:88) x (cid:182)u˜ (cid:49) ∀v∈V shall prove Theorem 4.1. The outline of the proof is as
e v
follows. First, we define the notion of a computation tree
e∈in(cid:52)v(cid:53)
0(cid:182)x (cid:182)u (cid:48) ∀e∈E (flow constraints). TN that is associated with each variable node x of (cid:77)(cid:67)(cid:70)
e e e e
for iteration N. We show that in fact the estimation xˆN
e
Above, c, u, and u˜ are all integral. To see that (cid:77)(cid:67)(cid:70) o is underBPistheoptimalsolutionofanappropriatelydefined
indeed an instance of (cid:77)(cid:67)(cid:70), consider the following. Split (cid:77)(cid:67)(cid:70) problem on TN (Lemma 5.1). Next, we show that
e
each v∈V into two vertices v and v , where v is inci- theoptimalassignmenttox underthemin-costflowprob-
in out in e
denttoallin-arcsofvwithf =0andv isincidenttoall lem on the computation tree TN is the same as the optimal
vin out e
out-arcs of v with f =f . Create an arc from v to v assignment to x under the original (cid:77)(cid:67)(cid:70) as long as N
vout v in out e
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
65:71
ta
,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
420 OperationsResearch60(2),pp.410–428,©2012INFORMS
is large enough (see §5.2). This immediately implies that tree. It should be noted that the definition of a computa-
BP finds the correct optimal solution for (cid:77)(cid:67)(cid:70) for large tion tree may appear slightly different compared to that in
enough N leading to Theorem 4.1. We note that this strat- relatedworkssuchasBayatietal.(2008a,b)andSanghavi
egy issimilar tothat of Bayatiet al. (2008a).However, the et al. (2007) (arc is the root here, in contrast to a vertex as
technical details are quite different. the root). However, the utility of the computation trees is
very similar.
Nowwearereadytorelatethecomputationtreewiththe
5.1. Computation Tree and BP
BP. Let Vo(cid:52)TN(cid:53)⊂V(cid:52)TN(cid:53) denote the set of all the vertices
e e
We start with the definition of a computation tree. The thatarenotontheNthlevelofTN.Considerthefollowing
e
N-level computation tree associated with arc e = (cid:52)v(cid:49)w(cid:53)
problem:
∈E is denoted by TN. It is essentially the breadth-first
e
search tree of G (with repetition of nodes allowed) start- minimize (cid:88) c x
(cid:226)(cid:52)e˜(cid:53) e˜
ing from e up to depth N. Formally, computation tree
e˜∈E(cid:52)Te N(cid:53)
T e N is defined inductively as follows. T e 0=(cid:52)V(cid:52)T e 0(cid:53)(cid:49)E(cid:52)T e 0(cid:53)(cid:53) subject to (cid:88) (cid:227)(cid:52)u(cid:48)(cid:49)e˜(cid:53)x =f (cid:49) ∀u(cid:48)∈Vo(cid:52)TN(cid:53)
is a tree with vertex set V(cid:52)T0(cid:53) = (cid:56)v(cid:48)(cid:49)w(cid:48)(cid:57) and arc set e˜ (cid:226)(cid:52)u(cid:48)(cid:53) e
E(cid:52)T0(cid:53)=(cid:56)e(cid:48) =(cid:52)v(cid:48)(cid:49)w(cid:48)(cid:53)(cid:57). The v
e
(cid:48)(cid:49)w(cid:48) are considered repli-
e˜∈Eu(cid:48)
e
cas of v(cid:49)w ∈ V, and this is represented by a mapping 0(cid:182)x (cid:182)u (cid:49) ∀f ∈E(cid:52)TN(cid:53)(cid:48) ((cid:77)(cid:67)(cid:70) N)
e˜ (cid:226)(cid:52)f(cid:53) e e
(cid:226)0(cid:50) V(cid:52)T0(cid:53)→V with (cid:226)0(cid:52)v(cid:48)(cid:53)=v and (cid:226)0(cid:52)w(cid:48)(cid:53)=w. The arc
e e e e
e(cid:48) is considered the “root” of T e 0, and vertices v(cid:48)(cid:49)w(cid:48) are Above, E u(cid:48) ⊂E(cid:52)T e N(cid:53) is the set of arcs incident on u(cid:48) ∈
considered to be at level 0. Inductively, let us suppose that Vo(cid:52)T e N(cid:53) in T e N and (cid:227)(cid:52)u(cid:48)(cid:49)e˜(cid:53) for e˜∈E u(cid:48) is defined as −1
tree TN =(cid:52)V(cid:52)TN(cid:53)(cid:49)E(cid:52)TN(cid:53)(cid:53) is defined with corresponding or +1, depending upon whether e(cid:48) is in-arc or out-arc for
(cid:226)N(cid:50) V e (cid:52)TN(cid:53)→V e such t e hat for u(cid:48)(cid:49)u(cid:48) ∈V(cid:52)TN(cid:53), (cid:52)u(cid:48)(cid:49)u(cid:48)(cid:53)∈ node u(cid:48). Loosely speaking, (cid:77)(cid:67)(cid:70) N e is essentially an (cid:77)(cid:67)(cid:70) E e (cid:52)TN(cid:53) o e nly if (cid:52)(cid:226)N(cid:52)u(cid:48)(cid:53)(cid:49)(cid:226)N(cid:52)u(cid:48)(cid:53)(cid:53) 1 ∈ E 2 . Let e P(cid:50) V(cid:52)T 1 N(cid:53) 2 → on T e N: there is a flow constraint for every arc e˜∈E(cid:52)T e N(cid:53)
e e 1 e 2 e
V(cid:52)TN(cid:53) represent the parent relation in TN. And for the and a demand/supply constraint for every node, except for
e e sake of simplicity, let w(cid:48) be the parent of v(cid:48)(cid:52)P(cid:52)v(cid:48)(cid:53)=w(cid:48)(cid:53) the nodes on the Nth level. Now we state the following
and v(cid:48) be the parent of w(cid:48)(cid:52)P(cid:52)w(cid:48)(cid:53) = v(cid:48)(cid:53). Let L(cid:52)TN(cid:53) be well-known result that exhibits the connection between BP
the set of leaves1 of TN. Now we shall define T e N+1 = and the computation trees.
e e
(cid:52)V(cid:52)TN+1(cid:53)(cid:49)E(cid:52)TN+1(cid:53)(cid:53), which contains TN as a subtree. Lemma 5.1. LetxˆN bethevalueproducedbyBPattheend
e e e e
Specifically,V(cid:52)TN+1(cid:53)andE(cid:52)TN+1(cid:53)areobtainedbyadding of iteration N for the flow value on edge e∈E. Then there e e
vertices to V(cid:52)T e N(cid:53) and arcs to E(cid:52)T e N(cid:53) as follows. For each exists an optimal solution y∗ of (cid:77)(cid:67)(cid:70) N e such that y e ∗ (cid:48) =xˆ e N
leaf node u(cid:48)∈L(cid:52)TN(cid:53), add node u˜(cid:48) to expand V(cid:52)TN(cid:53) and where e(cid:48) is the root of TN (and (cid:226)(cid:52)e(cid:48)(cid:53)=e).
e e e
addarc(cid:52)u(cid:48)(cid:49)u˜(cid:48)(cid:53)or(cid:52)u˜(cid:48)(cid:49)u(cid:48)(cid:53)toexpandE(cid:52)TN(cid:53)if(a)thereisa
e Proof. Lete(cid:48)=(cid:52)v(cid:48)(cid:49)w(cid:48)(cid:53)betherootarcofcomputationtree
nodeu˜∈V sothat(cid:52)u(cid:49)u˜(cid:53)or(cid:52)u˜(cid:49)u(cid:53)isinE with(cid:226)N(cid:52)u(cid:48)(cid:53)=u,
e TN with e=(cid:52)v(cid:49)w(cid:53), such that (cid:226)(cid:52)e(cid:48)(cid:53)=e, (cid:226)(cid:52)v(cid:48)(cid:53)=v, and
and (b) (cid:226)N(cid:52)P(cid:52)u(cid:48)(cid:53)(cid:53)(cid:54)=u˜. In this case, define P(cid:52)u˜(cid:48)(cid:53)=u(cid:48), the e
e (cid:226)(cid:52)w(cid:48)(cid:53)=w. By definition, TN has two components con-
map (cid:226)N+1(cid:52)u˜(cid:48)(cid:53)=u˜, and level of u˜(cid:48) as N +1. Indeed, (cid:226)N+1 e
e e nected via the root arc e(cid:48). Let C be the component con-
is identical to (cid:226)N for nodes V(cid:52)TN(cid:53)⊂V(cid:52)TN+1(cid:53). In what
e e e taining w(cid:48) and TN denote C∪e; indeed, TN is a tree.
follows, we shall drop reference to e, N in notation of (cid:226)N e(cid:48)→v(cid:48) e(cid:48)→v(cid:48)
e As before, let Vo(cid:52)TN (cid:53) be the set of all nodes, excluding
when clear from context and abuse notation by denoting e(cid:48)→v(cid:48)
those at the Nth level. Define
(cid:226)(cid:52)e(cid:48)=(cid:52)u(cid:48)(cid:49)u(cid:48)(cid:53)(cid:53)=(cid:52)(cid:226)(cid:52)u(cid:48)(cid:53)(cid:49)(cid:226)(cid:52)u(cid:48)(cid:53)(cid:53).
1 2 1 2
Sometimes TN is also called “unwrapped tree” of G minimize (cid:88) c x
e (cid:226)(cid:52)e˜(cid:53) e˜
rooted at e. Figure 4 gives an example of a computation e˜∈E(cid:52)T
e
N (cid:48)→v(cid:48)(cid:53)
subject to (cid:88) (cid:227)(cid:52)q(cid:48)(cid:49)e˜(cid:53)x =f (cid:49) ∀q(cid:48)∈Vo(cid:52)TN (cid:53)
e˜ (cid:226)(cid:52)q(cid:48)(cid:53) e(cid:48)→v(cid:48)
Figure 4. Computation tree of G rooted at e 3 =(cid:52)1(cid:49)3(cid:53). e˜∈Eq(cid:48)
v 1 e 3 (cid:1) v 3 x e(cid:48) =z(cid:49)
v e 5 v 0(cid:182)x (cid:182)u (cid:49) ∀e˜∈E(cid:52)TN (cid:53)(cid:48)
2 4 e˜ (cid:226)(cid:52)e˜(cid:53) e(cid:48)→v(cid:48)
(cid:52)(cid:77)(cid:67)(cid:70)N (cid:52)z(cid:53)(cid:53)(cid:48)
e
e(cid:48)→v(cid:48)
e 1 e 2 4 e 6 v 2 v 2 v 4 v 4 Now we shall establish that under the BP algorithm (run-
ning on G) the value of message function from e → v
e
3 evaluated at z, that is, mN (cid:52)z(cid:53), is the same as the cost
v 1 v 3 of the optimal assignment e→ fo v r MCFN (cid:52)z(cid:53). This can be
e(cid:48)→v(cid:48)
established inductively. To start with, for N =1, the state-
v v v v v v v v
1 4 1 4 2 3 1 2
ment can be checked to be true trivially. For N >1, let
G = (V,E) T e 2 3 E w(cid:48) denote the edges incident on w(cid:48) in T e N, where recall
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
. 65:71
ta
,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
OperationsResearch60(2),pp.410–428,©2012INFORMS 421
that e(cid:48)=(cid:52)v(cid:48)(cid:49)w(cid:48)(cid:53) is its root arc. Then for each g(cid:48)∈E \e(cid:48) with cost strictly lower than that of y∗. This will lead to
w(cid:48)
with g(cid:48) =(cid:52)u(cid:48)(cid:49)w(cid:48)(cid:53) (or (cid:52)w(cid:48)(cid:49)u(cid:48)(cid:53)), let TN−1 be the subtree contradictiontotheassumptionthatxˆN (cid:54)=x∗,andestablish
of TN that includes g(cid:48) and everyth
g
i
(cid:48)
n
→
g
w(cid:48)
in TN that is the result.
e0 e0
e(cid:48)→v(cid:48) e(cid:48)→v(cid:48)
part of its component that does not include w(cid:48). Define the To that end, let e(cid:48) =(cid:52)v(cid:48)(cid:49)v(cid:48)(cid:53) be the root edge of the
0 (cid:129) (cid:130)
optimization problem: computation tree TN as discussed earlier. Because y∗ is a
minimize (cid:88) c x feasible solution of
e0
(cid:77)(cid:67)(cid:70) N e0 and x∗ is a feasible solution
(cid:226)(cid:52)e˜(cid:53) e˜ of (cid:77)(cid:67)(cid:70),
e˜∈E(cid:52)T g N (cid:48)→ −1 w(cid:48)(cid:53)
(cid:88) (cid:88)
subject to
e˜
(cid:88)
∈Eq(cid:48)
(cid:227)(cid:52)q(cid:48)(cid:49)e˜(cid:53)x
e˜
=f
(cid:226)(cid:52)q(cid:48)(cid:53)
∀q(cid:48)∈Vo(cid:52)T
g
N
(cid:48)→
−1
w(cid:48)
(cid:53) f (cid:226)(cid:52)v(cid:129) (cid:48)(cid:53) =
e˜∈E v(cid:129) (cid:48)
(cid:227)(cid:52)v (cid:129) (cid:48)(cid:49)e˜(cid:53)y e ∗ ˜ =y e ∗
0
(cid:48) +
e˜∈E v(cid:129) (cid:48)\e 0 (cid:48)
(cid:227)(cid:52)v (cid:129) (cid:48)(cid:49)e˜(cid:53)y e ∗ ˜
x g(cid:48) =z(cid:49) (constraint at v (cid:129) (cid:48) in (cid:77)(cid:67)(cid:70) N e0 )
(cid:88) (cid:88)
0(cid:182)x e˜ (cid:182)u (cid:226)(cid:52)e˜(cid:53) (cid:49) ∀e˜∈E(cid:52)T g N (cid:48)→ −1 w(cid:48) (cid:53)(cid:48) f (cid:226)(cid:52)v(cid:129) (cid:48)(cid:53) = (cid:227)(cid:52)(cid:226)(cid:52)v (cid:129) (cid:48)(cid:53)(cid:49)e˜(cid:53)x e ∗ ˜ =x e ∗ 0 + (cid:227)(cid:52)(cid:226)(cid:52)v (cid:129) (cid:48)(cid:53)(cid:49)e˜(cid:53)x e ∗ ˜
((cid:77)(cid:67)(cid:70) N−1 (cid:52)z(cid:53)) e˜∈E (cid:226)(cid:52)v(cid:129) (cid:48)(cid:53) e˜∈E (cid:226)(cid:52)v(cid:129) (cid:48)(cid:53) \e0
g(cid:48)→w(cid:48) (constraint at (cid:226)(cid:52)v(cid:48)(cid:53) in (cid:77)(cid:67)(cid:70))(cid:48)
(cid:129)
By induction hypothesis, it must be that mN−1 (cid:52)z(cid:53) equals
the cost of the solution of (cid:77)(cid:67)(cid:70) N g(cid:48) − → 1 w(cid:48) (cid:52)z g (cid:53) (cid:48)→ . w G (cid:48) iven this N co o p t i e es th o at f t e h d e g e e d s ge in s i E n E v i (cid:129) (cid:48) n in G th w e h c e o r m e p v uta = tio (cid:226) n (cid:52)v tr (cid:48) e (cid:53) e . T T e N h 0 e a re re -
hypothesis and the relation of subtree T g N (cid:48)→ −1 w(cid:48) for all g(cid:48) ∈ fore, (cid:227)(cid:52)v(cid:48)(cid:49)e˜(cid:53) = (cid:227)(cid:52)(cid:226)(cid:52) v v (cid:129) (cid:53)(cid:49)(cid:226)(cid:52)e˜(cid:53)(cid:53) for e˜ (cid:129) ∈ E . (cid:129) Therefore,
(cid:77) E w (cid:67) (cid:48) \ (cid:70) e(cid:48) N with (cid:52)z T (cid:53) e N (cid:48) i → s v e (cid:48) q , u it iv f a o l l e lo n w t t s o that the optimization problem from the a (cid:129) bove inequali (cid:129) ties, it follows that v b (cid:129) (cid:48) ecause y e ∗ (cid:48) >
e(cid:48)→v(cid:48) x∗, there exists arc e(cid:48) (cid:54)= e(cid:48) incident on v(cid:48) in TN su 0 ch
minimize c z+ (cid:88) mN−1 (cid:52)x (cid:53) th e a 0 t (cid:227)(cid:52)v(cid:48)(cid:49)e(cid:48)(cid:53)(cid:52)x∗ − 1 y∗(cid:53) i 0 s strictly positi (cid:129) ve. Th e e 0 refore,
e (cid:226)(cid:52)g(cid:48)(cid:53)→(cid:226)(cid:52)w(cid:48)(cid:53) g(cid:48) (cid:129) 1 (cid:226)(cid:52)e(cid:48)(cid:53) e(cid:48)
g(cid:48)∈Ew(cid:48)\e(cid:48) if (cid:227)(cid:52)v
(cid:129)
(cid:48)(cid:49)e
1
(cid:48)(cid:53)=1, th 1 en x
(cid:226)
∗
(cid:52)e
1
(cid:48)(cid:53)
>y
e
∗
(cid:48)
, or else x
(cid:226)
∗
(cid:52)e(cid:48)(cid:53)
<y
e
∗
(cid:48)
. That
subject to (cid:227)(cid:52)w(cid:48)(cid:49)e(cid:48)(cid:53)z+ (cid:88) (cid:227)(cid:52)w(cid:48)(cid:49)g(cid:48)(cid:53)x g(cid:48) =f (cid:226)(cid:52)w(cid:48)(cid:53) a is t , n if od e e dg v e (cid:48) e ( 1 (cid:48) bo h t a h s a th re e o o u p t p g o o 1 s i i n t g eo fr r o i 1 e m nt v a (cid:48) ti , o a n n w d i h th e 1 n r c e e s , p o ec p 1 t p t o o si e te 0 (cid:48)
g(cid:48)∈Ew(cid:48)\e(cid:48)
orientatio
(cid:129)
n), then x∗ >y∗ or else
(cid:129)
x∗ <y∗. Figure 5
0(cid:182)x g(cid:48) (cid:182)u (cid:226)(cid:52)g(cid:48)(cid:53) (cid:49) ∀g(cid:48)∈E w(cid:48) \e(cid:48)(cid:48) explains this by me (cid:226) a (cid:52) n e 1 (cid:48) s (cid:53) of a e 1 (cid:48) simple exa (cid:226) m (cid:52)e p1 (cid:48)(cid:53) le. e 1 (cid:48)
More generally, using a similar argument, we can find
This is exactly the same as the relation between mN (cid:52)z(cid:53)
e→v arc e(cid:48) (cid:54)=e(cid:48) incident to v(cid:48) satisfying a similar condition.
and message function mN−1(cid:52)·(cid:53) for g ∈E \e as defined −1 0 (cid:130)
g→w w Letv(cid:48) ,v(cid:48) betheotherendpointsofe(cid:48),e(cid:48) ,respectively.
by BP; that is, mN e→v (cid:52)z(cid:53) is exactly the same as the cost of A rec (cid:129)1 ursi (cid:129) v − e 1 application of a similar 1 argu − m 1 ent utilizing
optimal assignment of (cid:77)(cid:67)(cid:70) N . We shall use this equiv-
e(cid:48)→v(cid:48) the feasibility condition of x∗ and y∗ and the inequalities
alence to complete the proof of Lemma 5.1.
between the value of components of x∗ and y∗ at edges
To that end, for given e=(cid:52)v(cid:49)w(cid:53) with 0(cid:182)z(cid:182)u , the
e e(cid:48) and e(cid:48) leads to the existence of arcs e(cid:48), e(cid:48) incident
optimization problem (cid:77)(cid:67)(cid:70) N(cid:52)z(cid:53) is equivalent to 1 −1 2 −2
e on v(cid:48) , v(cid:48) , respectively, so that x∗ (cid:54)=y∗ and x∗ (cid:54)=y∗
minimize c z+ (cid:88) c x + (cid:88) c x with (cid:129) i 1 neq (cid:129) u − a 1 lities being<or>depen e 2 (cid:48) ding e u2 (cid:48) pon the e − (cid:48) o2rient e a− (cid:48) 2-
e (cid:226)(cid:52)e˜(cid:53) e˜ (cid:226)(cid:52)e˜(cid:53) e˜ tion of the edges with respect to e . Continuing further in
e˜∈E(cid:52)T
e
N (cid:48)→v(cid:48)(cid:53) e˜∈E(cid:52)T
e
N (cid:48)→w(cid:48)(cid:53) 0
(cid:88)
subject to (cid:227)(cid:52)q(cid:48)(cid:49)e˜(cid:53)x =f (cid:49)
e˜ (cid:226)(cid:52)q(cid:48)(cid:53) Figure 5. An example of augmenting path between the
e˜∈Eq(cid:48)
flow assignment on computation tree T2 and
∀q(cid:48)∈Vo(cid:52)T
e
N(cid:53)∩(cid:52)V(cid:52)T
e
N
(cid:48)→v(cid:48)
(cid:53)∪V(cid:52)T
e
N
(cid:48)→w(cid:48)
(cid:53)(cid:53)
the flow assignment on G.
e3
0(cid:182)x (cid:182)u (cid:49) e˜∈E(cid:52)TN (cid:53)∪E(cid:52)TN (cid:53)(cid:51)
e˜ (cid:226)(cid:52)e˜(cid:53) e(cid:48)→v(cid:48) e(cid:48)→w(cid:48)
f 2 = 0 f 4 = 0 v 1 +2 v 3
t e h q a u t al i s s, m th N e→ e u c (cid:52) o z(cid:53) st + o m f N e a → n v (cid:52) o z p (cid:53) t + im c a e l z a f s o s r ig a n n m y e 0 nt (cid:182) o z f (cid:182) (cid:77) u (cid:67) e (cid:70) . N N e (cid:52) o z w (cid:53) v 2 x x = 5 = 0 0 v 4 0 +1 +1
the claim of Lemma 5.1 follows immediately. (cid:131) 2 0
x = 0
x 1 = 0 4 x 6 = 0 v 2 v 2 v 4 v 4
5.2. Proof of Theorem 4.1
x 3 = 1 0 0 0 0 +1 0 0 –1
N th o e w co w n e tra a r r y e t r h e a a t dy the to re e e s x ta i b st l s ish e T = he (cid:52) o v re (cid:49) m v 4 (cid:53) . ∈ 1. E Su a p n p d os N e t (cid:190) o v 1 v 3
0 (cid:129) (cid:130) f = 1 f = –1
(cid:52)(cid:143)L/(cid:52)2(cid:132)(cid:52)x∗(cid:53)(cid:53)(cid:144)+1(cid:53)n such that xˆN (cid:54)=x∗. By Lemma 5.1, 1 3
there exists an optimal solution e y 0 ∗ of e0 (cid:77)(cid:67)(cid:70) N such that v 1 v 4 v 1 v 4 v 2 v 3 v 1 v 2
y U e ∗ s0 (cid:48) in = g xˆ th e N 0 e . o W pt i i t m ho a u li t ty lo o s f s x o ∗ f , w ge e ne w r i a l l l it s y h , o a w ss t u h m at e e0 it y e ∗ i0 (cid:48) s > po x ss e ∗ i 0 - . Note. Thedas G h e = d ( e V d , g E es ) representtheedgesbelongi T n e g 2 3 totheaugmenting
ble to modify y∗ to obtain a feasible solution of (cid:77)(cid:67)(cid:70) N e0 path.Rootedgeandedgefromv 4 tov 1 havethesameorientation.
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
. 65:71
ta ,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
422 OperationsResearch60(2),pp.410–428,©2012INFORMS
this manner all the way down to the leaves, it is possible opposite orientation compared to e , we have that for any
0
to find arcs (cid:56)e(cid:48) (cid:49)e(cid:48) (cid:49)(cid:48)(cid:48)(cid:48)(cid:49)e(cid:48) (cid:49)e(cid:48)(cid:49)(cid:48)(cid:48)(cid:48)(cid:49)e(cid:48) (cid:57) such that for v(cid:48)∈Vo(cid:52)TN(cid:53),
−N (cid:182)i(cid:182)N,
−N −N+1 −1 1 N
(cid:88)
e0
(cid:88)
(cid:227)(cid:52)v(cid:48)(cid:49)e(cid:48)(cid:53)y˜ = (cid:227)(cid:52)v(cid:48)(cid:49)e(cid:48)(cid:53)y∗
e(cid:48) e(cid:48)
e(cid:48)∈Ev(cid:48) v(cid:48)∈Ev(cid:48)
y∗ >x∗ ⇐⇒ e(cid:48) has the same orientation as e (cid:49)
e(cid:48) (cid:226)(cid:52)e(cid:48)(cid:53) i 0 =f (cid:49)
i i (cid:226)(cid:52)e(cid:48)(cid:53)
y e ∗ (cid:48) <x (cid:226) ∗ (cid:52)e(cid:48)(cid:53) ⇐⇒ e i (cid:48) has the opposite orientation as e 0 (cid:48) which implies that y˜ satisfies all the demand/supply con-
i i
straints.Therefore,y˜ isafeasiblesolutionof(cid:77)(cid:67)(cid:70) N.Now
e0
Let us denote the path containing these edges as X = (cid:88) (cid:88)
c y∗ − c y˜
(cid:56)e(cid:48) (cid:49)e(cid:48) (cid:49)(cid:48)(cid:48)(cid:48)(cid:49)e(cid:48) (cid:49)e(cid:48)(cid:49)e(cid:48)(cid:49)(cid:48)(cid:48)(cid:48)(cid:49)e(cid:48) (cid:57). For any e(cid:48)=(cid:52)v(cid:48)(cid:49)v(cid:48)(cid:53) (cid:226)(cid:52)e(cid:48)(cid:53) e(cid:48) (cid:226)(cid:52)e(cid:48)(cid:53) e(cid:48)
∈X
−N
,de
−
fi
N
n
+
e
1
Aug(cid:52)e(cid:48)
−
(cid:53)
1
=(cid:52)
0
v(cid:48)(cid:49)
1
v(cid:48)(cid:53)ify
N
∗ >x∗ ,andAug(cid:52)
p
e(cid:48)(cid:53)
q
=
e(cid:48)∈E(cid:52)Te N
0
(cid:53) e(cid:48)∈E(cid:52)Te N
0
(cid:53)
p q e(cid:48) (cid:226)(cid:52)e(cid:48)(cid:53) (cid:88)
(cid:52)v(cid:48)(cid:49)v(cid:48)(cid:53) if y∗ < x∗ . Given the feasibility conditions = c (cid:52)y∗ −y˜ (cid:53)
q p e(cid:48) (cid:226)(cid:52)e(cid:48)(cid:53) (cid:226)(cid:52)e(cid:48)(cid:53) e(cid:48) e(cid:48)
of y∗ and definition of Aug(cid:52)e(cid:48)(cid:53), it can be checked that e(cid:48)∈E(cid:52)Te N
0
(cid:53)
(cid:226)(cid:52)Aug(cid:52)e(cid:48)(cid:53)(cid:53) is an arc in the residual graph G(cid:52)x∗(cid:53). The (cid:88) (cid:88)
= c (cid:139)− c (cid:139)
directed path W =(cid:52)Aug(cid:52)e(cid:48) (cid:53)(cid:49)(cid:48)(cid:48)(cid:48)(cid:49)Aug(cid:52)e(cid:48)(cid:53)(cid:49)(cid:48)(cid:48)(cid:48)(cid:49)Aug(cid:52)e(cid:48) (cid:53)(cid:53) (cid:226)(cid:52)e(cid:48)(cid:53) (cid:226)(cid:52)e(cid:48)(cid:53)
−N 0 N e(cid:48)∈FWD e(cid:48)∈BCK
on TN will be called the augmenting path of y∗ with
e0 =c∗(cid:52)W(cid:53)(cid:139)
respect to x∗. Also, (cid:226)(cid:52)W(cid:53) is a directed walk on G(cid:52)x∗(cid:53).
Now we can decompose (cid:226)(cid:52)W(cid:53) into a simple directed path >0(cid:48)
P No a w nd ea a ch co s ll i e m c p ti l o e n d o ir f ec s t i e m d pl c e yc d l i e rec o t r ed pa c t y h cl o e n s C G 1 (cid:52) (cid:49) x (cid:48) ∗ (cid:48) (cid:53) (cid:48)(cid:49) c C a k n . F A W bo D ve an w d e c h ∗ ave = u − se c d the fo fa r c e t (cid:48)∈ tha B t C c K (cid:226) ∗ (cid:52) . e(cid:48) T (cid:53) h = e c a (cid:226) b (cid:52) o e(cid:48) v (cid:53) e fo c r on e t (cid:48) ra ∈ -
(cid:226)(cid:52)e(cid:48)(cid:53) (cid:226)(cid:52)e(cid:48)(cid:53)
have at most n edges. Because W has 2N +1 arcs and dicts the optimality of y∗. Therefore, the assumption about
N (cid:190)(cid:52)(cid:143)L/(cid:52)2(cid:132)(cid:52)x∗(cid:53)(cid:53)(cid:144)+1(cid:53)n, it follows that k >L/(cid:52)(cid:132)(cid:52)x∗(cid:53)(cid:53). theBPestimatenotconvergingisfalse.Thiscompletesthe
Now the cost of path P, denoted by c∗(cid:52)P(cid:53) with respect to proof of Theorem 4.1.
theresidualgraphG(cid:52)x∗(cid:53),isatleast−L(andatmostL)by
definitionofL.BecauseeachC isasimplecycleinG(cid:52)x∗(cid:53), 5.3. Detection of Uniqueness of the Optimal
i
by definition its cost, denoted by c∗(cid:52)C(cid:53) with respect to Solution Using BP
i
G(cid:52)x∗(cid:53),isatleast(cid:132)(cid:52)x∗(cid:53);(cid:132)(cid:52)x∗(cid:53)>0becausex∗ istheunique
In this section, we establish an unusual property of BP in
optimal solution. Therefore, as explained below, we obtain terms of its ability to detect the uniqueness of the optimal
that the cost of W is strictly positive: solutioninthe(cid:77)(cid:67)(cid:70)inadistributedmanneraslongasthe
input parameters c, f, and u are integral. We state this as
(cid:88) N the following corollary of Theorem 4.1.
c∗ =c∗(cid:52)W(cid:53)
i=−N (cid:226)(cid:52)e i (cid:48)(cid:53) Corollary 5.2. Consider an instance of (cid:77)(cid:67)(cid:70) with inte-
=c∗(cid:52)P(cid:53)+ (cid:88) k c∗(cid:52)C (cid:53) gral c, f, and u. Suppose c max =max e∈E c e . Suppose the
j BP Algorithm 2 runs for N =n2c +n iterations. Let
max
j=1 z∗∈argminbN(cid:52)z(cid:53). Then
(cid:190)−L+k(cid:132)(cid:52)x∗(cid:53)
∀
e
e∈E(cid:49) min
e
(cid:0) bN(cid:52)z∗−1(cid:53)(cid:49)bN(cid:52)z∗+1(cid:53) (cid:1) L e e e e
>−L+ (cid:132)(cid:52)x∗(cid:53)=0(cid:48) >nc +bN(cid:52)z∗(cid:53) (11)
(cid:132)(cid:52)x∗(cid:53) max e e
if and only if the (cid:77)(cid:67)(cid:70) instance has a unique solution.
LetFWD=(cid:56)e∈X(cid:50)y e ∗>x (cid:226) ∗ (cid:52)e(cid:53) (cid:57),BCK=(cid:56)e∈X(cid:50)y e ∗<x (cid:226) ∗ (cid:52)e(cid:53) (cid:57). Proof. Wefirstestablishtheimplicationthatif(cid:77)(cid:67)(cid:70)hasa
Because both FWD and BCK are finite, there exists (cid:139)>0
uniqueoptimalsolution,then(11)holds.Tothatend,letus
such that y∗ −(cid:139)(cid:190)x∗ , ∀e∈FWD and y∗ +(cid:139)(cid:182)x∗ ,
e (cid:226)(cid:52)e(cid:53) e (cid:226)(cid:52)e(cid:53) suppose that the instance of (cid:77)(cid:67)(cid:70) of interest has a unique
∀e∈BCK. Define y˜∈(cid:18) (cid:151)E(cid:52)Te N 0 (cid:53)(cid:151) as solution. Consider any edge e ∈ E and its computation
treeTN.ThenfromLemma5.1,itfollowsthatz∗ isanopti-
 y∗−(cid:139) e∈FWD mal a e ssignment of the root edge e(cid:48) of TN with e respect to
y˜ =  y e ∗+(cid:139) e∈BCK the associated optimization problem (cid:77)(cid:67)(cid:70) e N e . Now suppose
e 0 e otherwise(cid:48) that y is an optimal solution of (cid:77)(cid:67)(cid:70) N e with the additional
constraint that flow on the root edge e(cid:48) of TN, denoted by
e
y ,isfixedtovaluez∗−1.Then,usingargumentssimilarto
e(cid:48) e
They˜ canbethoughtofasflowthatisobtainedbypushing thoseusedintheproofofTheorem4.1,itcanbeshownthat
(cid:139) units of additional flow along path W over the existing there exists an augmenting path W of y with respect to z∗
flowy∗ inTN.Becauseforeache∈FWD,y∗−(cid:139)(cid:190)x∗ (cid:190) of length 2n2c in TN. As before, W can be decomposed
0, and for e e a 0 ch e∈BCK, y∗+(cid:139)(cid:182)x∗ (cid:182)u e , y˜ sat (cid:226) i (cid:52) s e fi (cid:53) es intoatleast2n m c ax dis e j 0 ointsimplecyclesandasimplepath.
e (cid:226)(cid:52)e(cid:53) (cid:226)(cid:52)e(cid:53) max
all the flow constraints. Further, because all edges in FWD Now each cycle has a cost of at least (cid:132)(cid:52)x∗(cid:53), which is at
have the same orientation as e and those in BCK have the least 1 because (cid:77)(cid:67)(cid:70) has integral data. Because the (cid:77)(cid:67)(cid:70)
0
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
. 65:71
ta
,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
OperationsResearch60(2),pp.410–428,©2012INFORMS 423
and (cid:77)(cid:67)(cid:70) N have integral parameters, the y and x∗ can be 6. Network Flow: Piecewise-Linear
e
restricted to be integral. Therefore, the augmenting path W Convex Objective
must allow for pushing at least one unit amount of flow to
ThissectiondescribestheextensionofTheorem4.1forthe
modify y to result in the decrease of its cost by at least
network flow problem with piecewise-linear convex objec-
nc . This is because (a) the increase, due to pushing a
max tiveorcostfunction.Specifically,givenagraphG=(cid:52)V(cid:49)E(cid:53)
unit amount of flow on the simple path, could be at most
as before, consider
nc , and (b) decrease along (at least) 2nc cycles is
max max
(cid:88) at least 2nc . In summary, the modified solution is feasi- minimize c (cid:52)x (cid:53)
max e e
blefor(cid:77)(cid:67)(cid:70) N e onT e N withcostdecreasedbyatleastnc max . e∈E
Therefore, it would follow that the optimal cost bN(cid:52)z∗(cid:53) for (cid:88)
e e subject to (cid:227)(cid:52)v(cid:49)e(cid:53)x =f (cid:49) ∀v∈V
(cid:77)(cid:67)(cid:70) N e is less than b e N(cid:52)z∗ e −1(cid:53)−nc max . In a very similar e∈Ev e v ((cid:67)(cid:80))
manner, it can be argued that bN(cid:52)z∗(cid:53)<bN(cid:52)z∗+1(cid:53)−nc . (demand/supply constraints)
e e e e max
This concludes that min(cid:52)bN(cid:52)z∗+1(cid:53)(cid:49)bN(cid:52)z∗−1(cid:53)(cid:53) is at least
bN(cid:52)z∗(cid:53)+nc .
e e e e 0(cid:182)x
e
(cid:182)u
e
(cid:49) ∀e∈E
e e max (nonnegativity constraints)(cid:49)
To establish the other side of the equivalence, suppose
(cid:77)(cid:67)(cid:70) does not have a unique optimal solution. Consider where c (cid:50) (cid:18)→(cid:18) is a piecewise-linear convex function for
e
any arc e ∈ E, corresponding computation tree T e N, and each e∈E. As before, we shall assume that the (cid:67)(cid:80) is optimization problem (cid:77)(cid:67)(cid:70) N e . Let e(cid:48) be the root arc of feasible. Let (cid:150) be the same as before, and define
TN as before. Let y be the optimal assignment of (cid:77)(cid:67)(cid:70) N
e e (cid:40)
with the assignment for root arc e(cid:48) being y =z∗. Now, c (cid:52)z(cid:53) if 0(cid:182)z(cid:182)u
e(cid:48) e (cid:148) (cid:52)z(cid:53)= e e because (cid:77)(cid:67)(cid:70) has multiple optimal solutions, there exists e (cid:136) otherwise(cid:48)
another optimal assignment x∗ of (cid:77)(cid:67)(cid:70) so that x∗ (cid:54)=z∗.
e e Indeed, given that both (cid:77)(cid:67)(cid:70) N and (cid:77)(cid:67)(cid:70) are integral, we Algorithm 2 on G with functions (cid:150) and (cid:148) thus defined
e
can restrict our attention to z∗, x∗, and y having integral is the BP for this problem instance. Before we state
components. Because x∗(cid:54)=z∗, using arguments similar to our result, we need to define the corresponding residual
e e
thoseusedintheproofofTheorem4.1,itisindeedpossible graph. Suppose x is a feasible solution for (cid:67)(cid:80). Define
to find an augmenting path W, of length 2N, on TN with the residual graph of G and x, denoted by G(cid:52)x(cid:53) as fol-
e
respecttoy andx∗.Thisaugmentingpathdecomposesinto lows: ∀e =(cid:52)v (cid:49)v (cid:53)∈E, if x <u , then e is an arc in
(cid:129) (cid:130) e e
one simple path P of length at most n−1 and at least G(cid:52)x(cid:53) with cost cx=lim (cid:52)(cid:52)c(cid:52)x +t(cid:53)−c(cid:52)x (cid:53)(cid:53)/t(cid:53); if x >
e t↓0 e e e
2nc simple cycles. Because x∗ is an optimal solution, 0, then there is an arc e(cid:48)=(cid:52)v (cid:49)v (cid:53) in G(cid:52)x(cid:53) with cost cx =
max (cid:130) (cid:129) e(cid:48)
the cost of each of the cycles with respect to the residual lim (cid:52)(cid:52)c(cid:52)x (cid:53)−c(cid:52)x −t(cid:53)(cid:53)/t(cid:53). Finally, let
t↓0 e e
graph G(cid:52)x∗(cid:53) is nonpositive (it is not strictly negative like
(cid:26) (cid:27)
the proof of Theorem 4.1 because the x∗ is not unique). (cid:132)(cid:52)x(cid:53)=min (cid:88) cx (cid:49)
e
Thecostofthepath,however,isbetween−(cid:52)n−1(cid:53)c max and C∈(cid:67) e∈C
(cid:52)n−1(cid:53)c . Therefore, by pushing the unit amount of flow
max where (cid:67) is the set of all directed simple cycles in G(cid:52)x(cid:53).
(which is possible along this augmenting path W due to
We state the result about the convergence property of BP.
integrality of x∗ and y), the resulting flow y˜ on TN is such
that its total cost is at most (cid:52)n−1(cid:53)c more than e the cost Theorem 6.1. Suppose x∗ is the unique optimal solution
max
ofy.Noweithery˜ =z∗−1orz∗+1.Supposey˜ =z∗−1. for (cid:67)(cid:80), and hence (cid:132)(cid:52)x∗(cid:53)>0. Let L be the maximum cost
In that case, the y˜ e i (cid:48) s a f e easible so e lution of (cid:77)(cid:67)(cid:70) e N (cid:48) wit e h the of a simple directed path in G(cid:52)x∗(cid:53). Then, for any N (cid:190)
e
additional constraint that the root arc e(cid:48) has flow z∗−1. (cid:52)(cid:143)L/(cid:52)2(cid:132)(cid:52)x∗(cid:53)(cid:53)(cid:144)+1(cid:53)n, xˆN =x∗.
e
This cost is no less than the cost of an optimal solution of
The proof of Theorem 6.1 is identical to that of Theo-
(cid:77)(cid:67)(cid:70) N e with the additional constraint that the root arc e(cid:48) rem4.1withtheabove-definednotions.Therefore,weshall
has flow z∗−1, which is defined as bN(cid:52)z∗−1(cid:53). Putting all
e e e skip it.
this together, we obtain
bN(cid:52)z∗−1(cid:53)(cid:182)bN(cid:52)z∗(cid:53)+nc (cid:48) 7. Integral (cid:77)(cid:67)(cid:70): Run-Time Analysis
e e e e max
of BP
In a similar manner, if y˜ =z∗+1, then we would con-
e(cid:48) e
clude that Inthenexttwosections,weshallconsider(cid:77)(cid:67)(cid:70)withinte-
bN(cid:52)z∗+1(cid:53)(cid:182)bN(cid:52)z∗(cid:53)+nc (cid:48) gralcomponentsforc,u,andf.Ourgoalistoanalyzethe
e e e e max run time of BP for such integral (cid:77)(cid:67)(cid:70).
That is, we have established that if (cid:77)(cid:67)(cid:70) does not have a
unique optimal solution, then
Lemma 7.1. For an integral (cid:77)(cid:67)(cid:70), the total number of
operationsperformedbyAlgorithm2toupdateallthemes-
min (cid:0) b e N(cid:52)z∗ e −1(cid:53)(cid:49)b e N(cid:52)z∗ e +1(cid:53) (cid:1)(cid:182)b e N(cid:52)z∗ e (cid:53)+nc max (cid:48) sages at iteration t is O(cid:52)tc max mlogn(cid:53).
This completes the proof of the other side of equivalence, Proof. Recall that for edge e ∈E with v as one of its
and hence the proof of Corollary 5.2. (cid:131) end points (and w at the other), the message function is
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
65:71
ta
,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
424 OperationsResearch60(2),pp.410–428,©2012INFORMS
updated as integer D, set the costs of edges as c =c =D, c =
e1 e2 e3
2D−1; demands as b =1, b =0, and b =−1. It can
(cid:26) (cid:27) v1 v2 v3
mt (cid:52)z(cid:53)=(cid:148) (cid:52)z(cid:53)+ min (cid:150) (cid:52)z¯(cid:53)+ (cid:88) mt−1 (cid:52)z¯ (cid:53) (cid:48) be checked that xˆ 1 N alternates between 1 and −1 when
e→v e z¯∈(cid:18)(cid:151)Ew(cid:151)(cid:49)z¯e=z w
e˜∈Ew\e
e˜→w e˜ 2N +1<(cid:52)2D(cid:53)/3. This means that the BP algorithm takes
atleast(cid:236)(cid:52)D(cid:53)iterationstoconverge.Becausetheinputsize
From Corollary 4.12, all of the message functions have is (cid:228)(cid:52)logD(cid:53), we have that Algorithm 2 for (cid:77)(cid:67)(cid:70) does not
integral slopes for an instance of (cid:77)(cid:67)(cid:70) with integral com- convergetotheuniqueoptimalsolutioninpolynomialtime
ponents. The absolute values of these slopes are bounded in the size of the input.
by (cid:52)t−1(cid:53)c . This implies that each (convex piecewise-
max
linear) message (function) has at most 2(cid:52)t−1(cid:53)c max linear 7.1. Run Time of BP for Integral (cid:77)(cid:67)(cid:70) o
pieces. By Theorem 4.9 and Observation 4.10 it follows
HereweanalyzetheruntimeofBPforintegral(cid:77)(cid:67)(cid:70) o,the
that g(cid:52)z(cid:53) can be computed in O(cid:52)tc (cid:151)E (cid:151)log(cid:151)E (cid:151)(cid:53) =
max w w subclassof(cid:77)(cid:67)(cid:70)definedin§4.2,andproveTheorem4.14.
O(cid:52)tc (cid:151)E (cid:151)logn(cid:53) total operations because (cid:151)E (cid:151)(cid:182)n. Here,
max w w
ProofofTheorem4.14. Because(cid:77)(cid:67)(cid:70) o isaninstanceof
(cid:26) (cid:27)
g(cid:52)z(cid:53)= min (cid:150) (cid:52)z¯(cid:53)+ (cid:88) mt−1 (cid:52)z¯ (cid:53) (cid:48) (cid:77)(cid:67)(cid:70)withintegralcomponentsandauniqueoptimalsolu-
z¯∈(cid:18)(cid:151)Ew(cid:151)(cid:49)z¯e=z w
e˜∈Ew\e
e˜→w e˜ tion, from Theorem 4.1 it follows that the BP Algorithm 2
converges to the optimal solution within O(cid:52)Ln(cid:53) iterations.
Now, computing g(cid:52)z(cid:53)+(cid:148) (cid:52)z(cid:53) is a simple procedure that Toboundcomputationperformedineachiterationandsub-
e
requires increasing the slopes of linear pieces of g(cid:52)z(cid:53) by sequently bound overall computation cost, without loss of
a constant. Because g(cid:52)·(cid:53) has at most 2tc linear pieces, generality we shall assume that the piecewise-linear con- max
computing g(cid:52)z(cid:53)+(cid:148) (cid:52)z(cid:53) takes further O(cid:52)tc (cid:53) operations. vex message function is such that each linear piece is of
e max
In summary, it follows that all message updates can be unit length. This assumption is without loss of generality,
performed in a total of O(cid:52)tc mlogn(cid:53) operations because because each linear piece has integral vertices from Corol-
max
(cid:80) (cid:151)E (cid:151)=(cid:228)(cid:52)m(cid:53). (cid:131) lary 4.13, and hence assumption of each piece being unit
w w
length only leads to upper bound on computation. Now
We now complete the proof of Theorem 4.2.
each message function is defined on a uniformly bounded
Proof of Theorem 4.2. The integral instance of (cid:77)(cid:67)(cid:70) interval due to uniform bound K on the capacity of each
with a unique optimal solution has (cid:132)(cid:52)x∗(cid:53)(cid:190)1. Therefore, edge in (cid:77)(cid:67)(cid:70) o. Therefore, the number of pieces in each
by Theorem 4.1, the BP Algorithm 2 converges after at piecewise-linear convex message function is bounded by
most O(cid:52)nL(cid:53) iterations. By Lemma 7.1, the total com- K+1. Recall that for t(cid:190)1,
putation performed up to iteration t is O(cid:52)mlognc t2(cid:53).
max (cid:26) (cid:27)
Therefore, the total computation performed until conver- mt (cid:52)z(cid:53)=(cid:148) (cid:52)z(cid:53)+ min (cid:150) (cid:52)z¯(cid:53)+ (cid:88) mt−1 (cid:52)z¯ (cid:53) (cid:48)
e→v e w e˜→w e˜
gence is O(cid:52)mlognc
max
n2L2(cid:53). The L can be bounded as z¯∈(cid:18)(cid:151)Ew(cid:151)(cid:49)z¯e=z
e˜∈Ew\e
L=O(cid:52)nc (cid:53). Therefore, it follows that the overall cost is
max
at most O(cid:52)mn4c3 logn(cid:53). (cid:131) As explained in detail in §4.1, specifically Lemma 4.6 and
max
Theorem4.9,computingmt takesatmostO(cid:52)Klog(cid:151)E (cid:151)(cid:53),
The bound of Theorem 4.2 is pseudopolynomial time. which is O(cid:52)Klogn(cid:53) becau e s → e v (cid:151)E (cid:151)(cid:182)n for all w. Beca w use
In fact, qualitatively this is the best bound one can hope w
there are at most O(cid:52)m(cid:53) messages, total computation per
for. To see this, consider an example of (cid:77)(cid:67)(cid:70) defined iteration is O(cid:52)Kmlogn(cid:53). As discussed earlier, it takes
on a directed graph G as shown in Figure 6. Given large
O(cid:52)Ln(cid:53) iterations for the algorithm to converge. Therefore,
overall computation scales O(cid:52)KLmnlogn(cid:53). Finally, due to
Figure 6. An (cid:77)(cid:67)(cid:70) instance with exponential running
auniformboundofK onthecostofedges,L=O(cid:52)nc (cid:53)=
time. max
O(cid:52)nK(cid:53).Insummary,thetotalcomputationcostisbounded
v above by O(cid:52)K2mn2logn(cid:53). (cid:131)
2
e 8. FPRAS for (cid:77)(cid:67)(cid:70) Using BP
2
Inthissection,weprovideafullypolynomial-timerandom-
ized approximation scheme (FPRAS) for (cid:77)(cid:67)(cid:70), using BP
asasubroutine.Asmentionedearlier,weshallassumeinte-
e 1 v 3 gral (cid:77)(cid:67)(cid:70). We start by describing the insights behind the
algorithm, followed by precise description in §8.2. To this
end,recallthatthekeyhurdlesinmakingBPfullypolyno-
e
3 mial time as indicated by Theorem 4.2 are the following:
1. The convergence of BP requires (cid:77)(cid:67)(cid:70) to have a
v 1 unique optimal solution.
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
65:71
ta
,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

Gamarnik,Shah,andWei: BeliefPropagationforMin-CostNetworkFlow
OperationsResearch60(2),pp.410–428,©2012INFORMS 425
2. The running time of BP is polynomial in m, n, hand, if c¯ <(cid:129), then for any feasible solution x of (cid:77)(cid:67)(cid:70)
and c . where x e = 1 0, we have
There
m
fo
ax
re, to find FPRAS for any given instance of (cid:77)(cid:67)(cid:70),
e1
we need to overcome the requirement of uniqueness and (cid:88) c¯ x∗∗ (cid:52) < a(cid:53) (cid:88) c¯ x∗∗+(cid:129)x∗∗
dependence over c max of running time. To do so, we shall e∈E
e e
e∈E(cid:49)e(cid:54)=e1
e e e1
utilize the appropriate randomized modification of the cost
vectorsothattheresultingproblemwithmodifiedcostvec- (cid:52) (cid:182) b(cid:53) (cid:88) c¯ x +(cid:129)x
e e e1
tor c¯ has the following properties: e∈E(cid:49)e(cid:54)=e1
1. The modified problem has a unique optimal solution (cid:88)
= c¯ x (cid:48)
with high probability. e e
e∈E
2. The modified cost vector has c¯ polynomial in m,
max Above, (a) follows from x∗∗>0 and c¯ <(cid:129); (b) follows
n, and 1/(cid:152).
from x∗∗ being an optimal
e1
solution wit
e
h
1
c¯ =(cid:129). In sum-
3. The optimal solution of the modified problem pro- e1
mary, there exists at most one value for (cid:129) such that when
vides a 1+(cid:152) multiplicative approximation to the optimal
c¯ =(cid:129), (cid:77)(cid:67)(cid:70) has two solutions x∗, x∗∗ with x∗ =0 and
solution of (cid:77)(cid:67)(cid:70). x e ∗ 1 ∗ > 0. In a similar manner, it can be establ e i 1 shed that
Itseemsintuitivethatbyaddingenoughrandomnesstothe e1
there exists at most one value (cid:130) such that with c¯ =(cid:130),
cost vector, the modified problem will have a unique solu- e1
(cid:77)(cid:67)(cid:70) has two optimal solutions x∗, x∗∗ with x∗ <u and
tion with high probability. However, requiring the result-
x∗∗=u .
e1 e1
ing cost vector to be polynomially small in m, n, and e1 e1
1/(cid:152) as well as having a small approximation error is chal- Let (cid:79) be the set of all optimal solutions of (cid:77)(cid:67)(cid:70). From
lenging, and a priori not clear if it is even feasible. The the above discussion, it follows that for a given arc e, if
so-called Isolation Lemma introduced in Mulmuley et al.
c¯
e
ischosenuniformlyatrandomfrom4mdistinctpositive
(1987) helps to address precisely this question for a spe- integers, then the probability that there exist two solutions
cific class of combinatorial problems, including matching. x∗, x∗∗ in (cid:79) that satisfy either x e ∗ =0, x e ∗∗ >0 or x e ∗ <
It is not directly applicable to our setup, primarily because u e , x e ∗∗=u e is at most 1/(cid:52)2m(cid:53). Therefore, with probabil-
the Isolation Lemma requires the feasible set of the opti- ity at least 1−1/(cid:52)2m(cid:53), all solutions x in (cid:79) satisfy either
mization problem to be a monotone subset of (cid:56)0(cid:49)1(cid:57)M (for x e =0 or 0 <x e <u e or x e =u e . Denote this event by
(cid:84) appropriateM),whereasthefeasiblesetofinteresthereisa D(cid:52)e(cid:53). By union, bound e∈E D(cid:52)e(cid:53) holds with probability
at least 1/2. Now to conclude the proof of Theorem 8.1,
polytope derived from a linear programming problem. For
we state the following lemma.
this reason, we state and prove a variation of the Isolation
Lemma for our setup next. Lemma 8.2. Under event (cid:84) D(cid:52)e(cid:53), the (cid:77)(cid:67)(cid:70) has a
e∈E
unique optimal solution.
8.1. Variation of the Isolation Lemma
Proof. Supposetothecontrarythatunderevent (cid:84) D(cid:52)e(cid:53),
Theorem 8.1. Let (cid:77)(cid:67)(cid:70) be an instance of the min-cost (cid:77)(cid:67)(cid:70) has two distinct optimal solutions x∗ and e∈ x E ∗∗. Let
flow problem with underlying graph G=(cid:52)V(cid:49)E(cid:53), demand d=x∗∗−x∗; then x∗+(cid:139)d is an optimal solution of (cid:77)(cid:67)(cid:70)
vector b, constraint vector u. Let its cost vector c¯ be gen- iff 0(cid:182)(cid:52)x∗+(cid:139)d(cid:53) (cid:182)u , ∀e∈E. Because c¯ >0 for any
e e e
erated as follows: for each e∈E, c¯ e is chosen indepen- e∈E andc¯Td=c¯Tx∗∗−c¯Tx∗=0,thereexistssomee(cid:48)∈E
dently and uniformly over N e , where N e is a discrete set of suchthatd e(cid:48) <0.Let
4m positive numbers (m=(cid:151)E(cid:151)). Then, the probability that
(cid:77)(cid:67)(cid:70) has a unique optimal solution is at least 1. (cid:139)∗=sup (cid:8) (cid:139)(cid:190)0(cid:50) x∗+(cid:139)d is a feasible solution of (cid:77)(cid:67)(cid:70) (cid:9) (cid:48)
2
Proof. Fix an arc e ∈E and fix c¯ for all e∈E\e . First Because d <0, (cid:139)∗ is bounded and because x∗+d=x∗∗,
1 e 1 e(cid:48)
suppose that there exists a value (cid:129)(cid:190)0 such that when (cid:139)∗(cid:190)1. Further, the supremum (cid:139)∗ is achieved, that is, x∗+
c¯ =(cid:129),(cid:77)(cid:67)(cid:70)hastwooptimalsolutionsx∗,x∗∗ and,more- (cid:139)∗d is a feasible solution of (cid:77)(cid:67)(cid:70) because the feasible
o e v 1 er, x∗ =0 and x∗∗>0. Then, if c¯ >(cid:129), for any feasible space of (cid:77)(cid:67)(cid:70) is a closed set. By definition of (cid:139)∗, there
solution
e1
x of (cid:77)(cid:67)(cid:70)
e1
with x e1 >0,
e1
(cid:139)
m
∗
u
d
s
(cid:53)
t ex
=
ist
0
s
o
o
r
me
u
e
.
(cid:48)(cid:48)
B
su
e
c
c
h
au
t
s
h
e
at
(cid:139)∗
x e ∗
>
(cid:48)(cid:48) (cid:54)=
0,
x
x
e ∗ (cid:48) ∗ (cid:48)
∗
a
(cid:54)=
nd
(cid:52)x
e
∗
ith
+
er
(cid:139)
(cid:52)
∗
x
d
∗
(cid:53)
+
.
(cid:88) (cid:88) e(cid:48)(cid:48) e(cid:48)(cid:48) e(cid:48)(cid:48) e(cid:48)(cid:48)
c¯ x∗= c¯ x∗ That is, we have two solutions x∗ and x∗+(cid:139)∗d that do not
e e e e
e∈E e∈E(cid:49)e(cid:54)=e1 satisfy D(cid:52)e(cid:48)(cid:48)(cid:53). This contradicts the hypothesis, and hence
(cid:52) (cid:182) a(cid:53) (cid:88) c¯ x +x (cid:129) (cid:77)(cid:67)(cid:70) must have a unique optimal solution. (cid:131)
e e e1 We note that Theorem 8.1 can be easily modified for LP
e∈E(cid:49)e(cid:54)=e1
in the standard form.
(cid:52)b(cid:53)(cid:88)
< c¯ e x e (cid:48) Corollary 8.3. Let (cid:76)(cid:80) be an LP problem with con-
e∈E straint Ax=b, where A is an m×n matrix, b∈(cid:18)m. The
In the above, (a) follows from the fact that x∗ is optimal costvectorc¯of(cid:76)(cid:80)isgeneratedasfollows:foreache∈E,
with c¯ =(cid:129); (b) follows c¯ >(cid:129) and x >0. On the other c¯ is chosen independently and uniformly over N , where
e1 e1 e1 e e
.devreser
sthgir
lla
,ylno
esu
lanosrep
roF
.
65:71
ta ,5202
lirpA
61
no
]91.112.052.121[
yb
gro.smrofni
morf
dedaolnwoD

|     |     |     |     |     |     |     |     | Gamarnik,Shah,andWei: |     |     | BeliefPropagationforMin-CostNetworkFlow |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --------------------------------------- | --- | --- | --- | --- |
426
OperationsResearch60(2),pp.410–428,©2012INFORMS
N is a discrete set of 2n elements. Then, the probability e(cid:48)=argmaxc , ties broken arbitrarily, and define a new
| e   |     |     |     |     |     |     |     |     |     | e   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that (cid:76)(cid:80) has a unique optimal solution is at least 1. optimization problem (cid:77)(cid:67)(cid:70) as follows:
2
(cid:88)
|      |         |     |         |          |     |     |     | minimize |     |     | c x |     |     |     |     |
| ---- | ------- | --- | ------- | -------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| 8.2. | Finding | the | Correct | Modified |     |     |     |          |     |     | e e |     |     |     |     |
e∈E
c¯
|     | Cost | Vector |     |     |     |     |     |         |     | (cid:88) |                                      |     |               |     |     |
| --- | ---- | ------ | --- | --- | --- | --- | --- | ------- | --- | -------- | ------------------------------------ | --- | ------------- | --- | --- |
|     |      |        |     |     |     |     |     | subject |     | to       | (cid:227)(cid:52)v(cid:49)e(cid:53)x | =b  | (cid:49) ∀v∈V |     |     |
e v
Next,weconstructarandomlygeneratedcostvectorc¯with
 .devreser sthgir lla ,ylno esu lanosrep roF . 65:71 ta ,5202 lirpA 61 no ]91.112.052.121[ yb gro.smrofni morf dedaolnwoD e∈Ev ((cid:77)(cid:67)(cid:70))
thedesiredpropertiesstatedinthebeginningofthissection. (demand/supply constraints)
LetX(cid:50)E→(cid:56)1(cid:49)2(cid:49)(cid:48)(cid:48)(cid:48)(cid:49)4m(cid:57)bearandomfunctionwherefor
x =x(cid:52)2(cid:53)
each e∈E, X(cid:52)e(cid:53) is chosen independently and uniformly e(cid:48) e(cid:48)
|     |     |     |     |     |     |     |     |     |     | 0(cid:182)x | (cid:182)u |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | --- | --- | --- |
over the range. Let t=(cid:52)c (cid:152)(cid:53)/(cid:52)4mn(cid:53) and generate c¯ as (cid:49) ∀e∈E (flow constraints).
|          |     |           |     | max              |                                 |     |       |       |     |      | e   | e                  |     |     |     |
| -------- | --- | --------- | --- | ---------------- | ------------------------------- | --- | ----- | ----- | --- | ---- | --- | ------------------ | --- | --- | --- |
| follows: | for | each e∈E, | let | c¯ =4m(cid:143)c | /t(cid:144)+X(cid:52)e(cid:53). |     | Then, |       |     |      |     |                    |     |     |     |
|          |     |           |     | e                | e                               |     |       |       |     |      |     |                    |     |     |     |
|          |     |           |     |                  |                                 |     |       | Lemma |     | 8.5. |     | x(cid:52)3(cid:53) |     |     |     |
c¯ is polynomial in m, n, and 1/(cid:152). By Theorem 8.1, the Suppose is an optimal solution for
max
probability of (cid:77)(cid:67)(cid:70) having a unique optimal solution is ((cid:77)(cid:67)(cid:70)) and x(cid:52)1(cid:53) is an optimal solution of (cid:77)(cid:67)(cid:70). Then
| greater | than | 1/2. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Now we introduce algorithm APRXMT((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)) as cTx(cid:52)3(cid:53)−cTx(cid:52)1(cid:53)(cid:182)(cid:151)x(cid:52)2(cid:53)−x(cid:52)1(cid:53)(cid:151)nt(cid:48)
|          |     |          |        |         |          |                          |       |     |     |     | e(cid:48) | e(cid:48) |     |     |     |
| -------- | --- | -------- | ------ | ------- | -------- | ------------------------ | ----- | --- | --- | --- | --------- | --------- | --- | --- | --- |
| follows. |     | Select a | random | c¯; try | to solve | (cid:77)(cid:67)(cid:70) | using |     |     |     |           |           |     |     |     |
BP. If BP discovers that (cid:77)(cid:67)(cid:70) has no unique optimal Proof. Let d =x(cid:52)2(cid:53) −x(cid:52)1(cid:53). Call (cid:131) ∈(cid:56)−1(cid:49)0(cid:49)1(cid:57)(cid:151)E(cid:151) a syn-
solution (using Corollary 5.2), then restart the procedure chronous cycle vector of d if for any e∈E, (cid:131) =1 only if
e
by selecting another c¯ at random; otherwise, return the d >0, (cid:131) =−1 only if d <0, and the set (cid:56)e∈E(cid:50) (cid:131) =1
|        |                 |     |       |       |             |     |         |     | e                     | e     |         | e   |          |          | e      |
| ------ | --------------- | --- | ----- | ----- | ----------- | --- | ------- | --- | --------------------- | ----- | ------- | --- | -------- | -------- | ------ |
|        |                 |     |       |       |             |     |         | or  | (cid:131) =−1(cid:57) | forms | exactly | one | directed | cycle in | G. Now |
| unique | optimalsolution |     | found | byBP. | Formally,we |     | present |     | e                     |       |         |     |          |          |        |
APRXMT((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)) as Algorithm 3. d is an integral vector of circulation (i.e., d sends 0 unit
|           |     |                                                     |     |     |     |     |     | amount  |     | of flow | to every | vertex    | v∈V)   | because it   | is the dif- |
| --------- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | ------- | -------- | --------- | ------ | ------------ | ----------- |
| Algorithm |     | 3 APRXMT((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)) |     |     |     |     |     |         |     |         |          |           |        |              |             |
|           |     |                                                     |     |     |     |     |     | ference |     | of two  | feasible | solutions | of the | same network | flow        |
(cid:80)
1: Let t=(cid:52)c (cid:152)(cid:53)/(cid:52)4mn(cid:53), for any e∈E, assign problem. Therefore, d can be decomposed as (cid:131)=d
|     |     | max |     |     |     |     |     |     |     |     |     |     |     | (cid:131)∈(cid:75)(cid:48) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- |
with(cid:75)(cid:48)⊂(cid:75)and(cid:75)beingafinitesetofsynchronouscycle
|     | c¯ =4m·(cid:143)c | /t(cid:144)+p | ,   | where | p is an |     |     |     |     |     |     |     |     |     |     |
| --- | ----------------- | ------------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | e                 | e             | e   |       | e       |     |     |     |     |     |     |     |     |     |     |
integer chosen independently, uniformly random vectors of G (cf. see Ahuja et al. 1993). For any (cid:131)∈(cid:75)(cid:48),
(cid:56)1(cid:49)2(cid:49)(cid:48)(cid:48)(cid:48)(cid:49)4m(cid:57). observe that x(cid:52)2(cid:53)−(cid:131) is a feasible solution for (cid:77)(cid:67)(cid:70). Now,
from
2: Let (cid:77)(cid:67)(cid:70) be the problem with modified cost c¯. because x(cid:52)2(cid:53) is an optimal solution for (cid:77)(cid:67)(cid:70), it follows
|     |               |     |                             |     |        |     |     | that | c¯T(cid:131)(cid:182)0. | Now | for | any e∈E, |     |     |     |
| --- | ------------- | --- | --------------------------- | --- | ------ | --- | --- | ---- | ----------------------- | --- | --- | -------- | --- | --- | --- |
| 3:  | Run Algorithm | 2   | on (cid:77)(cid:67)(cid:70) | for | N =2c¯ | n2  |     |      |                         |     |     |          |     |     |     |
max
iterations.
|     |     |     |     |     |     |     |     |     |     | (cid:22) (cid:23) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
c
4: Use Corollary 5.2 to determine if (cid:77)(cid:67)(cid:70) has a c¯ = 4m e +p (cid:49) 1(cid:182)p (cid:182)4m(cid:49)
|     |        |           |     |     |     |     |     | e   |     | t   | e        |                   | e                |                           |     |
| --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | ---------------- | ------------------------- | --- |
|     | unique | solution. |     |     |     |     |     |     |     |     |          |                   |                  |                           |     |
|     |        |           |     |     |     |     |     |     |     |     | (cid:20) | (cid:22) (cid:23) | (cid:18)(cid:22) | (cid:23) (cid:19)(cid:21) |     |
5: if (cid:77)(cid:67)(cid:70) does not have a unique solution then 4mc c c
|     |     |     |     |     |     |     |     |     | ⇒c¯ (cid:49) | e   | ∈ 4m | e (cid:49)4m | e   | +1 (cid:49) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---- | ------------ | --- | ----------- | --- |
6: Restart the procedure APRXMT((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)). e t t t
| 7:  | else |     |     |     |     |     |     |     | (cid:12) |     | (cid:12)  |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --------- | --- | --- | --- | --- |
|     |      |     |     |     |     |     |     |     | (cid:12) | 4mc | e(cid:12) |     |     |     |     |
8: Terminate and return x(cid:52)2(cid:53)=xˆN, where xˆN is the ⇒ (cid:12)c¯ − (cid:12) (cid:182)4m(cid:49)
|                                                      |           |            |                                      |                  |     |            |         |       | e                    | t                        |                                |                         |                                                  |         |     |
| ---------------------------------------------------- | --------- | ---------- | ------------------------------------ | ---------------- | --- | ---------- | ------- | ----- | -------------------- | ------------------------ | ------------------------------ | ----------------------- | ------------------------------------------------ | ------- | --- |
|                                                      |           |            |                                      |                  |     |            |         |       | (cid:12)             |                          | (cid:12)                       |                         |                                                  |         |     |
|                                                      | estimate  | of optimal |                                      | flow assignments |     | found      | in      |       |                      |                          |                                |                         |                                                  |         |     |
|                                                      |           |            |                                      |                  |     |            |         |       |                      | (cid:12)                 | (cid:12)                       |                         |                                                  |         |     |
|                                                      | Algorithm | 2.         |                                      |                  |     |            |         |       | (cid:88)(cid:12)     | 4mc                      | (cid:12)                       |                         | (cid:88)                                         |         |     |
|                                                      |           |            |                                      |                  |     |            |         |       | ⇒                    | (cid:12) e               | −c¯ (cid:12)(cid:151)(cid:131) | (cid:151)(cid:182)4m    | (cid:151)(cid:131) (cid:151)(cid:182)4mn(cid:48) |         |     |
|                                                      |           |            |                                      |                  |     |            |         |       |                      |                          | e(cid:12)                      | e                       | e                                                |         |     |
| 9:                                                   | end if    |            |                                      |                  |     |            |         |       |                      | (cid:12) t               |                                |                         |                                                  |         |     |
|                                                      |           |            |                                      |                  |     |            |         |       | e                    |                          |                                |                         | e                                                |         |     |
| Corollary                                            |           | 8.4.       |                                      |                  |     |            |         |       |                      |                          |                                |                         |                                                  |         |     |
|                                                      |           |            | The APRXMT((cid:77)(cid:67)(cid:70), |                  |     | (cid:152)) | runs in |       |                      |                          |                                | c¯T(cid:131)(cid:182)0, |                                                  |         |     |
|                                                      |           |            |                                      |                  |     |            |         | Using | this                 | and                      | the fact                       | that                    |                                                  | we have |     |
| O(cid:52)(cid:52)n8m7logn(cid:53)/(cid:152)3(cid:53) |           |            | expected                             | time.            |     |            |         |       |                      |                          |                                |                         |                                                  |         |     |
|                                                      |           |            |                                      |                  |     |            |         | 4m    |                      | 4m                       |                                |                         |                                                  |         |     |
| Proof.                                               |           |            |                                      |                  |     |            |         |       | cT(cid:131)(cid:182) | cT(cid:131)−c¯T(cid:131) |                                |                         |                                                  |         |     |
Theorem8.1impliesthatonaverageO(cid:52)1(cid:53)instances
|     |                          |              |       |        |        |     |           |     | t   | t                             |     |          |     |     |     |
| --- | ------------------------ | ------------ | ----- | ------ | ------ | --- | --------- | --- | --- | ----------------------------- | --- | -------- | --- | --- | --- |
| of  | (cid:77)(cid:67)(cid:70) | are required | to be | solved | by the | BP. | Each such |     |     |                               |     |          |     |     |     |
|     |                          |              |       |        |        |     |           |     |     | (cid:12)                      |     | (cid:12) |     |     |     |
|     |                          |              |       |        |        |     | 2c¯       |     |     | (cid:182)(cid:88) (cid:12) 4m | c   | (cid:12) |     |     |     |
i n s ta n c e r e q u ir e s r u nn i n g A l g o ri t h m 2 f or O (cid:52) n (cid:53) i t er a - (cid:12) e −c¯ (cid:12) (cid:151)(cid:131) (cid:151)
|      |             |                 |            |             |           |                                                  | ma x                   |     |     | (cid:12)             | t   | e (cid:12) e |     |     |     |
| ---- | ----------- | --------------- | ---------- | ----------- | --------- | ------------------------------------------------ | ---------------------- | --- | --- | -------------------- | --- | ------------ | --- | --- | --- |
| t io | n s . T h e | r e fo r e , th | e t o t al | c o s t s c | a les a s | O (cid:52)c ¯ 3                                  | m n 4 l o g n (cid:53) |     |     |                      |     |              |     |     |     |
|      |             |                 |            |             |           | max                                              |                        |     |     | e                    |     |              |     |     |     |
|      |             |                 |            |             |           | =O(cid:52)(cid:52)m2n(cid:53)/(cid:152)(cid:53), |                        |     |     | (cid:182)4mn(cid:48) |     |              |     |     |     |
| on   | average     | by Lemma        | 7.1.       | Because     | c¯        |                                                  | it                     |     |     |                      |     |              |     |     |     |
max
| isboundedasO(cid:52)(cid:152)−3m7n7logn(cid:53). |     |     |     |     | (cid:131) |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cT(cid:131)(cid:182)nt.
|     |         |           |          |        |     |        |            | Therefore,          |          | we         | have       |     | By definition | of (cid:75)(cid:48), | x(cid:52)2(cid:53)= |
| --- | ------- | --------- | -------- | ------ | --- | ------ | ---------- | ------------------- | -------- | ---------- | ---------- | --- | ------------- | -------------------- | ------------------- |
|     | Now let | c¯ be the | randomly | chosen |     | vector | as per the |                     | (cid:80) |            |            |     |               |                      |                     |
|     |         |           |          |        |     |        |            | x(cid:52)1(cid:53)+ |          | (cid:131). | Therefore, | for | all e∈E       |                      |                     |
(cid:131)∈(cid:75)(cid:48)
| above-described |     | procedure |     | such | that (cid:77)(cid:67)(cid:70) | has | a unique |     |     |     |     |     |     |     |     |
| --------------- | --- | --------- | --- | ---- | ----------------------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
optimal solution, say x(cid:52)2(cid:53). Next, we show that x(cid:52)2(cid:53) is a (cid:88)
|                |     |          |     |                           |               |     |           | min(cid:56)x(cid:52)1(cid:53)(cid:49)x(cid:52)2(cid:53)(cid:57)(cid:182)x(cid:52)1(cid:53)+ |     |     |     | (cid:131) | (cid:182)max(cid:56)x(cid:52)1(cid:53)(cid:49)x(cid:52)2(cid:53)(cid:57)(cid:48) |     |     |
| -------------- | --- | -------- | --- | ------------------------- | ------------- | --- | --------- | ------------------------------------------------------------------------------------------- | --- | --- | --- | --------- | -------------------------------------------------------------------------------- | --- | --- |
|                |     |          |     |                           |               |     |           |                                                                                             | e   | e   | e   |           | e                                                                                | e e |     |
| “near-optimal” |     | solution | of  | (cid:77)(cid:67)(cid:70). | To accomplish |     | this, let |                                                                                             |     |     |     |           |                                                                                  |     |     |
(cid:131)∈(cid:75)(cid:48)

| Gamarnik,Shah,andWei: |     |     |     | BeliefPropagationforMin-CostNetworkFlow |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
427
OperationsResearch60(2),pp.410–428,©2012INFORMS
Therefore, it follows that x(cid:52)1(cid:53)+ (cid:80) (cid:131) is a feasible solu- Algorithm 4 AS((cid:77)(cid:67)(cid:70)(cid:49)(cid:152))
(cid:131)∈(cid:75)(cid:48)
tion for (cid:77)(cid:67)(cid:70). Because x(cid:52)3(cid:53) is the optimal solution of 1: Let G=(cid:52)V(cid:49)E(cid:53) be the underlying directed graph of
(cid:77)(cid:67)(cid:70),
|                                                    |     |     |                      |     |     |     |     | (cid:77)(cid:67)(cid:70) |                          | with m=(cid:151)E(cid:151), | n=(cid:151)V(cid:151).                       |          |                           |     |
| -------------------------------------------------- | --- | --- | -------------------- | --- | --- | --- | --- | ------------------------ | ------------------------ | --------------------------- | -------------------------------------------- | -------- | ------------------------- | --- |
|                                                    |     |     |                      |     |     |     |     | 2: while                 | (cid:77)(cid:67)(cid:70) | flows                       | for all                                      | arcs are | not assigned              | do  |
| cTx(cid:52)3(cid:53)(cid:182)cTx(cid:52)1(cid:53)+ |     |     | (cid:88) cT(cid:131) |     |     |     |     |                          |                          |                             |                                              |          |                           |     |
|                                                    |     |     |                      |     |     |     |     | 3: Run                   | APRXMT                   |                             | ((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)), | let      | x(cid:52)2(cid:53) be the |     |
(cid:131)∈(cid:75)(cid:48)
|     |     |     |     |     |     |     |     |     | solution | returned. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | --- | --- | --- |
(cid:182)cTx(cid:52)1(cid:53)+(cid:151)(cid:75)(cid:48)(cid:151)nt(cid:48) 4: Find e(cid:48)=argmax c and modify (cid:77)(cid:67)(cid:70) by fixing
 .devreser sthgir lla ,ylno esu lanosrep roF . 65:71 ta ,5202 lirpA 61 no ]91.112.052.121[ yb gro.smrofni morf dedaolnwoD e∈E e
(cid:52) 2 (cid:53);
(cid:12) (cid:12) (cid:182)(cid:12) (cid:53)(cid:12) t h e fl o w o n a r c e (cid:48) by x c h an g e t he
Because (cid:12)(cid:75)(cid:48) (cid:12)x (cid:52)2 (cid:53)−x (cid:52)1 (cid:12), it follows that e (cid:48)
(cid:12) e (cid:48) e (cid:48) d e m a n ds/ s up p l y o n no d e v(cid:48) , w (cid:48) w it h e(cid:48)=(cid:52)v(cid:48)(cid:49)w(cid:48)(cid:53).
| cTx(cid:52)3(cid:53)−cTx(cid:52)1(cid:53)(cid:182)(cid:151)x(cid:52)2(cid:53)−x(cid:52)1(cid:53)(cid:151)nt(cid:48) |     |     |     |     |     |     |     | 5:end | while |     |     |     |     |     |
| ------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- |
(cid:131)
|           |     |      | e(cid:48) | e(cid:48)                             |     |     |     |         |                                      |       |                                         |           |                                               |           |
| --------- | --- | ---- | --------- | ------------------------------------- | --- | --- | --- | ------- | ------------------------------------ | ----- | --------------------------------------- | --------- | --------------------------------------------- | --------- |
|           |     |      |           |                                       |     |     |     | Theorem | 8.7.                                 | Given | (cid:152) ∈ (cid:52)0(cid:49)1(cid:53), | algorithm | AS((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)) |           |
| Corollary |     | 8.6. | For any   | (cid:152)∈(cid:52)0(cid:49)1(cid:53), |     |     |     |         |                                      |       |                                         |           |                                               |           |
|           |     |      |           |                                       |     |     |     | takes   | O(cid:52)(cid:152)−3n7m8logn(cid:53) |       | operations                              |           | on average.                                   | Let x∗ be |
(cid:18) (cid:19) the solution produced by AS((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)). Then
(cid:152)
| cTx(cid:52)3(cid:53)(cid:182) |     |     | cTx(cid:52)1(cid:53)(cid:48) |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1+
2m
cTx∗(cid:182)(cid:52)1+(cid:152)(cid:53)cTx(cid:52)1(cid:53)(cid:48)
Proof.
|     | By  | Lemma | 8.5 | we may | assume | without | loss of |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | ------ | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
generality that x(cid:52)2(cid:53)(cid:54)=x(cid:52)1(cid:53). Also by Lemma 8.5, Proof. By Corollary 8.4, APRXMT((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)) takes
|                                           |     |     | e(cid:48) e(cid:48)  |                               |     |     |     |                                      |     |            |     |     |                  |     |
| ----------------------------------------- | --- | --- | -------------------- | ----------------------------- | --- | --- | --- | ------------------------------------ | --- | ---------- | --- | --- | ---------------- | --- |
|                                           |     |     |                      |                               |     |     |     | O(cid:52)(cid:152)−3n7m7logn(cid:53) |     | operations |     | on  | average. Because | AS  |
| cTx(cid:52)3(cid:53)−cTx(cid:52)1(cid:53) |     |     | (cid:52)2 (cid:53)−x | (cid:52)1 (cid:53)(cid:151)nt |     |     |     |                                      |     |            |     |     |                  |     |
(cid:151)x ((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)) invokes the method APRXMT((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)) m
|     |     | (cid:182) | e (cid:48) | e (cid:48) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cTx(cid:52)3(cid:53) cTx(cid:52)3(cid:53) times, AS((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)) performs on average total operations
(cid:151)x(cid:52)2(cid:53)−x(cid:52)1(cid:53)(cid:151)nt boundedasO(cid:52)(cid:152)−3n7m8logn(cid:53).Bysuccessiveapplicationof
nt
|     |     | (cid:182) | e(cid:48)            | e(cid:48)                    | =         | (cid:49) | (12) | Corollary | 8.6,     |           |     |     |     |     |
| --- | --- | --------- | -------------------- | ---------------------------- | --------- | -------- | ---- | --------- | -------- | --------- | --- | --- | --- | --- |
|     |     |           | (cid:52)2 (cid:53)−x | (cid:52)1 (cid:53)(cid:151)c | c         |          |      |           |          |           |     |     |     |     |
|     |     |           | (cid:151)x           |                              | e(cid:48) |          |      |           |          |           |     |     |     |     |
|     |     |           | e (cid:48)           | e (cid:48)                   | e(cid:48) |          |      |           |          |           |     |     |     |     |
|     |     |           |                      |                              |           |          |      |           | (cid:18) | (cid:19)m |     |     |     |     |
(cid:152)
wherethelastinequalityfollowsbecauseofcTx(cid:52)3(cid:53)(cid:190)(cid:151)x(cid:52)2(cid:53)− cTx∗(cid:182) 1+ cTx(cid:52)1(cid:53)
|                                                  |           |                                                                 |                    |           |                                       |            | e(cid:48)    |                                                                  |     | 2m  |     |     |     |     |
| ------------------------------------------------ | --------- | --------------------------------------------------------------- | ------------------ | --------- | ------------------------------------- | ---------- | ------------ | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| x(cid:52)1(cid:53)(cid:151)c                     |           |                                                                 |                    |           | x(cid:52)3(cid:53)=x(cid:52)2(cid:53) |            |              |                                                                  |     |     |     |     |     |     |
|                                                  | justified |                                                                 | as follows:        | using     |                                       | by         | definition,  |                                                                  |     |     |     |     |     |     |
| e(cid:48)                                        | e(cid:48) |                                                                 |                    |           | e(cid:48)                             | e(cid:48)  |              | (cid:182)e(cid:152)/2cTx(cid:52)1(cid:53)                        |     |     |     |     |     |     |
| cTx(cid:52)3(cid:53)(cid:190)x(cid:52)2(cid:53)c |           | (cid:190)(cid:52)x(cid:52)2(cid:53)−x(cid:52)1(cid:53)(cid:53)c |                    |           | (cid:51)                              |            |              |                                                                  |     |     |     |     |     |     |
|                                                  |           | e(cid:48) e(cid:48)                                             | e(cid:48)          | e(cid:48) | e(cid:48)                             |            |              | (cid:182)(cid:52)1+(cid:152)(cid:53)cTx(cid:52)1(cid:53)(cid:49) |     |     |     |     |     |     |
| the                                              | optimal   | solution                                                        | x(cid:52)3(cid:53) | of        | is                                    | a feasible | solution for |                                                                  |     |     |     |     |     |     |
(cid:77)(cid:67)(cid:70)
|                           |                    |            |          |     |                               |               |     | where | the last | two | inequalities | follows | for (cid:152)∈(cid:52)0(cid:49)1(cid:53) | and |
| ------------------------- | ------------------ | ---------- | -------- | --- | ----------------------------- | ------------- | --- | ----- | -------- | --- | ------------ | ------- | ---------------------------------------- | --- |
| (cid:77)(cid:67)(cid:70), | x(cid:52)1(cid:53) | is optimal | solution |     | for (cid:77)(cid:67)(cid:70), | and therefore |     |       |          |     |              |         |                                          |     |
m(cid:190)1. (cid:131)
| cTx(cid:52)3(cid:53)(cid:190)cTx(cid:52)1(cid:53)(cid:190)x(cid:52)1(cid:53)c |     |     |                     | (cid:190)(cid:52)x(cid:52)1(cid:53)−x(cid:52)2(cid:53)(cid:53)c |           | (cid:48)  |     |     |     |     |     |     |     |     |
| ----------------------------------------------------------------------------- | --- | --- | ------------------- | --------------------------------------------------------------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                                               |     |     | e(cid:48) e(cid:48) | e(cid:48)                                                       | e(cid:48) | e(cid:48) |     |     |     |     |     |     |     |     |
9. Conclusions
cTx(cid:52)3(cid:53)(cid:190)(cid:151)x(cid:52)2(cid:53)−x(cid:52)1(cid:53)(cid:151)c
| That | is, |     |           | e(cid:48) | .   |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|      |     |     | e(cid:48) | e(cid:48) |     |     |     |     |     |     |     |     |     |     |
Using t=(cid:52)c (cid:152)(cid:53)/(cid:52)4mn(cid:53), from (12) it follows that In this paper, we formulated and analyzed the Belief Prop-
e(cid:48)
|                                           |     |     |           |     |     |     |     | agation | (BP) | algorithm | for | the capacitated | min-cost | net- |
| ----------------------------------------- | --- | --- | --------- | --- | --- | --- | --- | ------- | ---- | --------- | --- | --------------- | -------- | ---- |
| cTx(cid:52)3(cid:53)−cTx(cid:52)1(cid:53) |     |     | (cid:152) |     |     |     |     |         |      |           |     |                 |          |      |
(cid:182) (cid:48) work flow problem (cid:77)(cid:67)(cid:70). We proved that the BP solves
cTx(cid:52)3(cid:53) 4m (cid:77)(cid:67)(cid:70) exactly in pseudopolynomial time when the optimal
|     |     |     |     |     |     |     |     | solution | is unique. | This | result | generalizes | an earlier | result |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ---- | ------ | ----------- | ---------- | ------ |
Therefore,
|     |          |     |            |     |          |          |     | from | Bayati | et al. (2008a) |     | and provides | new insights | for |
| --- | -------- | --- | ---------- | --- | -------- | -------- | --- | ---- | ------ | -------------- | --- | ------------ | ------------ | --- |
|     | (cid:18) |     | (cid:19)−1 |     | (cid:18) | (cid:19) |     |      |        |                |     |              |              |     |
(cid:152) (cid:152) understanding BP as an optimization solver. Although the
| cTx(cid:52)3(cid:53)(cid:182) |     |     | cTx(cid:52)1(cid:53)(cid:182) |     |     | cTx(cid:52)1(cid:53)(cid:49) |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                               |     | 1−  |                               |     | 1+  |                              |     |     |     |     |     |     |     |     |
4m 2m running time of BP for (cid:77)(cid:67)(cid:70) is slower than other existing
|     |     |     |     |     |     |     |     | algorithms |     | for (cid:77)(cid:67)(cid:70), | the advantage |     | of BP is | that it is a |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------------------------- | ------------- | --- | -------- | ------------ |
(cid:131)
where the last inequality holds because (cid:152)∈(cid:52)0(cid:49)1(cid:53). general-purpose distributed heuristic that is widely appli-
|     |     |     |     |     |     |     |     | cable | and that | is easy | to formulate |     | and implement | for a |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ------- | ------------ | --- | ------------- | ----- |
8.3. The FPRAS broad class of constrained optimization problems. We also
Loosely speaking, Corollary 8.6 shows that x(cid:52)2(cid:53) at arc e(cid:48) showed that a similar result holds for the network flow
is “near optimal” because fixing the flow at arc e(cid:48) to x(cid:52)2(cid:53) problem with the piecewise-linear convex cost function.
e(cid:48)
|       |     |            |     |          |          |                             |         | A salient | feature | of  | the BP | established | in this work | is the |
| ----- | --- | ---------- | --- | -------- | -------- | --------------------------- | ------- | --------- | ------- | --- | ------ | ----------- | ------------ | ------ |
| helps | us  | in finding | a   | feasible | solution | of (cid:77)(cid:67)(cid:70) | that is |           |         |     |        |             |              |        |
close to optimal. This leads us to an approximation algo- ability to detect the uniqueness of the optimal solution in
rithm AS((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)) (Algorithm 4) below. This algorithm an entirely distributed manner.
at every iteration uses APRXMT (Algorithm 3) and itera- We showed that the BP algorithm, in its original form,
tively fixes the flow values at the arc with the largest cost. at best leads to a pseudopolynomial-time algorithmic
Theorem 8.7 establishes that this algorithm AS((cid:77)(cid:67)(cid:70)(cid:49)(cid:152)) complexity. To address this problem, we have introduced
is indeed an FPRAS. a randomized variant of BP and showed that this variant

|     |     |     |     |     |     |     |     | Gamarnik,Shah,andWei: |     | BeliefPropagationforMin-CostNetworkFlow |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
428
OperationsResearch60(2),pp.410–428,©2012INFORMS
providesFPRAS.ThisisthefirstFPRASresultfortheBP-
|     |     |     |     |     |     |     |     | Gamarnik, | D., D. | Shah, Y. | Wei. 2010. | Belief | propagation |     | for min-cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | -------- | ---------- | ------ | ----------- | --- | ------------ |
type algorithms. Our variant of BP is based on fixing the network flow: Convergence and correctness. Proc. 21st ACM-SIAM
Sympos.DiscreteAlgorithms,SIAM,Philadelphia,279–292.
valuesofflowvariablesonebyoneinasequentialmanner.
|                   |     |      |          |     |              |     |       | Goldberg, | A., R. Tarjan. | 1987. | Solving | minimum-cost |     | flow | problems by |
| ----------------- | --- | ---- | -------- | --- | ------------ | --- | ----- | --------- | -------------- | ----- | ------- | ------------ | --- | ---- | ----------- |
| Such methodology, |     | used | commonly |     | in practice, | is  | known |           |                |       |         |              |     |      |             |
successiveapproximation.STOC’87:Proc.NineteenthAnnualACM
as the “decimation” procedure (see Montanari et al. 2007). Sympos.TheoryofComput.,ACM,NewYork,7–18.
To the best of our knowledge, this is the first disciplined, Goldberg, A. V., R. E. Tarjan. 1989. Finding minimum-cost circulations
bycancelingnegative.J.ACM36(4)873–886.
| provable | instance | of  | the decimation |     | procedure | in  | the con- |     |     |     |     |     |     |     |     |
| -------- | -------- | --- | -------------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
 .devreser sthgir lla ,ylno esu lanosrep roF . 65:71 ta ,5202 lirpA 61 no ]91.112.052.121[ yb gro.smrofni morf dedaolnwoD Horn,G.B.1999.Iterativedecodingandpseudocodewords.Ph.D.thesis,
| text of BP | algorithms. |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CaliforniaInstituteofTechnology,Pasadena,CA.
|     |     |     |     |     |     |     |     | Kanoria, | Y., M. Bayati, | C.  | Borgs, | J. T. Chayes, | A.  | Montanari. | 2011. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------ | ------------- | --- | ---------- | ----- |
Acknowledgments Fast convergence of natural bargaining dynamics in exchange net-
works.Proc.22ndACM-SIAMSympos.DiscreteAlgorithms,SIAM,
| The authors | thank | the | anonymous | referees | for | the helpful | com- |     |     |     |     |     |     |     |     |
| ----------- | ----- | --- | --------- | -------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Philadelphia,1518–1537.
| ments. A | conference |               | version | of this   | paper | appeared    | in Pro- |            |        |                |     |             |       |           |     |
| -------- | ---------- | ------------- | ------- | --------- | ----- | ----------- | ------- | ---------- | ------ | -------------- | --- | ----------- | ----- | --------- | --- |
|          |            |               |         |           |       |             |         | Malioutov, | D. M., | J. K. Johnson, | A.  | S. Willsky. | 2006. | Walk-sums | and |
| ceedings | of the     | 21st ACM-SIAM |         | Symposium |       | on Discrete | Algo-   |            |        |                |     |             |       |           |     |
beliefpropagationinGaussiangraphicalmodels.J.MachineLearn-
rithms (Gamarnik et al. 2010). While working on this paper, D. ingRes.72031–2064.
Mezard,M.,G.Parisi,R.Zecchina.2002.Analyticandalgorithmicsolu-
| Gamarnik | was partially |     | supported | by the | National | Science | Foun- |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | --------- | ------ | -------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
tionofrandomsatisfiabilityproblems.Science297812.
| dation [Project | CMMI-0726733]; |         |            | D. Shah | was     | supported | in part |           |           |          |       |             |     |         |         |
| --------------- | -------------- | ------- | ---------- | ------- | ------- | --------- | ------- | --------- | --------- | -------- | ----- | ----------- | --- | ------- | ------- |
|                 |                |         |            |         |         |           |         | Moallemi, | C. C., B. | Van Roy. | 2007. | Convergence | of  | min-sum | message |
| by the National |                | Science | Foundation | [EMT    | Project | CCF       | 0829893 |           |           |          |       |             |     |         |         |
passingforconvexoptimization.45thAllertonConf.Comm.,Control,
| and NSF | CAREER | project | CNS | 0546590]; | and | Y. Wei | was par- |     |     |     |     |     |     |     |     |
| ------- | ------ | ------- | --- | --------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Comput.,SIAM,Philadelphia.
| tially supported |     | by a Natural | Sciences |     | and Engineering |     | Research |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------ | -------- | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Moallemi,C.C.,B.VanRoy.2009.Convergenceofthemin-summessage
CouncilofCanadaPostgraduateScholarship. passingforquadraticoptimization.IEEETrans.Inform.Theory55(5)
2413–2423.
Endnote Montanari,A.,F.Ricci-Tersenghi,G.Semerjian.2007.Solvingconstraint
satisfactionproblemsthroughbeliefpropagation-guideddecimation.
| 1. A vertex | v(cid:48) | is called | leaf | if it is | connected | to  | exactly |     |     |     |     |     |     |     |     |
| ----------- | --------- | --------- | ---- | -------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
45thAllertonConf.Comm.,Control,Comput.,SIAM,Philadelphia.
one other vertex. Mulmuley, K., U. Vazirani, V. Vazirani. 1987. Matching is as easy as
matrixinversion.Combinatorica7(1)105–113.
|     |     |     |     |     |     |     |     | Orlin, J. | B. 1993. | A faster | strongly | polynomial |     | minimum | cost flow |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | -------- | -------- | ---------- | --- | ------- | --------- |
algorithm.Oper.Res.41(2)338–350.
References
|     |     |     |     |     |     |     |     | Pearl, J. 1988. | Probabilistic |     | Reasoning | in Intelligent |     | Systems: | Networks |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | --- | --------- | -------------- | --- | -------- | -------- |
Ahuja,R.,A.Goldberg,J.Orlin,R.Tarjan.1992.Findingminimum-cost
ofPlausibleInference.MorganKaufmann,SanFrancisco.
flowsbydoublescaling.Math.Programming53243–266.
|     |     |     |     |     |     |     |     | Richardson, | T., R. | Urbanke. | 2001. | The capacity | of  | low-density | parity |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | -------- | ----- | ------------ | --- | ----------- | ------ |
Ahuja,R.K.,T.L.Magnanti,J.B.Orlin.1993.NetworkFlows.Prentice-
|     |     |     |     |     |     |     |     | check | codes under | message-passing |     | decoding. | IEEE | Trans. | Inform. |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --------------- | --- | --------- | ---- | ------ | ------- |
HallInc,EnglewoodCliffs,NJ.
Theory47(2)599–618.
Aji,S.M.,R.J.McEliece.2000.Thegeneralizeddistributivelaw.IEEE
|     |     |     |     |     |     |     |     | Röck, H. | 1980. Scaling | techniques |     | for minimal | cost | flow | problems. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | ---------- | --- | ----------- | ---- | ---- | --------- |
Trans.Inform.Theory46(2)325–343.
DiscreteStructuresAlgorithms181–191.
| Bayati, M., | D. Shah,  | M.           | Sharma. | 2008a.       | Max-product | for         | maximum |             |               |       |     |             |     |         |            |
| ----------- | --------- | ------------ | ------- | ------------ | ----------- | ----------- | ------- | ----------- | ------------- | ----- | --- | ----------- | --- | ------- | ---------- |
|             |           |              |         |              |             |             |         | Ruozzi, N., | S. Tatikonda. | 2008. | s-t | paths using | the | min-sum | algorithm. |
| weight      | matching: | Convergence, |         | correctness, | and         | lp duality. | IEEE    |             |               |       |     |             |     |         |            |
Trans.Inform.Theory54(3)1241–1251. Forty-SixthAnnualAllertonConf.Comm.,Control,Comput.,Urbana,
| Bayati, M., | C. Borgs, | J.  | Chayes, | R. Zecchina. | 2008b. | On the | exactness | IL,918–921. |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ------- | ------------ | ------ | ------ | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
of the cavity method for weighted b-matchings on arbitrary graphs Sanghavi,S.,D.Malioutov,A.Willsky.2007.Linearprogramminganal-
ysisofloopybeliefpropagationforweightedmatching.Proc.NIPS
| and | its relation | to linear | programs. | J.  | Statist. | Mech.: Theory | and |     |     |     |     |     |     |     |     |
| --- | ------------ | --------- | --------- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Conf.,Vancouver,BritishColumbia,Canada.
ExperimentL06001.
|     |     |     |     |     |     |     |     | Sanghavi, | S., D. | Shah, A. | Willsky. | 2009. | Message-passing |     | for maxi- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | -------- | -------- | ----- | --------------- | --- | --------- |
Bertsekas,D.P.1986.Distributedrelaxationmethodsforlinearnetwork
|     |     |     |     |     |     |     |     | mum | weight | independent | set. | IEEE Trans. | Inform. | Theory | 51(11) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ---- | ----------- | ------- | ------ | ------ |
flowproblems.Proc.25thIEEEConf.DecisionandControl,Athens,
4822–4834.
Greece,2101–2106.
Bertsimas,D.,J.Tsitsiklis.1997.IntroductiontoLinearOptimization,3rd Schrijver,A.2003.CombinatorialOptimization.Springer,Berlin.
ed.AthenaScientific,Belmont,MA,289–290. Tardos, E. 1985. A strongly polynomial minimum cost circulation
Edmonds,J.,R.M.Karp.1972.Theoreticalimprovementsinalgorithmic algorithm.Combinatorica5(3)247–255.
efficiencyfornetworkflowproblems.J.ACM19(2)248–264. Weiss,Y.,W.Freeman.2001.Ontheoptimalityofsolutionsofthemax-
Fujishige,S.1986.Acapacity-roundingalgorithmfortheminimum-cost productbelief-propagationalgorithminarbitrarygraphs.IEEETrans.
circulation problem: A dual framework of the Tardos algorithm. Inform.Theory47(2)736–744.
Math.Programming35(3)298–308. Yedidia,J.,W.Freeman,Y.Weiss.2002.Understandingbeliefpropagation
Gallager, R. 1963. Low density parity check codes. Ph.D. thesis, and its generalizations. Technical Report, TR-2001-22, Mitsubishi
MassachusettsInstituteofTechnology,Cambridge,MA. ElectricResearchLab,Cambridge,MA.