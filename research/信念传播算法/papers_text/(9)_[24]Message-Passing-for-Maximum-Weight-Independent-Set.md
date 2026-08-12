4822 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.55,NO.11,NOVEMBER2009
|     |     | Message |     |     | Passing     |     | for | Maximum |     |     |     | Weight |     |     |     |
| --- | --- | ------- | --- | --- | ----------- | --- | --- | ------- | --- | --- | --- | ------ | --- | --- | --- |
|     |     |         |     |     | Independent |     |     |         | Set |     |     |        |     |     |     |
SujaySanghavi,Member,IEEE, Devavrat Shah,and AlanS.Willsky,Fellow,IEEE
Abstract—In this paper, we investigate the use of message- NP-hard, and hard to approximate [6]. In this paper, we in-
passingalgorithmsfortheproblemoffindingthemax-weightin-
|     |     |     |     |     |     |     |     | vestigate | the use | of message-passing |     |     | algorithms, |     | like loopy |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------------------ | --- | --- | ----------- | --- | ---------- |
dependentset(MWIS)inagraph.First,westudytheperformance
|                  |     |       |             |        |              |     |         | max-product | belief | propagation, |     | as practical |     | solutions | for the |
| ---------------- | --- | ----- | ----------- | ------ | ------------ | --- | ------- | ----------- | ------ | ------------ | --- | ------------ | --- | --------- | ------- |
| of the classical |     | loopy | max-product | belief | propagation. |     | We show |             |        |              |     |              |     |           |         |
that eachfixed-point estimateofmax product canbe mapped in MWISproblem.Wenowsummarizeourmotivationsfordoing
a natural way to an extreme point of the linear programming so,andthenoutlineourcontribution.
(LP)polytopeassociatedwiththeMWISproblem.However,this Ourprimarymotivationcomesfromapplications.TheMWIS
extremepointmaynotbetheonethatmaximizesthevalueofnode
|     |     |     |     |     |     |     |     | problem | arises naturally |     | in many | scenarios |     | involving | resource |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | --- | ------- | --------- | --- | --------- | -------- |
weights;theparticularextremepointatfinalconvergencedepends
allocationinthepresenceofinterference.Itisoftenthecasethat
| on the initialization |     | of  | max product. | We  | then | show that | if max |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ------------ | --- | ---- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
productisstartedfromthenaturalinitializationofuninformative large instances of the weighted independent set problem need
messages,italwayssolvesthecorrectLP,ifitconverges.Thisre- to be (at least approximately) solved in a distributed manner
sultisobtainedviaadirectanalysisoftheiterativealgorithm,and
usinglightweightdatastructures.InSectionII-A,wedescribe
cannotbeobtainedbylookingonlyatfixedpoints.Thetightness
onesuchapplication:schedulingchannelaccessandtransmis-
oftheLPrelaxationisthusnecessaryformax-productoptimality,
butitisnotsufficient.Motivatedbythisobservation,weshowthat sionsinwirelessnetworks.Message-passingalgorithmsprovide
a simple modification of max product becomes gradient descent apromisingalternativetocurrentschedulingalgorithms.
on (a smoothed version of) the dual of the LP, and converges to Another, equally important, motivation is the potential
thedualoptimum.Wealsodevelopamessage-passingalgorithm
|               |            |        |      |               |      |            |          | for obtaining   | new | insights    | into | the        | performance |          | of existing |
| ------------- | ---------- | ------ | ---- | ------------- | ---- | ---------- | -------- | --------------- | --- | ----------- | ---- | ---------- | ----------- | -------- | ----------- |
| that recovers | the        | primal | MWIS | solution      | from | the output | of the   |                 |     |             |      |            |             |          |             |
|               |            |        |      |               |      |            |          | message-passing |     | algorithms, |      | especially |             | on loopy | graphs.     |
| descent       | algorithm. | We     | show | that the MWIS |      | estimate   | obtained |                 |     |             |      |            |             |          |             |
using these two algorithms in conjunction is correct when the Tantalizing connections have been established between such
graph is bipartite and the MWIS is unique. Finally, we show algorithms and more traditional approaches like linear pro-
thatanyproblemofmaximumaposteriori(MAP)estimationfor
|     |     |     |     |     |     |     |     | gramming | (LP; | see [1], | [2], [12], | and | references |     | therein). We |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | -------- | ---------- | --- | ---------- | --- | ------------ |
probabilitydistributionsoverfinitedomainscanbereducedtoan
|     |     |     |     |     |     |     |     | consider | MWIS | problem | to  | understand | this | connection | as it |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------- | --- | ---------- | ---- | ---------- | ----- |
MWISproblem.Webelievethisreductionwillyieldnewinsights
|     |     |     |     |     |     |     |     | provides | a rich | (it is | NP-hard), | yet | relatively |     | (analytically) |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------ | --------- | --- | ---------- | --- | -------------- |
andalgorithmsforMAPestimation.
tractable,frameworktoinvestigatesuchconnections.
| Index       | Terms—Belief |     | propagation, | combinatorial |           | optimization, |     |     |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | ------------ | ------------- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| distributed | algorithms,  |     | independent  | set,          | iterative | algorithms,   |     |     |     |     |     |     |     |     |     |
linearprogramming(LP),optimization.
|     |     |     |     |     |     |     |     | A. RelatedWork |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Thedesignofmessage-passingalgorithmsforLPrelaxations
|     |     |     | I. INTRODUCTION |     |     |     |     |                   |     |              |     |          |      |      |             |
| --- | --- | --- | --------------- | --- | --- | --- | --- | ----------------- | --- | ------------ | --- | -------- | ---- | ---- | ----------- |
|     |     |     |                 |     |     |     |     | for combinatorial |     | optimization |     | problems | have | been | of interest |
T HEmax-weightindependentset(MWIS)problemis the for a while now. For example, the auction algorithm by Bert-
following: given a graph with positive weights on the sekas[27]attemptstodesignmessage-passingalgorithmforthe
|             |     |          |     |             |             |     |        | assignment | problem | by  | means | of an | approximate |     | primal-dual |
| ----------- | --- | -------- | --- | ----------- | ----------- | --- | ------ | ---------- | ------- | --- | ----- | ----- | ----------- | --- | ----------- |
| nodes, find | the | heaviest | set | of mutually | nonadjacent |     | nodes. |            |         |     |       |       |             |     |             |
MWIS is a well-studied combinatorial optimization problem algorithm,whichisinturnbasedonthedualcoordinatedescent
|                |     |        |         |               |     |          |       | algorithm.   | More            | recently,  | Wainwright, |       | Jaakkola,   |        | and Willsky |
| -------------- | --- | ------ | ------- | ------------- | --- | -------- | ----- | ------------ | --------------- | ---------- | ----------- | ----- | ----------- | ------ | ----------- |
| that naturally |     | arises | in many | applications. | It  | is known | to be |              |                 |            |             |       |             |        |             |
|                |     |        |         |               |     |          |       | [8] proposed | a tree          | reweighted |             | (TRW) | algorithm—a |        | general-    |
|                |     |        |         |               |     |          |       | ization of   | the max-product |            | algorithm.  |       | They        | showed | that fixed  |
ManuscriptreceivedJuly30,2008;revisedApril12,2009.Currentversion pointsoftheiralgorithmthatsatisfiedafurtherproperty,strong
publishedOctober21,2009.ThisworkwassupportedinpartbytheNational treeagreement(STA),willcorrespondtotheoptimumofa(cer-
ScienceFoundation(NSF)underProjectsCNS0546590,HSD0729361,andTF
tain)LPrelaxationofthemaximumaposteriori(MAP)estima-
0728554,bytheMURIfundedthroughtheArmyResearchOfficeunderGrant
W911NF-06-1-0076,andbytheU.S.AirForceOfficeofScientificResearch tionproblem.Insubsequentwork,Kolmogorov[4]provideda
underGrantFA9550-06-1-0324.Thematerialinthispaperwaspresentedin
counterexampletoshowthatthecorrespondencebetweenfixed
partattheConferenceonNeuralinformationProcessingSystems(NIPS),Van-
pointsofTRWandthesolutionofLPrelaxationmaynothold
couver,BC,Canada,December2007
S.SanghaviiswiththeDepartmentofElectricalandComputerEngineering, in general. However, Kolmogorov and Wainwright [20] estab-
PurdueUniversity,WestLafayette,IN47906USA(e-mail:sanghavi@purdue.
lishedthatforbinaryproblems,suchastheproblemofinterest
edu).
D.ShahandA.S.WillskyarewiththeDepartmentofElectricalEngineering inthispaper,thecorrespondencewillalwayshold;i.e.,thefixed
andComputerScience,MassachusettsInstituteofTechnology,Cambridge,MA pointsoftheTRWalgorithmalwayscorrespondtosolutionof
02139USA(e-mail:devavrat@mit.edu;willsky@mit.edu).
CommunicatedbyH.-A.Loeliger,AssociateEditorforCodingTechniques. the LP relaxation. However, this still does not guarantee that
DigitalObjectIdentifier10.1109/TIT.2009.2030448 TRWwillconvergetothefixedpoint.
0018-9448/$26.00©2009IEEE

SANGHAVIetal.:MESSAGEPASSINGFORMAXIMUMWEIGHTINDEPENDENTSET 4823
In work by Kolmogorov [4], a subsequential convergence Maxproductbearsastrikingsemanticsimilaritytodualcoor-
propertyofTRWwasestablishedunderamodified(orsequen- dinatedescentontheLP.Withtheintentionofmodifyingmax
tial) “scheduling ofmessage passing.” That is,the subsequen- product to make it as powerful as LP, in Section VI, we de-
|            |          |               |              |     |         |          | velop two | iterative | message-passing |     |     | algorithms. | The | first, ob- |
| ---------- | -------- | ------------- | ------------ | --- | ------- | -------- | --------- | --------- | --------------- | --- | --- | ----------- | --- | ---------- |
| tial limit | point of | the algorithm | will satisfy |     | what is | known as |           |           |                 |     |     |             |     |            |
theweaktreeagreement(WTA)condition.Forbinaryproblems, tainedbyaminormodificationofmaxproduct,approximately
thiswillmeanthatsuchasubsequentiallimitpointwillcorre- calculatestheoptimalsolutiontothedualoftheLPrelaxation
oftheMWISproblem.Itdoesthisviacoordinatedescentona
spondtosolutionofLPrelaxation.
SpecializedtothecaseofMWIS,acombinationofthesetwo convexifiedversionofthedual.Thesecondalgorithmusesthis
approximateoptimaldualtoproduceanestimateoftheMWIS.
resultswillimplythefollowing:underthemodifiedscheduling
Thisestimateiscorrectwhentheoriginalgraphisbipartite.We
oftheTRW,thereexistsalimitpoint(whichmayormaynotbe
identifiable)ofthealgorithmthatcorrespondstosolvingtheLP believethatthisalgorithmshouldbeofbroaderinterest.Wenote
that,tothebestofourknowledge,thisisthefirstiterative/mes-
relaxationoftheproblem.Therefore,whentheLPrelaxationis
|           |            |          |           |      |           |           | sage-passing | algorithm |          | for solving | MWIS | on              | weighted | bipar-  |
| --------- | ---------- | -------- | --------- | ---- | --------- | --------- | ------------ | --------- | -------- | ----------- | ---- | --------------- | -------- | ------- |
| tight and | has unique | integral | solution, | then | this will | yield the |              |           |          |             |      |                 |          |         |
|           |            |          |           |      |           |           | tite graph   | with      | provable | convergence |      | and correctness |          | guaran- |
MWIS.
tees.Thisresultstandsincontrastwiththefactthatthemodified
| Thefocus              | ofthispaper    |                                   | issomewhatdifferent.Unlike |          |             | many |                |            |           |         |                |          |              |            |
| --------------------- | -------------- | --------------------------------- | -------------------------- | -------- | ----------- | ---- | -------------- | ---------- | --------- | ------- | -------------- | -------- | ------------ | ---------- |
|                       |                |                                   |                            |          |             |      | TRW of         | Kolmogorov | [4]       | along   | with           | analysis | of           | Kolmogorov |
| of the above          | approaches     |                                   | where the algorithm        |          | is designed |      | to             |            |           |         |                |          |              |            |
|                       |                |                                   |                            |          |             |      | and Wainwright |            | [20] only | yields  | “subsequential |          | convergence” |            |
| solvethecorresponding |                | LPrelaxation,weinvestigatewhether |                            |          |             |      |                |            |           |         |                |          |              |            |
|                       |                |                                   |                            |          |             |      | guarantee;     | it is      | not clear | if such | a convergence  |          | can          | be indeed  |
| there is              | any connection | between                           | the                        | original | max-product | al-  |                |            |           |         |                |          |              |            |
verified(atleastnotcleartotheauthors).
gorithm—which at best can be viewed as tree-based approxi- TheaboveusesofmaxproductforMWISinvolvedposingthe
mationdynamicprogramming—andLPrelaxation.Alongthese
MWISasaMAPestimationproblem.InthefinalSectionVII,
lines,aseriesofrecentworks[1],[2],[13]leadtotheconclu-
wedothereverse:weshowhowanyMAPestimationproblem
sionthatfortheproblemof -matching,indeedthemaxproduct onfinitedomainscanbe convertedintoanMWISproblemon
isaspowerfulas(certain)LPrelaxation.Wereferaninterested
asuitablyconstructedauxiliarygraph.Thisimpliesthatanyal-
readertoarecentmonographonarelatedtopicbyWainwright
|     |     |     |     |     |     |     | gorithm | for solving | the | independent |     | set problem |     | immediately |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ----------- | --- | ----------- | --- | ----------- |
andJordan[10]. yields an algorithm for MAP estimation. This reduction may
proveusefulfrombothpracticalandanalyticalperspectives.
B. OurContributions
Tobeginwith,weformallydescribetheMWISproblem,for- II. MAX-WEIGHTINDEPENDENTSETANDITSLPRELAXATION
mulateitasanintegerprogram,andpresentitsnaturalLPrelax-
|     |     |     |     |     |     |     | Consider | a graph |     |     | , with | a set | of  | nodes and |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --- | --- | ------ | ----- | --- | --------- |
ation.WealsodescribehowtheMWISproblemarisesinwire-
|     |     |     |     |     |     |     | a set | of edges. | Let |     |     |     |     | be the |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --- | --- | --- | --- | --- | ------ |
lessnetworkscheduling(seeSectionII). neighborsof .Positiveweights areassociated
| Next,      | we describe | how | max product   | can | be used       | (as | a         |       |          |       |      |                |       |            |
| ---------- | ----------- | --- | ------------- | --- | ------------- | --- | --------- | ----- | -------- | ----- | ---- | -------------- | ----- | ---------- |
|            |             |     |               |     |               |     | with each | node. | A subset | of    | will | be represented |       | by vector  |
| heuristic) | for solving | the | MWIS problem. |     | Specifically, | we  |           |       |          |       |      |                |       |            |
|            |             |     |               |     |               |     |           |       | ,        | where |      | means          | is in | the subset |
constructaprobabilitydistributionwhoseMAPestimateisthe
|      |              |        |              |       |      |           | and | means | isnotinthesubset.Asubset |     |     |     |     | iscalledan |
| ---- | ------------ | ------ | ------------ | ----- | ---- | --------- | --- | ----- | ------------------------ | --- | --- | --- | --- | ---------- |
| MWIS | of the given | graph. | Max product, | which | is a | heuristic |     |       |                          |     |     |     |     |            |
independentsetifnotwonodesinthesubsetareconnectedby
for finding MAP estimates, emerges naturally from this con- anedge: forall .Weareinterestedin
struction(seeSectionIII).
|          |                    |     |                     |        |            |           | findinganMWIS |             | .Thiscanbenaturallyposedasaninteger |              |       |                 |            |             |
| -------- | ------------------ | --- | ------------------- | ------ | ---------- | --------- | ------------- | ----------- | ----------------------------------- | ------------ | ----- | --------------- | ---------- | ----------- |
| Now,     | max productis      | an  | iterativealgorithm, |        | andis      | typically |               |             |                                     |              |       |                 |            |             |
|          |                    |     |                     |        |            |           | program,      | denoted     | below                               | by           | . The | linear          | programing | relax-      |
| executed | until it converges |     | to a fixed          | point. | In Section | IV, we    | ation         |             |                                     |              |       |                 |            |             |
|          |                    |     |                     |        |            |           | of            | is obtained |                                     | by replacing |       | the integrality |            | constraints |
showthatfixedpointsalwaysexist,andcharacterizetheirstruc-
|     |     |     |     |     |     |     |     | with | the constraints |     |     | . We | will | denote the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------------- | --- | --- | ---- | ---- | ---------- |
ture. Specifically, we show that there is a one-to-one map be- correspondinglinearprogramby .Thedualof isdenoted
| tween estimates | of  | fixed | points, and extreme |     | points | of the in- |     |     |     |     |     |     |     |     |
| --------------- | --- | ----- | ------------------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
belowby
| dependent  | set LP      | polytope. | This polytope       |     | is defined   | only by |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --------- | ------------------- | --- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| the graph, | and each    | of its    | extrema corresponds |     | to the       | LP op-  |     |     |     |     |     |     |     |     |
| timum for  | a different | node      | weight function.    |     | This implies | that    |     |     |     |     |     |     |     |     |
max-productfixedpointsattempttosolve(theLPrelaxationof) forall
anMWISproblemonthecorrectgraph,butwithdifferent(pos-
siblyincorrect)nodeweights.Thisstandsincontrasttoitsper-
formancefortheweightedmatchingproblem[1],[2],[13],for
whichitisknowntoalwayssolvetheLPwithcorrectweights.
Sincemaxproductisadeterministicalgorithm,theparticular forall
fixedpoint(ifany)thatisreacheddependsontheinitialization.
InSectionV,wepursueanalternativelineofanalysis,anddi-
rectlyinvestigatetheperformanceoftheiterativealgorithmit-
| self, started | from | the “natural” | initialization |     | of uninformative |     |     |     |     |     |     |     |     |     |
| ------------- | ---- | ------------- | -------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
messages. For this case, we show that max-product estimates forall
exactlycorrespondtothetrueLP,atalltimes,notjustthefixed
| point. |     |     |     |     |     |     |     |     |     |     | forall |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |

4824 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.55,NO.11,NOVEMBER2009
Itiswellknownthat canbesolvedefficiently,andifithasan scheduling problem is to decide which nodes should transmit
integraloptimalsolutionthenthissolutionisanMWISof .If at a given time over a given frequency, so that 1) there is no
thisisthecase,wesaythatthereisnointegralitygapbetween interference, and 2) nodes which have a large amount of data
and ,orequivalently,thatthe relaxationistight. tosendaregivenpriority.Inparticular,itiswellknownthatif
eachnodeisgivenaweightequaltothedataithastotransmit,
A. Propertiesofthe optimalnetworkoperationdemandsschedulingthesetofnodes
|        |         |       |      |        |            |     |            | with highest | total weight. | If a | “ conflict | graph” | is  | made, with |
| ------ | ------- | ----- | ---- | ------ | ---------- | --- | ---------- | ------------ | ------------- | ---- | ---------- | ------ | --- | ---------- |
| We now | briefly | state | some | of the | well-known |     | properties | of           |               |      |            |        |     |            |
anedgebetweeneverypairofinterferingnodes,thescheduling
| the MWIS |     | , as these | will | be used/referred |     | to  | in the paper. |     |     |     |     |     |     |     |
| -------- | --- | ---------- | ---- | ---------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Thepolytopeofthe isthesetoffeasiblepointsforthelinear problemisexactlytheproblemoffindingtheMWISofthecon-
|          |            |     |       |        |          |        |             | flict graph. | The lack | of an infrastructure, |     | the | fact | that nodes |
| -------- | ---------- | --- | ----- | ------ | -------- | ------ | ----------- | ------------ | -------- | --------------------- | --- | --- | ---- | ---------- |
| program. | An extreme |     | point | of the | polytope | is one | that cannot |              |          |                       |     |     |      |            |
oftenhavelimitedcapabilities,andthelocalnatureofcommu-
| be expressed |     | as a convex |     | combination | of  | other | points in | the |     |     |     |     |     |     |
| ------------ | --- | ----------- | --- | ----------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
nication,allnecessitatealightweightdistributedalgorithmfor
polytope.
solvingtheMWISproblem.
| Lemma2.1[16,Th.64.7]: |     |     |     | The | polytopehasthefollowing |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
III. MAX-PRODUCTFORMWIS
properties:
1) foranygraph,theMWIS polytopeishalf-integral:any The classical max-product algorithm is a heuristic that can
| extremepointwillhaveeach |     |     |     |     |     | or  | ;   |         |                 |            |     |                  |     |           |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | ---------- | --- | ---------------- | --- | --------- |
|                          |     |     |     |     |     |     |     | be used | to find the MAP | assignment |     | of a probability |     | distribu- |
2) for bipartite graphs, the polytope is integral: each ex- tion.Now,givenanMWISproblemon ,associate
| tremepointwillhave |     |     |     |     | or . |     |     |                       |     |          |     |     |                |     |
| ------------------ | --- | --- | --- | --- | ---- | --- | --- | --------------------- | --- | -------- | --- | --- | -------------- | --- |
|                    |     |     |     |     |      |     |     | abinaryrandomvariable |     | witheach |     |     | andconsiderthe |     |
followingjointdistribution:for
Half-integralityisanintriguingpropertythatholdsforLPre-
| laxations | of a | few combinatorial |     | problems |     | (e.g., | vertex cover, |     |     |     |     |     |     |     |
| --------- | ---- | ----------------- | --- | -------- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
(1)
matchings,etc.).Half-integralityimpliesthatanyextremumop-
| timumof | willhavesomenodessetto |     |     |     |     | ,andalltheirneigh- |     |     |     |     |     |     |     |     |
| ------- | ---------------------- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
bors set to . The nodes set to will appear in clusters: each where is the normalization constant. In the above, is the
such node will have at least one other neighbor also set to . standard indicator function: and . It is
Wewillseelaterthatasimilarstructurearisesinmax-product easy to see that if is an indepen-
fixedpoints.
|                           |                                             |                |     |         |     |        |               | dent set,  | and                   | otherwise. |             | Thus, any | MAP         | estimate |
| ------------------------- | ------------------------------------------- | -------------- | --- | ------- | --- | ------ | ------------- | ---------- | --------------------- | ---------- | ----------- | --------- | ----------- | -------- |
|                           |                                             |                |     |         |     |        |               |            | correspondstoanMWISof |            |             |           | .           |          |
| Lemma                     | 2.2                                         | [22, Corollary |     | 64.9a]: |     | optima | are partially |            |                       |            |             |           |             |          |
|                           |                                             |                |     |         |     |        |               | The update | equations             | for max    | product     | can       | be derived  | in a     |
| correct:                  | for any                                     | graph,         | any | optimum |     | and    | any node      | , if       |                       |            |             |           |             |          |
|                           |                                             |                |     |         |     |        |               | standard   | and straightforward   |            | fashion     | from the  | probability | dis-     |
| themass                   | isintegralthenthereexistsanMWISforwhichthat |                |     |         |     |        |               |            |                       |            |             |           |             |          |
|                           |                                             |                |     |         |     |        |               | tribution. | We now describe       | the        | max-product |           | algorithm   | as de-   |
| node’smembershipisgivenby |                                             |                |     | .       |     |        |               |            |                       |            |             |           |             |          |
|                           |                                             |                |     |         |     |        |               | rived from | . At every            | iteration  | , each      | node      | sends       | a mes-   |
Thenextlemmastatesthestandardcomplimentaryslackness sage to each neighbor . Each
conditionsofLP,specializedfortheMWIS ,andforthecase nodealsomaintainsabelief vector.Themessage
whenthereisnointegralitygap. andbeliefupdates,aswellasthefinaloutput,arecomputedas
follows.
| Lemma | 2.3:    | When   | there  | is no      | integrality | gap | between |     |     |     |     |     |     |     |
| ----- | ------- | ------ | ------ | ---------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| and   | , there | exists | a pair | of optimal | solutions   |     |         | ,   |     |     |     |     |     |     |
Max-ProductforMWIS
|     |     | of  | and     | ,   | respectively, |        | such that: | a)            |     |     |     |        |     |     |
| --- | --- | --- | ------- | --- | ------------- | ------ | ---------- | ------------- | --- | --- | --- | ------ | --- | --- |
|     | ,b) |     |         |     |               | forall |            | ,and          |     |     |     |        |     |     |
|     |     |     |         |     |               |        |            | (o)Initially, |     |     |     | forall |     | .   |
| c)  |     |     | ,forall |     |               | .      |            |               |     |     |     |        |     |     |
(i)Themessagesareupdatedasfollows:
B. SampleApplication:SchedulinginWirelessNetworks
| We now       | briefly    | describe    |     | an important |          | application | that     | re-  |     |     |     |     |     |     |
| ------------ | ---------- | ----------- | --- | ------------ | -------- | ----------- | -------- | ---- | --- | --- | --- | --- | --- | --- |
| quires an    | efficient, | distributed |     | solution     | to       | the MWIS    | problem: |      |     |     |     |     |     |     |
| transmission | scheduling |             | in  | wireless     | networks | that        | lack a   | cen- |     |     |     |     |     |     |
tralizedinfrastructure,andwherenodescanonlycommunicate
withlocalneighbors(e.g.,see[19]).Suchnetworksareubiqui-
tousinthemodernworld:examplesrangefromsensornetworks
thatlackwiredconnectionstothefusioncenter,andadhocnet-
worksthatcanbequicklydeployedinareaswithoutcoverage,
| to the 802.11 |     | wi-fi networks |     | that currently |     | represent | the | most |     |     |     |     |     |     |
| ------------- | --- | -------------- | --- | -------------- | --- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- |
widelyusedmethodforwirelessdataaccess. (ii)Nodes ,computetheirbeliefsasfollows:
| Fundamentally, |     | any | two | wireless | nodes | that transmit | at  | the |     |     |     |     |     |     |
| -------------- | --- | --- | --- | -------- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
sametimeandoverthesamefrequencieswillinterferewitheach
| other, if | they are | located | close | by. | Interference | means | that | the |     |     |     |     |     |     |
| --------- | -------- | ------- | ----- | --- | ------------ | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
intendedreceiverswillnotbeabletodecodethetransmissions.
Typicallyinanetworkonlycertainpairsofnodesinterfere.The

SANGHAVIetal.:MESSAGEPASSINGFORMAXIMUMWEIGHTINDEPENDENTSET 4825
Thefollowinglemmaestablishesthatfixedpointsalwaysexist.
(iii)EstimateMWIS asfollows: Wenotethatsuchargumentshavebeenusedinliteratureinthe
contextofestablishingexistenceoffixedpoints(e.g.,see[7]).
if
|     |     |     |     |     |     |     | Lemma4.1: |     | Thereexistsatleastonefixedpoint |     |     |     |     | suchthat |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------------------------- | --- | --- | --- | --- | -------- |
foreach
|            |     |                     |     |     |              |     | Proof:       | Let |        |          | , and       | suppose    | at time   | each      |
| ---------- | --- | ------------------- | --- | --- | ------------ | --- | ------------ | --- | ------ | -------- | ----------- | ---------- | --------- | --------- |
|            |     |                     |     |     |              |     |              |     | . From | (2),     | it is clear | that       | this will | result in |
| (iv)Update |     | ;repeatfrom(i)until |     |     | convergesand |     |              |     |        |          |             |            |           |           |
|            |     |                     |     |     |              |     | the messages |     | at     | the next | timealso    | havingeach |           |           |
outputtheconvergedestimate.
.Thus,themax-productupdaterule(2)mapsamessage
|     |     |     |     |     |     |     | vector     |        |      | intoanothervectorin |              |           |     | .Also,     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ---- | ------------------- | ------------ | --------- | --- | ---------- |
|     |     |     |     |     |     |     | it is easy | to see | that | (2) is              | a continuous | function. |     | Therefore, |
Forthepurposeofanalysis,wefinditconvenienttotransform by Brouwer’s fixed-point theorem, there exists a fixed point
themessagesandtheirdynamicsasfollows.First,define
.
|     |     |     |     |     |     |     | We now | study | properties |     | of the fixed | points | in order | to un- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ---------- | --- | ------------ | ------ | -------- | ------ |
derstandthecorrectnessoftheestimateoutputbymaxproduct.
Thefollowingtheoremcharacterizesthestructureofestimates
|     |     |     |     |     |     |     | atfixedpoints.Recallthattheestimate |     |     |     |     |     | fornode | canbe |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | ------- | ----- |
Here,sincethealgorithmstartswithallmessagesbeingstrictly
, or .
positive,themessageswillremainstrictlypositiveoveranyfi-
nitenumberofiterations.Therefore,takinglogarithmisavalid Theorem 4.1: Let be a fixed point, and let
operation.Withthisnewdefinition,step(i)ofthemax-product
bethecorrespondingestimate.Then:
| becomes |     |     |     |     |     |     | 1) if |     | ,theneveryneighbor |     |     |     | has |     |
| ------- | --- | --- | --- | --- | --- | --- | ----- | --- | ------------------ | --- | --- | --- | --- | --- |
;
|     |     |     |     |     |     | (2) | 2) if |     | ,   | then at | least one | neighbor |     | has |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ------- | --------- | -------- | --- | --- |
;
|          |         |          |     |     |       |             | 3) if |     | , then | at least | one | neighbor |     | has |
| -------- | ------- | -------- | --- | --- | ----- | ----------- | ----- | --- | ------ | -------- | --- | -------- | --- | --- |
| where we | use the | notation |     |     | . The | final esti- |       |     | .      |          |     |          |     |     |
mationstep(iii)ofmaxproducttakesthefollowingform:
BeforeprovingTheorem4.1,wediscussitsimplications.Re-
|     |     |     |     |     |     |     | callfromLemma2.1thateveryextremepointofthe |     |     |     |     |     |     | poly- |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- |
if (3) tope consists of each node having a value of , or . If all
|     |     |     |     |     |     |     | weightsarepositive,theoptimumof    |      |                     |             |      | willhavethefollowing |       |           |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | ---- | ------------------- | ----------- | ---- | -------------------- | ----- | --------- |
|     |     |     |     |     |     | (4) | characteristics:everynodewithvalue |      |                     |             |      | willbesurroundedby   |       |           |
|     |     |     |     |     |     |     | nodeswithvalue                     |      | ,everynodewithvalue |             |      | willhaveatleastone   |       |           |
|     |     |     |     |     |     |     | neighbor                           | with | value               | , and every | node | with                 | value | will have |
(5)
|     |     |     |     |     |     |     | oneneighborwithvalue |     |     | .Thesepropertiesbeararemarkable |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------------------------------- | --- | --- | --- | --- |
similaritytothoseinTheorem4.1.Indeed,givenafixedpoint
|     |     |     |     |     |     |     | anditsestimates |     |     | ,makeavector |     |     | bysetting |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ------------ | --- | --- | --------- | --- |
Thismodificationofmaxproductisoftenknownasthe“min-
sum”algorithm,andisjustareformulationofthemaxproduct.
|             |         |        |             |         |        |          |     |     | ifestimatefor |     |     | is  |     |     |
| ----------- | ------- | ------ | ----------- | ------- | ------ | -------- | --- | --- | ------------- | --- | --- | --- | --- | --- |
| In the rest | of this | paper, | we refer to | this as | simply | the max- |     |     |               |     |     |     |     |     |
productalgorithm.
|     |     |     |     |     |     |     | Then,Theorem4.1impliesthat |     |     |     |     | willbeanextremepointof |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- |
IV. FIXEDPOINTSOFMAXPRODUCT
|     |     |     |     |     |     |     | the polytope,andalsoonethatmaximizessomeweightfunc- |     |             |      |          |       |          |      |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | ----------- | ---- | -------- | ----- | -------- | ---- |
|     |     |     |     |     |     |     | tion consisting                                     |     | of positive | node | weights. | Note, | however, | that |
Whenappliedtogeneralgraphs,maxproductmayeither1)
|               |     |           |           |             |         |       | thismaynotbethetrueweights |     |     |     | .Inotherwords,givenany |     |     |     |
| ------------- | --- | --------- | --------- | ----------- | ------- | ----- | -------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- |
| not converge, | 2)  | converge, | and yield | the correct | answer, | or 3) |                            |     |     |     |                        |     |     |     |
converge but yield an incorrect answer. Characterizing when MWISproblemwithgraph andweights ,eachmax-product
fixedpointrepresentstheoptimumoftheLPrelaxationofsome
| eachofthethree |     | situationscanoccurisachallengingandim- |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
portanttask.Oneapproachtothistaskhasbeentolookdirectly MWISproblemonthesamegraph ,butpossiblywithdifferent
|              |         |         |                  |           |     |             | weights  | .    |             |     |           |          |     |             |
| ------------ | ------- | ------- | ---------------- | --------- | --- | ----------- | -------- | ---- | ----------- | --- | --------- | -------- | --- | ----------- |
| at the fixed | points, | if any, | of the iterative | procedure |     | (see, e.g., |          |      |             |     |           |          |     |             |
|              |         |         |                  |           |     |             | The fact | that | max-product |     | estimates | optimize |     | a different |
[11]).Inthissection,weinvestigatepropertiesoffixedpoints,
byformallyestablishingaconnectiontothe polytope. weightfunctionmeansthatbotheventualitiesarepossible:
|                        |     |     |                           |     |     |     | giving the                          | correct | answer | but | max | product | failing,       | and vice |
| ---------------------- | --- | --- | ------------------------- | --- | --- | --- | ----------------------------------- | ------- | ------ | --- | --- | ------- | -------------- | -------- |
| Notethatasetofmessages |     |     | isafixedpointofmaxproduct |     |     |     |                                     |         |        |     |     |         |                |          |
| if,forall              |     |     |                           |     |     |     | versa.Wenowprovidesimpleexamplesfor |         |        |     |     |         | eachoneofthese |          |
situations.
|     |     |     |     |     |     |     | Figs. | 1 and | 2 present | graphs | and | the corresponding |     | fixed |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --------- | ------ | --- | ----------------- | --- | ----- |
(6) pointsofmaxproduct.Ineachgraph,numbersrepresentnode
|     |     |     |     |     |     |     | weights, | and an | arrow | from | to represents |     | a message | value |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----- | ---- | ------------- | --- | --------- | ----- |

4826 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.55,NO.11,NOVEMBER2009
(8)
Theaboveequationscovereverycaseexceptforedgesbetween
|     |     |     |     |     |     |     | twonodeswith     | estimates.Thisiscoveredbythefollowing: |            |     |                  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | -------------------------------------- | ---------- | --- | ---------------- | --- | --- |
|     |     |     |     |     |     |     |                  | and                                    |            |     |                  |     | (9) |
|     |     |     |     |     |     |     | Supposefirstthat |                                        | issuchthat |     | .Bydefinition(6) |     |     |
Fig.1. Thisexampleshowsthatmax-productfixedpointmayresultinanin-
ofthefixedpoint
correctanswereventhoughLPistight.
|     |     |     |     |     |     |     | However,by(3),thefactthat |     |     |     | impliesthat |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ----------- | --- | --- |
Puttingtheabovetwoequationstogetherproves(7).Theproof
|     |     |     |     |     |     |     | of(8)isalongsimilarlines.Supposenow |     |     |     | issuchthat |            |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | ---------- | ---------- | --- |
|     |     |     |     |     |     |     | .By(5),thisimpliesthat              |     |     |     |            | ,andsofrom |     |
Fig.2. Thisexampleshowsthatmax-productfixedpointcanfindrightMWIS (6),wehavethat
eventhoughLPrelaxationisnottight.
| of  | .Allothermessages,whichdonothavearrows, |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
have value zero. The boxed nodes indicate the ones for which Also,thefactthat meansthat
| theestimate |     |     | .Itiseasytoverifythatbothexamples |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
representmax-productfixedpoints.
ForthegraphinFig.1,themax-productfixedpointresultsin
anincorrectestimate.However,thegraphisbipartite,andhence
|     |     |     |     |     |     |     | Putting the | above two | equations | together | proves | (8). | We now |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --------- | -------- | ------ | ---- | ------ |
willprovidethecorrectanswer.ForthegraphinFig.2,there
provethethreepartsofTheorem4.1.
| is an integrality |     | gap between | and | : setting | each |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
yields an optimal value of for , while the optimal solu- ProofofPart1): Let haveestimate ,andsup-
|                |          |                                     |       |            |       |          | posethereexistsaneighbor   |     |     |                         | suchthat |                | or . |
| -------------- | -------- | ----------------------------------- | ----- | ---------- | ----- | -------- | -------------------------- | --- | --- | ----------------------- | -------- | -------------- | ---- |
| tionto         | hasvalue | .Notethattheestimateatthefixedpoint |       |            |       |          |                            |     |     |                         |          |                |      |
|                |          |                                     |       |            |       |          | Then,from(7),itfollowsthat |     |     |                         |          | ,andfrom(8),it |      |
| of max product |          | is the correct                      | MWIS. | It is also | worth | noticing |                            |     |     |                         |          |                |      |
|                |          |                                     |       |            |       |          | furtherfollowsthat         |     |     | .However,thisisacontra- |          |                |      |
thatforbothoftheseexamples,thefixedpointslieinthestrict
|     |     |     |     |     |     |     | diction,andthuseveryneighborof |     |     | hastohaveestimate |     |     | .   |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | ----------------- | --- | --- | --- |
interiorsofanontrivialregionofattraction:startingtheiterative
procedurefromwithintheseregionswillresultinconvergence ProofofPart2): Let haveestimate .Since
|     |     |     |     |     |     |     | , (4)impliesthatthere |     | existsat | leastone | neighbor |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | -------- | -------- | -------- | --- | --- |
tothecorrespondingfixedpoint.Theseexamplesindicatethatit
|     |     |     |     |     |     |     | suchthatthemessage |     |     | .From(9),thismeansthatthe |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ------------------------- | --- | --- | --- |
maynotbepossibletoresolvethequestionofrelativestrength
of the two procedures based solely on an analysis of the fixed estimate cannotbe .Supposenowthat .From
|     |     |     |     |     |     |     | (7),itfollowsthat |     |     |     | ,andso |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | ------ | --- | --- |
pointsofmaxproduct.
Theparticularfixedpoint,ifany,thatmaxproductconverges
todependsontheinitializationofthemessages;eachfixedpoint
| will have | its own | region | of convergence. | In  | Section | V, we di- |     |     |     |     |     |     |     |
| --------- | ------- | ------ | --------------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
rectlyanalyzetheiterativealgorithmwhenstartedfromthe“nat-
|                      |     |             |             |         |             |               | However,since |     |     | ,thismeansthat |     |     |     |
| -------------------- | --- | ----------- | ----------- | ------- | ----------- | ------------- | ------------- | --- | --- | -------------- | --- | --- | --- |
| ural” initialization |     | of unbiased | messages.   | As      | a byproduct | of            |               |     |     |                |     |     |     |
| this analysis,       | we  | prove       | that if max | product | from        | this initial- |               |     |     |                |     |     |     |
izationconverges,thentheresultingfixed-pointestimateisthe
| optimumof          |     | ;thus,inthiscase,themax-productfixedpoint |     |     |     |     |                |      |          |                |     |      |     |
| ------------------ | --- | ----------------------------------------- | --- | --- | --- | --- | -------------- | ---- | -------- | -------------- | --- | ---- | --- |
| solvesthe“correct” |     |                                           | .   |     |     |     |                |      |          |                |     |      |     |
|                    |     |                                           |     |     |     |     | which violates | (4), | and thus | the assumption |     | that | .   |
ProofofTheorem4.1: TheproofofTheorem4.1follows Thus,ithastobethat .
frommanipulationsofthefixedpoint(6).Foreaseofnotation,
|     |     |     |     |     |     |     | ProofofPart3): |     | Let haveestimate |     |     | .Since |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------- | --- | --- | ------ | --- |
wereplace by .Wefirstprovethefollowingstatementson , (5)impliesthatthere existsat leastone neighbor
how the estimates determine the relative ordering of the two suchthatthemessage .From(8),itfollowsthat
messages(oneineachdirection)onanygivenedge:
(7)

SANGHAVIetal.:MESSAGEPASSINGFORMAXIMUMWEIGHTINDEPENDENTSET 4827
| Thus, |                       |     | , which | by  | (5) means    | that |     | .   | A. ComputationTreeforMWIS |     |     |     |     |     |     |     |
| ----- | --------------------- | --- | ------- | --- | ------------ | ---- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Thus, | hasatleastoneneighbor |     |         |     | withestimate |      |     | .   |                           |     |     |     |     |     |     |     |
TheproofofTheorem5.1reliesonthecomputationtreein-
| We  | end | this section | with | a brief | discussion | about | the | half- |              |       |             |       |             |     |            |     |
| --- | --- | ------------ | ---- | ------- | ---------- | ----- | --- | ----- | ------------ | ----- | ----------- | ----- | ----------- | --- | ---------- | --- |
|     |     |              |      |         |            |       |     |       | terpretation | [23], | [26] of the | loopy | max-product |     | estimates. | In  |
interality property of the MWIS problem, as summarized by thissection,webrieflyoutlinethisinterpretation.Foranynode
Lemma2.1.Forus,thispropertyenabledanaturalinterpretation , the computation tree at time , denoted by , is defined
of the “?” estimates at a max-product fixed point: we simply recursivelyasfollows: isjustthenode .Thisistheroot
set those nodes to . It would be interesting to see if such an ofthetree,andinthiscase,itisalsoitsonlyleaf.Thetree
interpretation also holds for other problems with known half- attime isgeneratedfrom byaddingtoeachleafof
integralityproperties.Thatis,givenamax-productfixedpoint a copy of each of its neighbors in , except for the
foroneoftheseproblems,doesinterpreting“?”estimatesasan oneneighborthatisalreadypresentin .Eachnodein
|     |         |       |            |       |     |     |           |     | isacopyofanodein                    |     |     | ,andtheweightsofthenodesin |     |                 |     |     |
| --- | ------- | ----- | ---------- | ----- | --- | --- | --------- | --- | ----------------------------------- | --- | --- | -------------------------- | --- | --------------- | --- | --- |
|     | mass of | yield | an extreme | point | of  | the | polytope? | A   |                                     |     |     |                            |     |                 |     |     |
|     |         |       |            |       |     |     |           |     | arethesameasthecorrespondingnodesin |     |     |                            |     | .Thecomputation |     |     |
generalanswertothisquestionwouldbeinteresting.
treeinterpretationisstatedinthefollowinglemma.
|     |     |     |     |     |     |     |     |     | Lemma5.1: | Foranynode |     | attime | :   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------ | --- | --- | --- | --- |
V. DIRECTANALYSISOFTHEITERATIVEALGORITHM
|     |          |          |        |      |              |        |         |     | •           |     | ifandonlyiftherootof |     |     | isamemberof  |     |     |
| --- | -------- | -------- | ------ | ---- | ------------ | ------ | ------- | --- | ----------- | --- | -------------------- | --- | --- | ------------ | --- | --- |
|     |          |          |        |      |              |        |         |     | everyMWISon |     |                      | ;   |     |              |     |     |
| In  | the last | section, | we saw | that | fixed points | of max | product |     |             |     |                      |     |     |              |     |     |
|     |          |          |        |      |              |        |         |     | •           |     | ifandonlyiftherootof |     |     | isnotamember |     |     |
maycorrespondtooptima“wrong”linearprograms:onesthat
|                               |     |     |     |     |                        |     |     |     | ofanyMWISon |     |       | ;   |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | ----------- | --- | ----- | --- | --- | --- | --- | --- |
| operateonthesamefeasiblesetas |     |     |     |     | ,butoptimizeadifferent |     |     |     |             |     |       |     |     |     |     |     |
|                               |     |     |     |     |                        |     |     |     | •           |     | else. |     |     |     |     |     |
linearfunction.However,therewillalsobefixedpointsthatcor-
|         |     |            |     |         |           |     |         |      | Thus, the | max-product |     | estimates | correspond | to  | MWISs | on  |
| ------- | --- | ---------- | --- | ------- | --------- | --- | ------- | ---- | --------- | ----------- | --- | --------- | ---------- | --- | ----- | --- |
| respond | to  | optimizing | the | correct | function. | Max | product | is a |           |             |     |           |            |     |       |     |
deterministic algorithm, and so which of these fixed points (if thecomputationtrees ,asopposedtoontheoriginalgraph
| any)arereachedisdeterminedbytheinitialization.Inthissec- |     |     |     |     |     |     |     |     | .        |                             |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------------------- | --- | --- | --- | --- | --- | --- |
|                                                          |     |     |     |     |     |     |     |     | Example: | Considerthefollowingfigure: |     |     |     |     |     |     |
tion,wedirectlyanalyzetheiterativealgorithmitself,asstarted
| from | the “natural” |     | initialization |     | , which | corresponds |     | to  |     |     |     |     |     |     |     |     |
| ---- | ------------- | --- | -------------- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
uninformativemessages
Weshowthattheresultingestimatesarecharacterizedbyop-
| tima | of the | true | , at every | instant | (not | just at fixed | points). |     |     |     |     |     |     |     |     |     |
| ---- | ------ | ---- | ---------- | ------- | ---- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thisimpliesthat,ifafixedpointisreached,itwillexactlyre-
| flect | an optimum |     | of LP. Our | main | theorem | in this | section | is  |     |     |     |     |     |     |     |     |
| ----- | ---------- | --- | ---------- | ---- | ------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
statedbelow.
| Theorem5.1: |     | GivenanyMWISproblemonweightedgraph |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
,supposemaxproductisstartedfromtheinitialcondition
|                  |     |     |     |     |     |     |     |     | Ontheleftistheoriginalloopygraph |     |     |     | .Ontherightis |     |     | ,   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | ------------- | --- | --- | --- |
| .Then,foranynode |     |     |     | :   |     |     |     |     |                                  |     |     |     |               |     |     |     |
1) ifthereexistsanyoptimum of forwhichthe , thecomputationtreefornode attime .
|     |                            |     |     |     |     |       |            |     | Proof                                    | of Theorem | 5.1: | We now | prove | Theorem | 5.1. | For |
| --- | -------------------------- | --- | --- | --- | --- | ----- | ---------- | --- | ---------------------------------------- | ---------- | ---- | ------ | ----- | ------- | ---- | --- |
|     | thenthemax-productestimate |     |     |     |     | is or | foralleven |     |                                          |            |      |        |       |         |      |     |
|     |                            |     |     |     |     |       |            |     | brevity,inthisproof,wewillusethenotation |            |      |        |       |         |      | for |
|     | times                      | ;   |     |     |     |       |            |     |                                          |            |      |        |       |         |      |     |
theestimates.Supposenowthatpart1ofthetheoremisnottrue,
| 2)  | ifthereexistsanyoptimum    |     |     |     | of forwhichthe |       |           | ,   |                      |                      |            |     |     |      |       |      |
| --- | -------------------------- | --- | --- | --- | -------------- | ----- | --------- | --- | -------------------- | -------------------- | ---------- | --- | --- | ---- | ----- | ---- |
|     |                            |     |     |     |                |       |           |     | i.e.,thereexistsnode |                      | ,anoptimum |     | of  | with |       | ,and |
|     | thenthemax-productestimate |     |     |     |                | is or | forallodd |     |                      |                      |            |     |     |      |       |      |
|     |                            |     |     |     |                |       |           |     | anoddtime            | atwhichtheestimateis |            |     |     | .Let | bethe |      |
|     | times                      | .   |     |     |                |       |           |     |                      |                      |            |     |     |      |       |      |
correspondingcomputationtree.UsingLemma5.1,thismeans
WemakenoteoftwoimportantimplicationsoftheTheorem thattheroot isnotamemberofanyMWISof .Let be
| 5.1. |     |     |     |     |     |     |     |     | someMWISon |     | .Wenowdefinethefollowingsetofnodes: |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
1) IfLPhasanonintegralsolution,thenthemax-productes-
timateswillnotconvergetothecorrectanswer.Thisisbe-
|     |                            |        |                                     |     |                 |     |            |     |                   |     |                                   | andcopyof |     | in has         |     |     |
| --- | -------------------------- | ------ | ----------------------------------- | --- | --------------- | --- | ---------- | --- | ----------------- | --- | --------------------------------- | --------- | --- | -------------- | --- | --- |
|     | cause,if                   |        | ,thenbyabovetheorem,theestimate     |     |                 |     |            |     |                   |     |                                   |           |     |                |     |     |
|     | of will                    | either | keep varying                        |     | every alternate |     | time slot, | or  |                   |     |                                   |           |     |                |     |     |
|     |                            |        |                                     |     |                 |     |            |     | Inotherwords,     |     | isthesetofnodesin                 |           |     | ,whicharenotin |     |     |
|     | willconvergeto             |        | .Eitherway,maxproductwillfailtopro- |     |                 |     |            |     |                   |     |                                   |           |     |                |     |     |
|     |                            |        |                                     |     |                 |     |            |     | ,andwhosecopiesin |     | areassignedstrictlypositivemassby |           |     |                |     |     |
|     | videausefulestimatefornode |        |                                     |     | .               |     |            |     | theLPoptimum      |     | .                                 |           |     |                |     |     |
2) Astoppingcondition:stopwhenestimateisthesame(and
|     |       |     |             |      |        |         |          |     | Note that | by                | assumption | the root |         | and         | .       | Now, |
| --- | ----- | --- | ----------- | ---- | ------ | ------- | -------- | --- | --------- | ----------------- | ---------- | -------- | ------- | ----------- | ------- | ---- |
|     | ) for | two | consecutive | time | slots. | This is | because, | by  |           |                   |            |          |         |             |         |      |
|     |       |     |             |      |        |         |          |     | from the  | root, recursively |            | build a  | maximal | alternating | subtree |      |
statementoftheoremitfollowsthatiftheestimatesunder asfollows:firstaddroot ,whichisin .Then,addall
|     | maxproductattwoconsecutivetimesare |     |     |     |     | (or | ),then |     |             |           |     |                            |     |     |     |     |
| --- | ---------------------------------- | --- | --- | --- | --- | --- | ------ | --- | ----------- | --------- | --- | -------------------------- | --- | --- | --- | --- |
|     |                                    |     |     |     |     |     |        |     | neighborsof | thatarein |     | .Then,addalltheirneighbors |     |     |     |     |
thesolutionofalltheLPoptimamustbesuchthat in , and so on. The building of stops either when it
|     | (or | ).  |     |     |     |     |     |     | hitsthebottomlevelofthetree,orwhennomorenodescanbe |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Theproofofthistheoremreliesonthecomputationtreein-
addedwhilestillmaintainingthealternatingstructure.Notethe
terpretationofmax-productestimates.Wenowspecifythisin- followingpropertiesof .
terpretationforourproblem,andthenproveTheorem5.1. • isthedisjointunionof and .

4828 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.55,NO.11,NOVEMBER2009
• Forevery ,allitsneighborsin areincludedin Beforeweproceedtocheckingtheedgeconstraints,wemake
.Similarly,forevery ,allitsneighborsin twoobservations.Notethatforanynode inthetree, ,
areincludedin . thenwehavethefollowing.
• Anyedge in hasatmostoneendpointin , • , i.e., the mass put on by the optimum
andatmostonein . isstrictlylessthan .Thisisbecauseofthealternating
We now state a lemma, which we will prove later. The proof way in which the tree is constructed: a node in the tree
usesthefactthat isodd. isincludedin onlyiftheparent of isin
(note that the root by assumption). However,
Lemma5.2: Theweightssatisfy .
fromthedefinitionof ,thismeansthat ,i.e.,the
We now use this lemma to prove the theorem. Consider the parenthaspositivemassatthe optimum .Thismeans
set ,whichchanges byflipping that ,ashaving wouldmeanthattheedge
constraint isviolated.
• isnotaleafofthetree.Thisisbecause alternatesbe-
tween and , and starts with at the root in level
We firstshow that is also an independent seton .This (whichisodd).Hence, willoccupyevenlevelsofthe
means that we need to show that every edge in tree,butthetreehasodddepth(byassumption isodd).
touches at most one node in . There are thus three possible Nowconsidertheedgeconstraints.Foranyedge ,ifthe
scenariosforedge . optimum issuchthattheconstraintisloose,i.e.,if
• .Inthiscase,membershipof in isthesame , then making small enough will ensure that .
asin ,whichisanindependentset.So hasatmost Soweonlyneedtochecktheedgeconstraintswhicharetight
onenodetouching . at .
• Onenode .Inthiscase, ,andhenceagain Foredgeswith ,everytimeanycopyofoneofthe
atmostoneof belongsto . nodes or isincludedin ,theothernodeisincludedin
• One node but other node . This .Thisisbecauseofthefollowing:if isincludedin ,
meansthat ,becauseeveryneighborof in should and isitsparent,wearedonesincethismeans .So
be included in . This means that , and hence suppose isnottheparentof .Fromtheaboveitfollowsthat
onlynode foredge . isnotaleafofthetree,andhence willbeoneofitschildren.
Thus, is an independent set on . Also, by Lemma 5.2, Also,fromabove,themasson satisfies .However,by
we havethat assumption, ,andhence,themasson is .
Thismeansthatthechild hastobeincludedin .
Itisnoweasytoseethattheedgeconstraintsaresatisfied:for
everyedgeconstraintwhichistightat ,everytimethemass
However, isanMWIS,andhenceitfollowsthat isalsoan ononeoftheendpointsisincreasedby (becauseofthatnode
MWIS of .However,byconstruction, root , which appearingin ),themassontheotherendpointisdecreased
violatesthefactthat .Thecontradictionisthusestab- by (becauseitappears ).
lished,andpart1ofthetheoremisproved.Part2isprovedina
similarfashion. VI. ACONVERGENTMESSAGE-PASSINGALGORITHM
InSectionV,wesawthatmaxproductstartedfromthenat-
Proof of Lemma 5.2: The proof of this lemma involves a
uralinitialconditionsolvesthecorrect atthefixedpoint,if
perturbationargumentontheLP.Foreachnode ,let
itconverges.However,convergenceisnotguaranteed,indeedit
denotethenumberoftimes appearsin and thenumber
isquiteeasytoconstructexampleswhereitwillnotconverge.
oftimesitappearsin .Define
Forexample,considerathree-nodecompletegraph(atriangle
graph) with each node having exactly the same node weight
(10)
.Letallinitialmessagesbe alongalledges.Then,mes-
sageswilloscillatebetween and atevenandoddtimes.
We now show state a lemma that is proved immediately fol-
Inthissection,wepresentaconvergentmessage-passingal-
lowingthisone.
gorithmforfindingtheMWISofagraph.Itisbasedonmodi-
Lemma5.3: isafeasiblepointforLP,forsmallenough . fyingmaxproductbydrawinguponadualcoordinatedescent
andthebarriermethod.Thealgorithmretainstheiterativeand
We now use this lemma to finish the proof of Lemma 5.2.
distributednatureofmaxproduct.Thealgorithmleadstoanop-
Since isanoptimumofLP,itfollowsthat ,and
timalsolutionof foranyweightedgraph .Nowwhen
so .However,bydefinition, and
isbipartite,theLPrelaxationistight.Therefore,inprinciple,
.Thisfinishestheproof.
onecanhopetoobtainsolutionofMWISbysolving .Now,
ProofofLemma5.3: Wenowshowthatthis asdefined thesolutionsof and (primal)dosatisfycomplimen-
in(10)isafeasiblepointfor ,forsmallenough .Todoso tary slackness conditions. But this, in general, does not guar-
wehavetochecknodeconstraints andedgeconstraints anteerecoveryofprimalor solutionfrom .Here,we
foreveryedge .Considerfirstthenode developanovelprimalrecoveryalgorithmbasedontheoptimal
constraints.Clearly,weonlyneedtocheckthemforany which solutionof whentheMWISand haveuniquesolution
hasacopy .Ifthisisso,thenbythedefinition(V)of forbipartitegraph.Thealgorithmissimple,iterative,andstops
, .Thus,forany and ,making smallenough with iterations.Inouropinion,this shouldbeofinterest
canensurethat . initsownright.

SANGHAVIetal.:MESSAGEPASSINGFORMAXIMUMWEIGHTINDEPENDENTSET 4829
Now,weprovideanoverviewofouralgorithm.Thealgorithm Then,themodified optimizationproblembecomes
operatesintwosteps,asdescribedbelow.
forall
(o)GivenanMWISproblem,and(smallenough)positive
parameters ,runsubroutine toobtainan Thealgorithm iscoordinatedescenton ,
|        |     |     |     |     |                         |     |     |     | to within | tolerance | , implemented | via passing | messages | be- |
| ------ | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --------- | --------- | ------------- | ----------- | -------- | --- |
| output |     |     |     |     | thatisanapproximatedual |     |     |     |           |           |               |             |          |     |
tweennodes.Wedescribeitindetailasfollows.
oftheMWISproblem.
| (i)Next,using(smallenough) |     |     |     |     | ,use |     |     | ,   |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
toproduceanestimatefortheMWISasanoutputofthe
algorithm.
|                                                       |                 |     |     |     |     |                        |     |     | (o) Theparameters       |                        | are variables               | , one | for each edge |     |
| ----------------------------------------------------- | --------------- | --- | --- | --- | --- | ---------------------- | --- | --- | ----------------------- | ---------------------- | --------------------------- | ----- | ------------- | --- |
|                                                       |                 |     |     |     |     |                        |     |     |                         | .Wewillusenotationthat |                             |       | .Thevector    | is  |
|                                                       |                 |     |     |     |     |                        |     |     | iterativelyupdated,with |                        | denotingtheiterationnumber. |       |               |     |
|                                                       |                 |     |     |     |     |                        |     |     | • Initially,            |                        | set and                     |       | for all       |     |
|                                                       | Next,wedescribe |     |     | and |     | ,statetheirproperties, |     |     |                         |                        |                             |       |               |     |
| andthencombinethemtoproducethefollowingresultaboutthe |                 |     |     |     |     |                        |     |     |                         |                        | .                           |       |               |     |
convergence,correctnessandboundonconvergencetimeforthe
|     |     |     |     |     |     |     |     |     | (i)Initeration |     | ,updateparametersareasfollows. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------------------------ | --- | --- | --- |
overallalgorithm.
|     |     |     |     |     |     |     |     |     | • Pickanedge |     | .Theedgeselectionisdoneina |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------------------------- | --- | --- | --- |
round-robinmanneroveralledges.
| A.  |                    | :Algorithm |     |     |                          |     |     |     |          |     |     |     |                 |     |
| --- | ------------------ | ---------- | --- | --- | ------------------------ | --- | --- | --- | -------- | --- | --- | --- | --------------- | --- |
|     |                    |            |     |     |                          |     |     |     | • Forall |     |     |     | donothing,i.e., |     |
|     | Here,wedescribethe |            |     |     | algorithm.Itisinfluenced |     |     |     |          |     |     |     |                 |     |
by the max product and dual coordinate descent algorithm for • Foredge ,nodes and exchangemessagesas
follows:
|           | . First, | consider | the           | standard            | coordinate                |     | descent | algo- |     |     |     |     |     |     |
| --------- | -------- | -------- | ------------- | ------------------- | ------------------------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- |
| rithm     | for      |          | . It operates | with                | variables                 |     |         |       |     |     |     |     |     |     |
| (with     | notation |          |               | ). It is an         | iterativeprocedure;ineach |     |         |       |     |     |     |     |     |     |
| iteration |          | oneedge  |               | ispicked1andupdated |                           |     |         |       |     |     |     |     |     |     |
(11)
|     |                                       |     |     |     |     |     |     |     | • Update |     | asfollows:with |     | and |     |
| --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------------- | --- | --- | --- |
| The | onalltheotheredgesremainunchangedfrom |     |     |     |     |     |     | to  | .        |     |                |     |     |     |
Noticethesimilarity(atleastsyntactic)betweenstandarddual
coordinate descent (11) and max product (2). In essence, the (12)
dualcoordinatedescentcanbethoughtofasasequentialbidi-
rectionalversionofthemax-productalgorithm.
|        | Since the | dual        | coordinate | descent    | algorithm |          | is designed       | so       |                      |                   |                                  |                   |     |     |
| ------ | --------- | ----------- | ---------- | ---------- | --------- | -------- | ----------------- | -------- | -------------------- | ----------------- | -------------------------------- | ----------------- | --- | --- |
|        |           |             |            |            |           |          |                   |          | (ii)Update           |                   | andrepeatuntilalgorithmconverges |                   |     |     |
| that   | at each   | iteration,  | the        | cost of    | the       |          | is nonincreasing, |          |                      |                   |                                  |                   |     |     |
|        |           |             |            |            |           |          |                   |          | within               | foreachcomponent. |                                  |                   |     |     |
| it     | always    | converges   | in terms   | of         | the cost. | However, |                   | the con- |                      |                   |                                  |                   |     |     |
|        |           |             |            |            |           |          |                   |          | (iii)Outputthevector |                   | ,denotedby                       | ,whenthealgorithm |     |     |
| verged | solution  |             | may not    | be optimum | because   |          |                   | contains |                      |                   |                                  |                   |     |     |
| the    | “nonbox”  | constraints |            |            |           |          | . Therefore,      | a di-    | stops.               |                   |                                  |                   |     |     |
rectusageofdualcoordinatedescentisnotsufficient.Inorderto
makethealgorithmconvergentwithminimalmodificationwhile
retaining its iterative message-passing nature, we use barrier Remark: The updates in above are obtained by
(penalty)function-basedapproach.Withanappropriatechoice small, but important, perturbation of standard dual coordinate
of barrier and using result of Luo and Tseng [3], we will find descent(11).Toseethis,considertheiterativestepin(12).First,
| thenewalgorithmtobeconvergent. |          |      |          |               |                         |               |              |         | note that |     |     |     |     |     |
| ------------------------------ | -------- | ---- | -------- | ------------- | ----------------------- | ------------- | ------------ | ------- | --------- | --- | --- | --- | --- | --- |
|                                | To this  | end, | consider | the following |                         | convex        | optimization |         |           |     |     |     |     |     |
| problem                        | obtained |      | from     | byadding      |                         | a logarithmic |              | barrier |           |     |     |     |     |     |
| forconstraintviolationswith    |          |      |          |               | controllingpenaltydueto |               |              |         |           |     |     |     |     |     |
violation.Define
1Edgescanbepickedeitherinround-robinfashion,oruniformlyatrandom.

4830 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.55,NO.11,NOVEMBER2009
| Similarly |     |     |     |     |     |     |     | vector, and |     | is  | a strongly | convex | function | on its |
| --------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ---------- | ------ | -------- | ------ |
domain
|     |     |     |     |     |     |     |     | Wehave                     | beingopenandlet |              |     | denoteitsboundary.We |              |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --------------- | ------------ | --- | -------------------- | ------------ | --- |
|     |     |     |     |     |     |     |     | also have                  | that, along     | any sequence |     | such                 | that         |     |
|     |     |     |     |     |     |     |     | (i.e.,approachesboundaryof |                 |              | ),  |                      | .Thegoalisto |     |
solvetheoptimizationproblem
|     |     |     |     |     |     |     |     |     | minimize |     | over |     |     | (14) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | --- | --- | ---- |
Therefore,weconcludethat(12)canberewrittenas Intheabove,weassumethat isboxtype,i.e.,
|     |     |     |     |     |     |     |     | Let bethesetofalloptimalsolutionsoftheproblem(14). |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
The“round-robin”or“cyclic”coordinatedescentalgorithm(the
|     |     |     |     |     |     |     |     | oneusedin |     | )forthisproblemhasthefollowingcon- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------------------------------- | --- | --- | --- | --- |
vergenceproperty,asprovedinTheorem6.2[3].
| whereforsome |     |     | withitsprecisevaluedependenton |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
. This small perturbation takes close to the true Lemma6.2: Thereexistconstants and whichmayde-
dualoptimum.Inpractice,webelievethatinsteadofcalculating pend on the problem parameters in terms of such that
|             |     |             |                |        |               |        |     | starting from | the                            | initial value | , we | have | in iteration | of the |
| ----------- | --- | ----------- | -------------- | ------ | ------------- | ------ | --- | ------------- | ------------------------------ | ------------- | ---- | ---- | ------------ | ------ |
| exact value | of  | , use of    | some arbitrary |        |               | should | be  |               |                                |               |      |      |              |        |
| sufficient. |     |             |                |        |               |        |     | algorithm     |                                |               |      |      |              |        |
| B.          |     | :Properties |                |        |               |        |     |               |                                |               |      |      |              |        |
| The         |     | algorithm   | finds          | a good | approximation |        | to  |               |                                |               |      |      |              |        |
|             |     |             |                |        |               |        |     | Here,         | denotesdistancetotheoptimalset |               |      |      |              | .      |
an optimum of , for small enough . Furthermore, ProofofLemma6.1: Itsufficestocheckthattheconditions
| it always | converges, |     | and does | so quickly. | The | following |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | -------- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
assumedinthestatementofLemma6.2applyinoursetupof
lemmaspecifiestheconvergenceandcorrectnessguaranteesof
Lemma6.1inordertocompletetheproof.
|     | .   |     |     |     |     |     |     | Notefirstthattheconstraints |     |     |     | in  | areof“box |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --------- | --- |
Lemma6.1: Forgiven ,let betheparametervalue type,” as required by Lemma 6.2. Now, we need to show that
attheendofiteration under .Then,there satisfiestheconditionsthat satisfiedin(14).Byobser-
|                         |     |       |                          |     |     |       |      | vation,weseethatthelinearpartin |     |                                    |     | is  | corresponds  |     |
| ----------------------- | --- | ----- | ------------------------ | --- | --- | ----- | ---- | ------------------------------- | --- | ---------------------------------- | --- | --- | ------------ | --- |
| existsauniquelimitpoint |     |       | suchthat                 |     |     |       |      |                                 |     |                                    |     |     |              |     |
|                         |     |       |                          |     |     |       |      | tothelinearpartin               |     | .Now,theotherpartin                |     |     | ,whichcorre- |     |
|                         |     |       |                          |     |     |       | (13) | spondsto                        |     | wheredefine                        |     |     |              |     |
| forsomepositiveconstant |     |       | (whichmaydependonproblem |     |     |       |      |                                 |     |                                    |     |     |              |     |
| parameters              | and | ).Let | bethesolutionof          |     |     | .Then |      |                                 |     |                                    |     |     |              |     |
|                         |     |       |                          |     |     |       |      | Bydefinition,the                |     | isstrictlyconvexonitsdomainwhichis |     |     |              |     |
Further,bytaking , goesto ,anoptimalsolutionto anopensetasforany ,if
| the | .             |     |           |           |          |     |          |     |     |     |     |     |     |     |
| --- | ------------- | --- | --------- | --------- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| We  | first discuss | the | proofs of | two facts | in Lemma |     | 6.1: (a) |     |     |     |     |     |     |     |
isadirectconsequenceofthefactthatifwe
| ran    |     | algorithmwith              |     | ,itconverges;(b)thefact |     |             |     |      |              |     |     |                     |     |     |
| ------ | --- | -------------------------- | --- | ----------------------- | --- | ----------- | --- | ---- | ------------ | --- | --- | ------------------- | --- | --- |
|        |     |                            |     |                         |     |             |     | then | .Notethatfor |     |     | towardsboundarycor- |     |     |
| thatas | ,   | goestoadualoptimalsolution |     |                         |     | followsfrom |     |      |              |     |     |                     |     |     |
[17,Prop.4.1.1].Now,itremainstoestablishtheconvergenceof respondingto canbeadjustedbyredefining to
|     |     |                                      |     |     |     |     |     | include some          | parts | of the linear | term | in                  | . Finally, | the con- |
| --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --------------------- | ----- | ------------- | ---- | ------------------- | ---------- | -------- |
| the |     | algorithm.Thiswillfollowasacorollary |     |     |     |     |     |                       |       |               |      |                     |            |          |
|     |     |                                      |     |     |     |     |     | ditioncorrespondingto |       | nothaving     |      | anyzerocolumnin(14) |            |          |
ofresultbyLuoandTseng[3].Inordertostatetheresultin[3],
somenotationneedstobeintroducedasfollows. followsforanyconnectedgraph,whichisofourinteresthere.
Thus,wehaveverifiedconditionsofLemma6.2,andhencees-
| Considerarealvaluedfunction |     |     |     |     | definedas |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tablishedtheproofof(13).ThiscompletestheproofofLemma
6.1.
|     |     |     |     |     |     |     |     | C. :Algorithm |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
where isan matrixwithnozerocolumn(i.e., Thealgorithm yieldsagoodapproximationofthe
allcoordinatesof areuseful), isagivenfixed optimalsolutionto ,forsmallvaluesof and .However,

SANGHAVIetal.:MESSAGEPASSINGFORMAXIMUMWEIGHTINDEPENDENTSET 4831
our interest is in the (integral) optimum of , when it exists. namely,thefeasibilityof fortheIP.Thus,allthatremainsto
Thereisnogeneralproceduretorecoveranoptimumofalinear bedoneistoestablish(x3).
program froman optimumof itsdual.However,weshow that Assume now that (x3) is violated, i.e., there exists a subset
such arecoveryis possiblethroughour algorithm,called of the edges whose both endpoints are set to . Let
andpresentedbelow,fortheMWISproblemwhen isbipar- betheseendpoints.Notethat,byassumption,
titewithauniqueMWIS.Thisprocedureislikelytoextendfor . We now use and to construct two distinct
general when relaxationistightand hasauniquesolu- optima of , which will be a violation of our assumption of
tion.Inthefollowing, ischosentobeanappropriatelysmall uniquenessoftheMWIS.Thetwooptima,denoted and ,are
number,and isexpectedtobe(closeto)adualoptimum. obtainedasfollows:in ,modify forall toobtain
|     |     |     |     |     |     |     |     | ;in      | ,modify | forall                                      |     |     | toobtain  | .Wenowshow |         |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------------------------------------------- | --- | --- | --------- | ---------- | ------- |
|     |     |     |     |     |     |     |     | thatboth | and     | satisfyallthreeconditions(x1),(x2),and(x3). |     |     |           |            |         |
|     |     |     |     |     |     |     |     | Recall   | that    | the nodes                                   | in  | and | must have | been       | colored |
(o)Thealgorithmiterativelyestimates given red by the algorithm . Now, we establish optimality of
(expectedtobeadualoptimum). and .Byconstruction,both and satisfy(x1)sincewehave
onlychangedassignmentofrednodeswhichwerenotbinding
| (i) Initially, | color | a node | gray and | set | if  |     |     |     |     |     |     |     |     |     |     |
| -------------- | ----- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
forconstraint(x1).
.Colorallothernodeswithgreenand
|     |     |     |     |     |     |     |     | Now,weturnourattentiontowards(x2)and(x3)for |     |     |     |     |     |     | and . |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- |
leavetheirvaluesunspecified. Again,bothsolutionssatisfy(x2)and(x3)alongedges
|     |     |     |     |     |     |     |     | such | that |     | or  | else they | would | not have | been |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --------- | ----- | -------- | ---- |
(ii)Repeatthefollowingsteps(inanyorder)untilnomore
changescanhappen: colored red. By construction, they satisfy (x3) along all other
|                                     |          |     |                   |     |          |      |     | edgesaswell.Nowweshowthat            |        |      |     |     | satisfy(x2)alongedges |             |       |
| ----------------------------------- | -------- | --- | ----------------- | --- | -------- | ---- | --- | ------------------------------------ | ------ | ---- | --- | --- | --------------------- | ----------- | ----- |
| • if isgreenandthereexistsagraynode |          |     |                   |     |          | with |     |                                      |        |      |     |     |                       |             |       |
|                                     |          |     |                   |     |          |      |     |                                      | , such | that |     |     | or                    |             | . For |
|                                     | ,thenset |     | andcoloritorange; |     |          |      |     |                                      |        |      |     |     |                       |             |       |
|                                     |          |     |                   |     |          |      |     | this,weclaimthatallsuchedgesmusthave |        |      |     |     |                       | :ifnot,that |       |
| • if isgreenandsomeorangenode       |          |     |                   |     | ,thenset |      |     |                                      |        |      |     |     |                       |             |       |
andcoloritgray. is , then either or must have been colored orange
|     |     |     |     |     |     |     |     | andanorangenodecannotbepartof |     |     |     |     | or  | .Thus,wehave |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | ------------ | --- |
(iii)Ifanynodeisgreen,say ,set andcoloritred. established that both and along with satisfy (x1), (x2),
and(x3).Thecontradictionisthusestablished.
| (iv)Producetheoutput |     | asanestimation. |     |     |     |     |     |                            |     |                         |                        |           |     |                |      |
| -------------------- | --- | --------------- | --- | --- | --- | --- | --- | -------------------------- | --- | ----------------------- | ---------------------- | --------- | --- | -------------- | ---- |
|                      |     |                 |     |     |     |     |     | Thus,wehaveestablishedthat |     |                         |                        | alongwith |     | satisfies(x1), |      |
|                      |     |                 |     |     |     |     |     | (x2),and(x3).Therefore,    |     |                         | istheoptimalsolutionof |           |     |                | ,and |
|                      |     |                 |     |     |     |     |     | henceofthe                 |     | .Thiscompletestheproof. |                        |           |     |                |      |
D. :Properties
|     |     |     |     |     |     |     |     | Now,consideraversionof |     |     |     | wherewecheckforupdating |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | ----------------------- | --- | --- | --- |
nodesinaround-robinmanner.Thatis,inaniteration,weper-
| Lemma6.3: | Let | beanoptimalsolutionof |     |     |     | .If | is  |      |                                             |     |     |     |     |     |     |
| --------- | --- | --------------------- | --- | --- | --- | --- | --- | ---- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
|           |     |                       |     |     |     |     |     | form | operations.Now,westateasimpleboundonrunning |     |     |     |     |     |     |
abipartitegraphwithuniqueMWIS,thentheoutputproduced
|     |                                    |     |     |     |     |     |     | timeof |     | .   |     |     |     |     |     |
| --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| by  | isthemaximumweightindependentsetof |     |     |     |     |     | .   |        |     |     |     |     |     |     |     |
Proof: Let beoutputof ,and theunique Lemma 6.4: The algorithm stops after at most
| optimalMWIS.Toestablish |     |     | ,itissufficienttoestablish |     |     |     |     | iterations. |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | -------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
that and togethersatisfythecomplimentaryslacknesscon- Proof: Thealgorithmstopsaftertheiterationinwhichno
ditionsstatedinLemma2.3,namely: morenode’sstatusisupdated.Sinceeachnodecanbeupdated
(x1) forall ; at most once, withthe abovestoppingcondition, an algorithm
|             |                           |                |             |            |           |            |       | canrunforatmost                               |     |     | iterations.Thiscompletestheproofof |     |     |     |     |
| ----------- | ------------------------- | -------------- | ----------- | ---------- | --------- | ---------- | ----- | --------------------------------------------- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
| (x2)        |                           |                | forall      |            | ;         |            |       |                                               |     |     |                                    |     |     |     |     |
| (x3)        | isafeasiblesolutionforthe |                |             | .          |           |            |       | Lemma6.4.                                     |     |     |                                    |     |     |     |     |
| From the    | way                       | the color gray | is assigned | initially, |           | it follows |       |                                               |     |     |                                    |     |     |     |     |
| that either |                           | or             |             | for        | all nodes | .          | Thus, |                                               |     |     |                                    |     |     |     |     |
|             |                           |                |             |            |           |            |       | E. OverallAlgorithm:ConvergenceandCorrectness |     |     |                                    |     |     |     |     |
(x1)issatisfied.
| Before                                 | proceeding | we note | that all | nodes                 | initially     | colored |     |                                |         |                          |     |     |            |             |          |
| -------------------------------------- | ---------- | ------- | -------- | --------------------- | ------------- | ------- | --- | ------------------------------ | ------- | ------------------------ | --- | --- | ---------- | ----------- | -------- |
|                                        |            |         |          |                       |               |         |     | Before                         | stating | convergence,correctness, |     |     | and        | boundoncon- |          |
| gray are correct,                      |            | i.e.,   |          | ; this is             | because       | the     | op- |                                |         |                          |     |     |            |             |          |
|                                        |            |         |          |                       |               |         |     | vergencetime                   |         | of the                   |     |     | algorithm, | a few       | remarks  |
| timal satisfies(x1).Nowconsideranynode |            |         |          |                       | thatiscolored |         |     |                                |         |                          |     |     |            |             |          |
|                                        |            |         |          |                       |               |         |     | areinorder.Wefirstnotethatboth |         |                          |     |     |            | and         | areiter- |
| orangeduetotherebeinganeighbor         |            |         |          | thatisoneoftheinitial |               |         |     |                                |         |                          |     |     |            |             |          |
ativemessage-passingprocedures.Second,whentheMWISis
| grays,and |                                            | .Forthisnode,wehavethat |     |     |     |     | ,    |         |     |                                     |     |     |     |     |     |
| --------- | ------------------------------------------ | ----------------------- | --- | --- | --- | --- | ---- | ------- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
|           |                                            |                         |     |     |     |     |      | unique, |     | neednotproduceanexactdualoptimumfor |     |     |     |     |     |
| because   | satisfies(x2).Proceedinginthisfashion,itis |                         |     |     |     |     | easy |         |     |                                     |     |     |     |     |     |
toobtainthecorrectanswer.Finally,itisimportanttonote
| to establish | that all | nodes colored | gray | or orange | are | assigned |     |     |     |     |     |     |     |     |     |
| ------------ | -------- | ------------- | ---- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thattheabovealgorithmalwaysconvergesquickly,butmaynot
| valuesconsistentwiththeactualMWIS      |     |     |     | .   |     |           |     |                         |     |     |     |                              |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | ----------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- |
|                                        |     |     |     |     |     |           |     | producegoodestimatewhen |     |     |     | relaxationisnottight.Next,we |     |     |     |
| Nowtoprove(x2),consideraparticularedge |     |     |     |     |     | .Forthis, |     |                         |     |     |     |                              |     |     |     |
statetheprecisestatementofthisresult.
| if ,then(x2)issatisfied.Suppose |     |     |     |     | ,but |     |     |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
.Thiswillhappenifboth ,orbothareequalto Theorem 6.1: (Convergence and Correctness): The algo-
.Now,bothareequalto onlyiftheyarebothcoloredgray, rithm convergesforanychoiceof and
inwhichcaseweknowthattheactualoptima as forany .Thesolutionobtainedbyitiscorrectif isbipartite,
well. But this meansthat (x2) is violatedby the true optimum hasuniquesolution,and aresmallenough.
,whichisacontradiction.Thus,ithastobethat Proof: Theclaimthatalgorithm converges
forviolationtooccur.However,thisisalsoaviolationof(x3), forallvaluesof andforany followsimmediatelyfrom

4832 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.55,NO.11,NOVEMBER2009
Lemmas6.1,6.3,and6.4.Next,weworryaboutthecorrectness pair ,where isanassignment(i.e.,asetofvaluesfor
property. the variables) of domain . We will denote this node of by
Lemma 6.1 implies that for , the output of .Notethatsuchagraph canhavemuch largersize
|     | ,   |     |     | , where | is the | solution of |      |                                           |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | ------ | ----------- | ---- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |         |        |             | than | withincreaseinsizegovernedbythesizeofeach |     |     |     |     |     |     | .   |
. Again, as noted in Lemma 6.1, as , Thereisanedgein betweenanytwonodes and
where isanoptimalsolution2ofthe .Therefore,given if and only if there exists a variable index such
| ,forsmallenough |     |     |     | ,wehave |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that:
|     |     |     |     |     |     |     | 1)  | isinbothdomains,i.e., |     |     |     |     | and | ;   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
forall
|     |     |     |     |     |     |     | 2)  | the corresponding |     |     | variable | assignments | aredifferent, |     | i.e., |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | -------- | ----------- | ------------- | --- | ----- |
.
Wewillsupposethatthe ischosensuch.Asnotedearlier,the Inotherwords,weputanedgebetweenallpairsofnodesthat
| algorithmconvergesforallchoicesof |     |     |     |     | .Therefore,byLemma |     |                                                    |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ------------------ | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                   |     |     |     |     |                    |     | correspondtoinconsistentassignments.Giventhisgraph |     |     |     |     |     |     |     | ,we |
6.1,thereexistslargeenough suchthatfor ,wehave nowassignweightstothenodes.Let beanynumbersuch
|     |     |     |     |     |     |     | that |     |     | forall | and | .Theexistenceofsucha |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ------ | --- | -------------------- | --- | --- | --- |
forall
followsfromthefactthatthesetofassignmentsanddomains
|                                       |             |         |                               |                            |                  |          | isfinite.Assigntoeachnode |                                               |                      |     |                                      | aweightof              |                 |          | .     |
| ------------------------------------- | ----------- | ------- | ----------------------------- | -------------------------- | ---------------- | -------- | ------------------------- | --------------------------------------------- | -------------------- | --- | ------------------------------------ | ---------------------- | --------------- | -------- | ----- |
| Thus,for                              | ,wehave     |         |                               |                            |                  |          |                           |                                               |                      |     |                                      |                        |                 |          |       |
|                                       |             |         |                               |                            |                  |          | Lemma7.1:                 |                                               | Suppose              |     | and                                  | areasabove.a)If        |                 | isaMAP   |       |
|                                       |             |         |                               |                            |                  |          | estimateof                |                                               | ,let                 |     |                                      |                        | bethesetofnodes |          |       |
|                                       |             |         |                               | forall                     |                  | (15)     |                           |                                               |                      |     |                                      |                        |                 |          |       |
|                                       |             |         |                               |                            |                  |          | in                        | thatcorrespondtoeachdomainbeingconsistentwith |                      |     |                                      |                        |                 |          | .     |
|                                       |             |         |                               |                            |                  |          | Then,                     |                                               | is an MWIS           |     | of . b)                              | Conversely,            |                 | suppose  | is an |
| Now, recall                           | Lemma       | 6.3.    | It established                |                            | that the         |          |                           |                                               |                      |     |                                      |                        |                 |          |       |
|                                       |             |         |                               |                            |                  |          | MWISof                    |                                               | .Then,foreverydomain |     |                                      | ,thereisexactlyonenode |                 |          |       |
| produces                              | the correct | MWIS    | as                            | its output                 | under hypothesis | of       |                           |                                               |                      |     |                                      |                        |                 |          |       |
|                                       |             |         |                               |                            |                  |          |                           | includedin                                    |                      |     | .Further,thecorrespondingdomainas-   |                        |                 |          |       |
| Theorem6.1.Alsorecallthatthealgorithm |             |         |                               |                            |                  | checks   |                           |                                               |                      |     |                                      |                        |                 |          |       |
|                                       |             |         |                               |                            |                  |          | signments                 |                                               |                      |     | areconsistent,andtheresultingoverall |                        |                 |          |       |
| two conditions:                       | 1)          | whether |                               |                            | for              | ; and 2) |                           |                                               |                      |     |                                      |                        |                 |          |       |
|                                       |             |         |                               |                            |                  |          | vector                    |                                               | isaMAPestimateof     |     |                                      | .                      |                 |          |       |
| whether                               |             |         | .Giventhatthenumberofnodesand |                            |                  |          |                           |                                               |                      |     |                                      |                        |                 |          |       |
|                                       |             |         |                               |                            |                  |          |                           | Proof:                                        | A maximal            |     | independent                          | set                    | is one          | in which | every |
| edgesarefinite,thereexistsa           |             |         |                               | suchthat1)and2)arerobustto |                  |          |                           |                                               |                      |     |                                      |                        |                 |          |       |
noiseof .Therefore,byselectionofsmall forsuchchoice nodeiseitherintheset,orisadjacenttoanothernodethatisin
of ,wefindthattheoutputof algorithmwillbethe the set. Since weights are positive, any MWIS has to be max-
|              |                              |     |                         |     |     |     | imal.For |          | and     | asconstructed,thefollowingisclear. |         |            |          |          |        |
| ------------ | ---------------------------- | --- | ----------------------- | --- | --- | --- | -------- | -------- | ------- | ---------------------------------- | ------- | ---------- | -------- | -------- | ------ |
| sameasthatof |                              |     | .Thiscompletestheproof. |     |     |     |          |          |         |                                    |         |            |          |          |        |
|              |                              |     |                         |     |     |     | 1)       | If       | is an   | assignment                         | of      | variables, | consider | the      | corre- |
|              |                              |     |                         |     |     |     |          | sponding | set     | of nodes                           |         |            |          | . Each   | domain |
| VII.         | MAPESTIMATIONASANMWISPROBLEM |     |                         |     |     |     |          |          |         |                                    |         |            |          |          |        |
|              |                              |     |                         |     |     |     |          | has      | exactly | one                                | node in | this set.  | Also,    | this set | is an  |
Inthissection,weshowthatanyMAPestimationproblemis independentsetin ,becausethepartialassignments
equivalenttoanMWISproblemonasuitablyconstructedgraph for all the nodes are consistent with , and hence with
withnodeweights.Thisconstructionisrelatedtothe“overcom- eachother.Thismeansthattherewillnotbeanedgein
pletebasis”representation[9].Considerthefollowingcanonical betweenanytwonodesintheset.
MAP estimation problem: supposewe are given a distribution 2) Conversely,if isamaximalindependentsetin ,thenall
over vectors of variables , each of thesetsofpartialassignmentscorrespondingtoeachnode
whichcantakeafinitevalue.Supposealsothat factorsintoa in are allconsistentwith eachother, and witha global
productofstrictlypositivefunctions,whichwefindconvenient assignment .
todenoteinexponentialform There is thus a one-to-one correspondence between maximal
|     |     |     |     |     |     |     | independent |     | sets | in and | assignments |     | . The | lemma | follows |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---- | ------ | ----------- | --- | ----- | ----- | ------- |
fromthisobservation.
|     |     |     |     |     |     |     | Example |     | 7.1: | Let | and | be binary | variables | with | joint |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ---- | --- | --- | --------- | --------- | ---- | ----- |
distribution
| Here specifies |     | the domainofthe |     | function | ,and | is the |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --------------- | --- | -------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vectorofthosevariablesthatareinthedomainof .The ’s wherethe areanyrealnumbers.Thecorresponding isshown
| alsoserveasanindexforthefunctions. |            |         |     |                        | isthesetoffunctions. |         |                     |     |                     |                         |                       |     |     |      |     |
| ---------------------------------- | ---------- | ------- | --- | ---------------------- | -------------------- | ------- | ------------------- | --- | ------------------- | ----------------------- | --------------------- | --- | --- | ---- | --- |
|                                    |            |         |     |                        |                      |         | inFig.3.Let         |     | beanynumbersuchthat |                         |                       |     | ,   | ,and |     |
| The MAP                            | estimation | problem |     | is to find             | a maximizing         | assign- |                     |     |                     |                         |                       |     |     |      |     |
|                                    |            |         |     |                        |                      |         | areallgreaterthan   |     |                     | .Theweightsonthenodesin |                       |     |     | are: |     |
| ment                               |            |         | .   |                        |                      |         | onnode“1”ontheleft, |     |                     |                         | fornode“1”ontheright, |     |     |      |     |
| Wenowbuildanauxiliarygraph         |            |         |     | ,andassignweightstoits |                      |         |                     |     |                     |                         |                       |     |     |      |     |
|                                    |            |         |     |                        |                      |         | forthenode“11,”and  |     |                     |                         | foralltheothernodes.  |     |     |      |     |
nodes,suchthattheMAPestimationproblemaboveisequiva-
| lenttofindingtheMWISof                              |     |     | .Thereisonenodein |     |     | foreach     |     |     |     |       |            |     |     |     |     |
| --------------------------------------------------- | --- | --- | ----------------- | --- | --- | ----------- | --- | --- | --- | ----- | ---------- | --- | --- | --- | --- |
|                                                     |     |     |                   |     |     |             |     |     |     | VIII. | DISCUSSION |     |     |     |     |
| 2Theremaybemultipledualoptima,andinthiscase,(cid:0) |     |     |                   |     |     | maynothavea |     |     |     |       |            |     |     |     |     |
Webelievethispaperopensseveralinterestingdirectionsfor
uniquelimit.However,everylimitpointwillbeadualoptimum.Inthatcase,
thesameproofstillholds;weskipitheretokeepargumentssimple. investigation. In general, the exact relationship between max

SANGHAVIetal.:MESSAGEPASSINGFORMAXIMUMWEIGHTINDEPENDENTSET 4833
[12] Y.Weiss,C.Yanover,andT.Meltzer,“MAPestimation,linearpro-
grammingandbeliefpropagationwithconvexfreeenergies,”inProc.
Conf.UncertaintyArtif.Intell.,2007.
[13] M.Bayati,C.Borgs,J.Chayes,andR.Zecchina,“Belief-propagation
forweightedb-matchingsonarbitrarygraphsanditsrelationtolinear
programswithintegersolutions,”[Online].Available:http://arxiv.org/
abs/0709.1190
[14] P.O.VontobelandR.Koetter,“Ontherelationshipbetweenlinearpro-
grammingdecodingandmin-sumalgorithmdecoding,”inProc.Int.
Symp.Inf.TheoryAppl.,Parma,Italy,Oct.10–13,2004,pp.991–996.
Fig.3. ExampleofreductionfromMAPproblemtoMWISproblem. [15] S. Sanghavi, D. Shah, and A. Willsky, “Message-passing for
max-weight independent set,” in Advances in Neural Informa-
tion Processing Systems. Cambridge, MA: MIT Press, 2007, pp.
1281–1288.
[16] A.Schrijver,CombinatorialOptimization.PolyhedraandEfficiency.
productandLPisnotwellunderstood.Theirclosesimilarityfor
Berlin,Germany:Springer-Verlag,2003.
theMWISproblem,alongwiththereductionofMAPestimation [17] D.Bertsekas,NonLinearProgramming. Belmont,MA:AthenaSci-
to an MWIS problem, suggests that the MWIS problem may entific,1995.
[18] Grotschel,L.Lovasz,andSchrijver,“Polynomialalgorithmsforper-
provideagoodfirststepinaninvestigationofthisrelationship.
fectgraphs,”Ann.DiscreteMath.,vol.21,pp.325–356,1984.
Indeed, obtaining such an understanding in the context of LP [19] K.JungandD.Shah,“Lowdelayschedulinginwirelessnetworks,”in
decodingandmaxproductwouldbeaninterestingpursuit(e.g., Proc.IEEEInt.Symp.Inf.Theory,2007,pp.1396–1400.
[20] V.KolmogorovandM.Wainwright,“Onoptimalityoftree-reweighted
seeworkbyVontobelandKoetter[14]).
max-productmessage-passing,”inProc.Conf.UncertaintyArtif.In-
Our novel message-passing algorithm and the reduction of tell.,Edinburgh,Scotland,Jul.2005.
MAP estimation to an MWIS problem immediately yields a [21] Y.Weiss,C.Yanover,andT.Meltzer,“MAPestimation,linearpro-
grammingandbeliefpropagationwithconvexfreeenergies,”inProc.
new message-passing algorithm for general MAP estimation
Conf.UncertaintyArtif.Intell.,2007.
problem.Itwouldbeinterestingtoinvestigatethepowerofthis [22] A. Globerson and T. Jaakkola, “Fixing max-product: Convergent
algorithmonmoregeneraldiscreteestimationproblems. message passing algorithms for MAP LP-relaxations,” in Advances
in Neural Information Processing Systems. Cambridge, MA: MIT
Press,2007,pp.553–560.
[23] Y.WeissandW.Freeman,“Ontheoptimalityofsolutionsofthemax-
ACKNOWLEDGMENT
productbelief-propagationalgorithminarbitrarygraphs,”IEEETrans.
Inf.Theory,vol.47,no.2,pp.736–744,Feb.2001.
Theauthorswouldliketothankanonymousreviewersofthe
[24] S.M.Aji,G.B.Horn,andR.J.McEliece,“Ontheconvergenceof
firstsubmissionofthismanuscriptforhelpingthemimprovethe iterativedecodingongraphswithasinglecycle,”inProc.IEEEInt.
presentationofthematerial. Symp.Inf.Theory,Cambridge,MA,Aug.1998,pp.276–276.
[25] J. Yedidia, W. Freeman, and Y. Weiss, “Constructing free-energy
approximationsandgeneralizedbeliefpropagationalgorithms,”IEEE
Trans.Inf.Theory,vol.51,no.7,pp.2282–2312,Jul.2005.
REFERENCES
[26] S.TatikondaandM.I.Jordan,“LoopybeliefpropagationandGibbs
[1] M. Bayati, D. Shah, and M. Sharma, “Max-product for maximum measures,”inProc.Conf.UncertaintyArtif.Intell.,2002.
weight matching: Convergence, correctness and LP duality,” IEEE [27] D.P.Bertsekas,“Auctionalgorithmsfornetworkflowproblems:A
Trans.Inf.Theory,2009,acceptedforpublication. tutorialintroduction,”Comput.Optim.Appl.,vol.1,pp.7–66,1992.
[2] S.Sanghavi,D.Malioutov,andA.Willsky,“Linearprogramminganal-
ysisofLoopyBeliefPropagationforweightedmatching,”inAdvances
in Neural Information Processing Systems. Cambridge, MA: MIT
Press,2007,pp.1273–1280.
[3] Z.-Q.LuoandP.Tseng,“Onthelinearconvergenceofdescentmethods
SujaySanghavi(M’08)receivedthePh.D.degreefromtheElectricalandCom-
forconvexessentiallysmoothminimization,”SIAMJ.ControlOptim., puter Engineering Department, University of Illinois at Urbana-Champaign,
vol.30,no.2,pp.408–425,1992. Urbana,in2006.
[4] V.Kolmogorov,“Convergenttree-reweightedmessagepassingforen- Currently,heisanAssistantProfessorattheElectricalandComputerEn-
ergyminimization,”IEEETrans.PatternAnal.Mach.Intell.,vol.28, gineeringDepartment,PurdueUniversity,WestLafayette,IN,whichhejoined
no.10,pp.1568–1583,Oct.2006. in2008.Hisresearchinterestslieinprobability,optimizationandalgorithms,
[5] C.MoallemiandB.VanRoy,“Convergenceofthemin-summessage andtheirapplicationstonetworks,communication,andstatisticalinferenceand
passingalgorithmforquadraticoptimization,”2006[Online].Avail- learning.
able:arXiv:cs/0603058
[6] L.Trevisan,“Inapproximabilityofcombinatorialoptimizationprob-
lems,” Electron. Colloq. Comput. Complex., Tech. Rep. TR04–065,
2004. Devavrat Shah received the B.Tech. degree in computer science and engi-
[7] M.J.Wainwright,T.Jaakkola,andA.S.Willsky,“Treeconsistency neeringfromIndianInstituteofTechnology(IIT),Bombay,India,in1999with
andboundsontheperformanceofthemax-productalgorithmandits thehonorofthePresidentofIndiaGoldMedalandthePh.D.degreefromthe
generalizations,”Statist.Comput.,vol.14,pp.143–166,Apr.2004. ComputerScienceDepartment,StanfordUniversity,Stanford,CA,inOctober
[8] M. Wainwright, T. Jaakkola, and A. Willsky, “MAP estimation via 2004.
agreementon(hyper)trees:Message-passingandlinearprogramming He was a postdoc in the Statistics Department, Stanford University, in
approaches,”IEEETrans.Inf.Theory,vol.51,no.11,pp.3697–3717, 2004–2005. Currently, he is a Jamieson Career Development Assistant Pro-
Nov.2005. fessor at the Department of Electrical Engineering and Computer Science,
[9] M. Wainwright and M. Jordan, “Graphical models, exponential MassachusettsInstituteofTechnology(MIT),Cambridge.Hisresearchfocus
families, and variational inference,” Dept. Statist., Univ. California is on theory of largecomplex networks which includes network algorithms,
Berkeley,Berkeley,CA,Tech.Rep.649,2003. stochastic networks, network information theory, and large scale statistical
[10] M.WainwrightandM.Jordan,“Graphicalmodels,exponentialfami- inference.
lies,andvariationalinference,”Found.TrendsMach.Learn.,vol.1,no. Mr.ShahwascoawardedtheIEEEINFOCOMbestpaperawardin2004and
1-2,pp.1–305,2008. ACMSIGMETRICS/Performancebestpaperawardin2006.Hereceived2005
[11] J. Yedidia, W. Freeman, and Y. Weiss, “Generalized belief propa- GeorgeB.DantzigbestdissertationawardfromtheINFORMSandanNSF
gation,”MitsubishiElect.Res.Lab.,Cambridge,MA,TR-2000–26, CAREERawardin2006.HeistherecipientofthefirstACMSIGMETRICS
2000. RisingStarAward2008forhisworkonnetworkschedulingalgorithms.

4834 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.55,NO.11,NOVEMBER2009
AlanS.Willsky(S’70–M’73–SM’82–F’86) received thePh.D.degreefrom researchinterestsareinthedevelopmentandapplicationofadvancedmethods
MassachusettsInstituteofTechnology(MIT),Cambridge,in1972. ofestimation,machinelearning,andstatisticalsignalandimageprocessing.
HejoinedMITin1973andistheEdwinSibleyWebsterProfessorofElec- Dr.Willskyhasreceivedseveralawardsincludingthe1975AmericanAuto-
tricalEngineeringandCo-DirectoroftheLaboratoryforInformationandDe- maticControlCouncilDonaldP.EckmanAward,the1979ASCEAlfredNoble
cisionSystems.HewasafounderofAlphatech,Inc.andChiefScientificCon- Prize,the1980IEEEBrowderJ.ThompsonMemorialAward,theIEEEControl
sultant,aroleinwhichhecontinuesatBAESystemsAdvancedInformation SystemsSocietyDistinguishedMemberAwardin1988,the2004IEEEDonald
Technologies.From1998to2002,heservedontheU.S.AirForceScientific G.FinkPrizePaperAward,andDoctoratHonorisCausafromUniversitéde
AdvisoryBoard.Hehasdeliverednumerouskeynoteaddressesandiscoauthor Rennesin2005.
ofthetextSignalsandSystems(EnglewoodCliffs,NJ:Prentice-Hall,1997).His