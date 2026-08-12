IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.57,NO.4,APRIL2011 2203
| Belief |     | Propagation |          |     |     | and | LP  | Relaxation |        |     | for | Weighted |     |     |
| ------ | --- | ----------- | -------- | --- | --- | --- | --- | ---------- | ------ | --- | --- | -------- | --- | --- |
|        |     |             | Matching |     |     |     | in  | General    | Graphs |     |     |          |     |     |
SujaySanghavi,Member,IEEE, DmitryMalioutov,and AlanWillsky,Fellow,IEEE
Abstract—Loopy belief propagation has been employed in a muchstructure,andthisstructurecanbeusedtoprovideamuch
| wide variety | of applications |     | with | great | empirical | success, | but | it  |     |     |     |     |     |     |
| ------------ | --------------- | --- | ---- | ----- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
finercharacterizationofmax-productperformancethanwould
| comeswithfewtheoretical |     |     | guarantees.In |     | thispaper,weanalyze |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bepossibleforgeneralgraphicalmodels.Second,fastanddis-
| the performance | of  | the max-product |     | form | of belief | propagation |     |     |     |     |     |     |     |     |
| --------------- | --- | --------------- | --- | ---- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
tributedcomputationofweightedmatchingsisoftenrequiredin
| for theweighted | matching |     | problem | on general |     | graphs. | We show |     |     |     |     |     |     |     |
| --------------- | -------- | --- | ------- | ---------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
thattheperformanceofmax-productisexactlycharacterizedby areasasdiverseasresourceallocation,schedulingincommuni-
thenaturallinearprogramming(LP)relaxationoftheproblem.In cationsnetworks[8],andmachinelearning[9].
particular,wefirstshowthatiftheLPrelaxationhasnofractional Givenagraph withnonnegativeweights on
optimathenmax-productalwaysconvergestothecorrectanswer.
|                  |     |           |     |            |     |           |         | itsedges | ,theweightedmatchingproblemistofindthe |     |     |     |     |     |
| ---------------- | --- | --------- | --- | ---------- | --- | --------- | ------- | -------- | -------------------------------------- | --- | --- | --- | --- | --- |
| This establishes | the | extension | of  | the recent |     | result by | Bayati, |          |                                        |     |     |     |     |     |
heaviestsetofmutuallydisjointedges(i.e.,asetofedgessuch
ShahandSharma,whichconsideredbipartitegraphs,togeneral
graphs. Perhaps more interestingly, we also establish a tight thatnotwoedgesshareanode).Weightedmatchingcanbenat-
converse,namelythatthepresenceofanyfractionalLPoptimum urallyformulatedasanintegerprogram(IP).Thetechniqueof
impliesthatmax-productwillfailtoyieldusefulestimatesonsome linear programming (LP) relaxation involves replacing the in-
oftheedges.Weextendourresultstotheweighted(cid:0)-matchingand
(cid:2)-edge-coverproblems.Wealsodemonstratehowtosimplifythe teger constraints with linear inequality constraints. In general
graphs,thelinearprogramforweightedmatchingcanhavefrac-
| max-product | message-update |     | equations |     | for weighted | matching, |     |     |     |     |     |     |     |     |
| ----------- | -------------- | --- | --------- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
makingiteasilydeployableindistributedsettingslikewirelessor tionaloptima—i.e., those that assignfractional massto edges.
sensornetworks.
|     |     |     |     |     |     |     |     | The primary | contribution |     | of this | paper is an | exact characteri- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ------- | ----------- | ----------------- | --- |
zationofmax-productperformancefortheweightedmatching
| Index | Terms—Belief | propagation, |     | combinatorial |     | optimization, |     |     |     |     |     |     |     |     |
| ----- | ------------ | ------------ | --- | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
problem:weshowthat
| graphical | models, | Markov | random | fields, | matching, |     | message |     |     |     |     |     |     |     |
| --------- | ------- | ------ | ------ | ------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
passing. (cid:129) IftheLPhasnofractionaloptima(i.e.,iftheoptimumof
LPisuniqueandintegral),thenmax-productwillconverge
|     |     |     |              |     |     |     |     | and | the resulting | solutionwill |     | be exactlythe | max-weight |     |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | ------------- | ------------ | --- | ------------- | ---------- | --- |
|     |     | I.  | INTRODUCTION |     |     |     |     |     |               |              |     |               |            |     |
matching(Theorem1).
|        |        |             |     |       |         |          |         | (cid:129) Foranyedge,ifthereexistsanoptimumofLPthatassigns |     |     |     |     |     |     |
| ------ | ------ | ----------- | --- | ----- | ------- | -------- | ------- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| L OOPY | belief | propagation |     | (LBP) | and its | variants | [1]–[3] |                                                            |     |     |     |     |     |     |
have been shown empirically to be effective in solving fractionalmasstothatedge,thenthemax-productestimate
|     |     |     |     |     |     |     |     | for | that edge | will either | oscillate | or be ambiguous |     | (The- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --------- | --------------- | --- | ----- |
manyinstancesofhardproblemsinawiderangeoffields.These
orem2).Fortheentiregraph,thisimpliesthatiffractional
| algorithms | were originally |     | designed | for | exact | inference | (i.e., |     |     |     |     |     |     |     |
| ---------- | --------------- | --- | -------- | --- | ----- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
optimaexistthenmax-productwillfail(Corollary1).
| calculation | of marginals/MAP |     | estimates) |     | in probability |     | distri- |         |              |          |     |                    |        |       |
| ----------- | ---------------- | --- | ---------- | --- | -------------- | --- | ------- | ------- | ------------ | -------- | --- | ------------------ | ------ | ----- |
|             |                  |     |            |     |                |     |         | Most of | the existing | analysis |     | of classical loopy | belief | prop- |
butionswhoseassociatedgraphicalmodelsaretree-structured.
Whilesomeprogresshasbeenmadeinunderstandingtheircon- agation either provides sufficient conditions for correctness of
solutions(e.g.,[10]and[4]),orprovidesananalysis/interpreta-
| vergence | and accuracy | ongeneral |     | “loopy” | graphs | (see | [3]–[5] |     |     |     |     |     |     |     |
| -------- | ------------ | --------- | --- | ------- | ------ | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
tionoffixedpoints(e.g.,[5]and[3]).However,therearerela-
andtheirreferences),itstillremainsanactiveresearcharea.
Inthispaper,westudytheapplicationofthewidelyusedmax- tivelyfewresultsthatprovidenecessaryconditionsforthecon-
|     |     |     |     |     |     |     |     | vergence/correctness |     | of  | the iterative | procedure. | Theorem | 2 is |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------------- | ---------- | ------- | ---- |
productformofLBP(orsimplymax-product(MP)algorithm),
thussignificantinthisregard,andwebelieveitismoregeneral
totheweightedmatchingproblem.1Ourmotivationfordoingso
istwofold:first,weightedmatchingisaclassicalproblemwith thantheweightedmatchingandcoveringproblemsdiscussedin
|     |     |     |     |     |     |     |     | this paper. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Manytantalizingconnectionsbetweenbeliefpropagationand
ManuscriptreceivedDecember14,2007;revisedSeptember26,2010;ac-
linearprogramming(invariousforms)havebeenobserved/con-
ceptedOctober11,2010.DateofcurrentversionMarch16,2011.Thiswork
jectured[11].Thispaperprovidesapreciseconnectionbetween
wassupportedinpartbyNSFgrants0954059(CAREER)and0964391.The
materialinthispaperwaspresentedattheIEEEInformationTheoryWorkshop thetwofortheweightedmatchingproblem.Aninterestingin-
(ITW),Tahoe,CA,May2007.
sightinthisregard,obtainedfromourwork,istheimportance
S.SanghaviiswiththeUniversityofTexas,Austin,TX78750USA(e-mail:
oftheuniquenessoftheLPoptimum,asopposedtouniqueness
sanghavi@mail.utexas.edu).
D.MalioutoviswithDRWInc.,Chicago,ILUSA(e-mail:dmm@mit.edu). oftheIPoptimum.Inparticular,itiseasytoconstructexamples
A.WillskyiswiththeMassachusettsInstituteofTechnology,Cambridge, wheretheLPhasauniqueintegeroptimum,butalsohasaddi-
MA02139USA(e-mail:willsky@mit.edu).
tionalspuriousfractionaloptima,forwhichmax-productfailsto
CommunicatedbyH.-A.Loeliger,AssociateEditorforCodingTechniques.
DigitalObjectIdentifier10.1109/TIT.2011.2110170 beinformative.Amoredetaileddiscussionofthisispresented
inSectionV.
1Thispublicationisthejournalversionofearlierresultsreportedin[6].Also
relatedarerecentresultsbyBayati,Borgs,ChayesandZecchina[7].SeeSec- Weextendouranalysistoestablishthisequivalencebetween
tionIforadiscussion. max-product and LP relaxation for two related problems:
0018-9448/$26.00©2011IEEE
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 26,2025 at 03:18:15 UTC from IEEE Xplore.  Restrictions apply.

2204 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.57,NO.4,APRIL2011
weighted -matching and -edge-cover. Given a graph with Bothflavorsareiterativemessage-passingalgorithms,designed
edge weights and node capacities , the weighted -matching to be exact when the graphical model is a tree. Analysis of
problem is to pick the heaviest set of edges so that at most their performance in graphs with cycles has been of much
edgestouchnode ,foreach .Similarly,ifthegraphhas recent interest; existing analysis falls into two methodological
node requirements , the weighted -edge-cover problem is categories. The first category is the direct analysis of fixed
to pick the lightest set of edges so that each node has pointsoftheiterativealgorithm:[3]showsthatthefixedpoints
at least edges incident on it. Theorems 3 and 4 pertain to of SumProduct on general graphs correspond to zero-gradient
-matching,andTheorems5and6to -edge-cover. pointsoftheBetheapproximationtotheenergyfunction.[12]
Inaninsightfulpaper,Bayati,ShahandSharma[10]werethe
|     |     |     |     |     |     |     | shows that | the convergence |     | of SumProduct |     | is related | to the |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | ------------- | --- | ---------- | ------ |
first to analyze max-product for weighted matching problems; uniqueness of the Gibbs measure on the infinite model repre-
they established that max-product correctly solves weighted sentedbythecomputationtree.[11]showsthecorrespondence
matching in bipartite graphs, when the optimal matching is betweenBPfixedpointsandlinearprogramming(LP)solutions
unique. Theorem 1 represents a generalization of this result,2 forthedecoding problem.ForMaxProductongeneralgraphs,
asforbipartitegraphsitiswellknownthattheextremepoints
|     |     |     |     |     |     |     | [5] establish | that | the fixed | point solutions |     | are locally optimal, |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | --------- | --------------- | --- | -------------------- | --- |
of the matching LP polytope are integral. This means that if inagraph-theoreticsense.
the LP has a fractional optimum, it has to also have multiple The second category of analysis, also the one taken in this
integraloptima,i.e.,multipleoptimalmatchings.So,requiring
|     |     |     |     |     |     |     | paper, involves | direct | analysis | of the | dynamics | of the iterative |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | -------- | ------ | -------- | ---------------- | --- |
unique optima in bipartite graphs is equivalent to requiring procedure,tojointlyestablishbothconvergenceandrelationto
| no fractional | optima | for | the LP | relaxation. | In [9] | the results |     |     |     |     |     |     |     |
| ------------- | ------ | --- | ------ | ----------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
thecorrectsolution.Thisapproachwasfirstusedin[10]inthe
of [10] were extended to weighted -matchings on bipartite contextofweightedmatchingonbipartitegraphs(i.e.,thosethat
graphs. Theorem 3 represents the corresponding extension of have no odd cycles). They established that if the optimum is
| ourresultsto | -matchingongeneralgraphs. |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
unique,MaxProductalwaysconvergestoit;theyalsoprecisely
Apreliminaryversion[6]ofthispapercontainedadifferent bound the rate of convergence. Their approach generalizes to
proofofbothTheorems1and2.Theproofsinthatpapercanbe -matchingsaswell,asestablishedin[9].Ourpapergeneralizes
adaptedhandlemoregeneralmessageupdaterules(asopposed
thisresulttoall(i.e.,notjustbipartite)graphs,wheretherele-
tothe“fullysynchronous”caseconsideredinthispaper).Both vantnotionisnotuniquenessofthetrueoptimum,butunique-
| [6]andthis | paperconsiderthecaseof“imperfect”matchings, |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nessoftheLPrelaxation.Independentworkintherecentpaper
| where each | node | can have | at most | one | edge in the | matching, |     |     |     |     |     |     |     |
| ---------- | ---- | -------- | ------- | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
[7]alsoestablishesthisresult.Ourpaperalsoestablishesacon-
butmayhavenone.Independentlydevelopedrecentresultsby verse: that MaxProduct will fail on edges where the LP has a
Bayatietal.[7]provideanalternativeproofforoneofthetwo
fractionalvalueatsomeoptimum.Parallelwork[13]establishes
theorems—Theorem 1 which shows that tightness of LP im- thisconverseforthemoregeneralproblemoffindingthemax-
| plies BP | success—for | the | conceptually |     | harder case | of perfect |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ------------ | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
imumweightindependentset.
matchings.Theirproofalsoholdsforarbitrarymessageupdate
Arelatedbutseparatealgorithmicapproachtoinferenceare
schedules. thevariationaltechniquesdevelopedby[14](see[15]foramore
| The outline | of  | the paper | is as | follows. | In Section | III we set |     |     |     |     |     |     |     |
| ----------- | --- | --------- | ----- | -------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
recenttutorialsurveyofthisandrelatedmethods).ForMLes-
| up the weighted |     | matching | problem | and | its LP relaxation. | We  |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
timation,thesealgorithmsinvolveavariantofdirectcoordinate
| describe | the max-product |             | algorithm | for       | weighted matching |            | in         |          |        |         |           |           |       |
| -------- | --------------- | ----------- | --------- | --------- | ----------------- | ---------- | ---------- | -------- | ------ | ------- | --------- | --------- | ----- |
|          |                 |             |           |           |                   |            | descent on | the dual | of the | LP. The | algorithm | in[16] is | shown |
| Section  | IV. The         | main result | of        | the paper | is stated         | and proved |            |          |        |         |           |           |       |
toalwaysconvergetothedualoptimumforbinarypairwisein-
in Section V. In Section VI we establish the extensions to tegerproblems;moregenerallyconvergenceofthesealgorithms
| -matchingand |     | -edge-cover.Finally,inSectionVIIweshow |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
isnotfullyunderstood.
| how max-product |     | can be | radically | simplified | to make | it very |     |     |     |     |     |     |     |
| --------------- | --- | ------ | --------- | ---------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
amenableforimplementation. III. WEIGHTEDMATCHINGANDITSLPRELAXATION
|     |     |     |     |     |     |     | Supposethatwearegivenagraph |     |     |     | withedge-weights |     | .   |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ---------------- | --- | --- |
II. RELATEDWORK Amatchingisanysubsetofedgessuchthatthetotalnumberof
|     |     |     |     |     |     |     | edgesincidenttoanynode |     |     | isatmost1.Theweightedmatching |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ----------------------------- | --- | --- | --- |
Thispaperprovesnewresultsonthecorrectnessandconver-
|                    |     |                                   |     |     |     |     | problem | is to find | the matching | of  | largest | weight. Weighted |     |
| ------------------ | --- | --------------------------------- | --- | --- | --- | --- | ------- | ---------- | ------------ | --- | ------- | ---------------- | --- |
| genceofLoopyBelief |     | Propagationfortheweightedmatching |     |     |     |     |         |            |              |     |         |                  |     |
matchingcanbeformulatedasthefollowingintegerprogram:
problemongeneralgraphs.Beliefpropagationanditsvariants
| have proven | extremely | popular       |     | in practice | for the      | solution of |     |     |     |     |     |     |     |
| ----------- | --------- | ------------- | --- | ----------- | ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
| large-scale | problems  | in inference, |     | constraint  | satisfaction | etc.;       |     |     |     |     |     |     |     |
hereweprovideasummaryoftheworkmostdirectlyrelatedto
this paper.
| Classical        | BP  | in graphical | models |          | has two common    | fla- |     |     |     |     |     |     |     |
| ---------------- | --- | ------------ | ------ | -------- | ----------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| vors—SumProduct, |     | which        | is     | used for | finding marginals | of   |     |     |     |     |     |     |     |
individual/smallgroupsofvariables,andMaxProduct,whichis
|     |     |     |     |     |     |     | Here | is the set | of edges | incident | to node | . The linear | pro- |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | -------- | -------- | ------- | ------------ | ---- |
usedforfindingtheglobalmostlikelyassignmentofvariables. gramming(LP)relaxationoftheaboveproblemistoreplacethe
|            |             |       |       |              |           |              | constraint |     | withtheconstraint |     |     | ,foreach |     |
| ---------- | ----------- | ----- | ----- | ------------ | --------- | ------------ | ---------- | --- | ----------------- | --- | --- | -------- | --- |
| 2[10] uses | a graphical | model | which | is different | from ours | to represent |            |     |                   |     |     |          |     |
weightedmatching,butthisdoesnotchangetheresults. .Wedenotethecorrespondinglinearprogramby .
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 26,2025 at 03:18:15 UTC from IEEE Xplore.  Restrictions apply.

| SANGHAVIetal.:BELIEFPROPAGATIONANDLPRELAXATION |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 2205 |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
Inthispaper,weareinterestedinthepresenceorabsenceof IV. MAX-PRODUCTFORWEIGHTEDMATCHING
| fractionaloptimafor |     |     | .Anoptimum                           |     | of  | isfractionalif |     |                 |     |      |           |             |     |         |         |
| ------------------- | --- | --- | ------------------------------------ | --- | --- | -------------- | --- | --------------- | --- | ---- | --------- | ----------- | --- | ------- | ------- |
|                     |     |     |                                      |     |     |                |     | The Max-product |     | form | of belief | propagation |     | is used | to find |
| thereexistssomeedge |     |     | towhichitassignsfractionalmass,i.e., |     |     |                |     |                 |     |      |           |             |     |         |         |
themostlikelystate—theMAPestimate—ofaprobabilitydis-
| ifthereisan |     | suchthat |     | .Notethat |     | willhaveno |     |     |     |     |     |     |     |     |     |
| ----------- | --- | -------- | --- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tribution,whenthisdistributionisknowntobeaproductoffac-
| fractionaloptimaifandonlyif |     |     |     | hasauniqueoptimum,and |     |     |     |            |          |         |      |      |        |        |            |
| --------------------------- | --- | --- | --- | --------------------- | --- | --- | --- | ---------- | -------- | ------- | ---- | ---- | ------ | ------ | ---------- |
|                             |     |     |     |                       |     |     |     | tors, each | of which | depends | only | on a | subset | of the | variables. |
thisoptimumisintegral.
Max-productoperatesbyiterativelypassingmessagesbetween
Example 0 (Fractional Optima of ): Consider, for ex- variables and the factors they are a part of. In order to apply
ample,thefollowingthreegraphs. max-product, we now formulate weighted matching on as
|     |     |     |     |     |     |     |     | a MAP                      | estimation   | problem, | by           | constructing              | a         | suitable  | proba- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | ------------ | -------- | ------------ | ------------------------- | --------- | --------- | ------ |
|     |     |     |     |     |     |     |     | bility distribution.       |              | This     | construction | is                        | naturally | suggested | by     |
|     |     |     |     |     |     |     |     | theformoftheintegerprogram |              |          |              | .Associateabinaryvariable |           |           |        |
|     |     |     |     |     |     |     |     |                            | witheachedge |          |              | ,andconsiderthefollowing  |           |           |        |
probabilitydistribution:
(1)
| In the | cycle | on the | left, the | has | no fractional | optima: | the |     |     |     |     |     |     |     |     |
| ------ | ----- | ------ | --------- | --- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
uniqueoptimum(1,0,0)placesmass1ontheedgewithweight3, whichcontainsafactor foreachnode ,thevalue
and0ontheothertwoedges.Thetwocyclesontheright,how-
|     |     |     |     |     |     |     |     | of which | is  |     | if  |     | ,   | and 0 | otherwise. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | ----- | ---------- |
ever,dohavefractionaloptima.Themiddlecyclehas Note that we use to refer both to the nodes of and factors
| as its | unique | optimum, | while | the one | on the | right has | many |          |     |            |        |          |     |           |      |
| ------ | ------ | -------- | ----- | ------- | ------ | --------- | ---- | -------- | --- | ---------- | ------ | -------- | --- | --------- | ---- |
|        |        |          |       |         |        |           |      | of , and | to  | refer both | to the | edges of | and | variables | of . |
optima: (1,0,0), , and every convex combination of Thefactor enforcestheconstraintthatatmostoneedge
the two. Note that in the right-most cycle the LP relaxation is incident to node can be assigned the value “1”. It is easy to
| “tight”,i.e.,theoptimalvaluesof |     |     |     | and | areequal.Also,the |     |     |           |         |     |     |     |     |         |          |
| ------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --------- | ------- | --- | --- | --- | --- | ------- | -------- |
|                                 |     |     |     |     |                   |     |     | see that, | for any | ,   |     |     | if  | the set | of edges |
has a unique optimum. However, there still exist fractional constituteamatchingin ,and otherwise.
| optimaforthe |     | .   |     |     |     |     |     |            |            |     |          |                |     |     |         |
| ------------ | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | -------- | -------------- | --- | --- | ------- |
|              |     |     |     |     |     |     |     | Thus the   | max-weight |     | matching | of corresponds |     | to  | the MAP |
|              |     |     |     |     |     |     |     | estimateof | .          |     |          |                |     |     |         |
Notethatifthegraphisbipartite(i.e.,itcontainsnooddcy-
| cles),thenalltheextremepointsofthe |     |     |     |     | polytopeareintegral. |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Max-ProductforWeightedMatching
| As a                                | result, in | this | case, fractional | optima | exist            | if and | only | if  |     |     |     |     |     |     |     |
| ----------------------------------- | ---------- | ---- | ---------------- | ------ | ---------------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| therearemultipleintegraloptimaofthe |            |      |                  |        | .Thisisthereason |        |      |     |     |     |     |     |     |     |     |
ourTheorem1isageneralizationof[10]. (cid:129) (INIT)Set andinitializeeachmessageto1.
|     |     |     |     |     |     |     |     | (cid:129) (ITER) | Iteratively |     | compute | new messages |     | until |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ----------- | --- | ------- | ------------ | --- | ----- | --- |
WeneedthefollowinglemmafortheproofofTheorem1.Its
convergenceasfollows:
proofisobvious,andisomitted.
VariabletoFactor:
| Lemma1:          |     | Let | bethepolytopeoffeasiblesolutionsfor |     |     |     |     | ,   |     |     |     |     |     |     |     |
| ---------------- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| andlettheoptimum |     |     | beunique.Define                     |     |     |     |     |     |     |     |     |     |     |     |     |
FactortoVariable:
| Then,ithastobethat |     |           |        | .   |     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Remark:            | In  | the above | lemma, |     |     |     |     | is  |     |     |     |     |     |     |     |
the -norm of the perturbation from . The fact that the LP Also,ateach computebeliefs
| hasauniqueoptimummeansthatmovingawayfrom   |     |     |     |                           |     |              | along |                           |     |     |             |     |     |     |        |
| ------------------------------------------ | --- | --- | --- | ------------------------- | --- | ------------ | ----- | ------------------------- | --- | --- | ----------- | --- | --- | --- | ------ |
| anydirectionthatremainswithin              |     |     |     | willresultinastrictlinear |     |              |       |                           |     |     |             |     |     |     |        |
| decreaseintheobjectivefunction.Theconstant |     |     |     |                           |     | isnothingbut |       |                           |     |     |             |     |     |     |        |
|                                            |     |     |     |                           |     |              |       | (cid:129) (ESTIM)Eachedge |     |     | hasestimate |     |     |     | attime |
| thesmallestsuchrateofdecrease.Uniquenessof |     |     |     |                           |     | impliesthat  |       |                           |     |     |             |     |     |     |        |
shouldbestrictlypositive.
| Remark2:  |        | While     | hasbeendefinedviaaninfimumoverall |            |               |         |           |     |     |     |     |     |     |     |     |
| --------- | ------ | --------- | --------------------------------- | ---------- | ------------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| points    | in the | polytope, | it is                             | clear that | we can        | replace | this with |     |     |     |     |     |     |     |     |
| a minimum | over   | all       | extreme                           | points of  | the polytope. |         | So, if we |     |     |     |     |     |     |     |     |
considertheright-mosttrianglegraphinExample0above—the
one with edge weights 3,1,1–then . This is because The factor-graph version of the max-product algorithm [1]
the LPoptimumis withweight ,and passes messages between variables and the factors that con-
amongtheotherextremepoints(inthiscaseallfeasiblepoints tain them at each iteration . For the in (1), each variable is
whereeachcoordinateis0,1or [17])theonewhichachieves amemberofexactlytwofactors.Theoutputisanestimate of
the minimum is the point , which has weight the MAP of . We now present the max-product update equa-
|     | .   |     |     |     |     |     |     | tionsadaptedforthe |     |     | in(1).Weuse |     | and | todenotethe |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ----------- | --- | --- | ----------- | --- |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 26,2025 at 03:18:15 UTC from IEEE Xplore.  Restrictions apply.

2206 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.57,NO.4,APRIL2011
sameedge.Also,fortwosets and thesetdifferenceisde- isnotjustaparticularcase,itholdsingeneral—asstatedinthe
notedbythenotation . followingtheorem. We firststatethe most generalform ofthe
Notethatestimate meansthat,attime ,Max-product theorem,followedbycorollariesanddiscussion.
estimates that edge is part of a max-weight matching, while
Theorem2: Let beagraphwithnonnegativereal
means that it is not. means that Max-product
weights ontheedges .Thecorresponding may,in
cannot decide on the membership of . In this paper, we will
general,havemultipleoptima.Then,foranyedge in ,
saythatthemax-productestimateforanedgeisuninformative
1) If there existsany optimum of for which the mass
ifitsvaluekeepschangingevenafteralargeamountoftimehas
assignedtoedge satisfies ,thenthemax-product
passed,orifitsvalueremainsconstantandequalto?.
estimate is1or?foralloddtimes .
The message update rules are described above in a form
2) If there existsany optimum of for which the mass
familiar to readers already acquainted with Max-product. In
assignedtoedge satisfies ,thenthemax-product
SectionVIIweshowthattheupdaterulescanbesubstantially
estimate is0or?foralleventimes .
simplified into a “node-to-node” protocol that is much more
amenabletoimplementation. Remark: Inlightofthistheorem,itiseasytoseethatmax-
productyieldsusefulestimatesforalledgesifandonlyifeach
has an integral value that is consistent at all optima of
V. MAINRESULTS
LP.Thismeansthat hastohaveauniqueoptimum,andthis
Wenowstateandprovethemainresultsofthispaper.The- optimumhastobeintegral.Hence,Theorem1istight:anydevi-
orem1statesthatwhenevertheLPrelaxationhasnofractional ationfromthesufficientconditionthereinwillresultinuseless
optima, max-product is successful at finding the max-weight estimatesforsomeedges.
matching. Theorem 2, and Corollary 1, state the converse: if
Corollary1: Supposethe hasatleastonefractionalop-
thereexistfractionaloptima,thenmax-productwillfail.
timum. Then, Theorem 2 implies that max-product estimates
Theorem 1: Let be a graph with nonnegative
will be uninformative for all edges that are assigned noninte-
realweights ontheedges .Ifthelinearprogramming
gralmassatany optimum.
relaxation has no fractional optima, then the max-product
Inthecaseofnonuniqueoptima,notethatinTheorem2the
estimate iscorrect(i.e.,itisthetruemax-weightmatching)
choiceofLPoptimum isallowedtodependon ,theedgeof
foralltimes ,where isthemaximumweightof
interest.Thus,ifthereareoptima and of suchthat
anyedgeinthegraph,and isasdefinedinLemma1.
and , then the estimate willeither keep changing at
Remark 1: Note that the requirement of “no fractional op- everyiteration,orwillremainfixedat ,anuninformative
tima”isequivalenttosayingthatthe hasauniqueoptimum, estimate. It is thus easyto see thatTheorem 2 coversboth the
andthatthisoptimumisintegral.Thetimeafterwhichthees- case when the LP relaxation is loose (has no integral optima),
timates willconvergetocorrectvaluesisdeterminedbythe andthecasewhentheLPrelaxationistight,butmultipleoptima
“pointedness”ofthe polytopeattheoptimum,asrepresented exist.
bytheconstant ofLemma1. In general, when fractional optima exist, max-product may
Asnotedpreviously,therequirementofabsenceoffractional convergetousefulestimatesforsomeedgesandoscillateorbe
optima is in general strictly stronger than tightness of the LP uninformativeforothers.Itfollowsfromtheorem2that
relaxation. It is illustrativeat this point to consider the perfor- (cid:129) The useful estimates are exactly as predicted by the LP
mance of max-product on the right-most graph in Example 0: relaxation: if for some , then for
the three-cycle with weights 2,1,1. For this there are infinitely alloptima of , and correspondingly if then
manyoptimalsolutionsto :(1,0,0), ,andallconvex .
combinations of the two. Thus, eventhough the LP relaxation (cid:129) Anyedgewithfractionalmass willnothave
is tight, there exist fractional optima. For this graph, it can be useful estimates. However, the converse is not true: there
easily verified (e.g., using the computation tree interpretation may exist edges that are assigned the same integral mass
below)thattheestimatesasafunctionoftimewilloscillateas ineverymax-weightmatching,butforwhichmax-product
showninthetablebelow. isun-informative.Thus,inasenseMax-productisweaker
thanLPrelaxationforthematchingproblem.Considerthe
examplebelow.
Theunique optimumputsmass onallsixedgesinthe
Weseethattheedgeswithweights1willhaveestimatesthat twotriangles,mass1onthemiddleedgeofweight1.1,andmass
oscillatebetween0and?,whiletheedgewithweight2willos- 0 on the other two edges in the path. Max-product estimates
cillatebetween1and?.Theoscillatorybehaviorofthisexample oscillatebetween0and1onalledges.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 26,2025 at 03:18:15 UTC from IEEE Xplore. Restrictions apply.

| SANGHAVIetal.:BELIEFPROPAGATIONANDLPRELAXATION |     |     |     |     |     |     |     |     |     |     |     |     |     | 2207 |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
Fig.1. Computationtreefigureforexample1.
We now proceed to prove the two theorems above. Both Example 1 (Concepts Related to Computation Trees):
proofs rely on the well-known computation tree interpretation Consider Fig. 1. appears on the left, the numbers are the
of Max-product beliefs [5], [12], which we describe first. The edge weights and the letters are node labels. The max-weight
proofsfollowimmediatelyafter. matching on is , depicted in bold on
|     |     |     |     |     |     |     | .Inthecenterplotweshow |     |     |     | ,thecomputationtreeat |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --------------------- | --- | --- | --- |
A. TheComputationTreeforWeightedMatching time rootedatedge .Eachnodeislabeledinaccor-
|                                     |             |     |                                |                   |     |     | dancetoitscopyin |     | .Theboldedgesinthemiddletreedepict |              |     |     |      |     |
| ----------------------------------- | ----------- | --- | ------------------------------ | ----------------- | --- | --- | ---------------- | --- | ---------------------------------- | ------------ | --- | --- | ---- | --- |
| Recallthevariablesofthedistribution |             |     |                                | in(1)correspondto |     |     |                  |     |                                    |              |     |     |      |     |
|                                     |             |     |                                |                   |     |     | , the matching   |     | which                              | is the image | of  |     | onto | .   |
| edgesin                             | ,andnodesin |     | correspondtofactors.Foranyedge |                   |     |     |                  |     |                                    |              |     |     |      |     |
,the computationtreeat time rootedat ,which wedenote The weight of this matching is 6.6, and it is easy to see that
|                                    |     |     |     |     |               |     | anymatchingon |      |             | thatincludestherootedgewillhave |       |     |              |     |
| ---------------------------------- | --- | --- | --- | --- | ------------- | --- | ------------- | ---- | ----------- | ------------------------------- | ----- | --- | ------------ | --- |
| by ,isdefinedrecursivelyasfollows: |     |     |     |     | isjusttheedge |     |               |      |             |                                 |       |     |              |     |
|                                    |     |     |     |     |               |     | weight at     | most | 6.6. In the | right-most                      | tree, | the | dotted edges |     |
,therootofthetree.Thetwoendpointsoftheroot(nodesof
|                           |                            |          |                   |        |              |           | represent                                         | ,themax-weightmatchingonthetree |             |               |                     |                |                 | .   |
| ------------------------- | -------------------------- | -------- | ----------------- | ------ | ------------ | --------- | ------------------------------------------------- | ------------------------------- | ----------- | ------------- | ------------------- | -------------- | --------------- | --- |
| )aretheleavesof           |                            | .Thetree |                   | attime | isgenerated  |           |                                                   |                                 |             |               |                     |                |                 |     |
|                           |                            |          |                   |        |              |           | hasweight7.3.Inthisexampleweseethateventhough     |                                 |             |               |                     |                |                 | is  |
| from                      | by adding                  | to       | each leaf         | of     |              | a copy of |                                                   |                                 |             |               |                     |                |                 |     |
|                           |                            |          |                   |        |              |           | intheuniqueoptimalmatchingin                      |                                 |             |               | ,itturnsoutthatroot |                |                 |     |
| each of its               | neighbor                   | edges    | in , except       | for    | the neighbor | edge      |                                                   |                                 |             |               |                     |                |                 |     |
|                           |                            |          |                   |        |              |           | is not a member                                   |                                 | of any      | max-weight    | matching            |                | on              | ,   |
| thatisalreadypresentin    |                            |          | .Eachedgein       |        |              | isacopy   |                                                   |                                 |             |               |                     |                |                 |     |
|                           |                            |          |                   |        |              |           | and hence                                         | we have                         | that        |               | . Note              | also           | that the dotted |     |
| ofanedgein                | ,andtheweightsoftheedgesin |          |                   |        | arethesame   |           |                                                   |                                 |             |               |                     |                |                 |     |
|                           |                            |          |                   |        |              |           | edgesarenotanimageofanymatchingintheoriginalgraph |                                 |             |               |                     |                |                 | .   |
| asthecorrespondingedgesin |                            |          | .                 |        |              |           |                                                   |                                 |             |               |                     |                |                 |     |
|                           |                            |          |                   |        |              |           | Thisexamplethus                                   |                                 | illustrates | how“spurious” |                     | matchingsinthe |                 |     |
| For any                   | edge and                   | time     | , the max-product |        | estimate     | accu-     |                                                   |                                 |             |               |                     |                |                 |     |
computationtreecanleadtoincorrectbeliefs,andestimates.In
| rately represents | the | membership | of  | the root | in max-weight |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theexampleabovethereasonwhyMax-productdisagreeswith
| matchings | on the computation |     | tree | ,   | as opposed | to the |     |     |     |     |     |     |     |     |
| --------- | ------------------ | --- | ---- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
LPrelaxationisthatMax-producthasnotyetconverged.
| original graph | . This | is the | computation |     | tree interpretation, |     |     |     |     |     |     |     |     |     |
| -------------- | ------ | ------ | ----------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andisstatedformallyinthefollowinglemma(foraproof,see
|     |     |     |     |     |     |     | B. ProofofTheorem1 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
e.g., [5]).
|           |                      |     |        |                  |     |     | We now                            | prove | that the | uniqueness | and                | tightness | of the | LP  |
| --------- | -------------------- | --- | ------ | ---------------- | --- | --- | --------------------------------- | ----- | -------- | ---------- | ------------------ | --------- | ------ | --- |
| Lemma2:   | Foranyedge           |     | attime | ,                |     |     |                                   |       |          |            |                    |           |        |     |
|           |                      |     |        |                  |     |     | relaxationensuresthateachestimate |       |          |            | is0or1,andalsothat |           |        |     |
| (cid:129) | ifandonlyiftherootof |     |        | isamemberofevery |     |     |                                   |       |          |            |                    |           |        |     |
theestimatecorrespondstotheoptimalmatching.Asmentioned
| max-weightmatchingon |     |     | .   |     |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
intheIntroduction,thisisageneralizationofthebipartitegraph
| (cid:129)               | ifandonlyiftherootof |     |     |     | isnotamemberof |     |                                                |     |       |                                 |      |      |                 |     |
| ----------------------- | -------------------- | --- | --- | --- | -------------- | --- | ---------------------------------------------- | --- | ----- | ------------------------------- | ---- | ---- | --------------- | --- |
|                         |                      |     |     |     |                |     | result in [10]—since                           |     | it is | well known                      | [17] | that | inthe bipartite |     |
| anymax-weightmatchingon |                      |     |     | .   |                |     |                                                |     |       |                                 |      |      |                 |     |
|                         |                      |     |     |     |                |     | caseallverticesoftheLPpolytopeareintegral.3Let |     |       |                                 |      |      | bethe           |     |
| (cid:129)               | else.                |     |     |     |                |     |                                                |     |       |                                 |      |      |                 |     |
|                         |                      |     |     |     |                |     | optimalmatching,and                            |     |       | thecorresponding0–1vectorthatis |      |      |                 |     |
Remarks: The beliefs are the max-marginals at the theuniqueoptimumof .
| root of the | computation | tree | . If |     |     | then any |          |     |          |         |         |       |       |       |
| ----------- | ----------- | ---- | ---- | --- | --- | -------- | -------- | --- | -------- | ------- | ------- | ----- | ----- | ----- |
|             |             |      |      |     |     |          | To prove | the | theorem, | we need | to show | that, | for a | large |
matching in which excludes the root has a suboptimal enoughtime ,theestimatessatisfy
| weight.Similarly,if                       |     |     | ,thenanymatchingin |     |             |     |     |     |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | ------------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| includingtherootissuboptimal.However,when |     |     |                    |     |             |     | ,   |     |     |     |     |     |     |     |
| thenthereexistsanoptimalmatchingwith      |     |     |                    |     | ,andanother |     |     |     |     |     |     |     |     |     |
| optimalmatchingwith                       |     |     | .                  |     |             |     |     |     |     |     |     |     |     |     |
Note that max-product estimates correspond to max-weight Considernowanytime ,where is
| matchingsonthecomputationtrees |     |     |     | ,asopposedtoonthe |     |     |                                |     |     |     |                    |     |     |     |
| ------------------------------ | --- | --- | --- | ----------------- | --- | --- | ------------------------------ | --- | --- | --- | ------------------ | --- | --- | --- |
|                                |     |     |     |                   |     |     | theweightoftheheaviestedge,and |     |     |     | isasinLemma1above. |     |     |     |
originalgraph .Suppose isamatchingontheoriginalgraph Supposethatthereexistsanedge forwhichtheestimate
| , and | is a computation |     | tree. Then, | the | image of | in  |     |     |     |     |     |     |     |     |
| ----- | ---------------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is the set of edges in whose corresponding copy in is a 3Ourproofbelowisalongsimilarlinestotheonein[10],namelythatboth
proofsproceedviacontradictionbyconstructinganewoptimum.In[10],this
| memberof | .Wenowillustratetheideasofthissectionwith |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
newoptimumisactuallyanalternatematchingonthecomputationtree;inours
| asimpleexample. |     |     |     |     |     |     | itisanewLPoptimum. |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 26,2025 at 03:18:15 UTC from IEEE Xplore.  Restrictions apply.

2208 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.57,NO.4,APRIL2011
attime isnotcorrect: (i.e., ).Wenowshow a maximal alternating path that the root . Using Lemma 3, it
thatthisleadstoacontradiction. followsthat .Now,asbefore,define
We start with a brief outline of the proof. Let be the .Itfollowsthat
computationtreeattime forthatedge .FromLemma2,the ,violatingtheassumptionthat isanoptimalmatching
factthat meansthatthereexistsamax-weightmatching in . Thus the root has to have . This proves the
| on                         |     | thatdoesnotcontaintheroot |       |     | .Duetotheunique- |           |      | theorem.           |     |     |     |     |     |     |
| -------------------------- | --- | ------------------------- | ----- | --- | ---------------- | --------- | ---- | ------------------ | --- | --- | --- | --- | --- | --- |
| nessoftheLPoptimumwecanuse |     |                           |       |     | tomodify         | andobtain |      |                    |     |     |     |     |     |     |
|                            |     |                           |       |     |                  |           |      | C. ProofofTheorem2 |     |     |     |     |     |     |
| a matching                 |     | on                        | which | has | strictly larger  | weight    | than |                    |     |     |     |     |     |     |
.Thiscontradictstheoptimalityof on ,andproves We now prove Theorem 2. Suppose part 1 is not true, i.e.,
that hastobeequalto1. there exists edge , an optimum of with , and
Wenowgivethedetailsinfull.Let betheimageof an odd time at which the estimate is . Let be
onto . By assumption, in original graph , and thecorrespondingcomputationtree.UsingLemma2thismeans
hence the root . Recall that, from Lemma 2, thattheroot isnotamemberofanymax-weightmatchingof
impliesthereexistssomemax-weightmatching of that .Let besomemax-weightmatchingon .Wenow
does not contain the root,i.e., root . Thus the root definethefollowingsetofedges
|                 | .Fromroot |        | ,buildanalternatingpath        |             |                       | on     | by      |           |            |          |     |     |           |          |
| --------------- | --------- | ------ | ------------------------------ | ----------- | --------------------- | ------ | ------- | --------- | ---------- | -------- | --- | --- | --------- | -------- |
| successively    |           | adding | edges                          | as follows: | first add             | , then | add all |           |            |          |     |     |           |          |
| edgesadjacentto |           |        | thatarein                      |             | ,thenalltheiradjacent |        |         |           |            |          |     |     |           |          |
| edgesthatarein  |           |        | ,andsoforthuntilnomoreedgescan |             |                       |        |         |           |            |          |     |     |           |          |
|                 |           |        |                                |             |                       |        |         | In words, | is the set | of edges | in  |     | which are | not in , |
beadded.Thiswilloccureitherbecausenoedgesareavailable
thatmaintainthealternatingstructure,orbecausealeafof andwhosecopiesin areassignedstrictlypositivemassbythe
|     |              |     |               |     |                |         |     | LPoptimum | .   |     |     |     |     |     |
| --- | ------------ | --- | ------------- | --- | -------------- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- |
| has | beenreached. |     | Note alsothat |     | will be apath, | because |     |           |     |     |     |     |     |     |
and are matchings and so any node in can have at Notethatbyassumptiontheroot andhence .
mostoneadjacentedgeineachofthetwomatchings. Now, as done in the proof of Theorem 1, build a maximal al-
|                                              |     |     |     |     |     |     |        | ternating | path which | includes | the | root | , and alternates | be- |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --------- | ---------- | -------- | --- | ---- | ---------------- | --- |
| Forillustration,considerExample1ofSectionIV. |     |     |     |     |     |     | inthis |           |            |          |     |      |                  |     |
case is the edge , and is denoted by the bold edges tweenedgesin andedgesin .Bymaximal,wemeanthat
|        |           |        |     |                 |     |      |         | it should | not be possible | to  | add edges | to  | and still | maintain |
| ------ | --------- | ------ | --- | --------------- | --- | ---- | ------- | --------- | --------------- | --- | --------- | --- | --------- | -------- |
| in the | left-most | figure | .   | The computation |     | tree | at time |           |                 |     |           |     |           |          |
4 is shown in the center, with the image marked in bold. itsalternatingstructure.NotethatincontrasttoTheorem1,we
Notethattheroot .Intheright-mostfigureisdepicted mayhavemultipleedgesin touchinganode.Insuchacase,
|                                                    |              |     |          |     |                   |     |      | wepickanarbitraryoneofthemandaddto |     |     |     |     | .Weusethefol- |     |
| -------------------------------------------------- | ------------ | --- | -------- | --- | ----------------- | --- | ---- | ---------------------------------- | --- | --- | --- | --- | ------------- | --- |
| ,                                                  | a max-weight |     | matching | of  | . The alternating |     | path | ,                                  |     |     |     |     |               |     |
| asdefinedabove,wouldinthisexamplebethepathadcabcda |              |     |          |     |                   |     |      | lowinglemma.                       |     |     |     |     |               |     |
thatgoesfromtheleft-mostleaftotheright-mostleaf.Itiseasy
|                                           |     |     |     |     |     |     |     | Lemma4: | Theweightssatisfy |     |     |     |     | .   |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------------- | --- | --- | --- | --- | --- |
| toseethatthispathalternatesbetweenedgesin |     |     |     |     |     |     | and |         |                   |     |     |     |     |     |
Theproofisincludedintheappendixandissimilarinprin-
|     | .   | We now | use the | following | lemma | to complete | the |          |               |       |             |     |            |            |
| --- | --- | ------ | ------- | --------- | ----- | ----------- | --- | -------- | ------------- | ----- | ----------- | --- | ---------- | ---------- |
|     |     |        |         |           |       |             |     | ciple to | that of Lemma | 3: if | the weights |     | are not as | specified, |
proofofTheorem1.
|     |     |     |     |     |     |     |     | thenitispossibletoperturb |     |     | toobtainafeasiblesolutionof |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --------------------------- | --- | --- | --- |
Lemma 3: Suppose has no fractional optima. Let be withstrictlyhighervaluethan ,thusviolatingtheassump-
amatchingin whichdisagreeswith ontheroot,i.e., tionthat isanoptimumof .Thefactthat isoddisused
root .Let bethemaximalal- toensurethattheperturbationresultsinafeasiblepoint.
ternatingpathcontainingtheroot.Then WenowuseLemma4tofinishtheproofofpart1ofTheorem
| ,provided |     |     | .   |     |     |     |     | 2.Consider |     |     |     |     | ,whichisanew |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ------------ | --- |
Lemma3isprovedintheappendix,usingaperturbationar- matching of . Lemma 4 implies that ,
gument: if lemma is false, then it is possible to perturb to i.e., isalsoamax-weightmatchingof .However,note
obtainanewfeasiblepoint suchthat ,thus thattheroot ,andsothiscontradictsthefactthatroot
violatingtheoptimalityanduniquenessof fortheLPon . shouldnotbeinanymax-weightmatchingof .Thisproves
Now consider the matching , and change it by “flipping” part1ofthetheorem.
theedgesin .Specifically,let Part 2 is proved in a similar fashion, with the perturbation
bethematchingcontainingalledgesin excepttheonesin , argumentnowrequiringthat beodd.Specifically,supposepart
| whicharereplacedbytheedgesin |     |     |     |     | .Itiseasytoseethat |     |     |                                  |     |     |     |            |     |     |
| ---------------------------- | --- | --- | --- | --- | ------------------ | --- | --- | -------------------------------- | --- | --- | --- | ---------- | --- | --- |
|                              |     |     |     |     |                    |     |     | 2isnottrue,thenthereexistsanedge |     |     |     | ,anoptimum |     | of  |
is a matching in . Also, from Lemma 3(a) it follows with ,andaneventime atwhichtheestimateis
that . This however, violates the assumption . This implies that root is a member of every max-weight
that is an optimal matching in . We have arrived at a matchingof .Let beanysuchmax-weightmatchingin
contradiction,andthusithastobethecasethat forall ,anddefinethefollowingsetofedges
.
| A       | similar | argument | can         | be used | to establish | that     |          |     |     |     |     |     |     |     |
| ------- | ------- | -------- | ----------- | ------- | ------------ | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| for all |         | . In     | particular, | suppose | that         |          | for some |     |     |     |     |     |     |     |
|         | . This  | means    | there       | exists  | a max-weight | matching |          |     |     |     |     |     |     |     |
in that contains the root . Again, let be the image In words, is the set of edges in which are not in ,
of onto .Notethattheroot .Let be andwhosecopiesin areassignedstrictlypositivemassbythe
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 26,2025 at 03:18:15 UTC from IEEE Xplore.  Restrictions apply.

| SANGHAVIetal.:BELIEFPROPAGATIONANDLPRELAXATION |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 2209 |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
LPoptimum .Notethattheroot andhence . B. Weighted -Edge-Cover
| Let beamaximalalternatingpathwhichincludestheroot |                   |                                      |     |            |            |               |        | ,                                 |                   |     |             |         |     |             |             |
| ------------------------------------------------- | ----------------- | ------------------------------------ | --- | ---------- | ---------- | ------------- | ------ | --------------------------------- | ----------------- | --- | ----------- | ------- | --- | ----------- | ----------- |
|                                                   |                   |                                      |     |            |            |               |        | The                               | min-weight        |     | -edge-cover | problem | is  | given       | by the fol- |
| andalternatesbetweenedgesin                       |                   |                                      |     | andedgesin |            | .             |        |                                   |                   |     |             |         |     |             |             |
|                                                   |                   |                                      |     |            |            |               |        | lowingintegerprogram:givennumbers |                   |     |             |         |     | foreachnode |             |
| Lemma5:                                           | Theweightssatisfy |                                      |     |            |            |               | .      | ,where                            | isthedegreeofnode |     |             |         |     |             |             |
| The proof                                         | of                | this lemma                           | is  | similar    | to that of | Lemma         | 4, and |                                   |                   |     |             |         |     |             |             |
| isgivenintheappendix.Itusesthefactthat            |                   |                                      |     |            |            | iseven.Now,as |        |                                   |                   |     |             |         |     |             |             |
| before,consider                                   |                   |                                      |     |            |            | ,whichisa     |        |                                   |                   |     |             |         |     |             |             |
| newmatchingof                                     |                   | .Lemma5impliesthat                   |     |            |            |               |        | ,                                 |                   |     |             |         |     |             |             |
| i.e., isalsoamax-weightmatchingof                 |                   |                                      |     |            |            | .However,note |        |                                   |                   |     |             |         |     |             |             |
| thattheroot                                       |                   | ,andsothiscontradictsthefactthatroot |     |            |            |               |        |                                   |                   |     |             |         |     |             |             |
| shouldbeineverymax-weightmatchingof               |                   |                                      |     |            |            | .Thisproves   |        |                                   |                   |     |             |         |     |             |             |
part2ofthetheorem. TheLPrelaxationof isobtainedbyreplacingtheconstrains
|     |     |     |            |     |     |     |     |         |        | by the        | constraints |                |     | for each | .          |
| --- | --- | --- | ---------- | --- | --- | --- | --- | ------- | ------ | ------------- | ----------- | -------------- | --- | -------- | ---------- |
|     |     |     |            |     |     |     |     | We will | denote | the resulting |             | linear program |     | by       | . To apply |
|     |     | VI. | EXTENSIONS |     |     |     |     |         |        |               |             |                |     |          |            |
max-product,considerthefollowingprobabilitydistribution
| We now      | establish    | the | extensions |                             | of Theorems | 1 and | 2   | to  |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | ---------- | --------------------------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| theweighted | -matchingand |     |            | -edge-coverproblems.Themain |             |       |     |     |     |     |     |     |     |     | (2) |
ideasremainunchanged,andthustheproofsareoutlines,with
justtheimportantdifferencesfromthecorrespondingproofsfor
|     |     |     |     |     |     |     |     | Here the | factor |     | for | node takes | value | 1 if | and only |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --- | --- | ---------- | ----- | ---- | -------- |
thesimplematchinghighlighted.
|     |     |     |     |     |     |     |     | if  |     | , and | 0 otherwise. |     | It is easy | to see | that any |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | ---------- | ------ | -------- |
A. Weighted -Matching maximum of corresponds to a min-weight -edge-cover of
|                             |     |                                       |     |     |             |     |     | the graph. | The        | max-product |     | updates   | remain   | as specified | in    |
| --------------------------- | --- | ------------------------------------- | --- | --- | ----------- | --- | --- | ---------- | ---------- | ----------- | --- | --------- | -------- | ------------ | ----- |
| Theweighted                 |     | -matchingproblemisgivenbythefollowing |     |     |             |     |     |            |            |             |     |           |          |              |       |
|                             |     |                                       |     |     |             |     |     | Section    | IV, except | that        |     | should be | replaced | by           | . The |
| integerprogram:givennumbers |     |                                       |     |     | foreachnode |     |     |            |            |             |     |           |          |              |       |
twotheoremsarenowstatedhere.
|                      |                                          |         |         |                  |               |          |         | Theorem5:                     |         | If -                               | hasnofractionaloptima,thenthemax- |         |                   |        |         |
| -------------------- | ---------------------------------------- | ------- | ------- | ---------------- | ------------- | -------- | ------- | ----------------------------- | ------- | ---------------------------------- | --------------------------------- | ------- | ----------------- | ------ | ------- |
|                      |                                          |         |         |                  |               |          |         | productestimate               |         | iscorrect(i.e.,itisthetruemin-cost |                                   |         |                   |        | -edge-  |
|                      |                                          |         |         |                  |               |          |         | cover)                        | for all | times                              |                                   | , where |                   | is the | maximum |
|                      |                                          |         |         |                  |               |          |         | weightofanyedgeinthegraph,and |         |                                    |                                   |         | isasdefinedbelow( |        | is      |
|                      |                                          |         |         |                  |               |          |         | thefeasiblepolytopeof         |         |                                    |                                   | )       |                   |        |         |
| The LP relaxation    |                                          | of this | integer | program          | is            | obtained | by re-  |                               |         |                                    |                                   |         |                   |        |         |
| placingtheconstrains |                                          |         |         | bytheconstraints |               |          |         |                               |         |                                    |                                   |         |                   |        |         |
| foreach              | .Wewilldenotetheresultinglinearprogramby |         |         |                  |               |          |         |                               |         |                                    |                                   |         |                   |        |         |
| .                    |                                          |         |         |                  |               |          |         | Theorem6:                     |         | Foranyedge                         |                                   | in ,    |                   |        |         |
|                      |                                          |         |         |                  |               |          |         | 1) Ifthereexistsanyoptimum    |         |                                    |                                   | of      | forwhichthemass   |        |         |
| To apply             | Max-product,                             |         | first   | consider         | a probability |          | distri- |                               |         |                                    |                                   |         |                   |        |         |
bution as in (1), but with now defined to be 1 if assignedtoedge satisfies ,thenthemax-product
, and 0 otherwise. The max-product updates estimate is1or?foralloddtimes .
|     |     |     |     |     |     |     |     | 2) Ifthereexistsanyoptimum |     |     |     | of  | forwhichthemass |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --------------- | --- | --- |
remainasspecifiedinSectionIV.Thefollowingtwotheorems
aretherespectivegeneralizationsofTheorems1and2. assignedtoedge satisfies ,thenthemax-product
|     |     |     |     |     |     |     |     | estimate |     | is0or?foralleventimes |     |     |     | .   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --------------------- | --- | --- | --- | --- | --- |
Theorem 3: If has no fractional optima, then the max- Theorems 5 and 6 are most easily obtained by mapping the
| product estimate |             | is       | correct | (i.e., it | is the | true max-weight |     |                                      |     |     |     |                             |                   |     |     |
| ---------------- | ----------- | -------- | ------- | --------- | ------ | --------------- | --- | ------------------------------------ | --- | --- | --- | --------------------------- | ----------------- | --- | --- |
|                  |             |          |         |           |        |                 |     | max-productupdatesforthe             |     |     |     | -edge-coverproblemtothoseof |                   |     |     |
| -matching)       | foralltimes |          |         | ,where    |        | is themax-      |     |                                      |     |     |     |                             |                   |     |     |
|                  |             |          |         |           |        |                 |     | the -matchingproblem.Inparticular,if |     |     |     |                             | isthedegreeofnode |     |     |
| imum weight      | of          | any edge | in the  | graph,    | and    | is as defined   |     | in                                   |     |     |     |                             |                   |     |     |
, set
| Lemma1(butwith             |            | beingthe |           | -matchingpolytope) |                     |     |     |       |          |     |      |             |     |                |     |
| -------------------------- | ---------- | -------- | --------- | ------------------ | ------------------- | --- | --- | ----- | -------- | --- | ---- | ----------- | --- | -------------- | --- |
| Theorem4:                  | Foranyedge |          |           | in ,               |                     |     |     |       |          |     |      |             |     |                |     |
| 1) Ifthereexistsanyoptimum |            |          |           | of                 | forwhichthemass     |     |     |       |          |     |      |             |     |                |     |
|                            |            |          |           |                    |                     |     |     | Then, | any edge |     | will | be included | in  | the min-weight |     |
| assignedtoedge             |            |          | satisfies |                    | ,thenthemax-product |     |     |       |          |     |      |             |     |                |     |
-edge-coverifandonlyifitisnotincludedinthemax-weight
| estimate                   |     | is1or?foralloddtimes  |           |     | .                   |     |     |                    |        |           |           |                   |       |            |             |
| -------------------------- | --- | --------------------- | --------- | --- | ------------------- | --- | --- | ------------------ | ------ | --------- | --------- | ----------------- | ----- | ---------- | ----------- |
|                            |     |                       |           |     |                     |     |     | -matching.         | The    | following |           | lemma             | shows | that there | is an       |
| 2) Ifthereexistsanyoptimum |     |                       |           | of  | forwhichthemass     |     |     |                    |        |           |           |                   |       |            |             |
|                            |     |                       |           |     |                     |     |     | exact relationship |        | between   |           | the max-product   |       | updates    | for the     |
| assignedtoedge             |     |                       | satisfies |     | ,thenthemax-product |     |     |                    |        |           |           |                   |       |            |             |
|                            |     |                       |           |     |                     |     |     | -edge-cover        |        | problem   | and       | the corresponding |       |            | -matching   |
| estimate                   |     | is0or?foralleventimes |           |     | .                   |     |     |                    |        |           |           |                   |       |            |             |
|                            |     |                       |           |     |                     |     |     | problem.           | It can | easily    | be proved | by induction,     |       | we         | include the |
TheproofsofboththeoremsaresimilartothoseofTheorems
proofintheappendix.
1and2,respectively.Inparticular,notethattherewillbeanal-
ternatingpathbetweenanytwo -matchingsonthecomputation Lemma6: Givenaweighted -edge-coverproblem,let de-
tree.Allthealternatingpathandperturbationargumentsremain notethemax-productmessagesand thebeliefs.Considernow
as before. the weighted -matching problem where edge weights remain
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 26,2025 at 03:18:15 UTC from IEEE Xplore.  Restrictions apply.

2210 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.57,NO.4,APRIL2011
thesameandeach .Let and denotethemes- Formally, We define two length- vectors and as fol-
sages and beliefs for this -matching problem. Then, we have lows:forevery intheoriginalgraph,
thatfortime ,node andedge , number of (copies of) that appear in .
|     |     |     |     |     |     |     |     |                            | Notethat                              |        | onlyforedges |     |                        | ,and      |        |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | ------------------------------------- | ------ | ------------ | --- | ---------------------- | --------- | ------ | --- |
|     |     |     |     |     |     |     |     |                            | forotheredges                         |        |              | .   |                        |           |        |     |
|     |     |     |     |     |     |     |     |                            |                                       | number | of (copies   | of) | that                   | appear    | in     | ,   |
|     |     |     |     |     |     |     |     |                            | excludingcopiesthattouchaleafof       |        |              |     |                        | .Notethat |        |     |
|     |     |     |     |     |     |     |     |                            | onlyfor                               |        | ,and         |     | for                    |           | .      |     |
|     |     |     |     |     |     |     |     | Intheabove,theleavesoftree |                                       |        |              |     | arenodesatthelastlevel |           |        |     |
|     |     |     |     |     |     |     |     | of                         | ,i.e.,furthestawayfromtheroot.Thepath |        |              |     |                        |           | hastwo |     |
endpoints,andhenceitcanhaveatmosttwoleafedgesin
|                        |     |     |     |                       |     |     |     |               | .Let | and beequaltotheweightsofthesetwoedges,if |                                     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --------------------- | --- | --- | --- | ------------- | ---- | ----------------------------------------- | ----------------------------------- | --- | --- | --- | --- | --- |
| Notenowthattheestimate |     |     |     | dependsonlyontheratio |     |     |     | .             |      |                                           |                                     |     |     |     |     |     |
|                        |     |     |     |                       |     |     |     | theyexist,and |      |                                           | ifthecorrespondingedgedoesnotexist. |     |     |     |     |     |
In particular, if and only if is, respectively, Then,wehavethat
| , , | to 1. | Thus, Lemma | 6   | implies | that the | -edge | cover |     |     |     |     |     |     |     |     |     |
| --- | ----- | ----------- | --- | ------- | -------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
max-product estimate for edge will be 1 if and only if the (3)
| corresponding |     | -matchingmax-productestimateis0.Similarly, |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(4)
| 0 maps to | 1, and | ? to ? | Thus, | Theorems | 5 and | 6 follow | from |     |     |     |     |     |     |     |     |     |
| --------- | ------ | ------ | ----- | -------- | ----- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Theorems3and4,respectively.
Foranillustrationofthesedefinitions,lookatthefootnote.4We
|     |     |     |     |     |     |     |     | are | now ready | to define | the | perturbation: |     | let | be a | small |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------------- | --- | --- | ---- | ----- |
VII. PROTOCOLSIMPLIFICATION
positivenumber,and
| In this  | section, | we show | that       | max-product |                | for the | weighted |     |     |     |     |     |     |     |     |     |
| -------- | -------- | ------- | ---------- | ----------- | -------------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| matching | problem  | can be  | simplified | for         | implementation |         | pur-     |     |     |     |     |     |     |     |     |     |
(5)
| poses. Similar |            | simplificationshavealso |               |           | been   | performed  | in [9] |     |          |               |     |           |        |       |           |     |
| -------------- | ---------- | ----------------------- | ------------- | --------- | ------ | ---------- | ------ | --- | -------- | ------------- | --- | --------- | ------ | ----- | --------- | --- |
| and [10].      | Recall     | that in the             | specification |           | given  | in Section | IV,    |     |          |               |     |           |        |       |           |     |
|                |            |                         |               |           |        |            |        | We  | now need | the following |     | auxiliary | lemma, | which | is proved |     |
| messages       | are passed | between                 |               | edges and | nodes. | However,   |        | it  |          |               |     |           |        |       |           |     |
laterintheAppendix.
wouldbemoredesirabletojusthaveanimplementationwhere
messages are passed only between nodes. Toward this end, Lemma 7: Thevector asdefined in(5)is afeasible point
| for every | pair of | neighbors | and | , let |     | be  | the edge |     |                          |     |     |     |     |     |     |     |
| --------- | ------- | --------- | --- | ----- | --- | --- | -------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
|           |         |           |     |       |     |     |          | of  | ,forasmallenoughchoiceof |     |     |     | .   |     |     |     |
connectingthetwo,anddefine Wenowfinditconvenienttoseparatelyconsidertwopossible
|     |     |     |     |     |     |     |     | scenariosforthepath |     |     | andweights |     | ,   | .   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- |
Case1:
SupposenowthatthestatementofLemma3isnottrue,i.e.,
| Theprotocolwiththe |     | -messagesisspecifiedbelow. |     |     |     |     |     |               |     |     |     |                    |                    |     |     |     |
| ------------------ | --- | -------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | ------------------ | ------------------ | --- | --- | --- |
|                    |     |                            |     |     |     |     |     | supposethat   |     |     |     |                    | .From(3)and(4),and |     |     |     |
|                    |     |                            |     |     |     |     |     | theassumption |     |     |     | ,itthenfollowsthat |                    |     |     | .   |
SimplifiedMax-ProductforWeightedMatching
|     |     |     |     |     |     |     |     | From(5)itthenfollowsthat |     |                                   |     |     | .Notealsothat |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --------------------------------- | --- | --- | ------------- | --- | --- | --- |
|     |     |     |     |     |     |     |     | because                  |     | .Wehavethusobtainedafeasiblepoint |     |     |               |     |     | of  |
(cid:129) (INIT)Set andinitializeeach the withweightatleastaslargeastheuniqueoptimum .
| (cid:129) (ITER) | Iteratively | compute |     | new messages |     | until |     |     |     |     |     |     |     |     |     |     |
| ---------------- | ----------- | ------- | --- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thisisacontradiction,andhenceforthiscaseithastobethat
convergenceasfollows:
.
|                                                 |           |        |               |            |       |             |          |                              | Case2:          | Atleastoneof                         |             | or  | isnonzero. |                  |          |     |
| ----------------------------------------------- | --------- | ------ | ------------- | ---------- | ----- | ----------- | -------- | ---------------------------- | --------------- | ------------------------------------ | ----------- | --- | ---------- | ---------------- | -------- | --- |
|                                                 |           |        |               |            |       |             |          |                              | For             | or tobenon-zero,atleastoneendpointof |             |     |            |                  |          | has |
|                                                 |           |        |               |            |       |             |          | to                           | be a leaf       | of                                   | . The tree  | has | depth      | , and            | contains | the |
|                                                 |           |        |               |            |       |             |          | rootandaleaf,sothepathlength |                 |                                      |             |     |            | .Now,foreachedge |          |     |
| (cid:129) (ESTIM)Uponconvergence,outputestimate |           |        |               |            |       |             | :for     |                              |                 |                                      |             |     |            |                  |          |     |
|                                                 |           |        |               |            |       |             |          |                              | ,               |                                      | ,andforeach |     |            | ,                |          |     |
| eachedgeset                                     |           |        |               | or?if      |       |             | is,      |                              |                 |                                      |             |     |            |                  |          |     |
| respectively,                                   |           | , ,or  |               | .          |       |             |          |                              | .Thuswehavethat |                                      |             |     |            |                  |          |     |
| The update                                      | equations |        | for -matching |            | and   | -edge-cover | can      |                              |                 |                                      |             |     |            |                  |          |     |
| alsobesimplifiedbydefining                      |           |        |               | ’sasabove. |       |             |          |                              |                 |                                      |             |     |            |                  |          |     |
| Proof                                           | of Lemma  | 3: The | outline       | of the     | proof | is as       | follows: |                              |                 |                                      |             |     |            |                  |          |     |
we will use to define a new feasible point of the by 4Forillustrationofthesedefinitions,wereferbacktoexample1ofSectionV.
modifying ,the unique optimumofthe .Weobtain by Thecomputationtreeinthecentershowstheprojection(cid:0) ,andthetreeon
|     |     |     |     |     |     |     |     | therightshowsamax-weightmatching(cid:0)on(cid:2) |     |     |     |     |     | (cid:0)(cid:2)(cid:3).Supposenow(cid:3) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- |
isthe
subtracting from foreveryedgein andadding pathstartingfromtheleft-mostleafof(cid:2) (cid:0)(cid:2)(cid:3)andendingattheright-most
for everyedgein ,countingrepeatedoccurrences.The leaf.Italternatesbetween(cid:0)and(cid:0) .Forthis(cid:3),wehavethatthevectorsare:
|                   |     |                    |     |     |     |              |     | (cid:4)                                           | (cid:4) (cid:5),(cid:4)    | (cid:4) | (cid:6),and(cid:4)                               | (cid:4) (cid:7)forallotheredges(cid:5).(cid:6) |     |     |         | (cid:4) (cid:5), |
| ----------------- | --- | ------------------ | --- | --- | --- | ------------ | --- | ------------------------------------------------- | -------------------------- | ------- | ------------------------------------------------ | ---------------------------------------------- | --- | --- | ------- | ---------------- |
| factthattheweight |     | isstrictlylessthan |     |     |     | willprovethe |     |                                                   |                            |         |                                                  |                                                |     |     |         |                  |
|                   |     |                    |     |     |     |              |     | (cid:6)                                           | (cid:4) (cid:5),and(cid:6) | (cid:4) | (cid:7)forallotheredges(cid:5).Theweights(cid:7) |                                                |     |     | (cid:4) | (cid:7) (cid:4)  |
| lemma.            |     |                    |     |     |     |              |     | weightofedge(cid:0)(cid:8)(cid:9)(cid:10)(cid:3). |                            |         |                                                  |                                                |     |     |         |                  |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 26,2025 at 03:18:15 UTC from IEEE Xplore.  Restrictions apply.

SANGHAVIetal.:BELIEFPROPAGATIONANDLPRELAXATION 2211
Thuswehavethatthe -normsatisfies .Now,by ProofofLemma5: Let , and bedefinedexactlyasinthe
thedefinitionof inLemma1 proofofLemma4above,with replacedby .Byreasoning
exactlyasabove,itfollowsthatalledgeconstraints
are satisfied, and also all node constraints are satisfied except
possiblyfornodes thatareendpointsof whichareleafsof
andthus, .Also, .Thuswe
andalsothelastedge isin .However,thefact
havethat
thattheroot isin ,andthat iseven,meansthatlastedge
andnotin .Thus isafeasiblepointof .
Now,asbefore, wehavethat
However,byassumption ,andhenceithastobethat .Thus,ifthelemmaisnottrue,itfollowsthat
.Thisfinishestheproof. . ,violatingtheoptimalityof .Thelemmaisthusproved.
ProofofLemma4: Theproofofthislemmaisalsoapertur-
bation argument. For each edge , let denote the number ProofofLemma7: Wenowshowthat asdefinedin(5)is
of times appears in and the number of times it afeasiblepointof ,forsmallenough .Forthiswehaveto
appearsin .Define show that it satisfies the edge constraints for all
edges andthenodeconstraints forall
nodes (here isthesetofalledgestouchingnode )
We now show that this is a feasible point for , for small First the edge constraints. If , then the assumption
enough .Todosowehavetocheckedgeconstraints that isintegralmeansthat ,andhence .
andnodeconstraints .Considerfirsttheedge Thusforsmallenough ,itwillbethecasethat .
constraints.Forany ,bydefinition, .Thus, On the other hand, if then and .
for any and , making small enough can ensure that Thus,again,asmallenough willensure .
.Ontheotherhand,forany Wenowturntothenodeconstraints.Notethat
, , because a neighboring edge that belongs to
haspositiveweight.Making smallenoughensuresthat
.
Consider now the node constraints for a node . For every
copyof thatappearsintheinteriorof ,themassononeedge
Theterm countsthenumberoftimesedgesin
is increased by , and on another is decreased by . Thus the
touch(copiesof)node inthecomputationtree.Similarly,
onlynodeswherethereisapotentialforconstraintviolationare
countsthenumberoftimesedgesin touch
theendpointsof forwhichthecorrespondinglastedgeisin
. Suppose first that is not an endpoint of , so that every
.Supposethat isonesuchendpoint,andassumefornow
time touches it will do so with one edge in and one
that isnotaleafnodeof .Notenowthat,byconstruction,
in . This means that and hence
everyedgein has .So,thefactthat could
that .Thusthenodeconstraintat is
notbeextendedbeyond meansthat ,
notviolated.
where istheedgein (and )touching .Thismeansthat
Suppose now that appears as an endpoint of , and
theconstraintat isinactivefor ,andsoforsmall thenew
is the corresponding last edge of . If ,
willbefeasible.
this means that , and hence
The only remaining case to check is if the endpoint of
—so the constraint at node is
is a leaf node of . If the last edge in touching is in
notviolated.5Iflastedge andittouchesaleaf-node
,thenodeconstraintat willnotbeviolatedsincethe
thenitisnotcountedin (seehow isdefined).If
perturbationdecreasesthetotalmassat .Notethat,since is
and it ends in the interior of , then the fact that could
odd,thisincludesthecasewhere isaleafnodeatthelowest
notbeextendedbeyond meansthattherearenoedgesof
level.So,considerthefinalcasethat isaleafnodethatisnot
touching inthetree .Since istheimageof ,this
atthelowestlevelinthetree,suchthat endsin withanedge
means there are no edges in touching node in original
in .Thisedgehasmassstrictlylessthan1.Thefactthat
graph . Thus . So, for small enough we
isnotatthelowestlevelmeansthat isaleafintheoriginal
can ensure that , ensuring that the
graphaswell,andhanootheredgestouchingit.Thusithasto
constraintatnode isnotviolated.
be thattheconstraint atnode isnottightat theLP optimum
.Thismeansthatasmallfinite willensurefeasibility.
Thus isafeasiblepointof .Notethattheweightssatisfy REFERENCES
[1] F.Kschischang,B.Frey,andH.Loeliger,“Factorgraphsandthesum-
productalgorithm,”IEEETrans.Inf.Theory,vol.47,pp.498–519,Feb.
2001.
Thus, if , then we would have that [2] J.Pearl,ProbabilisticInferenceinIntelligentSystems. Boston,MA:
, which violates the assumption that is an op- MorganKaufmann,1988.
timum of . So it has to be that . 5Notethatequalityoccursonlyif(cid:0)isalsotheotherendpointof(cid:2),andthe
Thisprovesthelemma. correspondinglastedgethereisin(cid:2) (cid:0)(cid:3).
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 26,2025 at 03:18:15 UTC from IEEE Xplore. Restrictions apply.

2212 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.57,NO.4,APRIL2011
[3] J.Yedidia,W.Freeman,andY.Weiss,“Understandingbeliefpropaga- SujaySanghavi(S’02–M’06)receivedtheM.S.degreeinbothmathematics
tionanditsgeneralizations,”ExploringAIintheNewMillennium,pp. andelectricalandcomputerengineering,fromtheUniversityofIllinois,Ur-
239–269,2003. bana-Champaign,andthePh.D.degreeinelectricalandcomputerengineering,
[4] D.Malioutov,J.Johnson,andA.Willsky,“Walk-sumsandbeliefprop- in2006.
agationinGaussiangraphicalmodels,”J.Mach.Learn.Res.,vol.7,pp. HeisanAssistantProfessorofelectricalandcomputerengineeringwiththe
2031–2064,Oct.2006. UniversityofTexas,Austin,sinceJuly2009.Hespent2006–2008,aspostdoc-
[5] Y.WeissandW.Freeman,“Ontheoptimalityofsolutionsofthemax- toralscholarwiththeLaboratoryforInformationandDecisionSystems(LIDS),
MIT,and2008–2009asanAssistantProfessorofelectricalandcomputerengi-
productbelief-propagationalgorithminarbitrarygraphs,”IEEETrans.
neeringatPurdueUniversity,WestLafayette,IN.Hisinterestslieattheinter-
Inf.Theory,vol.47,no.2,pp.736–744,Feb.2001.
sectionofnetworks,networking,andstatisticalmachinelearning.
[6] S. Sanghavi, “Equivalence of LP relaxation and max-product for
Dr.SanghavireceivedtheNSFCAREERawardin2010.
weightedmatchingingeneralgraphs,”inProc.Inf.TheoryWorkshop,
Sep.2007.
[7] M.Bayati,C.Borgs,J.Chayes,andR.Zecchina,BeliefPropagationfor
Weighted(cid:0)-MatchingsonArbitraryGraphsanditsRelationtoLinear Dmitry Malioutov received the B.S. degree in electrical and computer en-
ProgramsWithIntegerSolutions[Online].Available:http://arxiv.org/ gineeringfromNortheasternUniversity,Boston,MA,in2001,andtheM.S.
abs/0807.3159 and Ph.D. degrees in electrical engineering and computer science from the
[8] L.TassiulasandA.Ephremides,“Stabilitypropertiesofconstrained MassachusettsInstituteofTechnology(MIT),Cambridge,in2003and2008,
queueingsystemsandschedulingpoliciesformaximumthroughputin respectively.
multihopradionetworks,”IEEETrans.Autom.Control,vol.37,no.12, After a postdoctoral position with the Machine Learning and Perception
Dec.1992. Group, Microsoft Research, Cambridge, U.K., he is currently a Researcher
inAlgorithmicTrainingatDRW,Chicago,IL.Hisresearchinterestsinclude
[9] B.HuangandT.Jebara,“Loopybeliefpropagationforbipartitemax-
statistical signal and image processing, machine learning, and convex opti-
imum weight b-matching,” in Proc. Artif. Intell. Statist. (AISTATS),
mizationwithemphasisongraphicalmodels,messagepassingalgorithms,and
Mar.2007.
sparsesignalrepresentation.
[10] M.Bayati,D.Shah,andM.Sharma,“Maximumweightmatchingvia
max-productbeliefpropagation,”inProc.Int.Symp.Inf.Theory(ISIT),
Sep.2005,pp.1763–1767.
[11] P.VontobelandR.Koetter,“Ontherelationshipbetweenlinearpro- Alan Willsky (S’70–M’73–SM’82–F’86) joined M.I.T. in 1973 and is the
grammingdecodingandmin-sumalgorithmdecoding,”inProc.ISITA Edwin Sibley Webster Professor of Electrical Engineering and Director of
2004,Parma,Italy. the Laboratory for Information and Decision Systems. He was a founder of
[12] S.TatikondaandM.Jordan,“LoopybeliefpropagationandGibbsmea- Alphatech,Inc.,andChiefScientificConsultant,aroleinwhichhecontinues
sures,”inProc.LoopybeliefpropagationandGibbsmeasures,2002, at BAE Systems Advanced Information Technologies. From 1998–2002, he
vol.18,pp.493–500. servedontheU.S.AirForceScientificAdvisoryBoard.Hehasdeliverednu-
[13] S.Sanghavi,D.Shah,andA.Willsky,“Messagepassingformaximum merouskeynoteaddressesandisco-authorofthetextSignalsandSystems.His
weightindependentset,”inProc.NeuralInf.Process.Syst.(NIPS), researchinterestsareinthedevelopmentandapplicationofadvancedmethods
ofestimation,machinelearning,andstatisticalsignalandimageprocessing.
2007.
Dr.Willskyhasreceivedanumberofawards,includingthe1975American
[14] M.J.Wainwright,T.S.Jaakkola,andA.S.Willsky,“MAPestimation
AutomaticControlCouncilDonaldP.EckmanAward,the1979ASCEAlfred
viaagreementon(hyper)trees:Message-passingandlinear-program-
NoblePrize,the1980IEEEBrowderJ.ThompsonMemorialAward,theIEEE
mingapproaches,”IEEETrans.Inf.Theory,vol.51,pp.3697–3717,
ControlSystemsSocietyDistinguishedMemberAwardin1988,the2004IEEE
Nov.2005.
DonaldG.FinkPrizePaperAward,DoctoratHonorisCausafromUniversité
[15] M.WainwrightandM.Jordan,“Graphicalmodels,exponentialfami-
deRennesin2005,andthe2009TechnicalAchievementAwardfromtheIEEE
lies,andvariationalinference,”Found.TrendsinMach.Learn.,vol.1,
SignalProcessingSociety.In2010,hewaselectedtotheNationalAcademy
no.1–2,pp.1–305,Dec.2008. ofEngineering.HeandhisstudentshavealsoreceivedavarietyofBestPaper
[16] V. N. Kolmogorov and M. J. Wainwright, “On optimality of Awardsatvariousconferencesandforpapersinjournals,includingthe2001
tree-reweighted max-product message-passing,” in Proc. Uncert. IEEEConferenceonComputerVisionandPatternRecognition,the2003Spring
Artif.Intell.,Edinburgh,Scotland,Jul.2005. MeetingoftheAmericanGeophysicalUnion,the2004NeuralInformationPro-
[17] A.Schrijver,CombinatorialOptimization. Berlin-Heidelberg,Ger- cessingSymposium,Fusion2005,andthe2008awardfromthejournalSignal
many:Springer-Verlag,2003. Processingfortheoutstandingpaperintheyear2007.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on November 26,2025 at 03:18:15 UTC from IEEE Xplore. Restrictions apply.