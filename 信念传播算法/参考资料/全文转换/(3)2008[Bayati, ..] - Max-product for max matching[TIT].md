IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.54,NO.3,MARCH2008 1241
Max-Product for Maximum Weight Matching:
Convergence, Correctness, and LP Duality
MohsenBayati, Devavrat Shah, and MayankSharma
Abstract—Max-product “belief propagation” (BP) is an itera- posteriori (MAP) probabilities, respectively. In general, cal-
tive,message-passingalgorithmforfindingthemaximumaposte- culating the marginal or MAP probabilities for an ensemble
riori(MAP)assignmentofadiscreteprobabilitydistributionspec-
of random variables would require a complete specification
ifiedbyagraphicalmodel.Despitethespectacularsuccessofthe
of the joint probability distribution. Further, the complexity
algorithminmanyapplicationareassuchasiterativedecodingand
combinatorialoptimization,whichinvolvegraphswithmanycy- of a brute-force calculation would be exponential in the size
cles,theoreticalresultsaboutboththecorrectnessandconvergence of the ensemble. GMs assist in exploiting the dependency
ofthealgorithmareknowninonlyafewcases(seeSectionIforref- structurebetweentherandomvariables,allowingforthedesign
erences).
ofefficientalgorithms.
Inthispaper,wewillprovethecorrectnessandconvergenceof
Thebeliefpropagation(BP)andmax-productalgorithms[16]
max-productforfindingthemaximumweightmatching(MWM)
in bipartite graphs. Even though the underlying graph of the were proposed in order to compute, respectively, the marginal
MWMproblemhasmanycycles,somewhatsurprisinglyweshow and MAP probabilities efficiently. Comprehensive surveys of
thatthemax-productalgorithmconvergestothecorrectMWMas
variousformulationsofBPanditsgeneralization,thejunction
longastheMWMisunique.Weprovideaboundonthenumber
of iterations required and show that for a graph of size n, the tree algorithm, can be found in [2], [24], [18]. BP-based mes-
computationalcostofthealgorithmscalesasO(n3 ),whichisthe sage-passing algorithmshavebeen verysuccessfulin the con-
sameasthecomputationalcostofthebestknownalgorithmsfor text of, for example, iterative decoding for turbo codes, com-
findingtheMWM. putervision,andfindingsatisfyingassignmentsforrandomsat-
Wealsoprovideaninterestingrelationbetweenthedynamicsof
isfiabilityproblems.Thesimplicity,widescopeofapplication,
themax-productalgorithmandtheauctionalgorithm,whichisa
andexperimentalsuccessofBPhasattractedalotofattention
well-knowndistributedalgorithmforsolvingtheMWMproblem.
recently[2],[11],[15],[17],[25].
Index Terms—Auction algorithm, belief propagation (BP),
BP(ormax-product)isknowntoconvergetothecorrectmar-
distributed optimization, linear programming, Markov random
ginal(orMAP)probabilitiesongraphswithnocycles[16].For
fields, maximum weight matching (MWM), max-product algo-
rithm,message-passingalgorithms,min-sumalgorithm. graphswithasinglecycle,theconvergenceandcorrectnessof
BP are rigorously analyzed in [1], [20]. For GMs with arbi-
trary underlying graphs, little is known about the correctness
I. INTRODUCTION of BP. Partial progress consists of: the correctness of BP for
Gaussian GMs was provedin [22],an attenuated modification
GRAPHICAL models (GMs) are a powerful method for ofBPisshowntowork[10],theiterativeturbodecodingalgo-
representing and manipulating joint probability distribu- rithm basedonBPis shownto workinthe asymptotic regime
tions. They have found major applications in several different with probabilistic guarantees in [17], and fixed points of BP
research communities such as artificial intelligence [16], sta- areshowntobelocallyoptimalin[23],[9].Tothebestofour
tistics [12], error-correcting codes [8], [11], [17], and neural knowledge, limited theoretical progress has been made in un-
networks.Twocentralproblemsinprobabilisticinferenceover derstandingwhenBPworksongraphswithcycles?
GMs are those of evaluating the marginal and maximum a Motivated by the objective of providing justification for the
successofBPonarbitrarygraphs,wefocusontheapplication
ofBPtothewell-knowncombinatorialoptimizationproblemof
ManuscriptreceivedNovember30,2005;revisedAugust8,2007.Thework
ofD.ShahwassupportedbytheNationalScienceFoundationunderCAREER finding the maximum weight matching (MWM) in a bipartite
GrantCNS-0546590.ThematerialinthispaperwaspresentedattheIEEEIn- graph,alsoknownasthe“AssignmentProblem.”Itisstandard
ternationalSymposiumonInformationTheory,Adelaide,Australia,September
to represent combinatorial optimization problems, like finding
2005.ThisworkwasperformedwhileM.BayatiwaswiththeDepartmentof
ElectricalEngineering,StanfordUniversity,Stanford,CA. theMWM,ascalculatingtheMAPprobabilityonasuitablyde-
M.BayatiiswithMicrosoftResearch,Redmond,WA98052USA(e-mail: fined GM which encodes the data and constraints of the op-
mohsenb@microsoft.com).
timization problem. Thus, the max-product algorithm can be
D. Shah is with the Department of Electrical Engineering and Computer
Science,MassachusettsInstituteofTechnology,Cambridge,MA02139USA viewed at least as a heuristic for solving the problem. In this
(e-mail:devavrat@mit.edu). paper,westudytheperformanceofthemax-productalgorithm
M.SharmaiswiththeIBMT.J.WatsonResearchCenter,YorktownHeights,
asamethodforfindingtheMWMonaweightedcompletebi-
NY10598USA(e-mail:mxsharma@us.ibm.com).
CommunicatedbyP.L.Bartlett,AssociateEditorforPatternRecognition, partitegraph.
StatisticalLearningandInference. Additionally,usingthemax-productalgorithmforproblems
ColorversionofFigure2inthispaperareavailableonlineathttp://ieeexplore.
like finding the MWM has the potential of being an exciting
ieee.org.
DigitalObjectIdentifier10.1109/TIT.2007.915695 application of BP in its own right. The assignment problem is
0018-9448/$25.00©2008IEEE
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on April 17,2025 at 00:40:37 UTC from IEEE Xplore. Restrictions apply.

1242 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.54,NO.3,MARCH2008
extremelywellstudiedalgorithmically.Attemptstofindbetter auction algorithm. The auction algorithm solves the dual of a
MWM algorithms contributed to the development of the rich linearprogramming(LP)relaxationfortheMWMproblem.Our
theory of network flow algorithms [9], [13]. The assignment result suggests the possibility of a deeper connection between
problem has been studied in various contexts such as job as- max-productanddualalgorithmsforoptimizationproblems.Fi-
signmentinmanufacturingsystems[9],switchschedulingalgo- nally,wediscusssomeimplicationsofourresultsinSectionVI.
| rithms[14],andauctionalgorithms[7].Recently, |     |     |     |     |     | weusedthe |     |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
max-productalgorithmeffectivelyinhigh-speedswitchsched- II. SETUPANDPROBLEMSTATEMENT
ulingandwirelessschedulingwherethedistributednatureofthe
|     |     |     |     |     |     |     |     | In this | section, we | first define | the problem | of  | finding | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ------------ | ----------- | --- | ------- | --- |
algorithmanditssimplicityareveryattractiveforimplementa-
MWMinaweightedcompletebipartitegraphandthendescribe
tionpurposes[5].
themax-productalgorithmforsolvingit.
A. OurResults
|     |     |     |     |     |     |     |     | A. MaximumWeightMatching |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
Themainresultofthispaperistoshowthatthemax-product Consider an undirected weighted complete bipartite
|     |     |     |     |     |     |     |     | graph |     |     | , where |     |     | ,   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ------- | --- | --- | --- |
algorithmforMWMalwaysfindsthecorrectsolution,aslong
asthesolutionisunique.Ourproofispurelycombinatorialand , and for , . Let
usesonlybipartitenatureofthegraph.Wethinkthatthisresult eachedge haveweight .
and in particular our methods may lead to further insights in If is a permutation of
understandinghowBPalgorithmsworkwhenappliedtoamore then the collection of edges
iscalledamatchingof
generalclassofoptimizationproblems. .Wedenoteboththe permutation
We show that the complexity of this algorithm scales as andthecorrespondingmatchingby .Theweightofmatching
|         |        |                      |        |     |         |                 |      | ,denotedby | ,isdefinedas |     |     |     |     |     |
| ------- | ------ | -------------------- | ------ | --- | ------- | --------------- | ---- | ---------- | ------------ | --- | --- | --- | --- | --- |
|         | ,where | isthesizeofthegraph, |        |     |         | isthedifference |      |            |              |     |     |     |     |     |
| between | weight | of the               | unique | MWM | and the | second          | MWM, |            |              |     |     |     |     |     |
and isthemaximalvalueofedgeweight.Thus,therunning
| time of max-product |         | for     | MWM     | is essentially |           | the same  | as the   |             |                       |     |     |     |     |     |
| ------------------- | ------- | ------- | ------- | -------------- | --------- | --------- | -------- | ----------- | --------------------- | --- | --- | --- | --- | --- |
| running time        | of both | the     | best    | centralized    | algorithm | (assuming |          |             |                       |     |     |     |     |     |
|                     |         |         |         |                |           |           |          | Then,theMWM | isthematchingsuchthat |     |     |     |     |     |
| , constant),        |         | and the | auction | algorithm      | proposed  |           | by Bert- |             |                       |     |     |     |     |     |
sekas.
Somewhatinterestingly,wefindthatthedynamicsoftheauc-
tionalgorithmandthemax-productalgorithmareessentiallythe
Note1.Inthispaper,wealwaysassumethattheweightsare
| same and  | this observation |     | leads   | to a precise |      | relation     | between |           |                  |            |                |            |         |      |
| --------- | ---------------- | --- | ------- | ------------ | ---- | ------------ | ------- | --------- | ---------------- | ---------- | -------------- | ---------- | ------- | ---- |
|           |                  |     |         |              |      |              |         | such that | the MWM is       | unique.    | In particular, | if the     | weights | of   |
| these two | algorithms.      | The | auction | algorithm    | with | a relaxation |         |           |                  |            |                |            |         |      |
|           |                  |     |         |              |      |              |         | the edges | are independent, | continuous | random         | variables, |         | then |
methodcanfindtheMWM(aswellasagoodapproximateso-
|     |     |     |     |     |     |     |     | with probability | , the | MWM | is unique. | Otherwise, | one | may |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ----- | --- | ---------- | ---------- | --- | --- |
lution)evenintheabsenceofauniquesolution.Theabovecon-
|     |     |     |     |     |     |     |     | make the | MWM unique | by adding | sufficiently | small | indepen- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --------- | ------------ | ----- | -------- | --- |
nectionbetweenauctionandmax-productsuggestsamodified
dentrandomnoisetoeachoftheedgeweights.
| version of | the max-product |     | algorithm. |     | We show | that | the fixed |     |     |     |     |     |     |     |
| ---------- | --------------- | --- | ---------- | --- | ------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
point of this modified max-product algorithm coincides with Next, we model the problem of finding MWM as finding
a good approximate solution and can lead to an MWM when a MAP assignment in a GM where the joint probability dis-
theparametersarechosenproperly.Ingeneral,thissuggestsa tribution can be completely specified in terms of the product
methodtoobtaina(deterministic)modificationofmax-product of functions that depend on at most two variables (nodes).
|     |     |     |     |     |     |     |     | For details | about GMs, | we urge | the reader | to see | [12]. | Now, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------- | ---------- | ------ | ----- | ---- |
whichcanconvergetoagoodapproximatesolutionevenwhen
theproblemhasmultiplesolutions.Webelievethatthisheuristic considerthefollowingGMdefinedon :Let ,
berandomvariablescorrespondingtotheverticesof
shouldalsobeofinterestforotheroptimizationproblems.
|     |     |     |     |     |     |     |     | andtakingvaluesfrom   |     |     |     | .Lettheirjointprob- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | ------------------- | --- | --- |
|     |     |     |     |     |     |     |     | ability distribution, |     |     |     |                     |     | ,   |
B. Organization
beoftheform
| The rest                                           | of the | paper | is organized | as  | follows. | In Section | II, |     |     |     |     |     |     |     |
| -------------------------------------------------- | ------ | ----- | ------------ | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| weprovidethesetup,definetheMWMproblem(orassignment |        |       |              |     |          |            |     |     |     |     |     |     |     | (1) |
problem)anddescribeaversionofthemax-productalgorithm
(orthemin-sumalgorithm)forfindingtheMWM.Inthispaper,
we will use the term max-product and min-sum interchange- where the pairwise compatibility functions are defined
as
ablyforthesamealgorithm.Essentially,themin-sumalgorithm
| isobtainedfromthemax-productalgorithmbyreplacingeach |     |     |     |     |     |     |     |     |     |     | and |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
variablewithitslogarithm.
and
SectionIIIstatesandprovesthemainresultofthispaper.Sec- otherwise,
tionIVpresentsasimplificationofthemax-productalgorithm
|               |     |               |     |       |         |             |     | thepotentialsatthenodes |     |     | aredefinedas |     |     |     |
| ------------- | --- | ------------- | --- | ----- | ------- | ----------- | --- | ----------------------- | --- | --- | ------------ | --- | --- | --- |
| and evaluates | its | computational |     | cost. | Section | V discusses | the |                         |     |     |              |     |     |     |
relationbetweenthemax-productalgorithmandthecelebrated
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on April 17,2025 at 00:40:37 UTC from IEEE Xplore.  Restrictions apply.

| BAYATIetal.:MAX-PRODUCTFORMAXIMUMWEIGHTMATCHING |     |     |     |     |     |     |     |     |     |     |     | 1243 |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
and isthenormalizationconstant.Wenotethatthepairwise theGMdefinedabove.Themax-productversionanditsequiva-
potential ensures that the following two constraints are satis- lencetomin-sumalgorithmaregivenin[3].Now,themin-sum
fied for any with positive probability: a) If node is algorithmisdescribedasfollows.
| matchedtonode |     |     | (i.e., | ),thennode |     | mustbematch |     |     |     |     |     |     |
| ------------- | --- | --- | ------ | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Min-sumalgorithm.
| to node     | (i.e., |           | ). b)           | If node     | is         | not matched  | to      |         |     |     |     |     |
| ----------- | ------ | --------- | --------------- | ----------- | ---------- | ------------ | ------- | ------- | --- | --- | --- | --- |
| (i.e.,      |        | ), then   | node            | must not    | be matched |              | to node |         |     |     |     |     |
| (i.e.,      |        | ). These  | two constraints |             | encode     | the property | that    | (1) Let |     |     |     |     |
| the support | of     | the above | defined         | probability |            | distribution | is re-  |         |     |     |     |     |
strictedtomatchings.
| Claim | 1:  | For the | GM as | defined | above,             | the joint | density |                             |     |     |     |       |
| ----- | --- | ------- | ----- | ------- | ------------------ | --------- | ------- | --------------------------- | --- | --- | --- | ----- |
|       |     |         |       |         | isnonzeroifandonly |           |         | denotethemessagespassedfrom |     |     | to  | inthe |
if
|          |            |     |     |     |     |            |      | iteration                    | ,for                           | ,   | .Similarly, |       |
| -------- | ---------- | --- | --- | --- | --- | ---------- | ---- | ---------------------------- | ------------------------------ | --- | ----------- | ----- |
|          |            |     |     |     |     |            |      | isthemessagevectorpassedfrom |                                |     | to          | inthe |
| and      |            |     |     |     |     |            |      | iteration                    | .                              |     |             |       |
|          |            |     |     |     |     |            |      | (2) Initially                | andsetthemessagesasfollows.Let |     |             |       |
| are both | matchings, |     | and |     |     | . Further, | when |                              |                                |     |             |       |
and
| nonzero,theyareequalto                               |     |     |        |             | .   |     |           |       |     |     |     |     |
| ---------------------------------------------------- | --- | --- | ------ | ----------- | --- | --- | --------- | ----- | --- | --- | --- | --- |
| When,                                                |     |     | , then | the product | of  | ’s  | makes the |       |     |     |     |     |
| probabilityamonotonefunctionofthesumoftheedgeweights |     |     |        |             |     |     |           | where |     |     |     |     |
thatarepartofthecorrespondingmatching.Formally,westate
if
| thefollowingclaim. |     |     |     |     |     |     |     |     |     |     |     | (2) |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
otherwise
if
| Claim2: | Let |     | besuchthat |     |     |     |     |     |     |     |     |     |
| ------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(3)
otherwise.
|       |                   |     |     |     |     |        |        | (3) For             | ,messagesiniteration |                       | areobtainedfrom |     |
| ----- | ----------------- | --- | --- | --- | --- | ------ | ------ | ------------------- | -------------------- | --------------------- | --------------- | --- |
|       |                   |     |     |     |     |        |        | messagesofiteration |                      | recursivelyasfollows: |                 |     |
|       |                   |     |     |     |     |        |        | forall              | , ,andall            | ,                     |                 |     |
| Then, | the corresponding |     |     |     |     | is the | MWM in |                     |                      |                       |                 |     |
.
| Claim   | 2 implies |            | that finding | the    | MWM        | is equivalent | to    |     |     |     |     |     |
| ------- | --------- | ---------- | ------------ | ------ | ---------- | ------------- | ----- | --- | --- | --- | --- | --- |
| finding | the MAP   | assignment |              | on the | GM defined | above.        | Thus, |     |     |     |     |     |
thestandardmax-productalgorithmcanbeusedasaniterative
| strategy                                           | for    | finding                             | the MWM. | In     | fact, | we show    | that this |                       |     |                 |     |     |
| -------------------------------------------------- | ------ | ----------------------------------- | -------- | ------ | ----- | ---------- | --------- | --------------------- | --- | --------------- | --- | --- |
| strategy                                           | yields | the correct                         | answer.  | Before |       | proceeding | further,  |                       |     |                 |     |     |
| weprovideanillustrativeexampleoftheabovedefinedGM. |        |                                     |          |        |       |            |           |                       |     |                 |     | (4) |
|                                                    |        |                                     |          |        |       |            |           | (4) Definethebeliefs( |     | vectors)atnodes |     | and |
| Example1:                                          |        | Consideracompletebipartitegraphwith |          |        |       |            | .         |                       |     |                 |     |     |
The random variables , correspond to the index , , ,initeration asfollows:
| of the  | node       | to which  |          | is connected | under      | the        | GM. Sim- |     |     |     |     |     |
| ------- | ---------- | --------- | -------- | ------------ | ---------- | ---------- | -------- | --- | --- | --- | --- | --- |
| ilarly, | the random | variables |          | ,            |            | correspond | to the   |     |     |     |     |     |
| index   | of the     | node      | to which | is           | connected. | For        | example, |     |     |     |     |     |
(5)
|           | means    | that |              | is connected | to  | . The        | pairwise  |                                         |     |     |     |      |
| --------- | -------- | ---- | ------------ | ------------ | --- | ------------ | --------- | --------------------------------------- | --- | --- | --- | ---- |
| potential | function |      | encodes      | the matching |     | constraints. | For       |                                         |     |     |     |      |
|           |          |      |              |              |     |              |           | (5) Theestimated1MWMattheendofiteration |     |     |     | is   |
| example,  |          |      |              |              |     | corresponds  | to the    |                                         |     |     |     |      |
|           |          |      |              |              |     |              |           | ,where                                  |     |     |     | ,for |
| matching  | where    |      | is connected | to           | and | is           | connected |                                         |     |     |     |      |
.
| to .       | This is | encoded | (and     | allowed) | by         | : in this    | example,    |                       |     |            |     |     |
| ---------- | ------- | ------- | -------- | -------- | ---------- | ------------ | ----------- | --------------------- | --- | ---------- | --- | --- |
|            |         |         |          |          |            |              |             | (6) Repeat(3)–(5)till |     | converges. |     |     |
|            |         |         |          |          | , etc.     | On the       | other hand, |                       |     |            |     |     |
|            |         |         |          | is not   | a matching |              | as con-     |                       |     |            |     |     |
| nects to   | while   |         | connects | to       | . This     | is imposed   | by the      |                       |     |            |     |     |
| following: |         |         |          |          |            | .Werecommend |             |                       |     |            |     |     |
III. MAINRESULT
| that the | reader | study | this example | in  | further | detail | in order to |     |     |     |     |     |
| -------- | ------ | ----- | ------------ | --- | ------- | ------ | ----------- | --- | --- | --- | --- | --- |
gainfamiliaritywiththeabovedefinedGM.
NowwestateandproveTheorem1,whichisthemaincon-
tributionofthispaper.Beforeproceedingfurther,weneedthe
B. Min-SumAlgorithmfor
followingdefinitions.
Themax-productandmin-sumalgorithmscanbeseentobe 1Notethat,asdefined,(cid:25)
neednotbeamatching.Theorem1showsthatfor
equivalent.Inthispaper,wewilllookatthemin-sumversionfor largeenoughk,(cid:25) isamatchingandcorrespondstotheMWM.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on April 17,2025 at 00:40:37 UTC from IEEE Xplore.  Restrictions apply.

1244 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.54,NO.3,MARCH2008
|        | Whenn | =   | 3(a)isT | and(b)isT |     |     |     |     |     |     |     |     |     |     |
| ------ | ----- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fig.1. |       |     |         |           | .   |     |     |     |     |     |     |     |     |     |
Definition1: Let bethedifferencebetweentheweightsof A collection of edges in the computation tree is called a
theMWMandthesecondMWM;i.e., -matchingifnotwoedgesof areadjacentinthetree( isa
matchinginthecomputationtree)andeachnon-leafnodeisthe
|                             |     |     |     |     |     |              |     |     | endpointofexactlyoneedgefrom |       |               | .Let        | betheweight      |        |
| --------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | ---------------------------- | ----- | ------------- | ----------- | ---------------- | ------ |
|                             |     |     |     |     |     |              |     |     | ofamaximumweight             |       |               | -matchingin | whichusestheedge |        |
| DuetotheuniquenessoftheMWM, |     |     |     |     |     | .Also,define |     |     | attheroot.                   |       |               |             |                  |        |
|                             |     |     |     |     |     |              |     |     | Now, we                      | state | two important | lemmas      | that will lead   | to the |
.
proofofTheorem1.Thefirstlemmapresentsanimportantchar-
|     | Theorem1: |     | Foranyweightedcompletebipartitegraph |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
acterizationofthemin-sumalgorithmwhilethesecondlemma
| with | unique  | MWM, | the max-product      |     | or  | min-sum    | algorithm |        |                |         |        |           |                    |     |
| ---- | ------- | ---- | -------------------- | --- | --- | ---------- | --------- | ------ | -------------- | ------- | ------ | --------- | ------------------ | --- |
|      |         |      |                      |     |     |            |           |        | relates the    | maximum | weight | -matching | of the computation |     |
| when | applied |      | to the corresponding |     | GM  | as defined |           | above, |                |         |        |           |                    |     |
|      |         |      |                      |     |     |            |           |        | treetotheMWMin |         |        | .         |                    |     |
convergestothecorrectMAPassignmentortheMWMwithin
iterations. Lemma 1: At the end of the th iteration of the min-sum
|     |     |     |     |     |     |     |     |     | algorithm, | the belief | at  | node of | is precisely |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ------- | ------------ | --- |
A. ProofofTheorem1
.
|     | We first | present | some useful | notation |     | and definitions. |     | Con- |       |     |     |     |     |     |
| --- | -------- | ------- | ----------- | -------- | --- | ---------------- | --- | ---- | ----- | --- | --- | --- | --- | --- |
|     |          |         |             |          |     |                  |     |      | Lemma | 2:  |     |     |     |     |
sider , . Let be the level- unrolled tree If is the MWM of graph then for
| correspondingto        |     |     | ,definedasfollows: |                               |     | isaweightedreg- |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | ------------------ | ----------------------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ularrootedtreeofheight |     |     |                    | witheverynon-leafhavingdegree |     |                 |     |     |     |     |     |     |     |     |
.Allnodeshavelabelsfromtheset
| according |          | tothe    | following | recursive | rule: | a)the  | root has | label |              |       |         |             |                  |     |
| --------- | -------- | -------- | --------- | --------- | ----- | ------ | -------- | ----- | ------------ | ----- | ------- | ----------- | ---------------- | --- |
|           |          |          |           |           |       |        |          |       | That is, for | large | enough, | the maximum | weight -matching |     |
|           | ; b) the | children | of        | the root  | have  | labels |          | ;     |              |       |         |             |                  |     |
and c) the children of each non-leaf node whose parent has in choosestheedge attheroot.
| label |     | (or | ) have labels |     |     |     |     | (or |          |         |     |              |                    |     |
| ----- | --- | --- | ------------- | --- | --- | --- | --- | --- | -------- | ------- | --- | ------------ | ------------------ | --- |
|       |     |     |               |     |     |     |     |     | Proof of | Theorem | 1:  | Consider the | min-sum algorithm. | Let |
).Theedgebetweennodeslabeled
|                        |         |          |                 |        |                     |             |     |         |     |     |     | .Recall that |                 | where  |
| ---------------------- | ------- | -------- | --------------- | ------ | ------------------- | ----------- | --- | ------- | --- | --- | --- | ------------ | --------------- | ------ |
|                        | in      | the tree | is assigned     | weight |                     | for         | ,   | .       |     |     |     |              |                 |        |
|                        |         |          |                 |        |                     |             |     |         |     |     |     | . Then,      | by Lemmas 1 and | 2, for |
| Examplesofsuchatreefor |         |          |                 |        | areshownintheFig.1. |             |     |         |     |     |     |              |                 |        |
|                        |         |          |                 |        |                     |             |     |         |     | ,   | .   |              |                 |        |
|                        | Note 2. |          | is often called | the    | level-              | computation |     | tree at |     |     |     |              |                 |        |
Next,wepresenttheproofsofLemmas1and2inthatorder.
| node |     | corresponding | to  | the GM | under | consideration. |     | The |     |     |     |     |     |     |
| ---- | --- | ------------- | --- | ------ | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
computation tree in general is constructed by replicating the ProofofLemma1: Itisknown[21]thatunderthemin-sum
pairwise compatibility functions and potentials (or max-product) algorithm, the vector corresponds to the
, , while preserving the local connectivity of correct max-marginals for the root of the MAP assignment
the original graph. They are constructed so that the messages on the GM corresponding to . The pairwise compatibility
receivedbythenode after iterationsintheactualgraphare functions force the MAP assignment on this tree to be a
equivalenttothosethatwouldbereceivedbytheroot inthe -matching. Now, each edge has two endpoints and hence its
computationtree, ifthe messagesare passed upalong the tree weightiscountedtwiceintheweightofthe -matching.
fromtheleavestotheroot.Thecomputationtreehasbeenused Next,consider the th entry of , . By definition, it
in most of the previous work on analyzing the BP algorithm, correspondstotheMAPassignmentwiththevalueof atthe
e.g.,[8],[10],[20],[22],[23]. rootbeing .Thatis,theedge ischosenattherootin
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on April 17,2025 at 00:40:37 UTC from IEEE Xplore.  Restrictions apply.

| BAYATIetal.:MAX-PRODUCTFORMAXIMUMWEIGHTMATCHING |     |     |     |     |     |     |     |     |     |     |     |     | 1245 |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
fork=4asshownin(d)isdecomposedto(b):pathQoflength4and(c):cycle
Fig.2. ConsideragraphwithMWMshownin(a).ProjectionofthepathP
| C   | oflength4.Thedashededgesbelongto(cid:3)whileboldedgesbelongto(cid:5) |     |     |     |     | .   |     |     |     |     |     |     |     |
| --- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the tree. From the above discussion, must be equal to Firstnotethatthesetofalledgesof whoseprojectionin
|     | .   |     |     |     |     |                  | belongs | to  | is  | a -matching | which                    | we denote | by . |
| --- | --- | --- | --- | --- | --- | ---------------- | ------- | --- | --- | ----------- | ------------------------ | --------- | ---- |
|     |     |     |     |     |     | Nowconsiderpaths |         |     |     | ,           | in ,thatcontainedgesfrom |           |      |
Lemma2isthemainstepinprovingTheorem1anditsproof
|        |      |                |        |       |                  |     | and | alternativelydefinedasfollows.Let |     |     |                 |       | ,   |
| ------ | ---- | -------------- | ------ | ----- | ---------------- | --- | --- | --------------------------------- | --- | --- | --------------- | ----- | --- |
| covers | more | than one page. | Before | going | into the details | of  |     |                                   |     |     |                 |       |     |
|        |      |                |        |       |                  |     | ,   | and                               |     | be  | a single vertex | path. | Let |
proof,letusgiveahighleveldescriptionofit.Considerthecom-
|              |     |                |     |                  |     |        |     |     | ,     | where | is such that |     | is con- |
| ------------ | --- | -------------- | --- | ---------------- | --- | ------ | --- | --- | ----- | ----- | ------------ | --- | ------- |
| putationtree |     | rootedatvertex |     | andlookatmaximum |     |        |     |     |       |       |              |     |         |
|              |     |                |     |                  |     | nected | to  |     | under | . For | , define     |     | and     |
weight -matchingonit.Weassumethatattheroot,maximum
recursivelyasfollows:
| weight | -matching               | of  | does not | choose             | the correct | edge |     |     |     |     |     |     |     |
| ------ | ----------------------- | --- | -------- | ------------------ | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
|        | .Thenweusethepropertyof |     |          | -matchingsthateach |             |      |     |     |     |     |     |     |     |
vertexisconnectedtoexactlyoneofitsneighborstoconstruct
| a new | -matching | on computation |     | tree. This | new matching | is  |     |     |     |     |     |     |     |
| ----- | --------- | -------------- | --- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
goingtohavelargertotalweightifdepthofthecomputationtree
| is large | enough. | This last | step uses | an augmenting | path | based |     |     |     |     |     |     |     |
| -------- | ------- | --------- | --------- | ------------- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
argumentforthismatchingproblem.Theabovewillcontradict
theassumptionthatdecisionattherootisincorrect,andproves where isthenodeatlevel towhichtheendpointnode
| Lemma | 2.       |          |            |          |          |          |                                  | ofpath  |     | isconnectedtounder |                | ,and | is  |
| ----- | -------- | -------- | ---------- | -------- | -------- | -------- | -------------------------------- | ------- | --- | ------------------ | -------------- | ---- | --- |
|       |          |          |            |          |          | suchthat |                                  | atlevel |     | (partof            | )isconnectedto |      |     |
|       | Proof of | Lemma 2: | Assume the | contrary | that for | some     |                                  |         |     |                    |                |      |     |
|       |          |          |            |          |          | under    | .Notethat,bydefinition,suchpaths |         |     |                    |                | for  |     |
,
|     |     |     |     |         |     | existsincethetree |           |                                          |                 | has | levelsandcansupportapath |     |     |
| --- | --- | --- | --- | ------- | --- | ----------------- | --------- | ---------------------------------------- | --------------- | --- | ------------------------ | --- | --- |
|     |     |     |     |         |     | oflengthatmost    |           |                                          | asdefinedabove. |     |                          |     |     |
|     |     |     |     | forsome |     | (6)               |           |                                          |                 |     |                          |     |     |
|     |     |     |     |         |     |                   | Example2: | Fig.2(d)providesanexampleofsuchapath.The |                 |     |                          |     |     |
Then,let for .Let bethe -matchingon correspondingbipartitegraphhas withitsMWMshown
whose weight is . We will modify and find whose inFig.2(a).Fig.2(d)shows ,thecomputationtreefornode
weight is more than and which connects at the ,tilldepth .Apath, ishighlightedbythickedges
rootinsteadof ,thuscontradicting(6). alternatively complete and bold (edges from ) and dashed
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on April 17,2025 at 00:40:37 UTC from IEEE Xplore.  Restrictions apply.

1246 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.54,NO.3,MARCH2008
(edges from ). In the figure, ; ; Since the path is of even length, either the first edge or the
;andsoon.Finally lastedgeisan -edge.Withoutlossofgenerality,assumeitis
thelastedge.Then,let
| where      |     |     |     | is a cycle | of        | length (see | Nowconsiderthecycle |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | ---------- | --------- | ----------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
| Fig. 2(c)) | and |     |     |            | is a path | of length   |                     |     |     |     |     |     |     |     |
(seeFig.2(b)).
| Now                            | consider the | path     | of length |               | . Its edges | are alter-  |                  |     |               |     |     |     |                 |     |
| ------------------------------ | ------------ | -------- | --------- | ------------- | ----------- | ----------- | ---------------- | --- | ------------- | --- | --- | --- | --------------- | --- |
| natelypartitionedintoedgesfrom |              |          |           | andedges      |             | .Letusrefer |                  |     |               |     |     |     |                 |     |
|                                |              |          |           |               |             |             | Alternateedgesof |     | arefromtheMWM |     |     |     | .Hence,usingthe |     |
| totheedgesof                   | asthe        | -edgesof |           | .Replacingthe |             | -edges      |                  |     |               |     |     |     |                 |     |
sameargumentasabove,weobtain
| of with                      | their complement |                      | in                        | (all             | edges       | of ) pro- |     |     |     |     |     |     |     |     |
| ---------------------------- | ---------------- | -------------------- | ------------------------- | ---------------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ducesanewmatching            |                  | in                   | ;thisfollowsfromthewaythe |                  |             |           |     |     |     |     |     |     |     |     |
| pathsareconstructed.Notethat |                  |                      |                           | isexactlyequalto |             | on        |     |     |     |     |     |     |     |     |
| exceptalongthepath           |                  | whereitusesedgesfrom |                           |                  |             | .         |     |     |     |     |     |     |     |     |
| Lemma                        | 3: The weight    |                      | of -matching              |                  | is strictly | higher    |     |     |     |     |     |     |     |     |
(9)
| thanthatof | ontree | .   |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ThiscompletestheproofofLemma2sinceLemma3shows
|                            |     |     |     |             |     |          | From(7)–(9),weobtainthatfor |     |     |     | -matchings |     | and | in  |
| -------------------------- | --- | --- | --- | ----------- | --- | -------- | --------------------------- | --- | --- | --- | ---------- | --- | --- | --- |
| that isnotthemaximumweight |     |     |     | -matchingon |     | ,leading |                             |     |     |     |            |     |     |     |
toacontradiction.
Now,weprovidetheproofofLemma3.
| ProoofofLemma3: |     | Itsufficestoshowthatthetotalweight |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofthe -edgesislessthanthetotalweightoftheircomplement
(10)
| in . Consider | the        | projection |         | of   | in the | graph         | .   |     |     |     |     |     |     |     |
| ------------- | ---------- | ---------- | ------- | ---- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| can be        | decomposed | into       | a union | of a | set of | simple cycles |     |     |     |     |     |     |     |     |
andatmostoneevenlengthpath oflength ThiscompletestheproofofLemma3.
| atmost      | .Sinceeachsimplecyclehasatmost |     |     |     |     | verticesand |         |          |     |                |         |     |            |        |
| ----------- | ------------------------------ | --- | --- | --- | --- | ----------- | ------- | -------- | --- | -------------- | ------- | --- | ---------- | ------ |
| thelengthof | is                             |     |     |     |     |             |         |          |     | IV. COMPLEXITY |         |     |            |        |
|             |                                |     |     |     |     |             | In this | section, | we  | will           | analyze | the | complexity | of the |
(7)
min-sumalgorithmdescribedinSectionII-B.Theorem1sug-
|     |     |     |     |     |     |     | gests that | the number |     | of iterations | required |     | to find | the MWM |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ------------- | -------- | --- | ------- | ------- |
Consider one of these simple cycles, say . Construct the is . Now, in each iteration of the min-sum algorithm
|          |     |             |     |     |     |                | each node | sends | a vector | of  | size | (i.e., | numbers) | to each |
| -------- | --- | ----------- | --- | --- | --- | -------------- | --------- | ----- | -------- | --- | ---- | ------ | -------- | ------- |
| matching | in  | as follows: | i)  | For |     | , select edges |           |       |          |     |      |        |          |         |
incidenton thatbelongto .Suchedgesexistbytheproperty of the nodes in the other partition. Thus, the total number
|             |      |          |     |         |     |           | of messages | exchanged |     | in each | iteration | are |     | with each |
| ----------- | ---- | -------- | --- | ------- | --- | --------- | ----------- | --------- | --- | ------- | --------- | --- | --- | --------- |
| of the path | that | contains | .   | ii) For |     | , connect | it          |           |     |         |           |     |     |           |
accordingto ,thatis,addtheedge . message of length . Now, each node performs basic
Now by construction. Since the MWM is unique, computational operations (comparison, addition) to compute
thedefinitionof givesus eachelementinamessagevectorofsize .Thatis,eachnode
|          |            |                                     |     |                        |     |     | performs             |           | operations                              |       | to compute   | a                        | message | vector in    |
| -------- | ---------- | ----------------------------------- | --- | ---------------------- | --- | --- | -------------------- | --------- | --------------------------------------- | ----- | ------------ | ------------------------ | ------- | ------------ |
|          |            |                                     |     |                        |     |     | each iteration.      |           | Since each                              | node  | sends        | message                  |         | vectors, the |
|          |            |                                     |     |                        |     |     | totalcostis          |           | pernodeor                               |       |              | periterationforallnodes. |         |              |
|          |            |                                     |     |                        |     |     | Thus,thetotalcostfor |           |                                         |       | iterationsis |                          |         | .            |
|          |            |                                     |     |                        |     |     | Thus,                | for fixed | and                                     | , the | running      | time                     | of the  | algorithm    |
| However, |            | isexactlyequaltothetotalweightofthe |     |                        |     |     |                      |           |                                         |       |              |                          |         |              |
|          |            |                                     |     |                        |     |     | scalesas             |           | .StandardalgorithmssuchastheEdmond–Karp |       |              |                          |         |              |
| -edgesof | ,denotedby |                                     |     | ,minusthetotalweightof |     |     |                      |           |                                         |       |              |                          |         |              |
algorithm[9]ortheauctionalgorithm[7]haveacomplexityof
| the -edgesof | ,denotedby |     |     | .Thus |     |     |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
.Inwhatfollows,wesimplifythemin-sumalgorithmso
|     |     |     |     |     |     |     | that the                                    | overall     | running                            | time | of the | algorithm | becomes    |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | ----------- | ---------------------------------- | ---- | ------ | --------- | ---------- | --- |
|     |     |     |     |     |     |     | forfixed                                    | and         | .WemakeanoteherethattheEdmond–Karp |      |        |           |            |     |
|     |     |     |     |     |     |     | algorithm                                   | is strongly | polynomial                         |      | (i.e., | does      | not depend | on  |
|     |     |     |     |     |     | (8) | and )whiletheauctionalgorithm’scomplexityis |             |                                    |      |        |           |            | .   |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on April 17,2025 at 00:40:37 UTC from IEEE Xplore.  Restrictions apply.

| BAYATIetal.:MAX-PRODUCTFORMAXIMUMWEIGHTMATCHING |     |     |     |     |     |     |     |     |     |     |     |     |     | 1247 |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
A. SimplifiedMin-SumAlgorithmfor For ,thisclaimholdsbydefinition.For ,consider
|     |     |     |     |     |     |     | thedefinitionof |     |     | ,   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Wefirstpresentthealgorithmandshowthatitisexactlythe
| same | as the | min-sum | algorithm. | Later, | we analyze | the com- |     |     |     |     |     |     |     |     |
| ---- | ------ | ------- | ---------- | ------ | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
plexityofthealgorithm.
Simplifiedmin-sumalgorithm.
(12)
|     | (1) Unlikemin-sumalgorithm,noweach |                                |     |     |     | sendsa |     |     |     |     |     |     |     |     |
| --- | ---------------------------------- | ------------------------------ | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     | numberto                           | andviceversa.Letthemessagefrom |     |     |     |        |     |     |     |     |     |     |     |     |
to initeration bedenotedas Thefirstequalityfollowsfromdefinitioninmin-sumalgorithm
|     |                              |     |     |     |     |             | while second                |     | equality | follows | from property         | of  |     | .   |
| --- | ---------------------------- | --- | --- | --- | --- | ----------- | --------------------------- | --- | -------- | ------- | --------------------- | --- | --- | --- |
|     |                              |     |     |     |     |             | Equation(12)isindependentof |     |          |         | .Thisprovesthedesired |     |     |     |
|     | Similarly,letthemessagesfrom |     |     |     | to  | initeration |                             |     |          |         |                       |     |     |     |
claim.
bedenotedas Theabovestatedpropertyofmin-sumalgorithmimmediately
|     |               |     |                             |     |     |     | implies           | that the | vector |                 | has only      | two distinct  | values,   |      |
| --- | ------------- | --- | --------------------------- | --- | --- | --- | ----------------- | -------- | ------ | --------------- | ------------- | ------------- | --------- | ---- |
|     |               |     |                             |     |     |     | one corresponding |          | to     |                 | and the other | corresponding |           |      |
|     | (2) Initially |     | andsetthemessagesasfollows: |     |     |     |                   |          |        |                 |               |               |           |      |
|     |               |     |                             |     |     |     | to                | ,        | .      | Now subtract    |               | ,             |           | from |
|     |               |     |                             |     |     |     | all coordinates   |          | of     | . Lemma         | 4 guarantees  | the           | resulting |      |
|     |               |     |                             |     |     |     | matching          | forall   |        | does notchange. | Performing    |               | the       | same |
Similarly
modificationtoallmessagevectorsyieldsamodifiedmin-sum
|     |     |     |     |     |     |     | algorithm                 | with | the same | outcome       | as min-sum.              | But | each        | mes- |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | ---- | -------- | ------------- | ------------------------ | --- | ----------- | ---- |
|     |     |     |     |     |     |     | sage vector               |      | in       | this modified | min-sum                  | has | all coordi- |      |
|     |     |     |     |     |     |     | natesequaltozeroexceptthe |      |          |               | thcoordinate.Denotethese |     |             | th   |
(3) For ,messagesiniteration areobtainedfrom coordinatesby .Now(4)showstheseforall , , num-
|     | messagesofiteration |     |     |     | recursivelyasfollows: |     |      |                                        |     |     |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --------------------- | --- | ---- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |                     |     |     |     |                       |     | bers | satisfythefollowingrecursiveequations: |     |     |     |     |     |     |
(11)
(13)
|     | (4) TheestimatedMWMattheendofiteration |     |     |     |     | is   |                               |     |     |     |     |     |     |     |
| --- | -------------------------------------- | --- | --- | --- | --- | ---- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | ,where                                 |     |     |     |     | ,for | Similarly,fornewbeliefswehave |     |     |     |     |     |     |     |
.
(5)
|                                                    | Repeat(3)–(4)till |     |     | converges |     |     |     |     |     |     |     |     |     |      |
| -------------------------------------------------- | ----------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
| Now,westateandprovetheclaimthatrelatestheabovemod- |                   |     |     |           |     |     |     |     |     |     |     |     |     | (14) |
ifiedalgorithmtotheoriginalmin-sumalgorithm.
|        |             |            |           |        |           |              | Nowbyadding                    |     | toeachsideof(13)anddividingthemby |     |     |     |     |     |
| ------ | ----------- | ---------- | --------- | ------ | --------- | ------------ | ------------------------------ | --- | --------------------------------- | --- | --- | --- | --- | --- |
| Lemma  | 4:          | In min-sum | algorithm |        | adding an | equal amount |                                |     |                                   |     |     |     |     |     |
|        |             |            |           |        |           |              | itcanbeseenfrom(11)thatnumbers |     |                                   |     |     | and |     |     |
| to all | coordinates | of any     | message   | vector |           | (similarly   |                                |     |                                   |     |     |     |     |     |
satisfythesamerecursiveequations.Theyalsosatisfythesame
|                                     | ) at   | any time does                      | not | change | the resulting | estimated |                                   |     |     |     |     |        |     |     |
| ----------------------------------- | ------ | ---------------------------------- | --- | ------ | ------------- | --------- | --------------------------------- | --- | --- | --- | --- | ------ | --- | --- |
|                                     |        |                                    |     |        |               |           | initialconditions.Asaresultforall |     |     |     | , , | wehave |     |     |
| matching                            |        | forall ,                           | .   |        |               |           |                                   |     |     |     |     |        |     |     |
|                                     | Proof: | Ifanumberisaddedtoallcoordinatesof |     |        |               |           | it                                |     |     |     |     |        |     |     |
| isnothardtoseefrom(4)andstructureof |        |                                    |     |        |               | thatother |                                   |     |     |     |     |        |     |     |
(15)
| message | and | belief vectors | will | change | only up | to an additive |     |     |     |     |     |     |     |     |
| ------- | --- | -------------- | ---- | ------ | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
constanttotheircoordinates.Hence,thesechangesdonotaffect
and
|     |     |     |     | ,for |     | .   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma5:
Thealgorithmsmin-sumandsimplifiedmin-sum
(16)
| produce    | identical | estimated                                     | matchings |              | at the     | end of every  |            |         |               |            |                   |            |          |     |
| ---------- | --------- | --------------------------------------------- | --------- | ------------ | ---------- | ------------- | ---------- | ------- | ------------- | ---------- | ----------------- | ---------- | -------- | --- |
| iteration  | .         |                                               |           |              |            |               |            |         |               |            |                   |            |          |     |
|            |           |                                               |           |              |            |               | This shows | that    | the estimated |            | matching computed |            | at nodes | in  |
|            | Proof:    | Considerthemin-sumalgorithm.Inparticular,con- |           |              |            |               |            |         |               |            |                   |            |          |     |
|            |           |                                               |           |              |            |               | modified   | min-sum | and           | simplified | min-sum           | algorithms | are      | ex- |
| sider      | a message | vector                                        |           | in iteration | . First,we | claim         |            |         |               |            |                   |            |          |     |
|            |           |                                               |           |              |            |               | actly the  | same    | at each       | iteration  | which completes   | the        | proof    | of  |
| thatallfor | anygiven  |                                               | ,         |              | ,          | are the same. |            |         |               |            |                   |            |          |     |
Lemma5.
| Thatis,for |     | and |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Note3.Thesimplifiedmin-sumequationscanalsobederived
inadirectwaybylookingattheinterpretationofthemessages
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on April 17,2025 at 00:40:37 UTC from IEEE Xplore.  Restrictions apply.

1248 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.54,NO.3,MARCH2008
|     |     |     |     |     |     |     | eachofthe |     | ,   |     | .Thatis,ittakes |     |     | opera- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --------------- | --- | --- | ------ |
inthecomputationtree.Morespecifically,con-
|                    |             |                         |                       |             |                |         | tionsforcomputingallmessages       |         |              |           |           | ,               | .            |         |
| ------------------ | ----------- | ----------------------- | --------------------- | ----------- | -------------- | ------- | ---------------------------------- | ------- | ------------ | --------- | --------- | --------------- | ------------ | ------- |
| siderthelevel-     |             | computationtreerootedat |                       |             | ,              | .Also   |                                    |         |              |           |           |                 |              |         |
|                    |             |                         |                       |             |                |         | Thus,                              | we have | established  |           | that each | node            | ,            | ,       |
| consideritssubtree |             |                         | ,builtbyaddingtheedge |             |                |         | at                                 |         |              |           |           |                 |              |         |
|                    |             |                         |                       |             |                |         | and                                | ,       |              | , need to | perform   |                 | computations | to      |
| the root of        |             | to graph                | of all                | descendants | of .           | One can |                                    |         |              |           |           |                 |              |         |
|                    |             |                         |                       |             |                |         | compute                            | all of  | its messages | in        | a given   | iteration.      | That         | is, the |
| show that          | the message |                         |                       | is equal to | the difference | be-     |                                    |         |              |           |           |                 |              |         |
|                    |             |                         |                       |             |                |         | totalcomputationcostperiterationis |         |              |           |           | .Insummary,The- |              |         |
| tween weight       | of          | maximum                 | weight                | -matching   | in             | that    |                                    |         |              |           |           |                 |              |         |
orem1,Lemma5,anddiscussionofthisSectionIV-Bimmedi-
| uses the edge |     | at  | the root | and weight | of the maximum |     |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | -------- | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
atelyyieldthefollowingresult.
| weight -matchingin |     |     | thatdoesnotusethatedge.Now |     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
asimpleinductiongivesustheupdate(11). Theorem 2: The simplified min-sum algorithm finds the
|     |     |     |     |     |     |     | MWM | in  | iterations |                                | with total | computation | cost | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------------------ | ---------- | ----------- | ---- | --- |
|     |     |     |     |     |     |     |     | and |            | totalnumberofmessageexchanges. |            |             |      |     |
B. ComplexityofSimplifiedMin-Sum
V. AUCTIONANDMIN-SUMALGORITHMS
| Lemma            | 5 and | Theorem       | 1 immediately |     | imply that | the sim- |     |               |     |            |            |         |           |     |
| ---------------- | ----- | ------------- | ------------- | --- | ---------- | -------- | --- | ------------- | --- | ---------- | ---------- | ------- | --------- | --- |
|                  |       |               |               |     |            |          | In  | this section, | we  | will first | recall the | auction | algorithm | [7] |
| plified min-sum, |       | like min-sum, | converges     |     | after      | iter-    |     |               |     |            |            |         |           |     |
andthendescribeitsrelationtothemin-sumalgorithm.
| ations. As                        | described | above, | the                                | simplified       | min-sum algorithm |     |     |                        |     |     |     |     |     |     |
| --------------------------------- | --------- | ------ | ---------------------------------- | ---------------- | ----------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
| requiresatotalof                  |           |        | messagesperiteration.Thus,forfixed |                  |                   |     |     |                        |     |     |     |     |     |     |
| and ,thealgorithmrequiresatotalof |           |        |                                    |                  | messagesto        |     |     |                        |     |     |     |     |     |     |
| beexchanged.                      |           |        |                                    |                  |                   |     | A.  | AuctionAlgorithmforMWM |     |     |     |     |     |     |
| Now, we                           | consider  | the    | number                             | of computational | operations        |     |     |                        |     |     |     |     |     |     |
donebyeachnodeinaniteration.Fromthedescriptionofsim- TheauctionalgorithmfindstheMWMviaan“auction”:all
|     |     |     |     |     |     |     | becomebuyersandall |     |     | becomeobjects.Let |     |     | denotethe |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ----------------- | --- | --- | --------- | --- |
plifiedmin-sumalgorithm,itmayseemthateachnodewillre-
quiretodo workforsendingeachmessageandthus priceof and bethevalueofobject forbuyer .The
|     |     |     |     |     |     |     | netbenefitofanassignmentormatching |     |     |     |     | isdefinedas |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | ----------- | --- | --- |
workoverallatonenode.But,wepresentasimplemethodthat
| showseachnodecancomputemessageforallofits |                                                 |     |     |                          | neighbors |     |                 |     |     |                                       |     |     |     |     |
| ----------------------------------------- | ----------------------------------------------- | --- | --- | ------------------------ | --------- | --- | --------------- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
| with                                      | computationaloperation(comparison,addition/sub- |     |     |                          |           |     |                 |     |     |                                       |     |     |     |     |
| traction).Thiswillresultin                |                                                 |     |     | overallcomputationperit- |           |     |                 |     |     |                                       |     |     |     |     |
| eration.Thus,itwilltake                   |                                                 |     |     | computationin            |           |     |                 |     |     |                                       |     |     |     |     |
|                                           |                                                 |     |     |                          |           |     | Thegoalistofind |     |     | thatmaximizesthisnetbenefit.Itisclear |     |     |     |     |
iterations. Thiswill result intotal complexityof in thatforanysetofprices ,theMWMmaximizesthe
termsofoverallmessagesaswellascomputationoperations. net benefit. The auction algorithm is an iterative method for
Here we describe an algorithm to compute messages findingtheoptimalpricesandanassignmentthatmaximizesthe
, using received messages , netbenefit(andisthereforetheMWM).
|       | .Thisisthesamealgorithmthatall |                          |     |     | ,   |     | ,                 |                           |     |     |                     |     |        |     |
| ----- | ------------------------------ | ------------------------ | --- | --- | --- | --- | ----------------- | ------------------------- | --- | --- | ------------------- | --- | ------ | --- |
| and , |                                | ,needtoemploy.Now,define |     |     |     |     | Auctionalgorithm. |                           |     |     |                     |     |        |     |
|       |                                |                          |     |     |     |     |                   | • Initializetheassignment |     |     | ,thesetofunassigned |     |        |     |
|       |                                |                          |     |     |     |     |                   | buyers                    |     |     | ,andprices          |     | forall | .   |
• Thealgorithmrunsintwophases,whicharerepeated
|     |     |     |     |     |     |     |     | until | isacompletematching. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------------------- | --- | --- | --- | --- | --- |
• Phase1:Bidding.
Forall
|     |     |     |     |     |     |     |     | (1) Findbenefitmaximizing |     |     |     | .Let |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ---- | --- | --- |
Then,from(11)weobtain
|                               |     |        |          |             |                    |         |     | and            |     |             |       |             |          | (18) |
| ----------------------------- | --- | ------ | -------- | ----------- | ------------------ | ------- | --- | -------------- | --- | ----------- | ----- | ----------- | -------- | ---- |
|                               |     |        |          |             |                    |         |     | (2) Computethe |     | ”bid”of     | buyer | , denotedby |          |      |
|                               |     |        |          |             |                    |         |     |                |     | as follows: | given | a fixed     | positive |      |
|                               |     |        |          | for         |                    | (17)    |     |                |     |             |       |             |          |      |
|                               |     |        |          |             |                    |         |     | constant       |     | ,           |       |             |          |      |
| Weseethatcomputingallmessages |     |        |          |             | takes              | op-     |     |                |     |             |       |             |          |      |
| erations.From(17),ittakesnode |     |        |          |             | computationstofind |         |     |                |     |             |       |             |          |      |
| , ,                           | ,   | , then | it takes | computation | to                 | compute |     |                |     |             |       |             |          |      |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on April 17,2025 at 00:40:37 UTC from IEEE Xplore.  Restrictions apply.

| BAYATIetal.:MAX-PRODUCTFORMAXIMUMWEIGHTMATCHING |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 1249 |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
Min-sumauctionII.
• Phase2:Assignment.
| Foreachobject |     | ,                         |     |     |     |     |          |     |                           |     |     |     |           |     |     |
| ------------- | --- | ------------------------- | --- | --- | --- | --- | -------- | --- | ------------------------- | --- | --- | --- | --------- | --- | --- |
|               |     |                           |     |     |     |     |          |     | • Initializetheassignment |     |     |     | andprices |     | for |
| (3)           | Let | bethesetofbuyersfromwhich |     |     |     |     | received |     |                           |     |     |     |           |     |     |
all .
|           | abid.If                |           | ,increase |     | tothehighestbid       |          |            |         |                                                |                            |                             |     |     |            |      |
| --------- | ---------------------- | --------- | --------- | --- | --------------------- | -------- | ---------- | ------- | ---------------------------------------------- | -------------------------- | --------------------------- | --- | --- | ---------- | ---- |
|           |                        |           |           |     |                       |          |            |         | • Thealgorithmrunsintwophases,whicharerepeated |                            |                             |     |     |            |      |
|           |                        |           |           |     |                       |          |            |         | until                                          | isacompletematching.       |                             |     |     |            |      |
|           |                        |           |           |     |                       |          |            |         | • Phase1:Bidding.                              |                            |                             |     |     |            |      |
|           |                        |           |           |     |                       |          |            |         | Forall                                         | ,                          |                             |     |     |            |      |
|           |                        |           |           |     |                       |          |            |         |                                                | (1) Find                   | thatmaximizesthebenefit.Let |     |     |            |      |
| (4)       | Removethemaximumbidder |           |           |     |                       | from     | andadd     |         |                                                |                            |                             |     |     |            |      |
|           |                        | to        | .If       |     | ,                     | ,thenput |            |         |                                                |                            |                             |     |     |            |      |
|           | backin                 | .         |           |     |                       |          |            |         |                                                |                            |                             |     |     |            |      |
|           |                        |           |           |     |                       |          |            |         |                                                | and                        |                             |     |     |            | (20) |
| Theorem   |                        | 3 [6]: If |           |     | , then                | the      | assignment |         |                                                |                            |                             |     |     |            |      |
| converges | to                     | the MWM   | in        |     | iterations            |          | with       | running |                                                |                            |                             |     |     |            |      |
|           |                        |           |           |     |                       |          |            |         |                                                | (2) Computethe”bid”ofbuyer |                             |     |     | ,denotedby |      |
| time      |                        | (where    |           | and | areasdefinedearlier). |          |            |         |                                                |                            |                             |     |     |            |      |
B. ConnectingMin-SumandAuction
| The | similarity | between |     | (17) and | (18) suggests |     | a connection |     |     |     |     |     |     |     |     |
| --- | ---------- | ------- | --- | -------- | ------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
and
betweenthemin-sumandauctionalgorithms.Intheauctional-
| gorithm, | the | equations | for | calculating | the | bids are | exactly | the |                      |     |     |     |     |     |     |
| -------- | --- | --------- | --- | ----------- | --- | -------- | ------- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
|          |     |           |     |             |     |          |         |     | • Phase2:Assignment. |     |     |     |     |     |     |
sameasthoseforupdatingmessagesinthesimplifiedmin-sum
Foreachobject
algorithm.Butwhenupdatingtheprices,themaximumistaken
|     |     |     |     |     |     |     |     |     |     | (3) Set | price | to the | highest | bid, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ------ | ------- | ---- | --- |
overallincomingbidswhichisdifferentfromthedynamicsof
.
thesimplifiedmin-sumequations.Moreover,intheauctional-
|          |         |     |         |            |           |           |     |         |     | (4) Reset |     | . Then,for | each | add the | pair |
| -------- | ------- | --- | ------- | ---------- | --------- | --------- | --- | ------- | --- | --------- | --- | ---------- | ---- | ------- | ---- |
| gorithm, | bidders | do  | not bid | at every   | iteration | and       | do  | not bid |     |           |     |            |      |         |      |
|          |         |     |         |            |           |           |     |         |     |           | to  | if         |      | ,where  | isa  |
| to every | object  | but | in the  | simplified | min-sum   | algorithm |     | each    |     |           |     |            |      |         |      |
buyerattainingthemaximuminstep(3)
vertexsendsamessagetoallofitsneighborsateveryiteration.
Basedonthesesimilaritiesandthedifferencewemademodifi-
|     |     |     |     |     |     |     |     |     | Theorem | 4: The | algorithms |     | min-sum | auction I | and II are |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ---------- | --- | ------- | --------- | ---------- |
cationstoboththesimplifiedmin-sumandauctionalgorithms
equivalent.
whichwecalledmin-sumauctionIandmin-sumauctionII,re-
|     |     |     |     |     |     |     |     |     | Proof: | Let |     | and | denotethebidsandpricesatthe |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --------------------------- | --- | --- |
spectively.Wewillshowthattheseversionsareequivalentand
|     |     |     |     |     |     |     |     |     | endofiteration |     | inalgorithmmin-sumauctionII.Now,identify |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------------------------------- | --- | --- | --- | --- |
derivesomeoftheirkeyproperties.Hereweconsiderthenaïve
|                       |     |     |     |                     |     |     |     |     | with |     | and | with |     | .Thenitisimmediate |     |
| --------------------- | --- | --- | --- | ------------------- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | ------------------ | --- |
| auctionalgorithm(when |     |     |     | )anddealwiththecase |     |     |     | in  |      |     |     |      |     |                    |     |
thatmin-sumauctionIIbecomesidenticaltomin-sumauction
SectionV-B-I.
I.ThiscompletestheproofofTheorem4.
Min-sumauctionI.
Nextwewillprovethatifthemin-sumauctionalgorithmter-
(1) Each sends a number to and vice versa. minates(weomitreferencetoIorII),itfindsthecorrectMWM.
|     | Let | the messages |     | in iteration | be  | denoted | as  |     |     |     |     |     |     |     |     |
| --- | --- | ------------ | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Aswewillsee,theproofusesstandardarguments(see[7]for
|     |                |                           |        | .   |     |     |     |     | example).                                  |     |               |        |                 |          |          |
| --- | -------------- | ------------------------- | ------ | --- | --- | --- | --- | --- | ------------------------------------------ | --- | ------------- | ------ | --------------- | -------- | -------- |
|     | (2) Initialize |                           | andset |     |     | .   |     |     |                                            |     |               |        |                 |          |          |
|     |                |                           |        |     |     |     |     |     | Theorem                                    | 5:  | Let           | be the | termination     | matching | of the   |
|     | (3) For        | ,updatemessagesasfollows: |        |     |     |     |     |     |                                            |     |               |        |                 |          |          |
|     |                |                           |        |     |     |     |     |     | min-sumauctionI(orII).ThenitistheMWM,i.e., |     |               |        |                 |          | .        |
|     |                |                           |        |     |     |     |     |     | Proof:                                     | The | proof follows |        | by establishing | that at  | termina- |
tion,themessagesofmin-sumauctionformtheoptimalsolution
|     |     |     |     |     |     |     |     |     | forthe dual | ofthe | MWM | problem | and | isthe corresponding |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --- | ------- | --- | ------------------- | --- |
(19)
|     |     |     |     |     |     |     |     |     | optimal | solution | to the | primal, | i.e., MWM. | To do so, | we first |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | ------- | ---------- | --------- | -------- |
statethedualoftheMWMproblem
|     | (4) TheestimatedMWMattheendofiteration |     |     |     |       |     |     | isthe |     |     |           |     |     |     |      |
| --- | -------------------------------------- | --- | --- | --- | ----- | --- | --- | ----- | --- | --- | --------- | --- | --- | --- | ---- |
|     | setofedges                             |     |     |     | where |     |     |       |     |     |           |     |     |     |      |
|     |                                        |     |     |     |       |     |     |       |     |     | subjectto |     |     |     | (21) |
and
|     |     |     |     |     |     |     |     |     | Let           | be the | optimal                           | solution | to  | the above stated | dual |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | --------------------------------- | -------- | --- | ---------------- | ---- |
|     |     |     |     |     |     |     |     |     | problemandlet |        | solvetheprimalMWMproblem.Then,the |          |     |                  |      |
standardcomplimentaryslacknessconditionsare
|     | (5) Repeat(3)–(4)till |     |     | isacompletematching. |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(22)
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on April 17,2025 at 00:40:37 UTC from IEEE Xplore.  Restrictions apply.

1250 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.54,NO.3,MARCH2008
Thus, are the optimal dual-primal solution for the Conjecture1: If isuniquethenthemin-sumauctionIter-
MWMproblemifandonlyifa) isamatching,b) sat- minatesinafinitenumberofiterationsifcondition“
isfy(21),andc)thetriplesatisfies(22).Tocompletetheproof,
”isremovedfromstep(4).
| wewillprovetheexistenceof |     |     |     | , suchthat                  |     |     | satisfy |               |     |             |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --------------------------- | --- | --- | ------- | ------------- | --- | ----------- | --- | --- | --- | --- | --- |
| conditionsa)–c).          |     |     |     |                             |     |     |         | C. Relationto |     | -Relaxation |     |     |     |     |     |
| Tothisend,firstnotethat   |     |     |     | isamatchingbythetermination |     |     |         |               |     |             |     |     |     |     |     |
Intheprevioussection,weestablishedarelationbetweenthe
| condition | of the | algorithm; | thus, | condition | a) is | satisfied. | We  |                        |     |     |     |                             |     |     |     |
| --------- | ------ | ---------- | ----- | --------- | ----- | ---------- | --- | ---------------------- | --- | --- | --- | --------------------------- | --- | --- | --- |
|           |        |            |       |           |       |            |     | min-sumandauction(with |     |     |     | )algorithms.In[7],[6]theau- |     |     |     |
shallconsiderthemin-sumauctionIIalgorithmforthepurpose
thorextendstheauctionalgorithmtoobtainguaranteedconver-
oftheproof.Supposethealgorithmterminatesatsomeiteration
|                       |     |               |                                   |              |     |     |     | genceinafinitenumberofiterationsviaa |              |     |                                  |     | -relaxationforsome |     |         |
| --------------------- | --- | ------------- | --------------------------------- | ------------ | --- | --- | --- | ------------------------------------ | ------------ | --- | -------------------------------- | --- | ------------------ | --- | ------- |
| .Let                  | and | bethepricesof |                                   | initerations |     |     | and | ,                                    |              |     |                                  |     |                    |     |         |
|                       |     |               |                                   |              |     |     |     | .Attermination,the                   |              |     | -relaxedalgorithmproducesatriple |     |                    |     |         |
| respectively.Sinceall |     |               | ’sarematchedatthetermination,from |              |     |     |     |                                      |              |     |                                  |     |                    |     |         |
|                       |     |               |                                   |              |     |     |     |                                      | suchthat(a1) |     | isamatching,(b1)                 |     |                    |     | satisfy |
step(4)ofthemin-sumauctionII,weobtain
(21),and(c1)thefollowingmodifiedcomplimentaryslackness
conditionsaresatisfied:
(23)
(26)
| At termination | (iteration |                                     | ),  | is matched | with |     | or  | is             |     |          |          |       |     |            |         |
| -------------- | ---------- | ----------------------------------- | --- | ---------- | ---- | --- | --- | -------------- | --- | -------- | -------- | ----- | --- | ---------- | ------- |
| matchedwith    |            | .Bythedefinitionofthemin-sumauction |     |            |      |     |     |                |     |          |          |       |     |            |         |
|                |            |                                     |     |            |      |     |     | The conditions |     | (c1) are | referred | to as | -CS | conditions | in [7]. |
II algorithm
|     |     |     |     |     |     |     |      | This modification                               |     | is reflected | in  | the description          |     | of  | the auction |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----------------------------------------------- | --- | ------------ | --- | ------------------------ | --- | --- | ----------- |
|     |     |     |     |     |     |     | (24) | algorithmwherewehaveadded                       |     |              |     | toeachbidinstep(2).Wees- |     |     |             |
|     |     |     |     |     |     |     |      | tablishedtherelationbetweenmin-sumandauctionfor |     |              |     |                          |     |     | in          |
|     |     |     |     |     |     |     |      | theprevioussection.Herewemakeanotethatforevery  |     |              |     |                          |     |     | ,           |
From(23)and(24),weobtainthat
asimilarrelationholds.Toseethis,weconsidermin-sumauc-
tionIandIIwherethebidcomputationismodifiedasfollows:
(25)
modifystep(3)ofmin-sumauctionIas
| Define |     |     | and |     | . Then, | from | (25), |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | ------- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
satisfythedualfeasibility,thatis,(21).Further,bydef-
initiontheysatisfythecomplimentaryslacknesscondition(22).
andmodifystep(2)ofmin-sumauctionIIas
| Thus,thetriple |     |     | satisfiesconditionsa)–c)asrequired. |     |     |     |     |     |     |     |     |     |                  |     |     |
| -------------- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- |
|                |     |     |                                     |     |     |     |     |     | and |     |     | ,   | Forthesemodified |     |     |
Hence,thealgorithmmin-sumauctionIIproducestheMWM,
algorithms,weobtainthefollowingresultusingargumentsvery
| i.e., | .   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
similartotheonesusedinTheorem5.
| The min-sum |     | auction | II algorithm | looks | very | similar | to the |           |     |     |      |                           |     |     |     |
| ----------- | --- | ------- | ------------ | ----- | ---- | ------- | ------ | --------- | --- | --- | ---- | ------------------------- | --- | --- | --- |
|             |     |         |              |       |      |         |        | Theorem7: |     | For | ,let | bethematchingobtainedfrom |     |     |     |
auctionalgorithmandinheritssomeofitsproperties.However,
themodifiedmin-sumauctionalgorithmI(orII).Then,
italsoinheritssomepropertiesofthemin-sumalgorithm.This
|     |     |     |     |     |     |     |     |     | (i.e., | iswithin | oftheMWM). |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ---------- | --- | --- | --- | --- |
causesittobehavedifferentlyfromtheauctionalgorithm.The
| proof of | convergence | of  | the auction | algorithm |     | relies | on two |                 |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ----------- | --------- | --- | ------ | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- |
|          |             |     |             |           |     |        |        | D. Implications |     |     |     |     |     |     |     |
propertiesoftheauctioningmechanism:a)thepricesarealways
|     |     |     |     |     |     |     |     | The | relation | between | min-sum | and | auction | algorithms | re- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------- | --- | ------- | ---------- | --- |
nondecreasingandb)thenumberofmatchedobjectsisalways
|                |     |         |        |        |          |     |          | sulted in | equivalent | algorithms |     | min-sum | auction | I   | and II. The |
| -------------- | --- | ------- | ------ | ------ | -------- | --- | -------- | --------- | ---------- | ---------- | --- | ------- | ------- | --- | ----------- |
| nondecreasing. | By  | design, | a) and | b) can | be shown | to  | hold for |           |            |            |     |         |         |     |             |
furthermodificationofthemin-sumauctionI(orII)basedonthe
| the auction | algorithm. | However, |         | it is not | clear if | a) and    | b) are |             |        |        |     |           |                 |     |      |
| ----------- | ---------- | -------- | ------- | --------- | -------- | --------- | ------ | ----------- | ------ | ------ | --- | --------- | --------------- | --- | ---- |
|             |            |          |         |           |          |           |        | -relaxation | method | allows | for | designing | (deterministic) |     | dis- |
| true for    | min-sum    | auction. | In what | follows,  | we       | state the | result |             |        |        |     |           |                 |     |      |
tributedalgorithmthatworkseveninthepresenceofnonunique
thatpricesareeventuallynondecreasinginthemin-sumauction
MWM(Theorem7).Thissuggestsamethodfordesigningmod-
| algorithm; | however, | it seems | difficult | to  | establish | a statement |     |           |            |     |             |     |         |              |     |
| ---------- | -------- | -------- | --------- | --- | --------- | ----------- | --- | --------- | ---------- | --- | ----------- | --- | ------- | ------------ | --- |
|            |          |          |           |     |           |             |     | ification | of min-sum | or  | max-product | for | general | optimization |     |
similartob)forthemin-sumalgorithmasofnow.
problemsoastoworkinthepresenceofanonuniquesolution.
Theorem 6: If is unique then in the min-sum auction II Further,themin-sumauctionIalgorithmbydesignisdualun-
| algorithmpriceseventuallyincrease.Thatis, |       |            |     |                  |     | ;        |        |                              |         |                    |     |      |     |       |             |
| ----------------------------------------- | ----- | ---------- | --- | ---------------- | --- | -------- | ------ | ---------------------------- | ------- | ------------------ | --- | ---- | --- | ----- | ----------- |
|                                           |       |            |     |                  |     |          |        | like the                     | auction | being primal-dual. |     | This | may | be of | interest in |
| s.t                                       | ;     | ,          |     | .                |     |          |        | optimizationmethodsonitsown. |         |                    |     |      |     |       |             |
| Proof:                                    | Proof | of Theorem |     | 6 is essentially |     | based on | i) the |                              |         |                    |     |      |     |       |             |
equivalence between the min-sum auction algorithms I and II, VI. DISCUSSIONANDCONCLUSION
andii)argumentsverysimilartotheonesusedintheproofof
Inthispaper,weprovedthatthemax-productalgorithmcon-
Lemma2,wherewerelatepriceswiththecomputationtree.
vergestothedesirablefixedpointinthecontextoffindingthe
Oursimulationssuggeststhatintheabsenceofthecondition MWMforabipartitegraph,eveninthepresenceofloops.This
“ ”fromstep(4)ofmin-sumauctionI,the resulthasatwofoldimpact.First,itwillpossiblyopenavenues
algorithm always terminates and finds the MWM as long as it forademystificationofthemax-productalgorithm.Second,the
isunique.ThisalongwithTheorem6leadsustothefollowing sameapproachmayprovablyworkforothercombinatorialop-
conjecture. timizationproblemsandpossiblyleadtobetteralgorithms.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on April 17,2025 at 00:40:37 UTC from IEEE Xplore.  Restrictions apply.

BAYATIetal.:MAX-PRODUCTFORMAXIMUMWEIGHTMATCHING 1251
Usingtheregularityofthestructureoftheproblem,weman-
[5] M.Bayati,B.Prabhakar,D.Shah,andM.Sharma,“Iterativesched-
aged to simplify the max-product algorithm. In the simplified ulingalgorithm,”inProc.IEEEInfocom,Anchorage,AK,May2007,
pp.445–453.
| algorithm,eachnodeneedstoperform |     |     | addition–subtrac- |     |     |     |     |
| -------------------------------- | --- | --- | ----------------- | --- | --- | --- | --- |
[6] D.P.Bertsekas,“Auctionalgorithmsfornetworkflowproblems:A
tion operations in each iteration. Since iterations are re- tutorialintroduction,”Comput.Optimiz.Applic.,vol.1,pp.7–66,1992.
quired inthe worst case, for finite and , the algorithm re- [7] D.BertsekasandJ.Tsitsiklis,ParallelandDistributedComputation:
|     |     |     |     | NumericalMethods. | EnglewoodCliffs,NJ:Prentice-Hall,1989. |     |     |
| --- | --- | --- | --- | ----------------- | -------------------------------------- | --- | --- |
quires operations at the most. This is comparable with [8] R.G.Gallager,LowDensityParityCheckCodes. Cambridge,MA:
the bestknown MWMalgorithm.Furthermore,the distributed MITPress,1963.
natureofthemax-productalgorithmmakesitparticularlysuit- [9] J.EdmondsandR.Karp,“Theoreticalimprovementsinalgorithmic
efficiencyfornetworkflowproblems,”J.ACM,vol.19,pp.248–264,
| able for networking | applicationslike | switchscheduling | where |     |     |     |     |
| ------------------- | ---------------- | ---------------- | ----- | --- | --- | --- | --- |
1972.
scalabilityisanecessaryproperty. [10] B.J.FreyandR.Koetter,“Exactinferenceusingtheattenuatedmax-
|              |                       |                 |                   | product algorithm,”            | in Advanced | Mean Field             | Methods: Theory and |
| ------------ | --------------------- | --------------- | ----------------- | ------------------------------ | ----------- | ---------------------- | ------------------- |
| The relation | that we established   | between         | the auction algo- |                                |             |                        |                     |
|              |                       |                 |                   | Practice,M.OpperandD.Saad,Eds. |             | Cambridge,MA:MITPress, |                     |
| rithm and    | the min-sum algorithm | is tantalizing. | It suggests a     |                                |             |                        |                     |
2000.
[11] G.B.Horn,“IterativeDecodingandPseudocodewords,”Ph.D.disser-
| method to | design modification | of max-product | algorithm for |     |     |     |     |
| --------- | ------------------- | -------------- | ------------- | --- | --- | --- | --- |
tation,Dep.Elec.Eng.,CaliforniaInsst.Technol.,Pasadena,CA,1999.
| general optimization      | problem | that may work | even in the pres- |                                   |     |                               |     |
| ------------------------- | ------- | ------------- | ----------------- | --------------------------------- | --- | ----------------------------- | --- |
|                           |         |               |                   | [12] S.Lauritzen,Graphicalmodels. |     | Oxford,U.K.:OxfordUniv.Press, |     |
| enceofnonuniquesolutions. |         |               |                   | 1996.                             |     |                               |     |
Future work will consist of trying to extend our result to [13] E. Lawler, Combinatorial Optimization: Networks and Matroids.
NewYork:Holt,RinehartandWinston,1976.
findingtheMWMinageneralgraph,asourcurrentarguments
|     |     |     |     | [14] N. McKeown, | V. Anantharam, | and J. Walrand, | “Achieving 100% |
| --- | --- | --- | --- | ---------------- | -------------- | --------------- | --------------- |
donotcarryover.2Also,wewouldliketoobtaintighterbounds throughputinaninput-queuedswitch,”inProc.IEEEInforcom,San
on the running time of the algorithm since simulation studies Francisco,CA,Mar.1996,vol.1,pp.296–302.
[15] M.Mezard,G.Parisi,andR.Zecchina,“Analyticandalgorithmicsolu-
show that the algorithm runs much faster on average than the tionofrandomsatisfiabilityproblems,”Science,vol.297,p.812,2002.
worstcaseboundobtainedinthispaper. [16] J.Pearl,ProbabilisticReasoninginIntelligentSystems:Networksof
|     |     |     |     | PlausibleInference. | SanFrancisco,CA:MorganKaufmann,1988. |     |     |
| --- | --- | --- | --- | ------------------- | ------------------------------------ | --- | --- |
[17] T.RichardsonandR.Urbanke,“Thecapacityoflow-densityparity
ACKNOWLEDGMENT check codes under message-passing decoding,” IEEE Trans. Inf.
Theory,vol.47,no.2,pp.599–618,Feb.2001.
[18] M.WainwrightandM.Jordan,GraphicalModels,ExponentialFami-
Theauthorswouldliketothanktheanonymousrefereesfor
lies,andVariationalInferenceDep.Statist.,Univ.California,Berkeley,
theirhelpfulcomments.
CA,2003.
[19] M.J.Wainwright,T.S.Jaakkola,andA.S.Willsky,“Treeconsistency
andboundsontheperformanceofthemax-productalgorithmandits
REFERENCES generalizations,”StatisticsandComputing,vol.14,pp.143–166,Apr.
2004.
[1] S.M.Aji,G.B.Horn,andR.J.McEliece,“Ontheconvergenceof [20] Y.Weiss,“Correctnessoflocalprobabilitypropagationingraphical
iterativedecodingongraphswithasinglecycle,”inProc.IEEEInt. modelswithloops,”NeuralComput.,vol.12,pp.1–42,2000.
Symp.InformationTheory,Cambridge,MA,Aug.1998,p.276. [21] Y.Weiss,BeliefPropagationandRevisioninNetworksWithLoops
[2] S.M.AjiandR.J.McEliece,“Thegeneralizeddistributivelaw,”IEEE MITAILab.,1997,Tech.Rep.1616.
Trans.Inf.Theory,vol.46,no.2,pp.325–343,Mar.2000. [22] Y. Weiss and W. Freeman, “Correctness of belief propagation in
[3] M.Bayati,D.Shah,andM.Sharma,“Maximumweightmatchingvia Gaussian graphical models of arbitrary topology,” Neural Comput.,
max-productbeliefpropagation,”inProc.IEEEInt.Symp.Information vol.13,no.10,pp.2173–2200,2001.
Theory,Adelaide,Australia,Sep.2005,pp.1763–1767. [23] Y.WeissandW.T.Freeman,“Ontheoptimalityofsolutionsofthe
[4] M.Bayati,D.Shah,andM.Sharma,“Asimplermax-productmax- max-productbelief-propagationalgorithminarbitrarygraphs,”IEEE
imumweightmatchingalgorithmandtheauctionalgorithm,”inProc. Trans.Inf.Theory,vol.47,no.2,pp.736–744,Feb.2001.
IEEE Int. Symp. Information Theory, Seattle, WA, Jul. 2006, pp. [24] J. Yedidia, W. Freeman, and Y. Weiss, Understanding Belief Prop-
557–561. agation and Its Generalizations Mitsubishi Elect. Res. Lab., 2000,
TR-2001-22.
2AkeyfactintheproofofLemma3wasthepropertythatbipartitegraphsdo [25] J.Yedidia,W.Freeman,andY.Weiss,GeneralizedBeliefPropagation
| nothaveoddcycles. |     |     |     | MitsubishiElect.Res.Lab.,2000,TR-2000-26. |     |     |     |
| ----------------- | --- | --- | --- | ----------------------------------------- | --- | --- | --- |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on April 17,2025 at 00:40:37 UTC from IEEE Xplore.  Restrictions apply.