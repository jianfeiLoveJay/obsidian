736 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
On the Optimality of Solutions of the Max-Product
Belief-Propagation Algorithm in Arbitrary Graphs
Yair Weiss, Member,IEEE,and WilliamT. Freeman, Member,IEEE
Abstract—Graphical models, such as Bayesian networks and Here we focus on the problem of finding an assignment for
Markovrandomfields(MRFs),representstatisticaldependencies the unobserved variables that is most probable given the ob-
ofvariablesbyagraph.Themax-product“beliefpropagation”al-
served ones. In general, this problem is NP-hard [19] but if
gorithmisalocal-message-passingalgorithmonthisgraphthatis
the graph is singly connected (i.e., there is only one path be-
knowntoconvergetoauniquefixedpointwhenthegraphisatree.
Furthermore,whenthegraphisatree,theassignmentbasedonthe tweenanytwogivennodes)thenthereexistefficientlocalmes-
fixedpointyieldsthemostprobablevaluesoftheunobservedvari- sage-passing schemes to perform this task. Pearl [18] derived
ablesgiventheobservedones. suchaschemeforsinglyconnectedBayesiannetworks.Theal-
Recently, good empirical performance has been obtained by
gorithm,whichhecalled“beliefrevision,”isidenticaltohisal-
running the max-product algorithm (or the equivalent min-sum
gorithmforfindingposteriormarginalsovernodesexceptthat
algorithm) on graphs with loops, for applications including the
decoding of “turbo” codes. Except for two simple graphs (cycle thesummationoperatorisreplacedwithamaximization.Ajiet
codes and single-loop graphs) there has been little theoretical al.[2]haveshownthatbothofPearl’salgorithmscan beseen
understanding of the max-product algorithm on graphs with asspecialcasesofgeneralizeddistributivelawsoverparticular
loops.
semirings.Inparticular,Pearl’salgorithmforfindingmaximum
Hereweprovearesultonthefixedpointsofmax-productona
a posteriori (MAP) assignments can be seen as a generalized
graphwitharbitrarytopologyandwitharbitraryprobabilitydistri-
butions(discrete-orcontinuous-valuednodes).Weshowthatthe distributivelawoverthemax-productsemiring.Wewillhence-
assignmentbasedonafixedpointisa“neighborhoodmaximum” forthrefertoitasthe“max-product”algorithm.
oftheposteriorprobability:theposteriorprobabilityofthemax- Pearl showed that for singly connected networks, the max-
productassignmentisguaranteedtobegreaterthanallotheras-
productalgorithmisguaranteedtoconvergeandthattheassign-
signmentsinaparticularlargeregionaroundthatassignment.The
mentbasedonthemessagesatconvergenceisguaranteedtogive
regionincludesallassignmentsthatdifferfromthemax-product
assignmentinanysubsetofnodesthatformnomorethanasingle theoptimalassignmentvaluescorrespondingtotheMAPsolu-
loopinthegraph.Insomegraphs,thisneighborhoodisexponen- tion.
tiallylarge.Weillustratetheanalysiswithexamples. Several groups have recently reported excellent exper-
IndexTerms—Bayesiannetworks,beliefpropagation,maximum imental results by running the max-product algorithm on
aposteriori(MAP)estimate,Markovrandomfields(MRFs),max- graphs with loops [23], [6], [3], [20], [6], [11]. Benedetto et
product,min-sum. al. used the max-product algorithm to decode “turbo” codes
and obtained excellent results that were slightly inferior to
the original turbo decoding algorithm (which is equivalent
I. INTRODUCTION
to the sum-product algorithm). Weiss [20] compared the
PROBLEMS involving probabilistic belief propagation
performanceofsum-productandmax-productona“toy”turbo
ariseinawidevarietyofapplications,includingerror-cor-
code problem while distinguishing between converged and
recting codes, speech recognition, and image understanding.
unconverged cases. He found that if one considers only the
Typically, a probability distribution is assumed over a set of
convergent cases, the performance of max-product decoding
variables and the task is to infer the values of the unobserved
is significantly better than sum-product decoding. However,
variables given the observed ones. The assumed probability
the max-product algorithm converges less often so its overall
distribution is described using a graphical model [14]—the
performance (including both convergent and nonconvergent
qualitative aspects of the distribution are specified by a graph cases)isinferior.
structure. The graph may either be directed as in a Bayesian
Progress in the analysis of the max-product algorithm has
network [18], [12] or undirected as in a Markov random field
beenmade fortwo specialtopologies:single-loopgraphs,and
(MRF)[18],[10].
“cycle codes.” For graphs with a single loop [23], [20], [21],
[5],[2],itcanbeshownthatthealgorithmconvergestoastable
fixedpoint or a periodic oscillation. If it converges to a stable
Manuscript received January 3, 2000. This work was supported under fixedpoint,thentheassignmentbasedonthefixed-pointmes-
Grants MURI-ARO-DAAH04-96-1-0341, MURI N00014-00-1-0637, and sagesistheoptimalassignment.Forgraphsthatcorrespondto
NSFIIS-9988642
cyclecodes(low-densityparity-checkcodes,inwhicheachbit
Y.WeissiswiththeComputerScienceDivision,UniversityofCaliforniaat
Berkeley,Berkeley,CA94720-1776USA(e-mail:yweiss@cs.berkeley.edu). ischeckedbyexactlytwochecknodes),Wiberg[23]gavesuffi-
W. T. Freeman is with MERL, Mitsubishi Electric Research Labs., Cam- cientconditionsformax-producttoconvergetothetransmitted
bridge,MA02139USA(e-mail:freeman@merl.com).
codewordandHorn[11]gavesufficientconditionsforconver-
CommunicatedbyB.J.Frey,GuestEditor.
PublisherItemIdentifierS0018-9448(01)00724-6. gencetotheMAPassignment.
0018–9448/01$10.00©2001IEEE
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 09:44:13 UTC from IEEE Xplore. Restrictions apply.

WEISSANDFREEMAN:SOLUTIONSOFTHEMAX-PRODUCTBELIEF-PROPAGATIONALGORITHM 737
|     |     |     |     |     |     | Wewillassume,withoutlossofgenerality,thateach |     |                           |     |     |     |     | node |
| --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | ------------------------- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | hasacorresponding                             |     | nodethatisconnectedonlyto |     |     |     | .   |      |
Thus
(2)
|     |     |     |     |     |     | The restriction |     | that all  | the variables  |     | are observed |              | and |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | -------------- | --- | ------------ | ------------ | --- |
|     |     |     |     |     |     | none of         | the | variables | are is just    | to  | make         | the notation |     |
|     |     |     |     |     |     | simple—         |     | may       | be independent |     | of           | (equivalent  |     |
(a)
|     |     |     |     |     |     | to being      | unobserved) |                         | or                | may          | be        |           |     |
| --- | --- | --- | --- | --- | --- | ------------- | ----------- | ----------------------- | ----------------- | ------------ | --------- | --------- | --- |
|     |     |     |     |     |     | (equivalentto |             | beingobserved,withvalue |                   |              | ).        |           |     |
|     |     |     |     |     |     | In describing | and         | analyzing               | belief            | propagation, |           | we assume |     |
|     |     |     |     |     |     | the graphical | model       | has                     | been preprocessed |              | so        | that all  | the |
|     |     |     |     |     |     | cliques       | consist of  | pairs                   | of units. Any     | graphical    |           | model     | can |
|     |     |     |     |     |     | be converted  | into        | this form               | before            | doing        | inference | through   | a   |
suitableclusteringofnodesintolargenodes[21].Fig.1shows
anexample—aBayesiannetworkisconvertedintoanMRFin
whichallthecliquesarepairsofunits.
Equation(2)becomes
(3)
(b)
Fig.1. AnyBayesiannetworkcanbeconvertedintoanundirectedgraphwith
wherethefirstproductisoverconnectedpairsofnodes.
pairwisecliquesbyaddingclusternodesforallparentsthatshareacommon
child.(a)ABayesiannetwork.(b)Thecorrespondingundirectedgraphwith TheimportantpropertyofMRFsthatwewillusethroughout
| pairwisecliques.Aclusternodefor(x |     |     | ;x )hasbeenadded.Thepotentials |     |     |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thispaperistheMarkovblanketproperty.Theprobabilityofa
canbesetsothatthejointprobabilityintheundirectedgraphisidenticaltothat
|     |     |     |     |     |     | subsetofnodes |     | givenallothernodesinthegraph |     |     |     | depends |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---------------------------- | --- | --- | --- | ------- | --- |
intheBayesiannetwork.Inthiscase,theupdaterulespresentedinthispaper
reducetoPearl’spropagationrulesintheoriginalBayesiannetwork[21]. only on the values of the nodes that immediately neighbor .
|     |     |     |     |     |     | Furthermore,theprobabilityof |     |     | givenallothernodesispro- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | ------------------------ | --- | --- | --- | --- |
Inthispaper,weanalyzethemax-productalgorithmingraphs portionaltotheproductofallcliquepotentialswithin andall
ofarbitrarytopology.Weshowthatatafixedpointofthealgo- cliquepotentialsbetween anditsimmediateneighbors
rithm,theassignmentisa“neighborhoodmaximum”ofthepos-
teriorprobability:theposteriorprobabilityofthemax-product (4)
| assignment | is guaranteed | to be | greater than | all other | assign- |     |     |     |     |     |     |     |     |
| ---------- | ------------- | ----- | ------------ | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
mentsinaparticularlargeregionaroundthatassignment.These
resultsmotivateusingthispowerfulalgorithminabroaderclass
(5)
ofnetworks.
Theadvantageofpreprocessingthegraphintoonewithpair-
II. THEMAX-PRODUCTALGORITHMINPAIRWISEMARKOV wise cliques is that the description and the analysis of belief
RANDOMFIELDS propagationbecomessimpler.Forcompleteness,wereviewthe
Pearl’soriginalalgorithmwasdescribedfordirectedgraphs, beliefpropagationschemeusedin[21].AswediscussintheAp-
|     |     |     |     |     |     | pendix,this | beliefpropagationschemeis |     |     | equivalenttoPearl’s |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------------------------- | --- | --- | ------------------- | --- | --- | --- |
butinthispaper,wefocusonundirectedgraphs.Everydirected
beliefpropagationalgorithmindirectedgraphs,theGeneralized
| graphical | model can be transformed |     | into | an undirected | graph- |     |     |     |     |     |     |     |     |
| --------- | ------------------------ | --- | ---- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
DistributiveLawalgorithmof[1]andthefactorgraphpropaga-
| ical model | before doing | inference | (see Fig. | 1). A | undirected |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --------- | --------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
tionalgorithmof[13].Thesethreealgorithmscorrespondtothe
graphicalmodel(oranMRF)isagraphinwhichthenodesrep-
resentvariablesandarcsrepresentscompatibilityrelationsbe- algorithmpresentedherewithaparticularwayofpreprocessing
thegraphinordertoobtainpairwisepotentials.
tweenthem.Assumingallprobabilitiesarenonzero,theHam-
|     |     |     |     |     |     | At every | iteration, | each | node sends | a   | (different) | message |     |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | ---- | ---------- | --- | ----------- | ------- | --- |
mersley–Cliffordtheorem(e.g.,[18])guaranteesthattheprob-
|     |     |     |     |     |     | to each | of its neighbors |     | and receives | a   | message | from | each |
| --- | --- | --- | --- | --- | --- | ------- | ---------------- | --- | ------------ | --- | ------- | ---- | ---- |
abilitydistributionwillfactorizeintoaproductoffunctionsof
|     |     |     |     |     |     | neighbor.Let | and |     | betwoneighboringnodesinthegraph. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --- | -------------------------------- | --- | --- | --- | --- |
themaximalcliquesofthegraph.
|          |               |     |                |           |        | Wedenoteby |     | themessagethatnode |      |       | sendstonode |     |     |
| -------- | ------------- | --- | -------------- | --------- | ------ | ---------- | --- | ------------------ | ---- | ----- | ----------- | --- | --- |
| Denoting | by the values | of  | all unobserved | variables | in the |            |     |                    |      |       |             |     |     |
|          |               |     |                |           |        | , by       | the | message            | that | sends | to , and    | by  |     |
graph,thefactorizationhastheform
|                                     |     |                              |     |     |     | thebeliefatnode              |     | .   |     |     |     |     |     |
| ----------------------------------- | --- | ---------------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                                     |     |                              |     |     | (1) | Themax-productupdaterulesare |     |     |     |     |     |     |     |
| where isasubsetof                   |     | thatformacliqueinthegraphand |     |     |     |                              |     |     |     |     |     |     |     |
| isthepotentialfunctionfortheclique. |     |                              |     |     |     |                              |     |     |     |     |     |     | (6) |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 09:44:13 UTC from IEEE Xplore.  Restrictions apply.

738 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
|     |     |     |     |     | (7) | Hereagain,ifiterationsof(8)convergeto |     |     |     |     |     | then | satisfies |
| --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | ---- | --------- |
.
|                                        |     |             |                  |         |       | Theequation  |         |      |        | isahighlynonlinearequationand |             |     |            |
| -------------------------------------- | --- | ----------- | ---------------- | ------- | ----- | ------------ | ------- | ---- | ------ | ----------------------------- | ----------- | --- | ---------- |
| where denotesanormalizationconstantand |     |             |                  |         | means |              |         |      |        |                               |             |     |            |
|                                        |     |             |                  |         |       | it is not    | obvious | how  | many   | solutions exist               | or          | how | to charac- |
| allnodesneighboring                    |     | ,except     | .                |         |       |              |         |      |        |                               |             |     |            |
|                                        |     |             |                  |         |       | terize them. | Horn    | [11] | showed | that in                       | single-loop |     | graphs,    |
| The procedure                          | is  | initialized | with all message | vectors | set   | to           |         |      |        |                               |             |     |            |
canbeconsideredasmatrixmultiplicationoverthemax-product
constantfunctions.Observednodesdonotreceivemessagesand
semiringandfixedpointscorrespondtoeigenvectorsofthatma-
| theyalwaystransmitthesamevector—if |     |     |     | isobservedtohave |     |     |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
trix.Thuseveninsingle-loopgraphs,onecanconstructexam-
| value then |     |     | .Thenormalizationof |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pleswithanynumberoffixedpoints.
in(6)isnotnecessary—whetherornotthemessageisnormal-
|                  |      |     |                     |             |     | The main | result      | of  | this paper | is a characterization |     |     | of how  |
| ---------------- | ---- | --- | ------------------- | ----------- | --- | -------- | ----------- | --- | ---------- | --------------------- | --- | --- | ------- |
| ized, the belief | will | be  | identical. However, | normalizing | the |          |             |     |            |                       |     |     |         |
|                  |      |     |                     |             |     | well the | max-product |     | assignment | approximates          |     | the | MAP as- |
messagesavoidsnumericalunderflowandaddstothestability
|     |     |     |     |     |     | signment.Weshowthattheassignment |     |     |     |     | mustbeaneighbor- |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- |
ofthealgorithm.Weassumethroughoutthispaperthatallnodes
|     |     |     |     |     |     | hoodmaximumof |     |     | :thatis, |     |     |     | forall |
| --- | --- | --- | --- | --- | --- | ------------- | --- | --- | -------- | --- | --- | --- | ------ |
simultaneouslyupdatetheirmessagesinparallel.
|     |     |     |     |     |     | inaparticularlargeregionaround |     |     |     | .Thisconditionisweaker |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | ---------------------- | --- | --- | --- |
Forsinglyconnectedgraphsitiseasytoshowthefollowing.
thanaglobalmaximumbutstrongerthanalocalmaximum.
• Thealgorithmconvergestoauniquefixedpointregardless Tobemoreprecise.wedefinethesingleloopsandtrees(SLT)
ofinitialconditionsinafinitenumberofiterations.
|     |     |     |     |     |     | neighborhood | of  | an assignment |     | in a | graphical | model | to  |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | ---- | --------- | ----- | --- |
• Atconvergence,thebeliefforanyvalue ofanode is includeallassignments thatcan beobtained from bythe
following.
| the maximum    |     | of the | posterior, conditioned | on  | that node |                             |     |     |     |           |     |              |     |
| -------------- | --- | ------ | ---------------------- | --- | --------- | --------------------------- | --- | --- | --- | --------- | --- | ------------ | --- |
| havingthevalue |     | :      |                        |     | .         |                             |     |     |     |           |     |              |     |
|                |     |        |                        |     |           | • Choosinganarbitrarysubset |     |     |     | ofnodesin |     | thatconsists |     |
• Definethemax-productassignment, by ofdisconnectedcombinationsoftreesandsingleloops.
|     |     |     |     |     |     | • Assigning                                  |     | arbitrary | values | to —the |     | chosen | subset of |
| --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --------- | ------ | ------- | --- | ------ | --------- |
|     |     |     |     |     |     | nodes.Theothernodeshavethesameassignmentasin |     |           |        |         |     |        | .         |
(assumingauniquemaximizingvalueexists).Then is Claim1: Foranarbitrarygraphicalmodelwitharbitrarypo-
theMAPassignment.
|     |     |     |     |     |     | tentials,if | isafixedpointofthemax-productalgorithmand |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
The max-product assignment assumes there are no “ties”— istheassignmentbasedon then for
thatauniquemaximizing existsforall .Tiescanarise all intheSLTneighborhoodof .
when the MAP assignment is not unique, e.g., when there are Fig. 2 illustrates example configurations within the SLT
two assignments that have identical posterior and both maxi- neighborhood of the max-product assignment. It shows ex-
mizetheposterior.Forsinglyconnectedgraphs,theconverseis amples of subsets of nodes that could be changed to arbitrary
alsotrue:iftherearenotiesin thentheMAPassignmentis valuesand the posteriorprobability of the assignment is guar-
unique.Inwhatfollows,weassumeauniqueMAPassignment. anteedtobeworsethanthatofthemax-productassignment.
In particular applications, it might be easier to work in the To build intuition, we first describe the proof for a specific
logdomainsothattheproductoperationin(7)isreplacedbya case,thediamondgraphofFig.3.Thegeneralproofisgivenin
| sumoperations.Thus,themax-productalgorithmissometimes |     |     |     |     |     | SectionIII-B. |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
referredtoasthemax-sumalgorithmorthemin-sumalgorithm
[23],[5].Ifthegraphisachain,themax-productisatwo-way
A. SpecificExample
versionoftheViterbialgorithminhiddenMarkovmodelsand
iscloselyrelatedtoconcurrentdynamicprogramming[4].De- Westartbygivinganoverviewoftheproofforthediamond
spitethisconnectiontowell-studiedalgorithms,therehasbeen
graphshowninFig.3(a).Theproofisbasedontheunwrapped
| very little analytical |     | success | in characterizing | the | solutions of |          |           |       |      |           |        |             |     |
| ---------------------- | --- | ------- | ----------------- | --- | ------------ | -------- | --------- | ----- | ---- | --------- | ------ | ----------- | --- |
|                        |     |         |                   |     |              | tree—the | graphical | model | that | the loopy | belief | propagation | is  |
themax-productalgorithmonarbitrarygraphswithloops.
|     |     |     |     |     |     | solving | exactly | when | applying | the belief | propagation |     | rules in |
| --- | --- | --- | --- | --- | --- | ------- | ------- | ---- | -------- | ---------- | ----------- | --- | -------- |
aloopynetwork[9],[23],[21],[22].Inerror-correctingcodes,
III. WHATARETHEFIXEDPOINTSOFTHEMAX-PRODUCT theunwrappedtreeisreferredtoasthe“computationtree”—it
ALGORITHM?
isbasedontheideathatthecomputationofamessagesentbya
|                  |     |                 |           |     |            | nodeattime | dependsonmessagesitreceivedfromitsneigh- |     |     |     |     |     |     |
| ---------------- | --- | --------------- | --------- | --- | ---------- | ---------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| Each iterationof |     | the max-product | algorithm | can | be thought |            |                                          |     |     |     |     |     |     |
ofasanoperator thatinputsalistofmessages andout- borsattime andthosemessagesdependonthemessages
puts a list of messages . Thus running belief theneighborsreceivedattime ,etc.
propagation can be thought of as an iterative way of finding a Fig. 3 shows an unwrapped tree around node for the di-
solution to the fixed-point equations with an initial amond-shaped graph on the left. Each node has a shaded ob-
servednodeattachedtoitthatisnotshownforsimplicity.Each
| guess inwhichallmessagesareconstantfunctions. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Note that this is not the only way of finding fixed points. nodehasashadedobservednodeattachedtoitthatisnotshown
Murphy et al. [17] describe an alternative method for finding forsimplicity.Weuse torefertounwrappedquantities.
fixedpointsof .Theysuggestediterating To simplify notation, we assume that , the assignment
|     |     |     |     |     |     | based on | a fixed | point | of the | max-product | algorithm |     | is equal |
| --- | --- | --- | --- | --- | --- | -------- | ------- | ----- | ------ | ----------- | --------- | --- | -------- |
(8)
|     |     |     |     |     |     | to zero |     | . The | periodic | assignment | lemma |     | from [22] |
| --- | --- | --- | --- | --- | --- | ------- | --- | ----- | -------- | ---------- | ----- | --- | --------- |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 09:44:13 UTC from IEEE Xplore.  Restrictions apply.

WEISSANDFREEMAN:SOLUTIONSOFTHEMAX-PRODUCTBELIEF-PROPAGATIONALGORITHM 739
(a)
(a)
(b)
Fig. 3. (a) An MRF with multiple loops. (b) The unwrapped graph cor-
responding to this structure. The unwrapped graphs are constructed by
replicatingthepotentials(cid:9)(x ;x )andobservationsy whilepreservingthe
localconnectivityoftheloopygraph.Theyareconstructedsothatthemessages
receivedbynodex aftertiterationsintheloopygraphareequivalenttothose
thatwouldbereceivedbyx intheunwrappedgraph.Anobservednodey ,
notshown,isconnectedtoeachdepictednode.
(b)
We now show that the global optimality of and the
method of construction of the unwrapped tree guarantee that
forall intheSLTneighborhoodof .
ReferringtoFig.3(a),supposethat
BytheMarkovpropertyofthediamondfigure,thismeansthat
(10)
Notethatnode hasexactlythesameneighborsintheun-
wrapped graph as has in the loopy graph. Furthermore, by
themethodofconstruction,thepotentialsbetween andeach
ofitsneighborsisthesameasthepotentialsbetween andits
neighbors.Thus,(10)impliesthat
(c)
Fig.2. (a)A25(cid:2)25gridofpoints.(b)and(c)Examplesofsubsetsofnodes (11)
thatformnomorethanasingleloop.Inthispaper,weprovethatchangingsuch
incontradictionto(9).Hence,nochangeofasingle canim-
asubsetofnodesfromthemax-productassignmentwillalwaysdecreasethe
posteriorprobability. provetheposteriorprobability.
What about changing two at a time? If we change a pair
that is not connected in the graph, say and , then by the
guaranteesthatwecanmodify fortheleafnodesso
Markov property this is equivalent to changing one at a time.
thattheoptimalassignmentintheunwrappedtreeisallzeros
Thus,suppose thisagainimpliesthat
(9)
andwehaveshownearlierthatthisleadstoacontradiction.Thus
[The aremodifiedtoincludethemessagesfromthe nochangeofassignmentintwounconnectednodescanimprove
nodestobeaddedatthenextstageoftheunwrapping.] theposteriorprobability.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 09:44:13 UTC from IEEE Xplore. Restrictions apply.

740 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
Ifthetwoareconnected,say thenthesameargument coveringof [16].Roughlyspeaking,itisatopologythatpre-
holds with respect to the pair of nodes . Note that the servesthelocaltopologyofthegraph butissinglyconnected.
subgraph isisomorphictothesubgraph andthetwo It is precisely this fact, that max-product gives the global op-
subgraphshavethesameneighbors.Hence timum on a graph that has the same local topology as , that
|     |     |     |     |     |     |     |     | makessurethat |     | isaneighborhoodmaximumof |     |     |     |     | .   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------------------ | --- | --- | --- | --- | --- |
(12)
|     |     |     |     |     |     |     |     | Wenowstatesomepropertiesof |     |     |     |     | .   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
impliesthat 1) EqualNeighborsProperty: Everynonleafnodein has
|     |     |     |     |     |     |     | (13) | thesamenumberofneighborsasthecorrespondingnodein |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
andtheneighborsareinone-to-onecorrespondence.If
| and this is | again in         | contradiction |       | to (9).     | Thus, | no change     | of  |      |          |        |     |     |           |     |          |
| ----------- | ---------------- | ------------- | ----- | ----------- | ----- | ------------- | --- | ---- | -------- | ------ | --- | --- | --------- | --- | -------- |
|             |                  |               |       |             |       |               |     | then | for each |        |     | ,   |           | and | for each |
| assignment  | in two connected |               | nodes | can improve |       | the posterior |     |      |          |        |     |     |           |     |          |
|             |                  |               |       |             |       |               |     |      | there    | exists |     |     | such that |     | .        |
probability.
|     |     |     |     |     |     |     |     | Thisfollowsdirectlyfromthemethodofconstructing |     |     |     |     |     |     | .   |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Similarargumentsshowthatnochangeofassignmentinany
|     |     |     |     |     |     |     |     | 2) EqualConditionalProbabilityProperty: |     |     |     |     |     | Theprobability |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- |
subtreeofthegraphcanimprovetheposteriorprobability(e.g.,
|                     |     |     |                       |     |     |     |     | of a nonleaf  | node |                               | given its | neighbors | in  | is equal | to the |
| ------------------- | --- | --- | --------------------- | --- | --- | --- | --- | ------------- | ---- | ----------------------------- | --------- | --------- | --- | -------- | ------ |
| changingthevaluesof |     |     | orchangingthevaluesof |     |     |     | and |               |      |                               |           |           |     |          |        |
|                     |     |     |                       |     |     |     |     | probabilityof |      | givenitsneighbors.Formally,if |           |           |     |          |        |
).
then
Theseargumentsnolongerhold,however,whenwechange
(15)
| a subset of | nodes that | form | a loopy | subgraph | of  | . For | ex- |     |     |     |     |     |     |     |     |
| ----------- | ---------- | ---- | ------- | -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ample,thesubgraph isnotisomorphictothesub- This follows from the Markov blanket property of MRFs [see
graph .Indeedsincetheunwrappedtreeisatree, (5)]andtheequalneighborhoodproperty.
|                |         |           |       |     |        |        |     | 3) Isomoprhic |     | Subtree | Property: |     | For any | subtree | ,   |
| -------------- | ------- | --------- | ----- | --- | ------ | ------ | --- | ------------- | --- | ------- | --------- | --- | ------- | ------- | --- |
| it cannot have | a loopy | subgraph. | Hence | we  | cannot | equate | the |               |     |         |           |     |         |         |     |
probabilitiesofthetwosubgraphsgiventheirneighbors. then for sufficiently large unwrapping count there exists an
|                     |       |          |        |           |      |             |     | isomorphic                       | subtree |     | .   | The nodes | of the       | subtrees | are in |
| ------------------- | ----- | -------- | ------ | --------- | ---- | ----------- | --- | -------------------------------- | ------- | --- | --- | --------- | ------------ | -------- | ------ |
| If the subset       | forms | a single | loop,  | however,  | then | there       | ex- |                                  |         |     |     |           |              |          |        |
|                     |       |          |        |           |      |             |     | one-to-onecorrespondence:foreach |         |     |     |           | thereexistsa |          |        |
| ists an arbitrarily | long  | chain    | in the | unwrapped | tree | that corre- |     |                                  |         |     |     |           |              |          |        |
sponds to the unwrapping of that loop. For example, note the such that and for each , .
|       |     |     |         |             |     |         |       | Toprovethiswepicktherootnodeof |     |     |     |     | ,   | astheinitialnode |     |
| ----- | --- | --- | ------- | ----------- | --- | ------- | ----- | ------------------------------ | --- | --- | --- | --- | --- | ---------------- | --- |
| chain |     |     | in Fig. | 3(b). Using | a   | similar | argu- |                                |     |     |     |     |     |                  |     |
ment to that used in proving optimality of max-product in a aroundwhichtoexpandtheunwrappedtree.Bythemethodof
|     |     |     |     |     |     |     |     | construction, | the | unwrapped |     | tree after | a number | of  | iterations |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | --- | ---------- | -------- | --- | ---------- |
single-loopgraph[23],[20],[2],[5]wecanshowthatifwecan
|     |     |     |     |     |     |     |     | equaltothedepthof |     |     | willbeisomoprhicto |     |     | andinone-to-one |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ------------------ | --- | --- | --------------- | --- |
improvetheposteriorintheloopygraphbychangingthevalue
of thenwecanalsoimprovetheposteriorinthe correspondence.Thisgivesus .Foranyotherchoiceofinitial
|     |     |     |     |     |     |     |     | nodefor | ,theunwrappedtreestartingwith |     |     |     |     | isasubtreeof |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------------------------- | --- | --- | --- | --- | ------------ | --- |
unwrappedgraphbychangingthevaluesofthearbitrarilylong
| chain.Thisagainleadstoacontradiction. |     |     |     |     |     |     |     | .                         |      |       |     |            |                   |              |      |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | ---- | ----- | --- | ---------- | ----------------- | ------------ | ---- |
|                                       |     |     |     |     |     |     |     | 4) InfiniteChainProperty: |      |       |     | Foranyloop |                   | ,thereexists |      |
|                                       |     |     |     |     |     |     |     | an arbitrarily            | long | chain |     | that       | is the unwrapping |              | of . |
B. ProofofClaim1
|             |                               |     |     |     |              |          |     | Furthermore,ifwedenoteby  |     |     |     | thelengthofthechaindivided |                     |     |     |
| ----------- | ----------------------------- | --- | --- | --- | ------------ | -------- | --- | ------------------------- | --- | --- | --- | -------------------------- | ------------------- | --- | --- |
| Wedenoteby  | theoriginalgraphandby         |     |     |     | theunwrapped |          |     |                           |     |     |     |                            |                     |     |     |
|             |                               |     |     |     |              |          |     | bythelengthoftheloopandby |     |     |     |                            | and thetwoendpoints |     |     |
| graph.Weuse | fornodesintheoriginalgraphand |     |     |     |              | fornodes |     |                           |     |     |     |                            |                     |     |     |
ofthechainthen
| intheunwrappedgraph.Wedefineamapping |     |     |     |     |     | fromnodesin |     |     |     |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(16)
| tonodesin                           | .Thismappingwillsayforeachnodein |     |     |     |                |     | what |                              |     |     |     |     |     |     |      |
| ----------------------------------- | -------------------------------- | --- | --- | --- | -------------- | --- | ---- | ---------------------------- | --- | --- | --- | --- | --- | --- | ---- |
| isthecorrespondingnodein            |                                  |     | :   |     | .              |     |      | with the“boundarypotentials” |     |     |     |     |     |     |      |
| Theunwrappedtreeis,therefore,agraph |                                  |     |     |     | andacorrespon- |     |      |                              |     |     |     |     |     |     | (17) |
dencemap.Wenowgivethemethodofconstructingboth.
Pickanarbitrarynodein ,say .Set .Iterate Note that is independent of . and refer to all node
times:
|                   |          |                     |         |     |              |     |     | variablesinthesets |     |           | and ,respectively. |      |         |          |          |
| ----------------- | -------- | ------------------- | ------- | --- | ------------ | --- | --- | ------------------ | --- | --------- | ------------------ | ---- | ------- | -------- | -------- |
|                   |          |                     |         |     |              |     |     | The existence      |     | of the    | arbitrarily        | long | chain   | follows  | from the |
| • gindallleavesof |          | (startwiththeroot); |         |     |              |     |     |                    |     |           |                    |      |         |          |          |
|                   |          |                     |         |     |              |     |     | equal neighbor     |     | property, | while              | (16) | follows | from the | Markov   |
| • foreachleaf     | ,findall |                     | nodesin |     | thatneighbor |     | ;   |                    |     |           |                    |      |         |          |          |
blanketpropertyforMRFs[see(5)].
• add nodes as children to , corresponding to all Anotherpropertyoftheunwrappedtreethatwewillneedwas
| neighborsof |     | except |     | ,where |     | istheparent |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------ | --- | ------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
provenin[22]:
| of  | .   |     |     |     |     |     |     |                             |     |     |     |                          |                      |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ------------------------ | -------------------- | --- | --- |
|     |     |     |     |     |     |     |     | 5) PeriodicAssignmentLemma: |     |     |     |                          | Let beafixed-pointof |     |     |
|     |     |     |     |     |     |     |     | themax-productalgorithmand  |     |     |     | themax-productassignment |                      |     |     |
Thepotentialmatricesandobservationsforeachnodeinthe
unwrappednetworkarecopiedfromthecorrespondingnodesin in .Let betheunwrappedtree.Supposewemodifytheob-
|                         |     |     |     |      |     |      |     | servationpotentials |       |       | attheleafnodestoincludethemessages |             |       |                |     |
| ----------------------- | --- | --- | --- | ---- | --- | ---- | --- | ------------------- | ----- | ----- | ---------------------------------- | ----------- | ----- | -------------- | --- |
| theloopygraph.Thatis,if |     |     |     | then |     | ,and |     |                     |       |       |                                    |             |       |                |     |
|                         |     |     |     |      |     |      |     | from the            | nodes | to be | added                              | at the next | stage | of unwrapping. |     |
(14)
|                                |     |     |     |     |       |               |     | Then, the | MAP  | assignment |     | in  | is a replication |     | of : if |
| ------------------------------ | --- | --- | --- | --- | ----- | ------------- | --- | --------- | ---- | ---------- | --- | --- | ---------------- | --- | ------- |
| Notethattheunwrappedtreearound |     |     |     |     | after | iterationsisa |     |           | then |            | .   |     |                  |     |         |
subtreeoftheunwrappedtreearound after iterations. Usingtheseproperties,wecanprovethemainclaim.Tosim-
If weletthe numberofiterations then the unwrapped plify notation, weagain assume that ,the assignmentbased
tree becomesawell-studiedobjectintopology:theuniversal onafixedpointofthemax-productalgorithm,isequaltozero
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 09:44:13 UTC from IEEE Xplore.  Restrictions apply.

WEISSANDFREEMAN:SOLUTIONSOFTHEMAX-PRODUCTBELIEF-PROPAGATIONALGORITHM 741
|           | . The | periodic assignment                |     | property | guarantees | that we |     |     |     |     |     |     |     |
| --------- | ----- | ---------------------------------- | --- | -------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| canmodify |       | fortheleafnodessothattheoptimalas- |     |          |            |         |     |     |     |     |     |     |     |
signmentintheunwrappedtreeisallzeros
(18)
| Now,                            | assume | that we | can choose | a   | subtree of        | and |     |     |     |     |     |     |     |
| ------------------------------- | ------ | ------- | ---------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| changetheassignmentofthesenodes |        |         |            |     | toanothervalueand |     |     |     |     |     |     |     |     |
increasetheposterior.Again,tosimplifynotation,assumethat
| maximizing |     | value is |     | . By the | Markov property, | this |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --- | -------- | ---------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
means that
|     |     |     |     |     |     | (19) | Fig.4. Turbocodestructure. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | -------------------------- | --- | --- | --- | --- | --- | --- |
Now,bytheisomorphicsubtreepropertyweknowthatthere
| exists                                           |     | thatisisomorphicto |     | .Wealsoknowthat |     | has   |     |     |     | IV. EXAMPLES |     |     |     |
| ------------------------------------------------ | --- | ------------------ | --- | --------------- | --- | ----- | --- | --- | --- | ------------ | --- | --- | --- |
| thesameconditionalprobabilitygivenitsneighborsas |     |                    |     |                 |     | does. |     |     |     |              |     |     |     |
Thus,(19)impliesthat Claim1holdsforarbitrarytopologiesandarbitrarypotentials
(bothdiscreteandcontinuousnodes).Weillustratetheimplica-
tionsofClaim1forspecificnetworks.
(20)
incontradictionto(18).Hence,changingthevalueofasubtree
|     |     |     |     |     |     |     | A. GaussianGraphicalModels |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
fromtheconvergedvaluesofthemax-productalgorithmcannot
AGaussiangraphicalmodelisoneinwhichthejointdistribu-
increasetheposteriorprobability.
Now, assume we change the value of a single loop tionover isGaussian.WeissandFreeman[22]haveanalyzed
beliefpropagationonsuchgraphs.Oneoftheresultsgiventhere
andincreasetheposteriorprobability.Thismeansthat
canalsobeprovedusingourClaim1.
|     |     |     |     |     |     | (21) | Corollary | 1:  | For a Gaussian | graphical |     | model of arbitrary |     |
| --- | --- | --- | --- | --- | --- | ---- | --------- | --- | -------------- | --------- | --- | ------------------ | --- |
By the infinite chain property, we know that for arbitrarily topology. If belief propagation converges, then the posterior
| large |     |     |     |     |     |     | marginalmeanscalculatedusingbeliefpropagationareexact. |               |     |             |     |             |     |
| ----- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | ------------- | --- | ----------- | --- | ----------- | --- |
|       |     |     |     |     |     |     | Proof:                                                 | ForGaussians, |     | max-product | and | sum-product | are |
(22)
|     |     |     |     |     |     |     | identical. | The posterior |     | means calculated |     | by belief propaga- |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | ---------------- | --- | ------------------ | --- |
Therefore,(21)impliesthat
tionarethereforeidenticaltothemax-productassignment.By
(23)
Claim1,weknowthatthismustbeaneighborhoodmaximum
| incontradictiontotheoptimalityof |     |     |     |     | .Hence,changing |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
oftheposteriorprobability.ButGaussiansareunimodal,hence,
the value ofa single loopcannot improvethe posteriorproba- itmustbeaglobalmaximumoftheposteriorprobability.Thus,
| bilityover |     | .                     |     |            |     |     |                 |     |                     |     |     |                 |     |
| ---------- | --- | --------------------- | --- | ---------- | --- | --- | --------------- | --- | ------------------- | --- | --- | --------------- | --- |
|            |     |                       |     |            |     |     | the max-product |     | assignmentmustequal |     | the | MAP assignment, |     |
| Now        | we  | take two disconnected |     | components |     |     |                 |     |                     |     |     |                 |     |
andtheposteriormeanscalculatedusingbeliefpropagationare
| andassumethatchangingthevaluesof |     |     |     |     | improvesthe |     | exact. |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- |
posteriorprobability.Again,bytheMarkovproperty
|     |     |     |     |     |     |     | B. TurboCodes |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
(24) Fig.4showsthepairwiseMarkovnetworkcorrespondingto
butsince and arenotconnected,thisimplies thedecodingofaturbocodewithsevenunknownbits.Thetop
andbottomnodesrepresentthetwotransmittedmessages(one
|     |     |     |     |     |     |     | for each     | constituent | code). | Thus, in        | this example, | the            | top and |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ------ | --------------- | ------------- | -------------- | ------- |
|     |     |     |     |     |     |     | bottom nodes | can         | take   | on 128 possible | values.       | The potentials |         |
(25) betweenthemessagenodesandtheirobservationsgivethepos-
Thisimpliesthateither terior probability of the transmitted word given one message,
andthepotentialsbetweenthemessagenodesandthebitnodes
|     |     |     |     |     |     |     | impose consistency. |     | For | example, |     |     | if  |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | -------- | --- | --- | --- |
(26)
|     |     |     |     |     |     |     | thefirstbitof |     |     | isequalto | andzerootherwise.It |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --------- | ------------------- | --- | --- |
or
iseasytoshow[21]thatsum-productbeliefpropagationonthis
graphgivestheturbodecodingalgorithmandmax-productbe-
(27)
liefpropagationgivesthemodifiedturbodecodingalgorithmof
| Thus, | if  | or are either | a   | tree or | a single loop this | leads |     |     |     |     |     |     |     |
| ----- | --- | ------------- | --- | ------- | ------------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
[3].
toacontradiction.Hence,wecannotsimultaneouslychangethe
valuesoftwosubtreesorofasubtreeandalooporoftwodis- Corollary 2: For a turbo code with arbitrary constituent
connected loops and increase the posterior probability. Simi- codes. Let be a fixed-point max-product decoding. Then
larly,wecanshowthatchangingthevalueofanyfinitenumber forall withinHammingdistance of .
ofdisconnectedtreesorsingleloopswillnotincreasethepos- Proof: Thisfollowsfromthemainclaim.Notethatwhen-
terior.ThisprovesClaim1. everwechangeanybitsinthegraphwealsohavetochangethe
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 09:44:13 UTC from IEEE Xplore.  Restrictions apply.

742 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
| two message |     | nodes so | changing | more | than | two | bits will | give |     |     |     |     |     |     |     |
| ----------- | --- | -------- | -------- | ---- | ---- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
two loops.
| An obvious |     | consequence |     | of Corollary |     | 2 is that | for | a turbo |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | ------------ | --- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
codewitharbitraryconstituentcodes,themax-productdecoding
| is either | the MAP | decoding  |     | or at | least  | Hamming         | distance |     |     |     |     |     |     |     |     |
| --------- | ------- | --------- | --- | ----- | ------ | --------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| from the  | MAP     | decoding. | In  | other | words, | the max-product |          | al- |     |     |     |     |     |     |     |
gorithmcannotconvergetoadecodingthatis“almost”right:if
itiswrong,itmustbewronginatleastthreebits.Inorderfor
max-producttoconvergetoawrongdecoding,theremustexist
| a decoding | that     | is at | leastdistance |        | from      | the MAP     | decoding, |      |     |     |     |     |     |     |     |
| ---------- | -------- | ----- | ------------- | ------ | --------- | ----------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| and that   | decoding | must  | have          | higher | posterior | probability |           | than |     |     |     |     |     |     |     |
anythinginitsneighborhood.Ifnosuchwrongdecodingexists,
| themax-productalgorithmmusteitherconvergetotheMAPde- |     |     |     |     |     |     |     |     |     |     |     | (a) |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
codingorfailtoconvergetoafixedpoint.
| This        | behavior  | can          | be contrasted |          | with             | the | behavior      | of  |     |     |     |     |     |     |     |
| ----------- | --------- | ------------ | ------------- | -------- | ---------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| “greedy”    | iterative | decoding     |               | which    | increases        |     | the posterior |     |     |     |     |     |     |     |     |
| probability | of        | the decoding |               | at every | iteration.Greedy |     | iterative     |     |     |     |     |     |     |     |     |
decodingchecksallbitsandcomparestheposteriorprobability
withthecurrentvalueofthatbitversusflippingthatbit.Ifthe
| posterior      | probability |            | improved | with        | flipping, |     | the algorithm |         |     |     |     |     |     |     |     |
| -------------- | ----------- | ---------- | -------- | ----------- | --------- | --- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| flips it (this | is          | equivalent | to       | free energy | decoding  |     | [15]          | at zero |     |     |     |     |     |     |     |
temperature).Thisgreedydecodingalgorithmisguaranteedto
convergetoalocalmaximumoftheposteriorprobability.
| To illustrate |              | these | properties   | we  | ran           | the following |           | simu- |     |     |     |     |     |     |     |
| ------------- | ------------ | ----- | ------------ | --- | ------------- | ------------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| lations.      | We simulated |       | transmitting |     | turbo-encoded |               | codewords |       |     |     |     |     |     |     |     |
of length 7 bits over a Gaussian channel. We compared the (b)
| max-product | decoding |     | and | the greedy | decoding |     | to the | MAP |                                                                      |     |     |     |     |     |     |
| ----------- | -------- | --- | --- | ---------- | -------- | --- | ------ | --- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|             |          |     |     |            |          |     |        |     | Fig.5. Resultsofsmallturbo-codesimulation.(a)Percentcorrectdecodings |     |     |     |     |     |     |
decoding(sinceweweredealingwithsuchshortblocklengths for max-product algorithm, compared with greedy gradient ascent in the
wecouldcalculatetheMAPdecodingusingexhaustivesearch). posterior probability. (b) Comparison of convergence results of the two
| Wevariedthenoise |       |              | oftheGaussianchannel. |           |       |     |             |     | algorithms. |     |     |     |     |     |     |
| ---------------- | ----- | ------------ | --------------------- | --------- | ----- | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
| Fig. 5           | shows | the results. |                       | Fig. 5(b) | shows | the | probability | of  |             |     |     |     |     |     |     |
convergenceforbothalgorithms.Convergencewasdetermined
|     |     |     |     |     |     |     |     |     | second best. | In comparison, |     | greedy | decoding | found the | MAP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | ------ | -------- | --------- | --- |
numericallyforbothalgorithms:ifthestandarddeviationofthe assignmentonlyon44%oftheruns andthe rankingwasany-
messages over10 successive iterations was less than we wherebetween4and61.
declaredconvergence.Ifthiscriterionwasnotachievedin100
iterations,wecalledthatrunafailuretoconverge.
V. DISCUSSION
Fig.5(a)showstheprobabilityofacorrectdecoding(i.e.,a
decoding equal to the MAP decoding) for the two algorithms The idea of using the computation tree to prove properties
onthecasesforwhichbothconverged.Whenmax-productcon- ofthemax-productassignmentwasalsousedin[23],[20],[8],
verges, it always finds the MAP decoding. In contrast, greedy [11].Themaintoolinthoseanalyseswasthefactthatthemax-
decodingveryfrequentlyconvergestoawrongdecoding. productassignmentwastheglobaloptimumintheunwrapped
tree.Therearetwoproblemswithgeneralizingthisapproachto
| C. Two-Dimensional(2-D)Grids |     |     |     |     |     |     |     |     | arbitrarytopologies. |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
First,theglobaloptimumdependsonthenumerosityofnode
Fig.2(a)showsa2-Dgrid.For2-Dgrids,itiseasytoshow
|     |     |     |     |     |     |     |     |     | replicas | in the unwrapped |     | tree. That | is, different | nodes | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ---------- | ------------- | ----- | --- |
thefollowingcorollaries.
|     |     |     |     |     |     |     |     |     | may have | a different | number | of replicas | in  | . This leads | to a |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------ | ----------- | --- | ------------ | ---- |
Corollary3: For2-Dgridsofarbitrarysizeandarbitrarypo- distinction between balanced (or nonskewed) graphs [20], [8]
tentials.Anyconfigurationiseither1)intheSLTregionofthe andunbalanced(orskewed)graphs.Balancedgraphsarethose
max-product assignment or 2) in the SLT region of an assign- forwhichallnodesin haveasymptoticallythesamenumber
mentthatisintheSLTregionofthemax-productassignment. ofreplicasin .Forunbalancedgraphs,itismuchmoredifficult
|                                        |     |         |       |         |     |          |        |     | torelateglobaloptimalityin |               |     | tooptimalityin |               | .   |          |
| -------------------------------------- | --- | ------- | ----- | ------- | --- | -------- | ------ | --- | -------------------------- | ------------- | --- | -------------- | ------------- | --- | -------- |
| Corollary                              | 4:  | For 2-D | grids | of size | .   | The size | of the | SLT |                            |               |     |                |               |     |          |
|                                        |     |         |       |         |     |          |        |     | Second,the                 | globaloptimum |     | inthe          | unwrappedtree |     | contains |
| neighborhoodincreasesexponentiallywith |     |         |       |         |     | .        |        |     |                            |               |     |                |               |     |          |
contributionsfromtheinteriornodes(thathaveexactlythesame
Bothcorollariesfollowfromthefactthatwecanchangethe neighborsin asdotheircorrespondingnodesin )andcontri-
valueofalltheeven(orodd)rowstoanarbitraryvalue. butionsfromtheleafnodes(thataremissingsomeoftheneigh-
Wecomparedgreedydecodingtomax-productdecodingon borsin ).Unfortunately,formostgraphs ,thenumberofleaf
the grid.Max-productfoundtheMAPdecodingin99%of nodesgrowsatthesamerateasthenonleafnodesandcannotbe
therunsandwhenitwaswrong,itsassignmentwasalwaysthe neglectedfromtheanalysis.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 09:44:13 UTC from IEEE Xplore.  Restrictions apply.

WEISSANDFREEMAN:SOLUTIONSOFTHEMAX-PRODUCTBELIEF-PROPAGATIONALGORITHM 743
|     |     |     |     |     |     |     | • findall                    | ofdegree        |                   | .Foreachsuch              |          | removeitfromthe   |                |          |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --------------- | ----------------- | ------------------------- | -------- | ----------------- | -------------- | -------- |
|     |     |     |     |     |     |     | graph                        | and directly    |                   | connect                   | the two  | variables         | nodes          | that     |
|     |     |     |     |     |     |     | were                         | connected       | to                | those function            |          | nodes.            | That is,       | if is    |
|     |     |     |     |     |     |     | adegree–                     | nodeconnectedto |                   |                           |          | wedirectlyconnect |                |          |
|     |     |     |     |     |     |     | and                          | andset          |                   |                           |          |                   | .              |          |
|     |     |     |     |     |     |     | • forall                     | ofdegree        |                   | ,replacethenode           |          |                   | withanew       |          |
|     |     |     |     |     |     |     | variable                     | node            |                   | . The                     | variable | node              | represents     |          |
|     |     |     |     |     |     |     | the joint                    | configuration   |                   | of                        | all the  | that              | were connected |          |
|     |     |     |     |     |     |     | to                           | . That          | is, if            | is connected              |          | to                |                | then the |
|     |     |     |     |     |     |     | new                          | variable        | isa               | vectorwiththreecomponents |          |                   |                |          |
|     |     |     | (a) |     |     |     |                              |                 | .Setthepotentials |                           |          |                   |                |          |
|     |     |     |     |     |     |     | Finally,addanobservationnode |                 |                   |                           |          | andset            |                |          |
Itiseasytoshowthat1)thejointdistributionoverthevari-
|     |     |     |     |     |     |     | ables | in  | the pairwise |     | Markov | graph | is exactly |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------------ | --- | ------ | ----- | ---------- | --- |
and2)thebeliefpropagationalgorithminthepairwiseMarkov
graphisequivalenttothebeliefpropagationalgorithmin[7].
B. ConvertingaJunctionGraphtoaPairwiseMarkovGraph
(b)
|     |     |     |     |     |     |     | Ajunctiongraph[1]isagraphinwhichvertices |     |     |     |     |     |     | represent |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --------- |
Fig. 6. Any factor graph can be converted into an MRF with pairwise “localdomains”ofaglobalfunction.Thus,if fac-
| potentials                                                          | that represents | exactly                            | the | same probability |     | distribution over |                           |     |     |     |     |     |     |      |
| ------------------------------------------------------------------- | --------------- | ---------------------------------- | --- | ---------------- | --- | ----------------- | ------------------------- | --- | --- | --- | --- | --- | --- | ---- |
| variables.Whenthisconversionisdone,thebeliefpropagationalgorithmfor |                 |                                    |     |                  |     |                   | torizessothat             |     |     |     |     |     |     |      |
| thepairwiseMarkovgraph                                              |                 | isequivalenttothebeliefpropagation |     |                  |     | algorithm         |                           |     |     |     |     |     |     |      |
| onthefactorgraph.                                                   |                 |                                    |     |                  |     |                   |                           |     |     |     |     |     |     | (28) |
|                                                                     |                 |                                    |     |                  |     |                   | thenthetwolocaldomainsare |     |     |     |     | and |     |      |
Inthisanalysis,ontheotherhand,weusedprimarilythelocal
|     |     |     |     |     |     |     | Edges between | these | vertices | correspond |     | to “communication |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | -------- | ---------- | --- | ----------------- | --- | --- |
propertiesofthecomputationtree.Nomatterwhatthetopology
|                                                |           |           |     |         |                |        | links” in a | message-passing |     | scheme | for | calculating | marginals |     |
| ---------------------------------------------- | --------- | --------- | --- | ------- | -------------- | ------ | ----------- | --------------- | --- | ------ | --- | ----------- | --------- | --- |
| of is,itisalwaysthecasethatthelocalstructureof |           |           |     |         |                | isthe  | of .        |                 |     |        |     |             |           |     |
| same as                                        | the local | structure | of  | . Thus, | the numerosity | of the |             |                 |     |        |     |             |           |     |
Ajietal.showedthatforsuchamessage-passingalgorithm
nodesin andtheratioofleafnodestononleafnodesisirrel- toexist,thejunctiongraphmustpossessthe“runningintersec-
evant.Inthisway,wecananalyzethemax-productassignment
tionproperty”—thesubsetofnodeswhosedomainsinclude
inarbitrarytopologies.
togetherwiththeedgescontainingthesenodesmustformacon-
Although we exploited the local properties, we would like nectedgraph.Wenowshowthatjunctiongraphsareequivalent
toextendouranalysisusingtheglobalpropertiesaswell.Our
topairwiseMarkovgraphs.
simulation results indicate that the max-product assignment is Toshowthis,weleavethegraphbetween unchangedand
betterthanouranalyticalresultsguarantee.Forexample,inthe
|                       |     |                |     |     |                      |     | add “observation” |     | nodes  | such      | that  |        |       | . We   |
| --------------------- | --- | -------------- | --- | --- | -------------------- | --- | ----------------- | --- | ------ | --------- | ----- | ------ | ----- | ------ |
| turbo-codesimulations |     | wefoundthatthe |     |     | posteriorprobability |     |                   |     |        |           |       |        |       |        |
|                       |     |                |     |     |                      |     | set               |     | if the | two nodes | agree | on the | value | of any |
oftencontainedtwoSLTmaximabutforallthesecases,max- thatexistsinbothdomainsandzerootherwise.Notethatthe
| product | found the | global | maximum | (and | not | the second SLT |     |     |     |     |     |     |     |     |
| ------- | --------- | ------ | ------- | ---- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
runningintersectionpropertyguaranteesthatanytwonodes(not
maximum).Incurrentwork,wearelookingintousingtheglobal necessarilyneighboring)mustagreeonthevalueofacommon
propertiesofthecomputationtreetoextendouranalysis.
forthejointdistributiontobenonzero.Whenthepotentials
|     |     |     |          |     |     |     | are set in                             | this way, | it is | easy to | see that | the joint | distribution |     |
| --- | --- | --- | -------- | --- | --- | --- | -------------------------------------- | --------- | ----- | ------- | -------- | --------- | ------------ | --- |
|     |     |     | APPENDIX |     |     |     | over inthepairwiseMarkovgraphisexactly |           |       |         |          |           | andthatthe   |     |
RELATIONSHIPBETWEENBELIEF-PROPAGATIONSCHEMES
beliefpropagationalgorithmintheMarkovgraphisequivalent
totheGDLalgorithmin[1].
A. ConvertingaFactorGraphtoaPairwiseMarkovGraph
Afactorgraph[7]isabipartitegraph(seeFig.6)withfunc-
REFERENCES
| tion nodes | denoted | by  | filled squares |     | and variable | nodes |     |     |     |     |     |     |     |     |
| ---------- | ------- | --- | -------------- | --- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
[1] S.M.AjiandR.J.McEliece,“Thegeneralizeddistributivelaw,”IEEE
denotedbyunfilledcircles.Thefunctionnodesdenoteadecom-
Trans.Inform.Theory,vol.46,pp.325–343,Mar.2000.
| position | of a “global” | function |     | into | a product | of “local” |     |     |     |     |     |     |     |     |
| -------- | ------------- | -------- | --- | ---- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
[2] S.M.Aji,G.B.Horn,andR.J.McEliece,“Ontheconvergenceofiter-
| functions | . We | will | assume | that | represents | a joint dis- |     |     |     |     |     |     |     |     |
| --------- | ---- | ---- | ------ | ---- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
ativedecodingongraphswithasinglecycle,”inProc.1998IEEEInt.
tribution over the variable nodes. The method of converting a Symp.InformationTheory,Cambridge,MA,Aug.1998,p.276.
[3] S.Benedetto,G.Montorsi,D.Divsalar,andF.Pollara,“Soft-outputde-
factorgraphintoapairwiseMarkovgraphistoremovethefunc-
codingalgorithmsiniterativedecodingofturbocodes,”JetPropulsion
tionnodes.Specifically Lab.,Pasadena,CA,Tech.Rep.42-124,JPLTDA,1996.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 09:44:13 UTC from IEEE Xplore.  Restrictions apply.

744 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
[4] D.P.Bertsekas,DynamicProgramming:DeterministicandStochastic [14] S.Lauritzen,GraphicalModels. Oxford,U.K.:OxfordUniv.Press,
Models. EnglewoodCliffs,NJ:Prentice-Hall,1987. 1996.
[5] G.D.Forney,F.R.Kschischang,andB.Marcus,“Iterativedecodingof [15] D.J.C.MacKay,“Gooderror-correctingcodesbasedonverysparse
tail-bitingtrellisses,”presentedatthe1998InformationTheoryWork- matrices,”IEEETrans.Inform.Theory,vol.45,pp.399–431,Mar.1999.
shop,SanDiego,CA,1998. [16] J.R.Munkres,Topology:AFirstCourse. EnglewoodCliffs,NJ:Pren-
[6] W.T.Freeman,E.C.Pasztor,andO.T.Carmichael,“Learningtoes- tice-Hall,1975.
timatescenesfromimages,”Int.J.Comput.Vision,vol.40,pp.25–47, [17] K.P.Murphy,Y.Weiss,andM.I.Jordan,“Loopybeliefpropagation
Nov.2000. forapproximateinference:Anempiricalstudy,”inProc.Uncertaintyin
[7] B.J.Frey,R.Koetter,andA.Vardy,“Skewnessandpseudocodewordsin ArtificialInrwlligence,1999.
iterativedecoding,”inProc.1998IEEEInt.Symp.InformationTheory, [18] J. Pearl, Probabilistic Reasoning in Intelligent Systems: Networks of
Cambridge,MA,Aug.1998,p.148. PlausibleInference. SanFrancisco,CA:MorganKaufmann,1988.
[8] ,“Signalspacecharacterizationofiterativedecoding,”IEEETrans. [19] S.E.Shimony,“FindingtheMAPsforbeliefnetworksisNP-hard,”Ar-
Inform.Theory,vol.47,pp.766–781,Feb.2001. tificialIntell.,vol.68,no.2,pp.399–410,1994.
[9] R.G.Gallager,LowDensityParityCheckCodes. Cambridge,MA: [20] Y.Weiss,“Beliefpropagationandrevisioninnetworkswithloops,”MIT
MITPress,1963. AILab.,Tech.Rep.1616,1997.
[10] S.GemanandD.Geman,“Stochasticrelaxation,Gibbsdistributions, [21] ,“Correctnessoflocalprobabilitypropagationingraphicalmodels
andtheBayesianrestorationofimages,”IEEETrans.PatternAnal.Ma- withloops,”NeuralComput.,vol.12,pp.1–42,2000.
chineIntell,vol.PAMI-6,pp.721–741,Nov.1984. [22] Y. Weiss and W. Freeman, “Correctness of belief propagation in
[11] G.B.Horn,“Iterativedecodingandpseudocodewords,”Ph.D.disserta- Gaussiangraphicalmodelsofarbitrarytopology,”NeuralComp.,tobe
tion,Dept.Elec.Eng.,Calif.Inst.Technol.,Pasadena,CA,May1999. published.
[12] F.V.Jensen,AnIntroductiontoBayesianNetworks. Berlin,Germany: [23] N.Wiberg,“Codesanddecodingongeneralgraphs,”Ph.D.dissertation,
Springer-Verlag,1996. Dept.Elec.Eng.,Univ.Linköping,Linköping,Sweden,1996.
[13] F.R.Kschischang,B.J.Frey,andH.A.Loeliger,“Factorgraphsand
thesum-productalgorithm,”IEEETrans.Inform.Theory,vol.47,pp.
498–519,Feb.2001.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 25,2025 at 09:44:13 UTC from IEEE Xplore. Restrictions apply.