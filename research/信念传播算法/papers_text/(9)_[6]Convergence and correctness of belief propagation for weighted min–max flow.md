DiscreteAppliedMathematics354(2024)122–130
ContentslistsavailableatScienceDirect
DiscreteAppliedMathematics
journalhomepage:www.elsevier.com/locate/dam
Convergenceandcorrectnessofbeliefpropagationfor
weightedmin–maxflow
GuoweiDaia,LongkunGuob,GregoryGutinc,XiaoyanZhanga,∗
,
Zan-BoZhangd
aSchoolofMathematicalScience&InstituteofMathematics,NanjingNormalUniversity,Nanjing,China
bDepartmentofComputerScience,QiluUniversityofTechnology,Jinan,China
cDepartmentofComputerScience,RoyalHollowayUniversityofLondon,Egham,UK
dSchoolofStatistics&Mathematics,andInstituteofArtificialIntelligence&DeepLearning,GuangdongUniversityofFinance&
Economics,Guangzhou,China
a r t i c l e i n f o a b s t r a c t
Articlehistory: In this paper, we investigate the performance of message-passing algorithms for the
Received9March2021 weighted min–max flow (WMMF) problem which was introduced by Ichimori et al.
Receivedinrevisedform21November2021 (1980).WMMF waswellstudiedincombinationaloptimization,asitprovidesimpor-
Accepted13December2021 tantapplicationsintimetransportationproblemandthestoragemanagementproblem.
Availableonline13January2022
We develop a message-passing algorithm called min–max belief propagation (BP) for
Keywords: determiningtheoptimalsolutionofWMMF.Asthemainresultofthispaper,weprove
Beliefpropagation that for a digraph of size n, BP converges to the optimal solution within O(n3) time
Min–maxBPalgorithm after O(n) iterations if the optimal solution of the underlying min–max flow problem
Message-passingalgorithm instanceisunique.Tothebestofourknowledge,thefastestpolynomialtimealgorithm
Min–maxflow for WMMF runs in essentially O(n6) time among the known algorithms, where n is
thenumberofvertices.Ontheotherhand,itisoneofaveryfewinstanceswhereBP
isprovedcorrectwithfully-polynomialrunningtime.
©2021ElsevierB.V.Allrightsreserved.
1. Introduction
Asanalgorithmicframework,messagepassingisextremelypowerfulandhasbeenwidelyusedonvariousgraphical
models (GMs). Belief propagation (BP), proposed by Pearl in 1988 [17], is a message-passing heuristic algorithm and
haswideapplicationsinthecontextofvarietyofdisciplinesincludingsatisfiabilityindiscreteoptimization[1,16],error
correctingcodeininformationtheory[15,18],anddataclusteringinmachinelearning[9].ThegreatpopularityofBPcan
beattributedtotwomainreasons.Firstly,itiseasytoimplementduetoitssimpleandmessage-passingnature.Secondly,
itperformswellinmanypracticalapplications.Thewidescopeofapplication,simplicity,andexperimentalsuccessofBP
hasgainedalotofattentionrecently[16,18,23].
BPisknowntoconvergetothecorrectsolutiononGMswithnocycles[17].Whentheunderlyinggraphisatree,theBP
algorithmessentiallyperformstherecursionofdynamicprogramming(DP)leadingtoacorrectsolution.Specifically,BP
providesanaturalparalleliterativeversionoftheDPinwhichmessagepassingoccursbetweenthevariablenodesalong
edgesofthegraphicalmodel.Surprisingly,evenforGMswithcycles,theBPheuristicperformswellinmanycases[22],
∗
Correspondingauthor.
E-mailaddresses: guoweidai@njnu.edu.cn(G.Dai),longkun.guo@qlu.edu.cn(L.Guo),gutin@cs.rhul.ac.uk(G.Gutin),zhangxiaoyan@njnu.edu.cn
(X.Zhang),zanbozhang@gdufe.edu.cn(Z.-B.Zhang).
https://doi.org/10.1016/j.dam.2021.12.025
0166-218X/©2021ElsevierB.V.Allrightsreserved.

G.Dai,L.Guo,G.Gutinetal. DiscreteAppliedMathematics354(2024)122–130
someofwhichrequirerigorousanalysisofoptimalityandconvergence[3,7,11,19,20].Unfortunately,thecorrectnessand
convergencepropertiesofBPforgeneralcombinatorialoptimizationproblemsarestillopen.
Asamajorbreakthrough,Bayatietal.[3]andChengetal.[6]werethefirsttosimplifytheBPalgorithmindependently
toobtainessentiallythesamealgorithmsforthemaximumweightmatching(MWM)inabipartitegraph.Theyestablished
the correctness and convergence of BP algorithm for MWM in pseudo-polynomial time. Sanghavi et al. [19] as well as
Bayati et al. [2] generalized the result to the minimum cost b-matching problem on arbitrary graphs and established
that BP algorithm converges to the optimal solution, in pseudo-polynomial time, as long as the corresponding linear
programmingrelaxationhasnofractionalsolutions.Furthermore,MWMcanbeviewedasaspecialcaseoftheminimum
costflow(MCF)problem.Recently,Gamarniketal.[11]studiedtheperformanceofBPalgorithmforfindingtheoptimal
solution of MCF and proved that BP algorithm converges to the optimal solution in pseudo-polynomial time, provided
that the optimal solution is unique. Brunsch et al. [4] studied BP algorithm in the framework of smoothed analysis and
provedthatwithhighprobabilitythenumberofiterationsneededtocomputemaximum-weightmatchingsandmin-cost
flowsisboundedbyapolynomialiftheweightsorcostsoftheedgesarerandomlyperturbed.
The running time of BP algorithm converging to the optimum is actually pseudo-polynomial for some combinatorial
optimizationproblems,althoughmostofthoseoptimizationproblems(e.g.,MWMandMCF)haveotherfullypolynomial
timealgorithms.Gamarniketal.[11]alsopresentedasimplemodificationofBPalgorithmtoobtainafullypolynomial
time randomized approximation scheme for MCF. However, as they said themselves in [11], the ‘near optimal’ solution
is ‘rather fuzzy’. In order to identify the class of optimization problems solvable in fully polynomial time using the
BP algorithm, we study the weighted min–max flow (WMMF) problem and develop a min–max BP algorithm for
determining the optimal solution of WMMF. As a variant of the maximum flow problems, WMMF was introduced
byIchimorietal.[14]andwaswellstudiedincombinationaloptimization[8,10,12],asitprovidesimportantapplications
intimetransportationproblem[5]andthestoragemanagementproblem[21].
Inthispaper,wewillinvestigatetheconvergenceandcorrectnessofthemin–maxBPalgorithmforfindingtheoptimal
solutionofWMMF onarbitrarydigraphs.Asthemainresult,weestablishthatouralgorithmconvergestotheoptimal
solution of WMMF after at most n/2 iterations where n represents the number of vertices, provided that the optimal
solutionisunique.Fromthedescriptionofmin–maxBPalgorithm,itisseenthateachofthemessagescanbecomputed
inO(n2)time.ThenduetothedistributednatureofBPalgorithm,thecomputationalcostofthealgorithmisO(n3)inO(n)
iterations. As a result, the min–max BP algorithm we developed is a fully polynomial time algorithm. On the one hand,
ouralgorithmisoneofaveryfewinstanceswhereBPisprovedcorrectwithfully-polynomialrunningtime.Ontheother
hand,tothebestofourknowledge,thefastestpolynomialtimealgorithmforWMMF runsinessentiallyO(n6)time[13]
among the known algorithms, where n is the number of vertices. According to our theoretical analysis, it may explain
whyBPcanperformwellformostofcombinationaloptimizationproblemsandrunfastinpractice.
The rest of the paper is organized as follows. In Section 2, we introduce the weighted min–max flow problem
(WMMF). In Section 3, we describe the min–max BP algorithm for WMMF, and state our main result. Proofs of
correctness and convergence for our algorithm are given in Section 4. Finally, Section 5 presents the conclusions and
directionsforfutureresearch.
2. Preliminaries
2.1. Definitionsandproblemstatement
Givenaweighteddigraph(i.e.,network)G = (V,E)whereV,E denotethesetofverticesandarcs,respectivelywith
|V|=n,|E|=m.Toeacharcse∈E,assignanonnegativeweightw andapositivecapacityc .Forgivensources∈V and
e e
sinkt ∈V,denotedbyf∗ thetotalvalueofgivenflowfromstot.Foranyvertexi∈V,letE − bethesetofarcsentering
i, that is, E − = {ji : ji ∈ E}. Similarly, E + = {ij : ij ∈ E} denotes the set of arcs leaving i. Le i t E = E −∪E + . We assume
for simplic i ity that |E−| = |E +| = 0. Th i e weighted min–max flow (WMMF) problem aims to i mini i mize i the maximum
s t
valueofweightedarc-flow(multipliedbyarc-weight).Then,theWMMF onGcanbeformulatedasthefollowinglinear
program:
min maxw x (I)
e e
e∈E
⎧ f∗, i=s;
∑ ∑ ⎨
s.t. x − x =f = −f∗, i=t; (1)
e e i
e∈E + e∈E − ⎩ 0, i∈V \{s,t},
i i
0≤x ≤c , ∀e∈E, (2)
e e
wherethevariablesx representtheflowvalueassignedtoeacharce∈E.Theconstraints(1)statethatthedifferenceof
e
out-flowandin-flowateachvertexi∈V equalsthevertexdemandf.Theconstraints(2)statethatflowvalueoneach
i
arce∈E isnonnegativeandatmostitscapacityc .Notethattoenabletheinstanceofnetworkflowtobefeasible,we
e
assumew.l.o.g.that|E|≥2foreachi∈V,orelse|E|=1,inwhichcasetheflowone∈E isdeterminedbyf.
i i i i
123

G.Dai,L.Guo,G.Gutinetal. DiscreteAppliedMathematics354(2024)122–130
|     |     |                                             |     | 2 withrootv | v    |     |
| --- | --- | ------------------------------------------- | --- | ----------- | ---- | --- |
|     |     | Fig.1. Anexampleofa2-levelcomputationtreeTv |     | v           | 1 2. |     |
1 2
2.2. Factorizedoptimizationproblem
Considertheoptimizationproblem(P)asfollows:
| ∑   | ∑   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
φ(x)+ ψ
| min | i i   | D (x D ) |     |     |     |     |
| --- | ----- | -------- | --- | --- | --- | --- |
| i∈V | D∈D   |          |     |     |     |     |
| ∈R, | ∀i∈V, |          |     |     |     |     |
s.t. x
i
where V is a finite set of variables and D is a finite collection of subsets of V representing constraints. Here φ : R →
i
R∪{∞}andψ :R|D| →R∪{∞},∀D∈D areextendedreal-valuedfunctions,whereeachφ
| D   |     |     |     |     | i iscalledavariablefunction |     |
| --- | --- | --- | --- | --- | --------------------------- | --- |
andeachψ iscalledafactorfunction.Wealsocalltheoptimizationproblem(P)afactorizedoptimizationproblem.
D
Itiswell-knownthatBPalgorithmsarealwaysviewedasheuristicalgorithmsforfactorizedoptimizationproblemsand
operate by passing messages iteratively with variables and factors. Next, we translate (I) into a factorized optimization
problem.Letx ={x :e∈E}foreachi∈V.Definevariableandfactorfunctionsφ,ψ foreache∈E,i∈V,respectively
| E i             | e         | i        |     |     |     |     |
| --------------- | --------- | -------- | --- | --- | --- | --- |
| asfollows:φ ( x | )=w x and |          |     |     |     |     |
| e e             | e e       |          |     |     |     |     |
|                 | ⎧         | ∑ ∑ ,    |     |     |     |     |
|                 | ⎪⎨ 0 if   | x − x =f |     |     |     |     |
|                 |           | e e i    |     |     |     |     |
| ψ (x )=         |           | + −      |     |     |     |     |
| i Ei            |           | e∈ E e∈E |     |     |     |     |
|                 | ⎪⎩+∞      | i i      |     |     |     |     |
oth e r wise.
Then,wecanformulateWMMF asanunconstrainedoptimizationproblemasfollows.
|         | {          | }   |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- |
| min max | φ (x ),ψ(x | )   |     |     |     |     |
e e i Ei
e∈E,i∈V
| s.t. | , ∀e∈E. |     |     |     |     |     |
| ---- | ------- | --- | --- | --- | --- | --- |
| 0≤x  | ≤c      |     |     |     |     |     |
|      | e e     |     |     |     |     |     |
3. BPalgorithmforWMMF
3.1. Computationtree
Hereweintroducetheconceptofrootedtreeandcomputationtree.Aconnectedacyclicgraph(i.e.,containsnocycles)
iscalledatree.Foranynontrivialtree,itmustcontainavertexwhichhasexactlyoneneighbor.Suchavertexinatree
is also called a leaf of the tree. Throughout of the paper, we define a rooted tree T as a tree T with a specified arc a,
a
calledtheroot ofT.Itshouldbenotedthatthedefinitionoftherootofatreesometimesreferstoaspecifiedvertex,in
contrasttoarootastheroot.Inatree,anytwoverticesareconnectedbyexactlyonepath.Wedenotetheuniquepath
connectingverticesiandjinatreeT byiTj.ForarootedtreeT a withroota,thelevelofavertexiinT a isthelengthof
ofi.Fortwoadjacentverticesi,jinT,ifiisanancestor
thepathaTi,andeachvertexonthepathaTiiscalledanancestor
| ofj,theniisalsocalledaparent |     | ofj,andjisachildofi. |     |     |     |     |
| ---------------------------- | --- | -------------------- | --- | --- | --- | --- |
WeuseTN todenotetheN-levelcomputationtreeassociatedwitharcaastheroot.Anexampleofcomputationtree
a
isgiveninFig.1.DenotethesetofverticesandarcsinTN byV(TN)andE(TN),respectively.EachvertexorarcofTN is
|     |     |     | a a | a   |     | a   |
| --- | --- | --- | --- | --- | --- | --- |
aduplicateofsomevertexorarcoftheoriginalgraphG.DefinethemappingγN :V(TN)→V suchthatifi′ ∈V(TN)is
|     |     |          |       | a   | a           | a     |
| --- | --- | -------- | ----- | --- | ----------- | ----- |
|     | ∈   | γN(i′) = | L(TN) | TN. | i′ ∈ V(TN), | P(i′) |
a duplicate of i V(G), then a i. Denote by a the set of leaves of a For any a denote by the
parentofi′ inTN.Itisessentiallythebreadth-firstsearchtreeofG(withrepetitionofverticesallowed)startingfroma
a
| uptodepthN.Indetail,weinductivelydefineTN |     |     | asthefollowingrules. |     |     |     |
| ----------------------------------------- | --- | --- | -------------------- | --- | --- | --- |
a
124

G.Dai,L.Guo,G.Gutinetal. DiscreteAppliedMathematics354(2024)122–130
• Letuv∈E(G).ThenthecomputationtreeT0 consistsoftwoverticesu′,v′ andanarcu′v′,suchthatγ0(u′)=uand
|     |     |     |     |     |     | a   |     |     |     |     |     | a   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
γ0(v′)=v.Thearca=u′v′ isconsideredthe‘‘root"ofT0,andverticesu′,v′ areconsideredtobeat0-levelofT0.
|     | a   |     |     |     |     |     |       | a   |       |            |                |     | a   |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | ---------- | -------------- | --- | --- |
|     | •   |     |     |     |     |     | TN−1, |     | i′,j′ | ∈ V(TN−1), | i′j′ ∈ E(TN−1) |     |     |
Inductively, suppose that we defined a tree a such that for any a a if and only if
|     | γN−1(i′)γN−1(j′) |     | ∈   |     |     |     | TN  | TN−1 |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
E(G). The computation tree contains as a subtree, which can be obtained by adding
verticestoV(TN−1)andarcstoE(TN−1)asfollows.Foreachleafvertexi′ a a a a ∈L(TN−1),addnodej′ toexpandV(TN−1)
andaddarci′j′orj′i′toexpandE(TN−1)ifthereisavertexj∈V(G)suchthatij∈E(G)orji∈E(G)withγN−1(i′)=i, a a a a
|     |     |     |     |     | a   |     |     |     |     |     |     | a   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andγN−1(P(i′))̸=j.Inthiscase,defineP(j′)=i′,themapγN(j′)=j,andlevelofj′ asN.Indeed,γN isidenticalto
|     | a   |     |     |     |     |     |     | a   |     |     |     | a   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
γN−1 forverticesinV(TN−1)⊆V(TN).
|     | a                              |     |     | a   | a   |           |     |     |     |     |     |     |     |
| --- | ------------------------------ | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
|     | • Foranye=ij∈E(G),thearcfromi′ |     |     |     |     | toj′ inTN |     |     |     |     |     |     |     |
isalsodenotedbyeforsimplicityandisassignedthesameweight
|     | w asthatinG,whereγN(i′)=iandγN(j′)=j. |     |     |     |     |     | a   |     |     |     |     |     |     |
| --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e
|     |     |     |     | a   |     | a   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Inwhatfollows,weshalldropreferencetoa,t innotationofγN whenclearfromcontextandabusenotationbydenoting
a
γ(i′j′)=γ(i′)γ(j′).
Note that the computation tree is locally equivalent to the original graph, which means one can view the iterative
process of BP algorithm as sending the messages along the way from leaf vertices to the root in the computation
tree. All the vertices on computation tree will send messages to their parents at each iteration, and the direction of
message-passingisindependentofthedirectionofthoseedges.
Givenaroota,letVo(TN) ⊂ V(TN)bethesetofallthenon-leafverticesofTN.Recallthatforanyvertexk ∈ V(TN),
|     |     |     |     | a   | a   |     |     |     |     | a   |     |     | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
E + (TN) and E − (TN) denote the set of arcs leaving k and entering k in TN, respe ctively. Then we consider the proble m
| k   | a   | k a |     |     |     |     |     |     | a   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
formulatedasWMMFN:
a
w
|     | min | max | y   |     |     |     |     |     |     |     |     |     | (II) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
e e
e∈E(Ta N)
|     |      | ∑   |     | ∑   |          |     |     |     |         |     |     |     |     |
| --- | ---- | --- | --- | --- | -------- | --- | --- | --- | ------- | --- | --- | --- | --- |
|     |      |     | −   |     | =fγ(k) , |     |     |     | ∀k∈Vo(T | N); |     |     |     |
|     | s.t. |     | y e | y e |          |     |     |     |         |     |     |     | (3) |
a
|     |     | + N)      |     | − N)  |     |     |     |     |           |     |     |     |     |
| --- | --- | --------- | --- | ----- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
|     |     | e∈E k (Ta | e∈E | k (Ta |     |     |     |     |           |     |     |     |     |
|     | 0≤y | ≤c        | ,   |       |     |     |     |     | ∀e∈E(TN), |     |     |     |     |
|     |     | e         | e   |       |     |     |     |     |           | a   |     |     | (4) |
wherethevariablesy representflowvalueassignedtoeacharce ∈ E(TN).Roughlyspeaking,WMMFN isaWMMF
|     |     |     | e   |     |     |     |     |     | a   |     |     | a   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
on the computation tree TN essentially: there is a network flow capacity constraint for every arc e ∈ E(TN) and a flow
|     |     |     |     | a   |     |     |     |     |     |     |     | a   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
balanceconstraintforeveryvertex,exceptfortheleafvertices.
3.2. Algorithmandresults
Foreacharce=ijonthecomputationtreeTN,bydefinition,TN hastwocomponentswhichareconnectedviathearc
|     |     |     |     |     |     | a   |     | a   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e.LetTN bethecomponentcontainingi,whichcanbeviewedasasubtreeofTN.LetTN :=TN ∪{e}.Defineamessage
|     | e→j |     |     |     |     |     |     |     |     | a i→e | e→j |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
functionm (x )onthesubtreeT N .Letthefunctionm (x )returnthemaximumvalueofarc-flow(multipliedbyarc-
|     | e→j | e   |     |     | e →j |     | e→j | e   |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
N
weight)oftheWMMF onthesubtreeT →j .Similarly,definethemessagefunctionm i→e (x e )whichreturnsthemaximum
e
valueofarc-flow(multipliedbyarc-weight)oftheWMMF onthesubtreeTN .Duetothenatureoftreestructure,these
i→e
twomessagefunctionscanberecursivelydefinedasfollows:foranyarce=ij,
|     |      |       | {         |         | }          |         |        |     |     |     |     |       |     |
| --- | ---- | ----- | --------- | ------- | ---------- | ------- | ------ | --- | --- | --- | --- | ----- | --- |
|     | m (x | )=max | φ         | (x ),m  | (x ) ,     |         |        |     |     |     |     |       | (5) |
|     | e→j  | e     |           | e e i→e | e          |         |        |     |     |     |     |       |     |
|     |      |       | {         |         |            |         | }      |     |     |     |     |       |     |
|     | m (x | )=m   | i n max{ψ | (x      | ), m a x m | e′→i (x | e′)} . |     |     |     |     |       | (6) |
|     | i→e  | e     |           | i Ei    | ′∈E        |         |        |     |     |     |     |       |     |
|     |      | xEi   | \ e       |         | e i \e     |         |        |     |     |     |     |       |     |
|     |      |       |           |         |            |         |        |     |     |     |     | ∈ E,i | ∈   |
Using (5)–(6), starting from leaves, the message functions m e→j (x e ) and m i→e (x e ) can be computed for all e V.
Then,theupdatemessagesforeachvertexandarcisasfollows:
|     |        |       | {     |          | }        |      |      |     |     |     |     |     |     |
| --- | ------ | ----- | ----- | -------- | -------- | ---- | ---- | --- | --- | --- | --- | --- | --- |
|     | mt     | )=max | φ     | ),mt−1(x | ,        |      |      |     |     |     |     |     |     |
|     | e→j (x |       |       | (x       | )        |      |      |     |     |     |     |     |     |
|     |        | e     |       | e e i→e  | e        |      |      |     |     |     |     |     |     |
|     |        |       | {     |          |          |      | }    |     |     |     |     |     |     |
|     |        |       | max{ψ |          | ),       |      | .    |     |     |     |     |     |     |
|     | mt (x  | )=m   | i n   | (x       | m a x mt | (x   | e′)} |     |     |     |     |     |     |
|     | i→e    | e     |       | i Ei     | ′∈E \e   | e′→i |      |     |     |     |     |     |     |
|     |        | xEi   | \ e   |          | e i      |      |      |     |     |     |     |     |     |
= uv,
Finally, combine the messages m a→u (x a ) and m a→v(x a ) at the root arc a we can derive the estimation of belief at
onthecomputationtreeTN
| theendofiterationN |     |     |     |     |     |     | as  |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a
|     |          |     | {   |      | }         |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | bN )=max |     | mN  | ),mN |           | .   |     |     |     |     |     |     |     |
|     | (x a     |     | a→u | (x a | a→v(x a ) |     |     |     |     |     |     |     |     |
a
Theparallelalgorithmcalledmin–maxBPforsolvingWMMF isdescribedindetailasAlgorithm1.
Next,wewillstateourresult,theproofofwhichispresentedinSection4.
125

G.Dai,L.Guo,G.Gutinetal. DiscreteAppliedMathematics354(2024)122–130
Algorithm1min–maxBPforWMMF
|     |     | 1:Initializet |               | =0,messagem0 |                          | (x      | )=w  | x foreache=ij∈E. |             |        |     |     |     |
| --- | --- | ------------- | ------------- | ------------ | ------------------------ | ------- | ---- | ---------------- | ----------- | ------ | --- | --- | --- |
|     |     |               |               |              |                          | i→e     | e    | e e              |             |        |     |     |     |
|     |     | 2:fort        | =1,2,...,N    |              | do                       |         |      |                  |             |        |     |     |     |
|     |     | 3:            | Foreache=ij∈E |              | updatemessagesasfollows: |         |      |                  |             |        |     |     |     |
|     |     |               |               |              |                          |         | {    | ),mt−1(x         | }           |        |     |     |     |
|     |     |               |               |              | mt (x                    | )=max   | φ    | (x               | ) ,         |        |     |     |     |
|     |     |               |               |              | e→j                      | e       |      | e e              | i→e e       |        |     |     |     |
|     |     |               |               |              |                          | {       |      |                  |             | }      |     |     |     |
|     |     |               |               | mt           | )=m                      | max{ψ   |      | ),               | mt          | e′)} . |     |     |     |
|     |     |               |               | i→e          | (x e                     | i n     | i (x | Ei m             | a x e′→i (x |        |     |     |     |
|     |     |               |               |              |                          | xEi \ e |      | e ′∈E            | \e          |        |     |     |     |
i
|     |     | 4:  | t :=t+1 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5:endfor
|     |     |                                            |     |     |     |     |     |     |       | {   |       | }      |     |
| --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | ------ | --- |
|     |     | 6:Foreache=ij∈E,setthebelieffunctionasbN(x |     |     |     |     |     |     |       |     | ),mN  |        |     |
|     |     |                                            |     |     |     |     |     |     | )=max | mN  | (x    | (x ) . |     |
|     |     |                                            |     |     |     |     |     |     | e e   |     | e→i e | e→j e  |     |
7:CalculatethebeliefestimatebyfindingˆxN ∈arg bN )foreache∈E.
|     |     |             |     |        |                                          |     |     |     | m i n      | (x e |     |     |     |
| --- | --- | ----------- | --- | ------ | ---------------------------------------- | --- | --- | --- | ---------- | ---- | --- | --- | --- |
|     |     |             |     |        |                                          |     |     | e   | 0≤ xe ≤ ce | e    |     |     |     |
|     |     | 8:ReturnˆxN |     | ={ ˆxN | :e∈E}asanestimationoftheoptimalsolution. |     |     |     |            |      |     |     |     |
e
onGhasauniqueoptimalsolutionx∗,thenAlgorithm1
| Theorem1.     |     | ForanydigraphGofordern,iftheproblemWMMF |     |     |        |     |                 |     |     |     |     |     |     |
| ------------- | --- | --------------------------------------- | --- | --- | ------ | --- | --------------- | --- | --- | --- | --- | --- | --- |
| convergestox∗ |     |                                         |     |     | =x∗    |     |                 |     |     |     |     |     |     |
|               |     | after n iterations,i.e.,ˆxN             |     |     | afterN |     | ≥ n iterations. |     |     |     |     |     |     |
|               |     | 2                                       |     |     |        |     | 2               |     |     |     |     |     |     |
Fromthedescriptionofmin–maxBPalgorithm,itisseenthateachofthemessagescanbecomputedinO(n2)time.
ThenduetothedistributednatureofBPalgorithm,thetotalcomputationaltimeofouralgorithmisO(n3)in n iterations.
2
AsacorollaryofTheorem1,themin–maxBPalgorithmwedevelopedisafullypolynomialtimealgorithm.
onGhasauniqueoptimalsolutionx∗,thenmin–maxBP
| Corollary1.            |     | ForanydigraphGofordern,iftheproblemWMMF |              |     |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --------------------------------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| algorithmconvergestox∗ |     |                                         | inO(n3)time. |     |     |     |     |     |     |     |     |     |     |
4. Proofofcorrectnessandconvergence
Inthissection,wewillestablishtheconvergenceofBPtotheoptimalsolutionoftheWMMF undertheassumption
oftheuniquenessoftheoptimalsolution,namelyweshallproveTheorem1.Notethatourstrategyissomewhatsimilar
tothatof[11],butthetechnicaldetailsarequitedifferent.
Lemma2. LetˆxN bethevalueoftheoutputoftheBPalgorithmattheendofiterationN onarca∈E.Thenthereexistsan
a
| optimalsolutiony∗ |     | ofWMMFN |     | suchthaty∗ | =   | ˆxN whereaistherootofT |     |     | N.  |     |     |     |     |
| ----------------- | --- | ------- | --- | ---------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
|                   |     |         |     | a          | a   | a                      |     |     | a   |     |     |     |     |
Leta=ijbetherootofTN.Bydefinition,TN
| Proof. |     |     |     |     |     |     | hastwocomponentsconnectedbythearca.Denotethecomponent |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|        |     |     |     | a   |     | a   |                                                       |     |     |     |     |     |     |
containingibyC andTN denotesC witharca(indeedTN isatree).LetV0(TN )bethesetofalltheverticeswhich
|                        |     |       | a→j |              |     |               | a→j |     |     | a→j |     |        |      |
| ---------------------- | --- | ----- | --- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | ------ | ---- |
| arenotontheN-levelofTN |     |       |     | .DefineWMMFN |     | (z)asfollows. |     |     |     |     |     |        |      |
|                        |     |       | a→j |              |     | a→j           |     |     |     |     |     |        |      |
|                        | min | max w | y   |              |     |               |     |     |     |     |     | (WMMFN | (z)) |
|                        |     | e     | e   |              |     |               |     |     |     |     |     |        | a→j  |
e∈E(T N →j )
a
|     |      | ∑         | ∑   |           | ,   |     |     |     |         |     |      |     |     |
| --- | ---- | --------- | --- | --------- | --- | --- | --- | --- | ------- | --- | ---- | --- | --- |
|     | s.t. | y         | −   | y =fγ(k)  |     |     |     |     | ∀k∈Vo(T |     | N )  |     |     |
|     |      | e         |     | e         |     |     |     |     |         |     | a →j |     |     |
|     |      | +         | −   |           |     |     |     |     |         |     |      |     |     |
|     | e∈E  | (T N →j ) | e∈E | (T N →j ) |     |     |     |     |         |     |      |     |     |
|     |      | k a       | k   | a         |     |     |     |     |         |     |      |     |     |
=z
y a
|     | 0≤y | ≤c , |     |     |     |     |     |     | ∀e∈E(TN |     | ).  |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
|     |     | e e  |     |     |     |     |     |     |         |     | a→j |     |     |
Now,weshowthatundertheBPalgorithmthevalueofmN (z)isthesameastheweightoftheoptimalassignment
a→γ(j)
forWMMFN (z).Thiscanbeestablishedinductively.WhenN =1,thestatementiseasytobechecked.ForN >1and
a→j
TN−1
each b ∈ E\a with b = pi (or ip), let be the subtree of TN that includes b and does not include i. Consider the
|     | i   |     |     |     | b→i |     |     | a→j |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
subproblemWMMFN−1(z)asfollows.
b→i
|     |     | w   |     |     |     |     |     |     |     |     |     | (WMMFN−1(z)) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
|     | min | max | y   |     |     |     |     |     |     |     |     |              |     |
|     |     | − e | e   |     |     |     |     |     |     |     |     |              | b→i |
e∈E(T N → 1)
b i
|     |      | ∑   | ∑   |        |     |     |     |     |     |         |        |     |     |
| --- | ---- | --- | --- | ------ | --- | --- | --- | --- | --- | ------- | ------ | --- | --- |
|     |      |     | −   | =fγ(k) | ,   |     |     |     |     | ∀k∈Vo(T | N − 1) |     |     |
|     | s.t. | y e |     | y e    |     |     |     |     |     |         | →      |     |     |
b i
|     |     | + N − 1) | −   | N − 1) |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | e∈E | (T →     | e∈E | (T →   |     |     |     |     |     |     |     |     |     |
|     |     | k b i    | k   | b i    |     |     |     |     |     |     |     |     |     |
y =z
b
∀e∈E(TN−1).
|     | 0≤y | ≤c , |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | e e  |     |     |     |     |     |     |     |     | b→i |     |     |
126

G.Dai,L.Guo,G.Gutinetal. DiscreteAppliedMathematics354(2024)122–130
Byinductionhypothesis,itiseasytoseethatthevalueofmN b→ −1 γ(i) (z)equalstheweightofthesolutionofWMMFN b→ −1 i (z).
Given this hypothesis and the relation of sub-tree TN−1 for all b ∈ E\a with TN , it follows that the problem
b→i i a→j
WMMFN (z)isequivalentto
a→j
{ }
min max w a z,
b
m
∈E
a
i \
x
a
mN b→ −1 γ(i) (y b )
∑ ∑
s.t. y
e
− y
e
=fγ(i) ,
e∈E i + (T a N →j ) e∈E i − (T a N →j )
y =z
a
0≤y ≤c , ∀b∈E\a.
b b i
ThisisexactlythesameastherelationbetweenmN
a→γ(j)
(z)andmessagefunctionmN
b→
−1
γ(i)
(·)forb∈E
i
\aas
{ }
mN a→j (z)=max w a z,
b
m
∈E
a
i \
x
a
mN g→ −1 γ(i) (y b ) .
Thatis,mN a→γ(j) (z)isexactlythesameastheweightofoptimalassignmentofWMMFN a→j (z).Usingthisequivalence,we
willcompletetheproofofLemma2.
Forgivena=ijwith0≤z ≤c ,theproblemWMMFN(z)isequivalentto
a a
{ }
min max max w y , max w y
e e e e
e∈E(T a N →i ) e∈E(T a N →j )
∑ ∑
s.t. y
e
− y
e
=fγ(k) , ∀k∈Vo(T
a
N)∩(Vo(T
a
N
→k
)∪Vo(T
a
N
→j
))
e∈E
k
+ (Ta N) e∈E
k
− (Ta N)
0≤y ≤c , ∀e∈E(TN )∪E(TN ).
e e a→i a→j
{
That is, the maximum value of weighted arc-flow of the optimal solution of WMMFN a (z) equals max mN a→γ(i) (z),
}
mN a→γ(j) (z) ,forany0≤z ≤c a .NowtheclaimofLemma2followsimmediately. □
ItisclearthatLemma2establishestherelationbetweenBPalgorithmandcomputationtreeTN.Next,weshallshow
a
thecorrectnessandconvergenceofmin–maxBPalgorithmforWMMF asfollows.
P
as
r
s
o
u L
o
e m
f
t e
o
e
f
w
T
. = l
h
.o
e
.
o
g u .
r
v ˆ
e
x
m
N e b 0 e >
1
t
.
h x e ∗ e
T
0
o
r . o T
t
o h
h
t e
e
n o
c
, f
o
b t
n
y h
t
e
r
L
a
e c
r
m o
y
m
,
m
w
p a u
e
2 t
s
a ,
u
t t i h
p
o e
p
n r
o
e t
s
r
e
i e s e
t
a
h
n T
at
N o
t
p
h
a t s
e
im
r
a
e
a b l
i
o
s
s v o
a
e l
n
. u F t
a
i o o
r
r
c
n a
e
y n 0 ∗ y
∈
o v f e
E
W rt
s
e M
u
x
c
M
h
i
t
∈ F
ha
N e0 V
tˆ
o s
x
( u
N
e T 0 c N h
̸=
), th d
x
a e
∗
e t 0 n y o
w
∗ e t 0 e
h
>
e
b
r
y
e
x∗ e
N
E 0 . +
>
(TN 2
n
)
.
a
W
nd
e
E − (TN) t 0 he set of arcs leaving and entering i in TN, res e p 0 ectively. Since x∗ and y∗ are the feas e i 0 ble solutions of i W e M 0 MF
i e0 e0
andWMMFN,respectively,
e0
∑ ∑
fγ(u) =x ∗
e0
+ x ∗
e
− x ∗
e
, (7)
e∈E
i
+\e0 e∈E
i
−
∑ ∑
fγ(u) =y ∗
e0
+ y ∗
e
− y ∗
e
. (8)
e∈E
i
+ (Te N
0
)\e0 e∈E
i
− (Te N
0
)
Due to the inequality y∗ > x∗ , using (7)–(8), there exists an arc e ̸= e incident to u such that y∗ > x∗ if e and e
have the same orientati e o 0 n at e u 0 (e is ingoing from u and e is outg 1 oing 0 from u), or y∗ < x∗ , othe e r 1 wise. e1 Simil 1 arly, we 0
o ca th n e f r i w nd ise a . rc A e s − im 1 i ̸= lar e a 0 rg in u c m id e e n n t t c t a o n 1 v be su a c p h pl t i h ed at re y c ∗ e− u 1 rs > ive x ly ∗ e− u 1 t i i 0 f liz e i − n 1 g a t n h d ei e n 0 e h q a u v a e lit t i h e e sb sa e m tw e e e 1 e o n rie v n a e t l 1 u at e io o n fc a o t m v p , o o n r e y n ∗ e− ts 1 o < fx x ∗ ∗ e , − y 1∗ ,
andtheequalityconstraint(1),(3)inlinearprogramming(I)and(II)oneachvertex,respectively.Continuingfurtherall
t
fo
h
r
e
−
w
N
ay
≤
do
i
w
≤
n
N
t
,
otheleavesofT
e
N
0
,wewillfinallyobtainapathdenotedbyP = {e−N ,...,e−1 ,e
0
,e
1
,...,e
N
}suchthat
y ∗ >x ∗ ⇔ bothe ande havethesameorientation, (9)
ei ei i 0
y ∗ <x ∗ ⇔ bothe ande havetheoppositeorientation. (10)
ei ei i 0
Accordingtothedefinitionsofx∗andy∗,suchapathisguaranteedtoexist.Fig.2depictsanexampleofsuchapathgiven
bydashedarcs.
Letmax (x)=max{w x :e∈E},wherexisafeasiblesolutionoftheWMMF.Ifafeasiblesolutiony′ ofWMMFN
canbeobta E inedbymodif e yi e ngy∗ suchthat e0
max(y ∗ )>max(y ′ ),
E(Te N
0
) E(Te N
0
)
127

G.Dai,L.Guo,G.Gutinetal. DiscreteAppliedMathematics354(2024)122–130
|     |     |     | Fig.2. | AnexampleofthepathP |     | onacomputationtreeTv |     | 2     | withdashedarcs. |
| --- | --- | --- | ------ | ------------------- | --- | -------------------- | --- | ----- | --------------- |
|     |     |     |        |                     |     |                      |     | 1 v 2 |                 |
thenacontradictionarisestotheoptimalityofy∗.DefineA = {e ∈ P : y∗ > x∗}andB = {e ∈ P : y∗ < x∗}.AsbothA
|     |     |     |     |     |     |     |     | e   | e e e |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
andB arefinitesets,thereexistsε>0suchthaty∗−ε≥x∗ foranye∈A andy∗+ε≤x∗ foranye∈B.Let
|     |         |     |     |     | e   | e   |     |     | e e |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | ⎧ y∗−ε, |     | e∈A |     |     |     |     |     |     |
⎨ e
′
|     | y = y∗+ε, |     | e∈B        |     |     |     |     |     |     |
| --- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
|     | e         | e   |            |     |     |     |     |     |     |
|     | ⎩ y∗,     |     | otherwise. |     |     |     |     |     |     |
e
|     | y′ = y∗ | −ε ≥ | x∗ ≥ | ∈   | y′ = | y∗ +ε | ≤ x∗ ≤ |     | ∈   |
| --- | ------- | ---- | ---- | --- | ---- | ----- | ------ | --- | --- |
Then 0 for any e A and c for any e B, which satisfies all the capacity
| constraintsof(II).Next,wewilldistinguishthreecasesbelowtoshowthaty′ | e e |     | e   |     | e   | e   | e   | e   |     |
| ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
satisfiesalltheotherequalityconstraints
of(I).Notethat,bythedefinitionofy′,weonlyneedtoconsidertheedgesbelongingtoE(P)
= A ∪B.Foranyvertex
| i∈Vo(TN),lete′,e′′ |     | ∈A  | ∪B bethearcsincidenttoi. |     |     |     |     |     |     |
| ------------------ | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
e 0
| Case | 1 .e′ ande′′ | havethesameorientationase |     |     | .   |     |     |     |     |
| ---- | ------------ | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
0
By(9)andthedefinitionofA,wehavethate′,e′′ ∈A.Sincee′ande′′areinthesameorientation,oneof{e′,e′′}isan
arcenteringi,andtheotherisanarcleavingi.Withoutlossofgenerality,weassumethate′ ∈E + (TN)ande′′ ∈E − (TN).
i e0 i e0
Then
|     | ∑         |         | ∑            |           |           |         |     |     |     |
| --- | --------- | ------- | ------------ | --------- | --------- | ------- | --- | --- | --- |
|     |           | ′ −     | ′            |           |           |         |     |     |     |
|     |           | y       | y            |           |           |         |     |     |     |
|     |           | e       | e            |           |           |         |     |     |     |
|     | e∈E +     | N       | e∈E − N      |           |           |         |     |     |     |
|     | i (Te     | )       | i (Te )      |           |           |         |     |     |     |
|     | (         | 0       | ) 0          | (         | )         |         |     |     |     |
|     | ′         | ∑       | ′            | ′ ∑       | ′         |         |     |     |     |
|     | = y e′ +  |         | y −          | y e′′ +   | y         |         |     |     |     |
|     |           |         | e            |           | e         |         |     |     |     |
|     |           | +       |              | −         |           |         |     |     |     |
|     |           | e∈E (Te | N )\e′       | e∈E (Te   | N )\e′′   |         |     |     |     |
|     |           | i       | 0            | i         | 0         |         |     |     |     |
|     | (         |         | ∑            | ) (       | ∑         | )       |     |     |     |
|     | = y ∗ −ε+ |         | y ∗          | − y ∗ −ε+ |           | y ∗     |     |     |     |
|     | e′        |         | e            | e′′       |           | e       |     |     |     |
|     |           | e∈E     | + (Te N )\e′ |           | e∈E − (Te | N )\e′′ |     |     |     |
|     |           |         | i 0          |           | i         | 0       |     |     |     |
|     | ∑         |         | ∑            |           |           |         |     |     |     |
|     | =         | y ∗−    | y ∗          |           |           |         |     |     |     |
|     |           | e       | e            |           |           |         |     |     |     |
|     | e∈E +     | N       | e∈E − N      |           |           |         |     |     |     |
|     | i (Te     | 0 )     | i (Te 0 )    |           |           |         |     |     |     |
|     | = .       |         |              |           |           |         |     |     |     |
fγ(i)
| Case2.e′ | ande′′ | havetheoppositeorientationase |     |     |     | .   |     |     |     |
| -------- | ------ | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
0
By(10)andthedefinitionofB,wehavethate′,e′′ ∈B.Sincee′ande′′areinthesameorientation,oneof{e′,e′′}isan
arcenteringi,andtheotherisanarcleavingi.Withoutlossofgenerality,weassumethate′ ∈E + (TN)ande′′ ∈E − (TN).
i e0 i e0
Then
|     | ∑         |           | ∑            |           |           |         |     |     |     |
| --- | --------- | --------- | ------------ | --------- | --------- | ------- | --- | --- | --- |
|     |           | ′ −       | ′            |           |           |         |     |     |     |
|     |           | y e       | y e          |           |           |         |     |     |     |
|     | e∈E +     | N         | e∈E − N      |           |           |         |     |     |     |
|     | i (Te     | 0 )       | i (Te )0 )   |           |           |         |     |     |     |
|     | (         | ∑         |              | ( ∑       | )         |         |     |     |     |
|     | = y ′ +   |           | y ′ −        | y ′ +     | y ′       |         |     |     |     |
|     | e′        |           | e            | e′′       | e         |         |     |     |     |
|     |           | e∈E + (Te | N ) \e′      | e∈E − (Te | N )\e′′   |         |     |     |     |
|     |           | i         | 0            | i         | 0         |         |     |     |     |
|     | (         |           | ∑            | ) (       | ∑         | )       |     |     |     |
|     | = y ∗ +ε+ |           | y ∗          | − y ∗ +ε+ |           | y ∗     |     |     |     |
|     | e′        |           | e            | e′′       |           | e       |     |     |     |
|     |           | e∈E       | + (Te N )\e′ |           | e∈E − (Te | N )\e′′ |     |     |     |
|     |           |           | i 0          |           | i         | 0       |     |     |     |
|     | ∑         | ∗−        | ∑ ∗          |           |           |         |     |     |     |
|     | =         | y         | y            |           |           |         |     |     |     |
|     |           | e         | e            |           |           |         |     |     |     |
|     | +         |           | −            |           |           |         |     |     |     |
|     | e∈E (Te   | N )       | e∈E (Te N )  |           |           |         |     |     |     |
|     | i         | 0         | i 0          |           |           |         |     |     |     |
|     | = fγ(i) . |           |              |           |           |         |     |     |     |
128

G.Dai,L.Guo,G.Gutinetal. DiscreteAppliedMathematics354(2024)122–130
| Case3.e′ | ande′′ | areintheoppositeorientation. |     |     |     |     |     |     |     |     |
| -------- | ------ | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Inthiscase,thereisexactlyoneof{e′,e′′}hasthesameorientationase .Withoutlossofgenerality,weassumethat
0
| e′  |     |     |     | e′′ |     |     |     |     |     | e′ ∈ A |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
has the same orientation as e 0 , and has the opposite orientation as e 0 . Then by (9) and (10), we have that
| ande′′ | ∈B.Sincee′ | ande′′ | areintheoppositeorientation,bothe′ |     |     |     |     | ande′′ |     |     |
| ------ | ---------- | ------ | ---------------------------------- | --- | --- | --- | --- | ------ | --- | --- |
arearcsenteringorleavingi.
| • Ifbothe′ | ande′′ | arearcsenteringi,then |            |     |                    |       |              |     |     |     |
| ---------- | ------ | --------------------- | ---------- | --- | ------------------ | ----- | ------------ | --- | --- | --- |
|            |        | ∑ ′                   | − ∑        | ′   |                    |       |              |     |     |     |
|            |        | y                     |            | y   |                    |       |              |     |     |     |
|            |        | e                     |            | e   |                    |       |              |     |     |     |
|            |        | +                     | −          |     |                    |       |              |     |     |     |
|            | e∈E    | (Te N )               | e∈E (Te N  | )   |                    |       |              |     |     |     |
|            |        | i 0                   | i 0        |     |                    |       |              |     |     |     |
|            |        | ∑                     | (          |     | ∑                  |       | )            |     |     |     |
|            | =      | y ′                   | − y ′ +y   | ′ + |                    | y ′   |              |     |     |     |
|            |        | e                     | e′         | e′′ |                    | e     |              |     |     |     |
|            | e∈E    | + (Te N )             |            | e∈E | − (Te N )\{e′,e′′} |       |              |     |     |     |
|            |        | i 0                   |            |     | i 0                |       |              |     |     |     |
|            |        | ∑                     | (          |     |                    |       | ∑            | )   |     |     |
|            | =      | ∗                     | − ∗ −ε)+(y |     | ∗ +ε)+             |       |              | ∗   |     |     |
|            |        | y e                   | (y e′      |     | e′′                |       |              | y e |     |     |
|            | e∈E    | + N                   |            |     |                    | e∈E − | N )\{e′,e′′} |     |     |     |
|            |        | i (Te 0 )             |            |     |                    | i     | (Te 0        |     |     |     |
|            |        | ∑                     | ∑          |     |                    |       |              |     |     |     |
|            | =      | ∗−                    |            | ∗   |                    |       |              |     |     |     |
|            |        | y                     |            | y   |                    |       |              |     |     |     |
|            |        | e                     |            | e   |                    |       |              |     |     |     |
|            | e∈E    | + N                   | e∈E − N    |     |                    |       |              |     |     |     |
|            |        | i (Te 0 )             | i (Te 0    | )   |                    |       |              |     |     |     |
.
= fγ(i)
| • Ifbothe′ | ande′′ |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
arearcsleavingi,then
|     |      | ∑         | ∑                    |       |                  |         |       |         |     |     |
| --- | ---- | --------- | -------------------- | ----- | ---------------- | ------- | ----- | ------- | --- | --- |
|     |      | ′         | −                    | ′     |                  |         |       |         |     |     |
|     |      | y         |                      | y     |                  |         |       |         |     |     |
|     |      | e         |                      | e     |                  |         |       |         |     |     |
|     | e∈E  | + N       | e∈E − N              |       |                  |         |       |         |     |     |
|     |      | i (Te 0 ) | i (Te 0              | )     |                  |         |       |         |     |     |
|     | (    |           |                      |       | )                |         |       |         |     |     |
|     |      | ′ ′       | ∑                    |       | ′                | ∑       | ′     |         |     |     |
|     | = y  | e′ +y e′′ | +                    | y     | −                | y       |       |         |     |     |
|     |      |           |                      |       | e                |         | e     |         |     |     |
|     |      |           | +                    |       |                  | −       |       |         |     |     |
|     |      |           | e∈E (Te N )\{e′,e′′} |       | e∈E              | (Te N ) |       |         |     |     |
|     |      |           | i 0                  |       |                  | i 0     |       |         |     |     |
|     | (    |           |                      |       | ∑                | )       | ∑     |         |     |     |
|     | = (y | ∗ −ε)+(y  | ∗ +ε)+               |       |                  | y ∗     | −     | y ∗     |     |     |
|     |      | e′        | e′′                  |       |                  | e       |       | e       |     |     |
|     |      |           |                      | e∈E + | (Te N )\{e′,e′′} |         | e∈E − | (Te N ) |     |     |
|     |      |           |                      | i     | 0                |         | i     | 0       |     |     |
|     |      | ∑         | ∑                    |       |                  |         |       |         |     |     |
|     | =    | y ∗−      |                      | y ∗   |                  |         |       |         |     |     |
|     |      | e         |                      | e     |                  |         |       |         |     |     |
|     | e∈E  | + (Te N ) | e∈E − (Te N          | )     |                  |         |       |         |     |     |
|     |      | i 0       | i 0                  |       |                  |         |       |         |     |     |
= .
fγ(i)
| Thisimpliesy′ | isafeasiblesolutionofWMMFN. |     |     |     |     |     |     |     |     |     |
| ------------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e
|     |     |     |     |     | y∗  | 0 > |     | y′  | ∗ andy′ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
N o w , w e o n ly n e e d to s h o w t h a tm a x E(T N ) ( ) ma x E ( Te N ) ( ). Sinc e t h e o n l y d if f er e n ce b e t w e en y istheflow
|     |     |     |     |     | e 0 |     | >0  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
valu e s o f ar c s in P , i t is su f fi ci en t t o sh o w t h a t m a x ( y ∗ ) m a x ( y′) . S u p p o s e o n t h e co n t r ar y th a t
|       |         |      |      |     |     | E(P) |     | E(P) |     |      |
| ----- | ------- | ---- | ---- | --- | --- | ---- | --- | ---- | --- | ---- |
|       | ∗       |      | ′ ). |     |     |      |     |      |     |      |
| max(y | )≤max(y |      |      |     |     |      |     |      |     | (11) |
|       | E(P)    | E(P) |      |     |     |      |     |      |     |      |
NotethatP canbedecomposedintoasimpleundirectedpathandsomesimpleundirectedcyclesinG.LetC denotethe
|                                                           |     |     |     |     |     |        |     | iterationsis2N+1andthus | 2N+1 | ≥ n+1 >1, |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | ------ | --- | ----------------------- | ---- | --------- |
| setofthesesimpleundirectedcycles.SincethelengthofthepathP |     |     |     |     |     |        |     | afterN                  |      |           |
|                                                           |     |     |     |     |     | ∈C.Let |     |                         | n    | n         |
theremustexistatleastoneundirectedcycleC
⎧
|     | x∗+ε, |     | e∈A ∩E(C) |     |     |     |     |     |     |     |
| --- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
⎨ e
|     | ′ = x∗−ε, |     | e∈B∩E(C) |     |     |     |     |     |     |     |
| --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
x
|     | e e   |     |            |     |     |     |     |     |     |     |
| --- | ----- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|     | ⎩ x∗, |     | otherwise. |     |     |     |     |     |     |     |
e
|     |     |     | y′, |     |     |     | x′  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
By a similar argument as it is not difficult to show that is a feasible solution of WMMF on the original graph G.
| Accordingtothedefinitionsofx′ |           |      | andy′,itfollowsfrom(11)that |     |     |     |     |     |     |      |
| ----------------------------- | --------- | ---- | --------------------------- | --- | --- | --- | --- | --- | --- | ---- |
|                               | ′ )≤max(x | ∗    | ).                          |     |     |     |     |     |     |      |
| max(x                         |           |      |                             |     |     |     |     |     |     | (12) |
|                               | E(P)      | E(P) |                             |     |     |     |     |     |     |      |
Dueto(12),wehavethat
|     | ∗ )≥max(x | ∗   | )≥max(x | ′ )≥max(x | ′ ). |     |     |     |     |     |
| --- | --------- | --- | ------- | --------- | ---- | --- | --- | --- | --- | --- |
max(x
|     | E   | E(P) | E(P) | E(C) |     |     |     |     |     |     |
| --- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- |
Sincetheonlydifferencebetweenx∗ andx′ istheflowvaluesofarcsinC,bythedefinitionsofx′,itistoseethatx′ isa
|     |     |     |     |     | (x′) | ≤   | (x∗).Thisleadstoacontradictionthatx∗ |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ------------------------------------ | --- | --- | --- |
feasiblesolutionofWMMF suchthatmax E max E istheuniqueoptimal
| solutionofWMMF |     | whichcompletestheproof. |     |     |     | □   |     |     |     |     |
| -------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
129

G.Dai,L.Guo,G.Gutinetal. DiscreteAppliedMathematics354(2024)122–130
5. Conclusion
As a distributed, message-passing algorithm, Belief Propagation (BP) algorithm has been widely used in areas like
modernstatistics,codingtheory,combinatorialoptimizationandartificialintelligence.DespiteempiricalsuccessesofBP
algorithm in many practical scenarios, the theoretical understanding of the performance of BP algorithm remains far
from complete. In this paper, we derive a min–max BP algorithm for the weighted min–max flow (WMMF) problem
andanalyzethecorrectnessandconvergenceofthealgorithmpresented.Weprovethatmin–maxBPalgorithmconverges
totheoptimalsolutionwithfully-polynomialrunningtime,providedthattheoptimalsolutionisunique.Moreover,based
ontheresearchresultsandcontributionsofGamarniketal.[11],asimplemodificationofBPalgorithmcanbeprovided
to obtain a fully polynomial-time randomized approximation scheme (FPRAS) without requiring the uniqueness of the
optimalsolution.Finally,itremainsopenforfutureresearchtostudymoregeneraloptimizationproblemsandviability
ofBPalgorithmsforthem.
Acknowledgments
Weareverygratefultothereviewersfortheirinvaluablesuggestionsandcomments,whichgreatlyhelptoimprove
themanuscript.TheresearchwaspartiallysupportedbyNationalNaturalScienceFoundationofChinaunderGrantNos.
11871280,U1811461,61772005,11971349andNaturalScienceFoundationofGuangdongProvinceofChinaunderGrant
No.2020B1515310009.
References
[1] D.Achlioptas,F.Ricci-Tersenghi,Onthesolution-spacegeometryofrandomconstraintsatisfactionproblems,in:ProceedingsoftheThirty-Eighth
AnnualACMSymposiumonTheoryofComputing,ACM,2006,pp.130–139.
[2] M.Bayati,C.Borgs,J.Chayes,R.Zecchina,Beliefpropagationforweightedb-matchingsonarbitrarygraphsanditsrelationtolinearprograms
withintegersolutions,SIAMJ.DiscreteMath.25(2011)989–1011.
[3] M. Bayati, D. Shah, M. Sharma, Max-product for maximum weight matching: convergence, correctness, and LP duality, IEEE Trans. Inform.
Theory54(2008)1241–1251.
[4] T.Brunsch,K.Cornelissen,B.Manthey,H.Röglin,Smoothedanalysisofbeliefpropagationforminimum-costflowandmatching,in:WALCOM:
AlgorithmsandComputation,Springer,BerlinHeidelberg,2012,pp.182–193.
[5] R.E.Burkard,Ageneralhungarianmethodforthealgebraietranspertationproblem,DiscreteMath.22(1978)219–232.
[6] Y. Cheng, M. Neely, K.M. Chugg, Iterative message passing algorithm for bipartite maximum weighted matching, in: Proceedings of IEEE
InternationalSymposiumInformationTheory,Cambridge,2006,pp.1934–1938.
[7] G.Dai,F.Li,Y.Sun,D.Xu,X.Zhang,ConvergenceandcorrectnessofbeliefpropagationfortheChinesepostmanproblem,J.GlobalOptim.75
(2019)813–831.
[8] H.A.Eiselt,M.Gendreau,Anoptimalalgorithmforweightedminimaxflowcentersontrees,Transp.Sci.25(1991)314–316.
[9] B.J.Frey,D.Dueck,Clusteringbypassingmessagesbetweendatapoints,Science315(2007)972–976.
[10] S.Fujishige,A.Nakayama,W.Cui,Ontheequivalenceofthemaximumbalancedflowproblemandtheweightedminimaxflowproblem,Oper.
Res.Lett.5(1986)207–209.
[11] D.Gamarnik,D.Shah,Y.Wei,Beliefpropagationformin-costnetworkflow:convergence&correctness,Oper.Res.60(2012)410–428.
[12] T.Ichimori,H.Ishii,T.Nishida,Findingtheweightedminimaxflowinapolynomialtime,J.Oper.Res.Soc.Japan23(1980)268–271.
[13] T.Ichimori,H.Ishii,T.Nishida,Weightedminimaxreal-valuedflows,J.Oper.Res.Soc.Japan24(1981)52–59.
[14] T.Ichimori,M.Murata,H.Ishii,T.Nishida,Minimaxcostflowproblem,Technol.Repts.OsakaUniv.30(1980)39–44.
[15] M.Mézard,Passingmessagesbetweendisciplines,Science301(2003)1685–1686.
[16] M.Mézard,G.Parisi,R.Zecchina,Analyticandalgorithmicsolutionofrandomsatisfiabilityproblems,Science297(2002)812–815.
[17] J.Pearl,ProbabilisticReasoninginIntelligentSystems:NetworksofPlausibleReasoning,MorganKaufmann,CA,1988.
[18] T. Richardson, R. Urbanke, The capacity of low-density parity check codes under message-passing decoding, IEEE Trans. Inform. Theory 47
(2001)599–618.
[19] S.Sanghavi,D.Malioutov,A.Willsky,BeliefpropagationandLPrelaxationforweightedmatchingingeneralgraphs,IEEETrans.Inform.Theory
54(2011)2203–2212.
[20] S.Sanghavi,D.Shah,A.S.Willsky,Messagepassingformaximumweightindependentset,IEEETrans.Inform.Theory55(2009)4822–4834.
[21] D.F.Stanat,G.A.Magó,Minimizingmaximumflowsinlineargraphs,Networks9(1979)333–361.
[22] Y.Weiss,W.Freeman,Ontheoptimalityofsolutionsofthemax-productbelief-propagationalgorithminarbitrarygraphs,IEEETrans.Inform.
Theory47(2001)736–744.
[23] J.Yedidia,W.Freeman,Y.Weiss,Constructingfree-energyapproximationsandgeneralizedbeliefpropagationalgorithms,IEEETrans.Inform.
Theory51(2005)2282–2312.
130