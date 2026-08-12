498 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
Factor Graphs and the Sum-Product Algorithm
Frank R. Kschischang, Senior Member, IEEE, Brendan J. Frey, Member, IEEE, and
Hans-Andrea Loeliger, Member, IEEE
Abstract—Algorithms that must deal with complicated global The aim of this tutorial paper is to introduce factor graphs
functionsofmanyvariablesoftenexploitthemannerinwhichthe andtodescribeagenericmessage-passingalgorithm,calledthe
given functions factor as a product of “local” functions, each of
sum-productalgorithm,whichoperatesinafactorgraphandat-
which dependson a subset of the variables.Such a factorization
tempts to compute various marginal functions associated with
canbevisualizedwithabipartitegraphthatwecallafactorgraph.
Inthistutorialpaper,wepresentagenericmessage-passingalgo- the global function. The basic ideas are very simple; yet, as
rithm,thesum-productalgorithm,thatoperatesinafactorgraph. we willshow,a surprisingly wide varietyofalgorithms devel-
Following a single, simple computational rule, the sum-product oped in the artificial intelligence, signal processing, and dig-
algorithm computes—either exactly or approximately—var-
ital communications communities may be derived as specific
ious marginal functions derived from the global function. A
instancesofthesum-productalgorithm,operatinginanappro-
wide variety of algorithms developed in artificial intelligence,
signal processing, and digital communications can be derived as priatelychosenfactorgraph.
specific instances of the sum-product algorithm, including the Genealogically, factor graphs are a straightforward gen-
forward/backwardalgorithm,theViterbialgorithm,theiterative eralization of the “Tanner graphs” of Wiberg et al. [31],
“turbo”decodingalgorithm,Pearl’sbeliefpropagationalgorithm
[32]. Tanner [29] introduced bipartite graphs to describe
forBayesiannetworks,theKalmanfilter,andcertainfastFourier
familiesofcodeswhich are generalizationsofthe low-density
transform(FFT)algorithms.
parity-check(LDPC)codesofGallager[11],andalsodescribed
Index Terms—Belief propagation, factor graphs, fast Fourier
the sum-product algorithm in this setting. In Tanner’s original
transform, forward/backward algorithm, graphical models, iter-
formulation, all variables are codeword symbols and hence
ative decoding, Kalman filtering, marginalization, sum-product
algorithm,Tannergraphs,Viterbialgorithm. “visible”;Wibergetal.,introduced“hidden”(latent)statevari-
ables and also suggested applications beyond coding. Factor
graphs take these graph-theoretic models one step further, by
I. INTRODUCTION
applyingthemto functions.From the factor-graph perspective
THISpaperprovidesatutorialintroductiontofactorgraphs (as we will describe in Section III-A), a Tanner graph for a
and the sum-product algorithm, a simple way to under- code represents a particular factorization of the characteristic
standalargenumberofseeminglydifferentalgorithmsthathave (indicator)functionofthecode.
beendevelopedincomputerscienceandengineering.Wecon- While it may seem intuitively reasonable that some algo-
sideralgorithmsthatdealwithcomplicated“global”functions rithms should exploit the manner in which a global function
ofmanyvariablesandthatderivetheircomputationalefficiency factorsintoaproductoflocalfunctions,thefundamentalinsight
byexploitingthewayinwhichtheglobalfunctionfactorsinto thatmanywell-knownalgorithmsessentiallysolvethe“MPF”
aproductofsimpler“local”functions,eachofwhichdepends (marginalize product-of-functions) problem,each in their own
onasubsetofthevariables.Suchafactorizationcanbevisual- particular setting, was first made explicit in the work of Aji
izedusingafactorgraph,abipartitegraphthatexpresseswhich and McEliece [1]. In a landmark paper [2], Aji and McEliece
variablesareargumentsofwhichlocalfunctions. develop a “generalized distributive law” (GDL) that in some
casessolvestheMPFproblemusinga“junctiontree”represen-
ManuscriptreceivedAugust3,1998;revisedOctober17,2000.Thework tation of the global function. Factor graphs may be viewed as
ofF.R.Kschischangwassupportedinpart,whileonleaveattheMassachu- an alternative approach with closer ties to Tanner graphs and
setts Institute of Technology, by the Office of Naval Research under Grant
previously developed graphical representations for codes. Es-
N00014-96-1-0930,andbytheArmyResearchLaboratoryunderCooperative
Agreement DAAL01-96-2-0002. The work of B. J. Frey was supported, sentially, every result developed in the junction tree/GDL set-
whileaBeckmanFellowattheBeckmanInstituteofAdvancedScienceand ting may be translated into an equivalent result in the factor
Technology, University of Illinois at Urbana-Champaign, by a grant from
graph/sum-productalgorithmsetting,andviceversa.Weprefer
theArnoldandMabelBeckmanFoundation.Thematerialinthispaperwas
presentedinpartatthe35thAnnualAllertonConferenceonCommunication, thelattersettingnotonlybecauseitisbetterconnectedwithpre-
Control,andComputing,Monticello,IL,September1997. viousapproaches,butalsobecausewefeelthatfactorgraphsare
F. R. Kschischang is with the Department of Electrical and Computer
insomewayseasiertodescribe,givingthemamodestpedagog-
Engineering,UniversityofToronto,Toronto,ONM5S3G4,Canada(e-mail:
frank@comm.utoronto.ca). icaladvantage.Moreover,thesum-productalgorithmcanoften
B.J.FreyiswiththeFacultyofComputerScience,UniversityofWaterloo, beappliedsuccessfullyinsituationswhereexactsolutionstothe
Waterloo, ON N2L 3G1, Canada, and the Faculty of Electrical and Com-
MPFproblem(asprovidedbyjunctiontrees)becomecomputa-
puter Engineering, University of Illinois at Urbana-Champaign, Urbana, IL
61801-2307USA(e-mail:frey@.uwaterloo.ca). tionallyintractable,themostprominentexamplebeingtheiter-
H.-A. Loeliger is with the Signal Processing Lab (ISI), ETH Zentrum, ativedecodingofturbocodesand LDPCcodes.InSectionVI
CH-8092Zürich,Switzerland(e-mail:loeliger@isi.ee.ethz.ch).
wedo,however,discussstrategiesforachievingexactsolutions
CommunicatedbyT.E.Fuja,AssociateEditorAtLarge.
PublisherItemIdentifierS0018-9448(01)00721-0. totheMPFprobleminfactorgraphs.
0018–9448/01$10.00©2001IEEE
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore. Restrictions apply.

| KSCHISCHANGetal.:FACTORGRAPHSANDTHESUM-PRODUCTALGORITHM |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 499 |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
There are also close connectionsbetween factor graphs and andcodomain .Thedomain of iscalledtheconfiguration
graphical representations (graphical models) for multidimen- spaceforthegivencollectionofvariables,andeachelementof
sional probability distributions such as Markov random fields is a particular configurationof the variables,i.e., an assign-
[16],[18],[26]andBayesian(belief)networks[25],[17].Like mentofavaluetoeachvariable.Thecodomain of mayin
factorgraphs,thesegraphicalmodelsencodeintheirstructurea generalbeanysemiring[2],[31,Sec.3.6];however,atleastini-
particularfactorizationofthejointprobabilitymassfunctionof tially,wewilllosenothingessentialbyassumingthat isthe
severalrandomvariables.Pearl’spowerful“beliefpropagation” setofrealnumbers.
algorithm [25], which operates by “message-passing” in a Assumingthatsummationin iswelldefined,thenassoci-
Bayesian network, translates immediately into an instance of ated with every function are marginal func-
the sum-product algorithm operating in a factor graph that tions .Foreach ,thevalueof isobtainedby
expressesthesamefactorization.Bayesiannetworksandbelief summingthevalueof overallconfigurationsof
propagation have been used previously to explain the iterative thevariablesthathave .
decodingofturbocodesandLDPCcodes[9],[10],[19],[21], Thistypeofsumissocentraltothispaperthatweintroduce
[22], [24], the most powerful practically decodable codes anonstandardnotationtohandleit:the“not-sum”orsummary.
known. Note, however, that Wiberg [31] had earlier described Insteadofindicatingthevariablesbeingsummedover,weindi-
these decoding algorithms as instances of the sum-product catethosevariablesnotbeingsummedover.Forexample,if is
algorithm;seealso[7]. afunctionofthreevariables , ,and ,thenthe“summary
WebeginthepaperinSectionIIwithasmallworkedexample for ”isdenotedby
thatillustratestheoperationofthesum-productalgorithmina
| simple factor |      | graph.        | We will | see that      | when     | a factor graph | is       |     |     |     |     |     |     |     |     |
| ------------- | ---- | ------------- | ------- | ------------- | -------- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| cycle-free,   | then | the structure |         | of the factor | graph    | not only       | en-      |     |     |     |     |     |     |     |     |
| codes the     | way  | in which      | a given | function      | factors, | but            | also en- |     |     |     |     |     |     |     |     |
Inthisnotationwehave
codesexpressionsforcomputingthevariousmarginalfunctions
| associated | with | the given | function. | These | expressions |     | lead di- |     |     |     |     |     |     |     |     |
| ---------- | ---- | --------- | --------- | ----- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
rectlytothesum-productalgorithm.
InSectionIII,weshowhowfactorgraphsmaybeusedasa
|     |     |     |     |     |     |     |     | i.e.,the | thmarginalfunctionassociatedwith |     |     |     |     |     | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------------------------- | --- | --- | --- | --- | --- | --- |
systemandsignal-modelingtool.Weseethatfactorgraphsare
|     |     |     |     |     |     |     |     | thesummaryfor |     | of  | .   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
compatiblebothwith“behavioral”and“probabilistic”modeling
Weareinterestedindevelopingefficientproceduresforcom-
| styles. Connectionsbetween |     |     |     | factor graphs | and | other graphical |     |                |     |                 |     |            |     |             |     |
| -------------------------- | --- | --- | --- | ------------- | --- | --------------- | --- | -------------- | --- | --------------- | --- | ---------- | --- | ----------- | --- |
|                            |     |     |     |               |     |                 |     | putingmarginal |     | functionsthata) |     | exploitthe |     | way inwhich | the |
modelsaredescribedbrieflyinAppendixB,wherewerecover
globalfunctionfactors,usingthedistributivelawtosimplifythe
Pearl’sbeliefpropagationalgorithmasaninstanceofthesum-
|     |     |     |     |     |     |     |     | summations, | and | b) reuses | intermediate |     | values | (partial | sums). |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ------------ | --- | ------ | -------- | ------ |
productalgorithm.
|            |     |        |       |                 |     |           |     | As we will | see, | such | procedures | can | be expressed |     | very natu- |
| ---------- | --- | ------ | ----- | --------------- | --- | --------- | --- | ---------- | ---- | ---- | ---------- | --- | ------------ | --- | ---------- |
| In Section |     | IV, we | apply | the sum-product |     | algorithm | to  |            |      |      |            |     |              |     |            |
rallybyuseofafactorgraph.
| trellis-structured |        | (hidden      | Markov) | models,         |            | and obtain | the     |                  |     |      |        |                              |        |     |     |
| ------------------ | ------ | ------------ | ------- | --------------- | ---------- | ---------- | ------- | ---------------- | --- | ---- | ------ | ---------------------------- | ------ | --- | --- |
|                    |        |              |         |                 |            |            |         | Supposethat      |     |      |        | factorsintoaproductofseveral |        |     |     |
| forward/backward   |        | algorithm,   |         | the Viterbi     | algorithm, |            | and the |                  |     |      |        |                              |        |     |     |
|                    |        |              |         |                 |            |            |         | local functions, |     | each | having | some                         | subset | of  | as  |
| Kalman             | filter | as instances | of      | the sum-product |            | algorithm. | In      |                  |     |      |        |                              |        |     |     |
arguments;i.e.,supposethat
| Section       | V, we      | consider | factor | graphs    | with cycles, | and   | obtain |     |     |     |     |     |     |     |     |
| ------------- | ---------- | -------- | ------ | --------- | ------------ | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| the iterative | algorithms |          | used   | to decode | turbo-like   | codes | as     |     |     |     |     |     |     |     |     |
(1)
instancesofthesum-productalgorithm.
| In Section | VI,      | we    | describe | several    | generic   | transformations |         |       |                      |            |        |             |          |     |          |
| ---------- | -------- | ----- | -------- | ---------- | --------- | --------------- | ------- | ----- | -------------------- | ---------- | ------ | ----------- | -------- | --- | -------- |
|            |          |       |          |            |           |                 |         | where | isadiscreteindexset, |            |        | isasubsetof |          |     | ,        |
| by which   | a factor | graph | with     | cycles may | sometimes |                 | be con- |       |                      |            |        |             |          |     |          |
|            |          |       |          |            |           |                 |         | and   | is                   | a function | having | the         | elements | of  | as argu- |
verted—oftenatgreatexpenseincomplexity—toanequivalent
| cycle-freeform.Weapplytheseideastothefactorgraphrepre- |     |     |     |     |     |     |     | ments. |     |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
sentingthediscreteFouriertransform(DFT)kernel,andderive Definition: Afactorgraphisabipartitegraphthatexpresses
| a fast Fourier |     | transform | (FFT) | algorithm | as  | an instance | of the |     |     |     |     |     |     |     |     |
| -------------- | --- | --------- | ----- | --------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
thestructureofthefactorization(1).Afactorgraphhasavari-
sum-productalgorithm. ablenodeforeachvariable ,afactornodeforeachlocalfunc-
SomeconcludingremarksaregiveninSectionVII. tion ,andanedge-connectingvariablenode tofactornode
|     |     |     |     |     |     |     |     | ifandonlyif |     | isanargumentof |     |     | .   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --- | --- | --- | --- | --- |
II. MARGINAL FUNCTIONS, FACTOR GRAPHS, AND THE Afactorgraphisthusastandardbipartitegraphicalrepresen-
SUM-PRODUCTALGORITHM
tationofamathematicalrelation—inthiscase,the“isanargu-
mentof”relationbetweenvariablesandlocalfunctions.
Throughoutthispaperwedealwithfunctionsofmanyvari-
| ables.Let | ,   |     | beacollectionofvariables,inwhich, |     |     |     |     |         |     |           |        |     |         |     |     |
| --------- | --- | --- | --------------------------------- | --- | --- | --- | --- | ------- | --- | --------- | ------ | --- | ------- | --- | --- |
|           |     |     |                                   |     |     |     |     | Example | 1   | (A Simple | Factor |     | Graph): | Let |     |
for each , takes on values in some (usually finite) domain beafunctionoffivevariables,andsupposethat can
| (or alphabet) |     | . Let |     | be  | an  | -valued function |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ----- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
beexpressedasaproduct
ofthesevariables,i.e.,afunctionwithdomain
(2)
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

500 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
Fig.2. Anexpressiontreerepresentingx(y+z).
| Fig. 1. A | factor graph | for | the product | f (x | )f (x )f | (x ;x ;x | )   |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ----------- | ---- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:1)f
(x ;x )f (x ;x ). it is unnecessary to order the vertices to avoid ambiguity in
interpretingtheexpressionrepresentedbythetree.
of five factors, so that , , Inthispaper,weextendexpressiontreessothattheleafver-
, , ,and tices represent functions, not just variables or constants. Sums
andproductsinsuchexpressiontreescombinetheiroperandsin
.Thefactorgraphthatcorrespondsto(2)isshownin
| Fig.1. |     |     |     |     |     |     | theusual(pointwise)mannerinwhichfunctionsareaddedand |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
multiplied.Forexample,Fig.3(a)unambiguouslyrepresentsthe
expressionontheright-handsideof(3),andFig.4(a)unambigu-
A. ExpressionTrees
ouslyrepresentstheexpressionontheright-handsideof(4).The
| In many | situations | (for | example, | when |     | rep- |     |     |     |     |     |     |     |     |
| ------- | ---------- | ---- | -------- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
operatorsshowninthesefiguresarethefunctionproductandthe
| resents a | joint probability |     | mass | function), | we are | interested | in  |     |     |     |     |     |     |     |
| --------- | ----------------- | --- | ---- | ---------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
summary,havingvariouslocalfunctionsastheirarguments.
| computingthemarginalfunctions |     |     |     | .Wecanobtainanex- |     |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AlsoshowninFigs.3(b)and4(b),areredrawingsofthefactor
pressionforeachmarginalfunctionbyusing(2)andexploiting
|     |     |     |     |     |     |     | graphofFig. | 1asa | rooted | tree | with | and | as root | vertex, |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------ | ---- | ---- | --- | ------- | ------- |
thedistributivelaw.
|                      |     |     |     |                |     |     | respectively. | This    | is possible  | because |     | the global | function      | de- |
| -------------------- | --- | --- | --- | -------------- | --- | --- | ------------- | ------- | ------------ | ------- | --- | ---------- | ------------- | --- |
| Toillustrate,wewrite |     |     |     | fromExample1as |     |     |               |         |              |         |     |            |               |     |
|                      |     |     |     |                |     |     | fined in      | (2) was | deliberately | chosen  | so  | that the   | corresponding |     |
factorgraphisatree.Comparingthefactorgraphswiththecor-
|     |     |     |     |     |     |     | responding | trees | representing | the | expression | for | the marginal |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ------------ | --- | ---------- | --- | ------------ | --- |
function,itiseasytonotetheircorrespondence.Thisobserva-
|     |     |     |     |     |     |     | tion is simple, | but | key: when | a   | factor | graph is | cycle-free, | the |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --- | ------ | -------- | ----------- | --- |
factorgraphnotonlyencodesinitsstructurethefactorization
oftheglobalfunction,butalsoencodesarithmeticexpressions
or,insummarynotation bywhichthemarginalfunctionsassociatedwiththeglobalfunc-
tionmaybecomputed.
Formally,asweshowinAppendixA,toconvertacycle-free
|     |     |     |     |     |     |     | factorgraphrepresentingafunction |     |                  |     |                       |                  | tothecor- |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | ---------------- | --- | --------------------- | ---------------- | --------- | --- |
|     |     |     |     |     |     |     | respondingexpressiontreefor      |     |                  |     | ,drawthefactorgraphas |                  |           |     |
|     |     |     |     |     |     |     | arootedtreewith                  |     | asroot.Everynode |     |                       | inthefactorgraph |           |     |
thenhasaclearlydefinedparentnode,namely,theneighboring
|     |     |     |     |     |     |     | nodethroughwhichtheuniquepathfrom |     |     |     |     | to  | mustpass.Re- |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | ------------ | --- |
placeeachvariablenodeinthefactorgraphwithaproductop-
erator.Replaceeachfactornodeinthefactorgraphwitha“form
(3)
|     |     |     |     |     |     |     | productandmultiplyby |        |          | ”operator,andbetweenafactornode |         |           |     |       |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | ------ | -------- | ------------------------------- | ------- | --------- | --- | ----- |
|     |     |     |     |     |     |     | and its              | parent | , insert | a                               | summary | operator. |     | These |
Similarly,wefindthat
|     |     |     |     |     |     |     | local transformations            |             | are | illustrated | in       | Fig. 5(a)  | for a    | variable |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------- | ----------- | --- | ----------- | -------- | ---------- | -------- | -------- |
|     |     |     |     |     |     |     | node,andinFig.5(b)forafactornode |             |     |             |          | withparent |          | .Trivial |
|     |     |     |     |     |     |     | products                         | (those with | one | or no       | operand) | act as     | identity | opera-   |
tors,ormaybeomittediftheyareleafnodesintheexpression
|     |     |     |     |     |     |     | tree.Asummaryoperator |     |                                          |     | appliedtoafunctionwitha |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ---------------------------------------- | --- | ----------------------- | --- | --- | --- |
|     |     |     |     |     |     |     | singleargument        |     | isalsoatrivialoperation,andmaybeomitted. |     |                         |     |     |     |
(4)
ApplyingthistransformationtothetreeofFig.3(b)yieldsthe
expressiontreeofFig.3(a),andsimilarlyforFig.4.Trivialop-
In computer science, arithmetic expressions like the erationsareindicatedwithdashedlinesinthesefigures.
| right-hand | sides | of (3) | and (4) | are often | represented | by or- |     |     |     |     |     |     |     |     |
| ---------- | ----- | ------ | ------- | --------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
B. ComputingaSingleMarginalFunction
| dered rooted | trees | [28, Sec. | 8.3], | here called | expression | trees, |     |     |     |     |     |     |     |     |
| ------------ | ----- | --------- | ----- | ----------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
in which internal vertices (i.e., vertices with descendants) Everyexpressiontreerepresentsanalgorithmforcomputing
represent arithmetic operators (e.g., addition, multiplication, thecorrespondingexpression.Onemightdescribethealgorithm
negation, etc.) and leaf vertices (i.e., vertices without descen- asarecursive“top-down”procedurethatstartsattherootvertex
dants)representvariablesorconstants.Forexample,thetreeof andevaluateseachsubtreedescendingfromtheroot,combining
Fig.2representstheexpression .Whentheoperators theresultsasdictatedbytheoperatorattheroot.Equivalently,
inanexpressiontreearerestrictedtothosethatarecompletely weprefertodescribethealgorithmasa“bottom-up”procedure
symmetricintheiroperands(e.g.,multiplicationandaddition), that begins at the leaves of the tree, with each operator vertex
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

KSCHISCHANGetal.:FACTORGRAPHSANDTHESUM-PRODUCTALGORITHM 501
Fig.3. (a)Atreerepresentationfortheright-handsideof(3).(b)ThefactorgraphofFig.1,redrawnasarootedtreewithx asroot.
Fig.4. (a)Atreerepresentationfortheright-handsideof(4).(b)ThefactorgraphofFig.1,redrawnasarootedtreewithx asroot.
combiningitsoperandsandpassingontheresultasanoperand computes,forasinglevalueof ,themarginalfunction
for its parent. For example, , represented by the ex- inarootedcycle-freefactorgraph,with takenasrootvertex.
pressiontreeofFig.2,mightbeevaluatedbystartingattheleaf Thecomputationbeginsattheleavesofthefactorgraph.Each
nodes and ,evaluating ,andpassingontheresultasan leafvariablenodesendsatrivial“identityfunction”messageto
operandforthe operator,whichmultipliestheresultwith . its parent, and each leaf factor node sends a description of
Rather than working with the expression tree, it is simpler to its parent. Each vertex waits for messages from all of its
andmoredirecttodescribesuchmarginalizationalgorithmsin childrenbeforecomputingthemessagetobesenttoitsparent.
terms of the corresponding factor graph. To best understand Thiscomputationisperformedaccordingtothetransformation
such algorithms, it helps to imagine that there is a processor showninFig.5;i.e.,avariablenodesimplysendstheproduct
associated with each vertex of the factor graph, and that the of messages received from its children, while a factor node
factor-graph edges represent channels by which these proces- withparent formstheproductof withthemessagesreceived
sors may communicate. For us, “messages” sent between pro- fromitschildren,andthenoperatesontheresultwitha
cessorsarealwayssimplysomeappropriatedescriptionofsome summary operator. By a “product of messages” we mean an
marginalfunction.(Wedescribesomeusefulrepresentationsin appropriate description of the (pointwise) product of the cor-
SectionV-E.) responding functions. If the messages are parametrizations of
We now describe a message-passing algorithm that we will thefunctions,thentheresultingmessageistheparametrization
temporarily callthe “single- sum-product algorithm,”sinceit oftheproductfunction,not(necessarily)literallythenumerical
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore. Restrictions apply.

502 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
|     |     |     |     |     |     |     |     | Fig.6. Afactor-graphfragment,showingtheupdaterulesofthesum-product |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- |
Fig.5. Localsubstitutionsthattransformarootedcycle-freefactorgraphto
| anexpressiontreeforamarginalfunctionat(a)avariablenodeand(b)afactor |     |     |     |     |     |     |     | algorithm. |     |     |     |     |     |
| ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
node.
|     |     |     |     |     |     |     |     | single- algorithm,oncethesemessageshavearrived, |           |            |        |               | isable |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --------- | ---------- | ------ | ------------- | ------ |
|     |     |     |     |     |     |     |     | to compute                                      | a message | to be sent | on the | one remaining | edge   |
productofthemessages.Similarly,thesummaryoperatorisap-
|     |     |     |     |     |     |     |     | to its neighbor | (temporarily | regarded | as  | the parent), | just as in |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------ | -------- | --- | ------------ | ---------- |
pliedtothefunctions,notnecessarilyliterallytothemessages
themselves. the single- algorithm, i.e., according to Fig. 5. Let us denote
|                 |     |            |     |        |           |     |           | this temporaryparentasvertex |     |     | . Aftersending |     | amessage to |
| --------------- | --- | ---------- | --- | ------ | --------- | --- | --------- | ---------------------------- | --- | --- | -------------- | --- | ----------- |
| The computation |     | terminates |     | at the | root node | ,   | where the |                              |     |     |                |     |             |
marginalfunction isobtainedastheproductofallmes- ,vertex returnstotheidlestate,waitingfora“returnmes-
|                 |     |         |      |           |        |     |          | sage”toarrivefrom | .Oncethismessagehasarrived,thevertex |               |     |         |               |
| --------------- | --- | ------- | ---- | --------- | ------ | --- | -------- | ----------------- | ------------------------------------ | ------------- | --- | ------- | ------------- |
| sagesreceivedat |     | .       |      |           |        |     |          |                   |                                      |               |     |         |               |
|                 |     |         |      |           |        |     |          | is able to        | compute and                          | send messages |     | to each | of its neigh- |
| It is important |     | to note | that | a message | passed | on  | the edge |                   |                                      |               |     |         |               |
, either from variable to factor , or vice versa, is a bors (other than ), each being regarded, in turn, as a parent.
Thealgorithmterminatesoncetwomessageshavebeenpassed
| single-argumentfunctionof |     |     |     | ,thevariableassociatedwiththe |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
givenedge.Thisfollowssince,ateveryfactornode,summary over every edge, one in each direction. At variable node ,
|     |     |     |     |     |     |     |     | the product | of all incoming | messages | is  | the marginal | function |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | -------- | --- | ------------ | -------- |
operationsarealwaysperformedforthevariableassociatedwith
|     |     |     |     |     |     |     |     | ,justasinthesingle- |     | algorithm.Sincethisalgorithmop- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------------------------------- | --- | --- | --- |
theedgeonwhichthemessageispassed.Likewise,atavariable
node,allmessagesarefunctionsofthatvariable,andsoisany erates by computing various sums and products, we refer to it
asthesum-productalgorithm.
productofthesemessages.
The message passed on an edge during the operation of the The sum-product algorithm operates according to the fol-
lowingsimplerule:
single- sum-productalgorithmcanbeinterpretedasfollows.If
|     | is  | an edge | in the | tree, where | is  | a variable | node |     |     |     |     |     |     |
| --- | --- | ------- | ------ | ----------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
and isafactornode,thentheanalysisofAppendixAshows
|     |     |     |     |     |     |     |     | Themessagesentfromanode |     |     | onanedge |     | isthe |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | -------- | --- | ----- |
thatthemessagepassed on duringtheoperationofthesum- productofthelocalfunctionat (ortheunitfunction
| productalgorithmissimplyasummaryfor |     |     |     |     |     | oftheproductof |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
if isavariablenode)withallmessagesreceivedat
| the local | functions | descending |     | from | the vertex | that | originates |              |      |                           |     |     |     |
| --------- | --------- | ---------- | --- | ---- | ---------- | ---- | ---------- | ------------ | ---- | ------------------------- | --- | --- | --- |
|           |           |            |     |      |            |      |            | onedgesother | than | ,summarizedforthevariable |     |     |     |
the message.
|     |     |     |     |     |     |     |     | associatedwith | .   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
C. ComputingAllMarginalFunctions Let denote the message sent from node to node
In manycircumstances, we may be interested in computing in the operation of the sum-product algorithm, let
formorethanonevalueof .Suchacomputationmight denotethemessagesentfromnode tonode .Also,let
beaccomplishedbyapplyingthesingle- algorithmseparately denotethesetofneighborsofagivennode inafactorgraph.
for each desired value of , but this approach is unlikely to Then, as illustrated in Fig. 6, the message computations per-
beefficient,sincemanyofthesubcomputationsperformedfor formedbythesum-productalgorithmmaybeexpressedasfol-
| different | values | of will | be the | same. | Computation |     | of  | lows: |     |     |     |     |     |
| --------- | ------ | ------- | ------ | ----- | ----------- | --- | --- | ----- | --- | --- | --- | --- | --- |
forall simultaneouslycanbeefficientlyaccomplishedbyes-
| sentially | “overlaying” |     | on a single | factor | graph | all possible | in- |     |     |     |     |     |     |
| --------- | ------------ | --- | ----------- | ------ | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
(5)
| stancesof         | thesingle- |            | algorithm.Noparticularvertexis |          |               |              | taken    |     |     |     |     |     |     |
| ----------------- | ---------- | ---------- | ------------------------------ | -------- | ------------- | ------------ | -------- | --- | --- | --- | --- | --- | --- |
| as a root         | vertex,    | so there   | is no                          | fixed    | parent/child  | relationship |          |     |     |     |     |     |     |
| among neighboring |            | vertices.  |                                | Instead, | each neighbor |              | of any   |     |     |     |     |     |     |
| given vertex      |            | is at some | point                          | regarded | as a          | parent       | of . The |     |     |     |     |     |     |
(6)
| messagepassedfrom   |     |     | to iscomputedjustasinthesingle- |     |     |             |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ------------------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| algorithm,i.e.,asif |     |     | wereindeedtheparentof           |     |     | andallother |     |     |     |     |     |     |     |
neighborsof werechildren. where isthesetofargumentsofthefunction .
As in the single- algorithm, message passing is initiated at Theupdateruleatavariablenode takesontheparticularly
the leaves.Each vertex remains idleuntil messageshavear- simple form givenby(5) because there is nolocal function to
rived on all but one of the edges incident on . Just as in the include,andthesummaryfor ofaproductoffunctionsof is
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

| KSCHISCHANGetal.:FACTORGRAPHSANDTHESUM-PRODUCTALGORITHM |     |     |     |     |     |     |     |     |     |     | 503 |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Termination:
| Fig. 7. Messages | generated in | each (circled) step | of the sum-product |     |     |     |     |     |     |     |     |
| ---------------- | ------------ | ------------------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
algorithm.
simplythatproduct.Ontheotherhand,theupdateruleatalocal Intheterminationstep,wecompute astheproductof
functionnodegivenby(6)ingeneralinvolvesnontrivialfunc- allmessagesdirectedtoward .Equivalently,sincethemessage
tionmultiplications,followedbyanapplicationofthesummary passedonanygivenedgeisequaltotheproductofallbutone
|     |     |     |     | ofthesemessages,wemaycompute |     |     |     |     | astheproductofthe |     |     |
| --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | ----------------- | --- | --- |
operator.
We also observe that variable nodes of degree two perform twomessagesthatwerepassed(inoppositedirections)overany
nocomputation:amessagearrivingonone(incoming)edgeis singleedgeincidenton .Thus,forexample,wemaycompute
simplytransferredtotheother(outgoing)edge. inthreeotherwaysasfollows:
D. ADetailedExample
Fig.7showstheflowofmessagesthatwouldbegeneratedby
thesum-productalgorithmappliedtothefactorgraphofFig.1.
Themessagesmaybegeneratedinfivesteps,asindicatedwith
circlesinFig.7.Indetail,themessagesaregeneratedasfollows. III. MODELINGSYSTEMSWITHFACTORGRAPHS
Step1:
Wedescribenowvariouswaysinwhichfactorgraphsmaybe
usedtomodelsystems,i.e.,collectionsofinteractingvariables.
|     |     |     |     | In probabilistic |     | modeling | of  | systems, | a factor | graph | can be |
| --- | --- | --- | --- | ---------------- | --- | -------- | --- | -------- | -------- | ----- | ------ |
usedtorepresentthejointprobabilitymassfunctionofthevari-
|     |     |     |     | ables that | comprise  | the         | system. | Factorizations |             | of this      | function |
| --- | --- | --- | --- | ---------- | --------- | ----------- | ------- | -------------- | ----------- | ------------ | -------- |
|     |     |     |     | can give   | important | information |         | about          | statistical | dependencies |          |
amongthesevariables.
|        |     |     |     | Likewise,                                             | in         | “behavioral” | modeling  |                | of systems—as   |                | in the     |
| ------ | --- | --- | --- | ----------------------------------------------------- | ---------- | ------------ | --------- | -------------- | --------------- | -------------- | ---------- |
| Step2: |     |     |     | workofWillems[33]—systembehaviorisspecifiedinset-the- |            |              |           |                |                 |                |            |
|        |     |     |     | oretic terms                                          | by         | specifying   | which     | particular     |                 | configurations | of         |
|        |     |     |     | variables                                             | are valid. | This         | approach  | can            | be accommodated |                | by a       |
|        |     |     |     | factor graph                                          | that       | represents   | the       | characteristic |                 | (i.e.,         | indicator) |
|        |     |     |     | function                                              | for the    | given        | behavior. | Factorizations |                 | of this        | charac-    |
teristicfunctioncangiveimportantstructuralinformationabout
the model.
|        |     |     |     | In some                                              | applications, |          | we may     | even | wish          | to combine | these     |
| ------ | --- | --- | --- | ---------------------------------------------------- | ------------- | -------- | ---------- | ---- | ------------- | ---------- | --------- |
| Step3: |     |     |     | twomodelingstyles.Forexample,inchannelcoding,wemodel |               |          |            |      |               |            |           |
|        |     |     |     | both the                                             | valid         | behavior | (i.e., the | set  | of codewords) |            | and the a |
posteriorijointprobabilitymassfunctionoverthevariablesthat
|     |     |     |     | define the | codewords | given | the | received | output | of  | a channel. |
| --- | --- | --- | --- | ---------- | --------- | ----- | --- | -------- | ------ | --- | ---------- |
(Whileitmayevenbefeasibletomodelcomplicatedchannels
Step4:
withmemory[31],inthispaperwewillmodelonlymemoryless
channels.)
|     |     |     |     | In behavioral                   |          | modeling,     | “Iverson’s  |          | convention” |              | [14, p. 24] |
| --- | --- | --- | --- | ------------------------------- | -------- | ------------- | ----------- | -------- | ----------- | ------------ | ----------- |
|     |     |     |     | can be                          | useful.  | If is         | a predicate | (Boolean |             | proposition) | in-         |
|     |     |     |     | volving                         | some set | of variables, |             | then     | is          | the          | -valued     |
|     |     |     |     | functionthatindicatesthetruthof |          |               |             | ,i.e.    |             |              |             |
|     |     |     |     |                                 |          |               |             | if       | istrue      |              |             |
(7)
otherwise.
Step5:
|     |     |     |     | For example,  |     |                |     |     | is  | the function    | that |
| --- | --- | --- | --- | ------------- | --- | -------------- | --- | --- | --- | --------------- | ---- |
|     |     |     |     | takesavalueof |     | ifthecondition |     |     |     | issatisfied,and |      |
otherwise.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

504 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
| Ifwelet | denotethelogicalconjunctionor“AND”operator, |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thenanimportantpropertyofIverson’sconventionisthat
(8)
| (assuming                              |     | and |     | ).Thus,if |               | canbewritten |     |     |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --------- | ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| asalogicalconjunctionofpredicates,then |     |     |     |           | canbefactored |              |     |     |     |     |     |     |     |     |     |
accordingto(8),andhencerepresentedbyafactorgraph.
A. BehavioralModeling
| Let |     | beacollectionofvariableswithconfig- |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
urationspace .Byabehaviorin , Fig.8. ATannergraphforthebinarylinearcodeofExample2.
| we mean | any subset |     | of . | The elements | of  | are the valid |     |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ---- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
configurations.Sincea systemis specifiedvia its behavior , where denotesthesuminGF .Thecorrespondingfactor
thisapproachisknownasbehavioralmodeling[33]. graphisshowninFig.8,wherewehaveusedaspecialsymbol
Behavioral modeling is natural for codes. If the domain of for the parity checks (a square with a “ ” sign). Although
eachvariableissomefinitealphabet ,sothattheconfiguration strictly speaking the factor graph represents the factorization
spaceisthe -foldCartesianproduct ,thenabehavior ofthecode’scharacteristicfunction,wewilloftenrefertothe
iscalledablockcodeoflength over ,andthevalid factor graph as representing the code itself. A factor graph
configurationsarecalledcodewords. obtainedinthiswayisoftencalledaTannergraph,after[29].
Thecharacteristic(orsetmembershipindicator)functionfor ItshouldbeobviousthataTannergraphforany linear
abehavior isdefinedas block code may be obtained from a parity-check matrix
|               |            |                                          |               |     |               |       |                           | forthecode.Suchaparity-checkmatrixhas |                                          |           |                |         |          | columnsand  |         |
| ------------- | ---------- | ---------------------------------------- | ------------- | --- | ------------- | ----- | ------------------------- | ------------------------------------- | ---------------------------------------- | --------- | -------------- | ------- | -------- | ----------- | ------- |
|               |            |                                          |               |     |               |       | atleast                   |                                       | rows.Variablenodescorrespondtothecolumns |           |                |         |          |             |         |
|               |            |                                          |               |     |               |       | of                        | and                                   | factor                                   | nodes (or | checks)        | to the  | rows     | of ,        | with an |
| Obviously,    | specifying |                                          | is equivalent |     | to specifying | . (We |                           |                                       |                                          |           |                |         |          |             |         |
|               |            |                                          |               |     |               |       | edge-connectingfactornode |                                       |                                          |           | tovariablenode |         |          | ifandonlyif |         |
| mightalsogive |            | aprobabilisticinterpretationbynotingthat |               |     |               |       |                           |                                       |                                          |           |                |         |          |             |         |
|               |            |                                          |               |     |               |       |                           | .                                     | Of course,                               | since     | there          | are, in | general, | many        | parity- |
isproportionaltoaprobabilitymassfunctionthatisuniform
checkmatricesthatrepresentagivencode,thereare,ingeneral,
overthevalidconfigurations.)
manyTannergraphrepresentationsforthecode.
Inmanyimportantcases,membershipofaparticularconfig-
urationinabehavior canbedeterminedbyapplyingaseries Givenacollectionofgeneralnonlinearlocalchecks,itmaybe
of tests (checks), each involving some subset of the variables. acomputationallyintractableproblemtodeterminewhetherthe
|     |     |     |     |     |     |     | corresponding |     | behavior | is  | nonempty. | For | example, | the | canon- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | --- | --------- | --- | -------- | --- | ------ |
Aconfigurationisdeemedvalidifandonlyifitpassesalltests;
i.e.,thepredicate maybewrittenasalogical ical NP-complete problem SAT (Boolean satisfiability) [13] is
conjunctionofaseriesof“simpler”predicates.Then factors simplytheproblemofdeterminingwhetherornotacollection
accordingto(8)intoaproductofcharacteristicfunctions,each ofBooleanvariablessatisfiesallclausesinagivenset.Ineffect,
indicatingwhetheraparticularsubsetofvariablesisanelement eachclauseisalocalcheck.
Often,adescriptionofasystemissimplifiedbyintroducing
ofsome“localbehavior.”
|                                       |     |     |     |     |     |          | hidden | (sometimes |     | called | auxiliary, | latent, | or state) | variables. |     |
| ------------------------------------- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | --- | ------ | ---------- | ------- | --------- | ---------- | --- |
| Example2(TannerGraphsforLinearCodes): |     |     |     |     |     | Thechar- |        |            |     |        |            |         |           |            |     |
Nonhiddenvariablesarecalledvisible.Aparticularbehavior
| acteristicfunctionforanylinearcodedefinedbyan |     |                                      |     |     |     | parity-  |                                |      |           |             |        |                    |         |              |     |
| --------------------------------------------- | --- | ------------------------------------ | --- | --- | --- | -------- | ------------------------------ | ---- | --------- | ----------- | ------ | ------------------ | ------- | ------------ | --- |
|                                               |     |                                      |     |     |     |          | with                           | both | auxiliary | and visible |        | variables          | is said | to represent | a   |
| checkmatrix                                   |     | canberepresentedbyafactorgraphhaving |     |     |     |          |                                |      |           |             |        |                    |         |              |     |
|                                               |     |                                      |     |     |     |          | given(visible)                 |      | behavior  |             | if the | projection         | of      | the elements | of  |
| variablenodesand                              |     | factornodes.Forexample,if            |     |     |     | isthebi- |                                |      |           |             |        |                    |         |              |     |
|                                               |     |                                      |     |     |     |          | onthevisiblevariablesisequalto |      |           |             |        | .Anyfactorgraphfor |         |              |     |
narylinearcodewithparity-checkmatrix
|     |     |     |     |     |     |     | isthenconsideredtobealsoafactorgraphfor |     |     |     |     |     |     | .Suchgraphs |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- |
wereintroducedbyWibergetal.[31],[32]andmaybecalled
Wiberg-typegraphs.Inourfactorgraphdiagrams,asinWiberg,
(9)
hiddenvariablenodesareindicatedbyadoublecircle.
|     |     |     |     |     |     |     | An  | important |     | class of | models | with hidden | variables |     | are the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | ------ | ----------- | --------- | --- | ------- |
then is the set of all binary -tuples trellisrepresentations(see[30]foranexcellentsurvey).Atrellis
|              |       |              |     |           |           |           | forablockcode |     |     | isanedge-labeleddirectedgraphwithdistin- |     |     |     |     |     |
| ------------ | ----- | ------------ | --- | --------- | --------- | --------- | ------------- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
| that satisfy | three | simultaneous |     | equations | expressed | in matrix |               |     |     |                                          |     |     |     |     |     |
guishedrootandgoalvertices,essentiallydefinedbytheprop-
| form as |     | . (This | is a | so-called | kernel representation, |     |      |           |          |     |      |        |             |     |         |
| ------- | --- | ------- | ---- | --------- | ---------------------- | --- | ---- | --------- | -------- | --- | ---- | ------ | ----------- | --- | ------- |
|         |     |         |      |           |                        |     | erty | that each | sequence | of  | edge | labels | encountered | in  | any di- |
sincethelinearcodeisdefinedasthekernelofaparticularlinear
rectedpathfromtherootvertextothegoalvertexisacodeword
| transformation.)Membershipin |     |     |     | iscompletelydeterminedby |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
checkingwhethereachofthethreeequationsissatisfied.There- in ,andthateachcodewordin isrepresentedbyatleastone
|     |     |     |     |     |     |     | such | path. | Trellises | also | have the | property | that | all paths | from |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --------- | ---- | -------- | -------- | ---- | --------- | ---- |
fore,using(8)and(9)wehave
theroottoanygivenvertexshouldhavethesamefixedlength
,calledthedepthofthegivenvertex.Therootvertexhasdepth
|     |     |     |     |     |     |     | ,andthegoalvertexhasdepth              |     |     |     |     | .Thesetofdepth |     |              | vertices |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | -------------- | --- | ------------ | -------- |
|     |     |     |     |     |     |     | canbeviewedasthedomainofastatevariable |     |     |     |     |                |     | .Forexample, |          |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

| KSCHISCHANGetal.:FACTORGRAPHSANDTHESUM-PRODUCTALGORITHM |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 505 |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.9. (a)Atrellisand(b)thecorrespondingWiberg-typegraphforthecodeofFig.8.
| Fig. 9(a) | is a trellis for | the code | of Example |     | 2. Vertices |     | at the |     |     |     |     |     |     |     |     |
| --------- | ---------------- | -------- | ---------- | --- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
samedeptharegroupedvertically.Therootvertexisleftmost,
| the goal | vertex is rightmost, |     | and edges | are | implicitly | directed |     |     |     |     |     |     |     |     |     |
| -------- | -------------------- | --- | --------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fromlefttoright.
| Atrellisdividesnaturallyinto          |                                               |                       | sections,wherethe |     |                | thtrellis |     |     |     |     |     |     |     |     |     |
| ------------------------------------- | --------------------------------------------- | --------------------- | ----------------- | --- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| section                               | isthesubgraphofthetrellisinducedbythevertices |                       |                   |     |                |           |     |     |     |     |     |     |     |     |     |
| atdepth                               | anddepth                                      | .Thesetofedgelabelsin |                   |     |                | maybe     |     |     |     |     |     |     |     |     |     |
| viewedasthedomainofa(visible)variable |                                               |                       |                   |     | .Ineffect,each |           |     |     |     |     |     |     |     |     |     |
trellis section defines a “local behavior” that constrains the Fig.10. Genericfactorgraphforastate-spacemodelofatime-invariantor
| possiblecombinationsof |           |         | , ,and     | .   |                   |     |     | time-varyingsystem. |     |     |     |     |     |     |     |
| ---------------------- | --------- | ------- | ---------- | --- | ----------------- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
| Globally,              | a trellis | defines | a behavior | in  | the configuration |     |     |                     |     |     |     |     |     |     |     |
space of the variables . A configu- tion,itfollowsthateverycodecanberepresentedbyacycle-free
factorgraph.Unfortunately,itoftenturnsoutthatthestate-space
| ration of | these variables | is valid | if and | only | if it | satisfies | the |     |     |     |     |     |     |     |     |
| --------- | --------------- | -------- | ------ | ---- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sizes(thesizesofdomainsofthestatevariables)caneasilybe-
| local constraints | imposed | by  | each of | the trellis | sections. |     | The |     |     |     |     |     |     |     |     |
| ----------------- | ------- | --- | ------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
characteristic function for this behavior thus factors naturally cometoolargetobepractical.Forexample,trellisrepresenta-
tionsofturbocodeshaveenormousstatespaces[12].However,
| into factors,wherethe |     | thfactorcorrespondstothe |     |     |     | thtrellis |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | ------------------------ | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
section andhas , ,and asitsarguments. suchcodesmaywellhavefactorgraphrepresentationswithrea-
Thefollowingexampleillustratestheseconceptsindetailfor sonable complexities, but necessarily with cycles. Indeed, the
|     |     |     |     |     |     |     |     | “cut-set | bound” of | [31] | (see also | [8]) strongly |     | motivates | the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---- | --------- | ------------- | --- | --------- | --- |
thecodeofExample2.
studyofgraphrepresentationswithcycles.
| Example       | 3 (A        | Trellis Description): |           |          | Fig. 9(a) | shows | a       |                 |                 |     |                     |     |             |               |        |
| ------------- | ----------- | --------------------- | --------- | -------- | --------- | ----- | ------- | --------------- | --------------- | --- | ------------------- | --- | ----------- | ------------- | ------ |
|               |             |                       |           |          |           |       |         | Trellises       | are basically   |     | conventional        |     | state-space |               | system |
| trellis for   | the code    | of Example            | 2,        | and Fig. | 9(b)      | shows | the     |                 |                 |     |                     |     |             |               |        |
|               |             |                       |           |          |           |       |         | models,         | and the generic |     | factor graph        | of  | Fig. 10     | can represent |        |
| corresponding | Wiberg-type |                       | graph. In | addition | to        | the   | visible |                 |                 |     |                     |     |             |               |        |
|               |             |                       |           |          |           |       |         | any state-space | model           |     | of a time-invariant |     | or          | time-varying  |        |
variable nodes , there are also hidden (state) system. As in Fig. 9, each local check represents a trellis
| variable       | nodes              |     | . Each           | local | check, | shown   | as a |          |                  |     |                 |          |        |         |         |
| -------------- | ------------------ | --- | ---------------- | ----- | ------ | ------- | ---- | -------- | ---------------- | --- | --------------- | -------- | ------ | ------- | ------- |
|                |                    |     |                  |       |        |         |      | section; | i.e., each check |     | is an indicator | function |        | for the | set of  |
| generic factor | node(blacksquare), |     | correspondstoone |       |        | section |      |          |                  |     |                 |          |        |         |         |
|                |                    |     |                  |       |        |         |      | allowed  | combinations     | of  | left (previous) |          | state, | input   | symbol, |
ofthe trellis.
|         |              |       |          |               |     |     |        | output symbol, | and | right | (next)state. | (Here, | we  | allow | a trellis |
| ------- | ------------ | ----- | -------- | ------------- | --- | --- | ------ | -------------- | --- | ----- | ------------ | ------ | --- | ----- | --------- |
| In this | example, the | local | behavior | corresponding |     |     | to the |                |     |       |              |        |     |       |           |
edgetohavebothaninputlabelandanoutputlabel.)
secondtrellissectionfromtheleftinFig.9consistsofthefol-
lowingtriples : Example 4 (State-Space Models): For example, the
classicallineartime-invariantstate-spacemodelisgivenbythe
(10)
equations
| wherethedomainsofthestatevariables |                 |                                  |     |           | and      | aretakento |        |     |     |     |     |     |     |     |     |
| ---------------------------------- | --------------- | -------------------------------- | --- | --------- | -------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| be                                 | and             | ,respectively,numberedfrombottom |     |           |          |            |        |     |     |     |     |     |     |     |     |
| to top in                          | Fig. 9(a). Each | element                          | of  | the local | behavior |            | corre- |     |     |     |     |     |     |     |     |
(11)
| sponds to | one trellis | edge. The | corresponding |     | factor | node | in  |       |        |          |      |        |     |     |     |
| --------- | ----------- | --------- | ------------- | --- | ------ | ---- | --- | ----- | ------ | -------- | ---- | ------ | --- | --- | --- |
|           |             |           |               |     |        |      |     | where | is the | discrete | time | index, |     |     |     |
theWiberg-typegraphistheindicatorfunction
|     |     |     |     |     |     |     |     | arethetime- |     | inputvariables, |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------------- | --- | --- | --- | --- | --- |
.
|     |     |     |     |     |     |     |     | arethetime- | outputvariables, |     |     |     |     |     | are |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------------- | --- | --- | --- | --- | --- | --- |
It is important to note that a factor graph corresponding to thetime- statevariables, , , ,and are matricesofap-
atrellisiscycle-free.Sinceeverycodehasatrellisrepresenta- propriatedimension,andtheequationsareoversomefield .
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

506 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
AnysuchsystemgivesrisetothefactorgraphofFig.10.The
time- checkfunction
is
| Inother | words,the | checkfunction |     | enforcesthe |     | local | behavior |                                                                 |     |     |     |     |     |     |
| ------- | --------- | ------------- | --- | ----------- | --- | ----- | -------- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|         |           |               |     |             |     |       |          | Fig.11. FactorgraphforthejointAPPdistributionofcodewordsymbols. |     |     |     |     |     |     |
definedby(11).
|     |     |     |     |     |     |     |     | Forexample,if | isthebinarylinearcodeofExample2,then |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------------------------ | --- | --- | --- | --- | --- |
B. ProbabilisticModeling
|     |     |     |     |     |     |     |     | we have |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Weturnnowtoanotherimportantclassoffunctionsthatwe
willrepresentbyfactorgraphs:probabilitydistributions.Since
| conditional | and | unconditional |     | independence |     | of random | vari- |     |     |     |     |     |     |     |
| ----------- | --- | ------------- | --- | ------------ | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
ablesisexpressedintermsofafactorizationoftheirjointprob-
ability mass or density function, factor graphs for probability whosefactorgraphisshowninFig.11.
| distributions | arise | in many | situations. |     | We begin | again | with an |         |                 |        |     |             |     |        |
| ------------- | ----- | ------- | ----------- | --- | -------- | ----- | ------- | ------- | --------------- | ------ | --- | ----------- | --- | ------ |
|               |       |         |             |     |          |       |         | Various | types of Markov | models | are | widely used | in  | signal |
examplefromcodingtheory.
|     |     |     |     |     |     |     |     | processing | and communications. |     | The | key feature | of  | such |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------- | --- | --- | ----------- | --- | ---- |
Example 5 (APP Distributions): Consider the standard modelsisthattheyimplyanontrivialfactorizationofthejoint
coding model in which a codeword is probabilitymassfunctionoftherandomvariablesinquestion.
selected from a code of length and transmitted over a Thisfactorizationmayberepresentedbyafactorgraph.
| memoryless   | channel     |       | with corresponding |              |             | output | sequence    |                                            |     |        |           |             |     |      |
| ------------ | ----------- | ----- | ------------------ | ------------ | ----------- | ------ | ----------- | ------------------------------------------ | --- | ------ | --------- | ----------- | --- | ---- |
|              |             |       |                    |              |             |        |             | Example6(MarkovChains,HiddenMarkovModels): |     |        |           |             |     | In   |
|              |             | . For | each               | fixed        | observation |        | , the joint |                                            |     |        |           |             |     |      |
|              |             |       |                    |              |             |        |             | general, let                               |     | denote | the joint | probability |     | mass |
| a posteriori | probability |       | (APP)              | distribution |             | for    | the com-    |                                            |     |        |           |             |     |      |
functionofacollectionofrandomvariables.Bythechainrule
| ponents | of  | (i.e., | ) is | proportional |     | to the | function |     |     |     |     |     |     |     |
| ------- | --- | ------ | ---- | ------------ | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
ofconditionalprobability,wemayalwaysexpressthisfunction
|     |     | ,   | where | is  | the a | priori distribution |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | ----- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
as
| for the                       | transmitted  | vectors, |          | and      | is              | the conditional |     |     |     |     |     |     |     |     |
| ----------------------------- | ------------ | -------- | -------- | -------- | --------------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| probabilitydensityfunctionfor |              |          |          | when     | istransmitted.  |                 |     |     |     |     |     |     |     |     |
| Since                         | the observed |          | sequence | is fixed | for             | any instance    | of  |     |     |     |     |     |     |     |
| “decoding”agraphwemayconsider |              |          |          |          | tobeafunctionof |                 |     |     |     |     |     |     |     |     |
only,withthecomponentsof regardedasparameters.Inother Forexample,if ,then
| words,wemaywrite |     |     | or  |     | as  | ,meaningthat |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
theexpressiontobe“decoded”alwayshasthesameparametric
whichhasthefactorgraphrepresentationshowninFig.12(b).
| form, but | that | the parameter |     | will in | general | be different |     | in          |           |           |        |              |     |     |
| --------- | ---- | ------------- | --- | ------- | ------- | ------------ | --- | ----------- | --------- | --------- | ------ | ------------ | --- | --- |
|           |      |               |     |         |         |              |     | In general, | since all | variables | appear | as arguments |     | of  |
differentdecodinginstances.
,thefactorgraphofFig.12(b)hasnoad-
| Assuming | that | the | a priori | distribution | for | the transmitted |     |     |     |     |     |     |     |     |
| -------- | ---- | --- | -------- | ------------ | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
vantageoverthetrivialfactorgraphshowninFig.12(a).Onthe
| vectorsisuniformovercodewords,wehave |                                |     |     |     |     |     |       | ,                                    |     |     |     |     |     |     |
| ------------------------------------ | ------------------------------ | --- | --- | --- | --- | --- | ----- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
|                                      |                                |     |     |     |     |     |       | otherhand,supposethatrandomvariables |     |     |     |     |     | (in |
| where                                | isthecharacteristicfunctionfor |     |     |     |     | and | isthe |                                      |     |     |     |     |     |     |
thatorder)formaMarkovchain.Wethenobtainthenontrivial
| numberofcodewordsin |     |     | .Ifthechannelismemoryless,then |     |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
factorization
factorsas
|     |     |     |     |     |     |     |     | whosefactorgraphisshowninFig.12(c)for |     |     |     |     | .   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
Undertheseassumptions,wehave ContinuingthisMarkovchainexample,ifwecannotobserve
|     |     |     |     |     |     |     |      | each directly,butinsteadcanobserveonly |     |                                |     | ,theoutputofa |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------------------------------------- | --- | ------------------------------ | --- | ------------- | --- | --- |
|     |     |     |     |     |     |     | (12) | memorylesschannelwith                  |     | asinput,thenweobtainaso-called |     |               |     |     |
“hiddenMarkovmodel.”Thejointprobabilitymassordensity
functionfortheserandomvariablesthenfactorsas
| Now thecharacteristicfunction |     |     |     |     | itselfmayfactor |     | intoa |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
productoflocalcharacteristicfunctions,asdescribedinthepre-
| vioussubsection.Givenafactorgraph |     |     |     |     | for | ,weobtaina |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
factorgraphfor(ascaledversionof)theAPPdistributionover whose factor graph is shown in Fig. 12(d) for . Hidden
simplybyaugmenting withfactornodescorrespondingtothe Markov models are widely used in a variety of applications;
different factors in(12). The th such factor hasonly e.g., see [27] for a tutorial emphasizing applications in signal
| one argument, |     | namely | , since | is  | regarded | as a | parameter. | processing. |     |     |     |     |     |     |
| ------------- | --- | ------ | ------- | --- | -------- | ---- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
Thus,thecorrespondingfactornodesappearaspendantvertices Ofcourse,sincetrellisesmayberegardedasMarkovmodels
(“dongles”)inthefactorgraph. forcodes,thestrongresemblancebetweenthefactorgraphsof
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

KSCHISCHANGetal.:FACTORGRAPHSANDTHESUM-PRODUCTALGORITHM 507
Fig.12. Factorgraphsforprobabilitydistributions.(a)Thetrivialfactorgraph.(b)Thechain-rulefactorization.(c)AMarkovchain.(d)AhiddenMarkovmodel.
| Fig. 12(c) | and | (d) and | the factor | graphs | representing |     | trellises |     |     |     |     |     |
| ---------- | --- | ------- | ---------- | ------ | ------------ | --- | --------- | --- | --- | --- | --- | --- |
(Figs.9(b)and10)isnotaccidental.
InAppendixBwedescribeverybrieflythecloserelationship
| between | factor | graphs | and other | graphical | models | for | proba- |     |     |     |     |     |
| ------- | ------ | ------ | --------- | --------- | ------ | --- | ------ | --- | --- | --- | --- | --- |
bilitydistributions:modelsbasedonundirectedgraphs(Markov
| random | fields) | and models | based | on  | directed | acyclic | graphs |     |     |     |     |     |
| ------ | ------- | ---------- | ----- | --- | -------- | ------- | ------ | --- | --- | --- | --- | --- |
(Bayesiannetworks).
|     |     |     |     |     |     |     |     | Fig.13. Thefactorgraphinwhichtheforward/backwardalgorithmoperates: |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- |
IV. TRELLISPROCESSING thes arestatevariables,theu areinputvariables,thex areoutputvariables,
|     |     |     |     |     |     |     |     | andeachy istheoutputofamemorylesschannelwithinputx |     |     |     | .   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- |
Asdescribedintheprevioussection,animportantfamilyof
factor graphs contains the chain graphs that represent trellises theaposteriorijointprobabilitymassfunctionfor , ,and
or Markov models. We now apply the sum-product algorithm giventheobservation isproportionalto
| to such graphs, |     | and show | that | a variety | of well-known |     | algo- |     |     |     |     |     |
| --------------- | --- | -------- | ---- | --------- | ------------- | --- | ----- | --- | --- | --- | --- | --- |
rithms—theforward/backwardalgorithm,theViterbialgorithm,
| and the Kalman |     | filter—may | be  | viewed | as special | cases | of the |     |     |     |     |     |
| -------------- | --- | ---------- | --- | ------ | ---------- | ----- | ------ | --- | --- | --- | --- | --- |
sum-productalgorithm.
|     |     |     |     |     |     |     |     | where isagainregardedasaparameterof |     |     |     | (notanargument). |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | ---------------- |
ThefactorgraphofFig.13representsthisfactorizationof .
|     |     |     |     |     |     |     |     | Given ,wewouldliketofindtheAPPs |     |     |     | foreach . |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --------- |
A. TheForward/BackwardAlgorithm
|     |     |     |     |     |     |     |     | These marginal | probabilities |     | are proportional | to the following |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------- | --- | ---------------- | ---------------- |
Westartwiththeforward/backwardalgorithm,sometimesre- marginalfunctionsassociatedwith :
ferredtoincodingtheoryastheBCJR[4],APP,or“MAP”al-
| gorithm.  | This algorithm |        | is an  | application | of         | the sum-product |          |     |     |     |     |     |
| --------- | -------------- | ------ | ------ | ----------- | ---------- | --------------- | -------- | --- | --- | --- | --- | --- |
| algorithm | to the         | hidden | Markov | model       | of Example |                 | 6, shown |     |     |     |     |     |
inFig.12(d),ortothetrellisesofexamplesExamples3and4
|     |     |     |     |     |     |     |     | Since the factor | graph | of  | Fig. 13 is cycle-free, | these marginal |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ----- | --- | ---------------------- | -------------- |
(Figs. 9 and 10)in which certain variablesare observed at the functionsmaybecomputedbyapplyingthesum-productalgo-
| outputofamemorylesschannel. |     |     |     |     |     |     |     | rithmtothefactorgraphofFig.13. |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
The factor graph of Fig. 13 models the most general situ- Initialization: Asusualinacycle-freefactorgraph,thesum-
ation, which involves a combination of behavioral and prob- productalgorithmbeginsattheleafnodes.Trivialmessagesare
| abilistic | modeling. | We  | have | vectors |     |     |     | ,   |     |     |     |     |
| --------- | --------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
sentbytheinputvariablenodesandtheendmoststatevariable
,and thatrepresent,re- nodes.Eachpendantfactornodesendsamessagetothecorre-
spectively,inputvariables,outputvariables,andstatevariables spondingoutputvariablenode.AsdiscussedinSectionII,since
inaMarkovmodel,whereeachvariableisassumedtotakeon the output variable nodes have degree two, no computation is
valuesinafinitedomain.Thebehaviorisdefinedbylocalcheck performed; instead, incoming messages received on one edge
| functions |     |     |     | ,asdescribedinExamples3and |     |     |     |            |             |     |                    |                    |
| --------- | --- | --- | --- | -------------------------- | --- | --- | --- | ---------- | ----------- | --- | ------------------ | ------------------ |
|           |     |     |     |                            |     |     |     | are simply | transferred | to  | the other edge and | sent to the corre- |
4.Tohandlesituationssuchasterminatedconvolutionalcodes, spondingtrellischecknode.
wealsoallowfortheinputvariabletobesuppressedincertain Oncetheinitializationhasbeenperformed,thetwoendmost
trellissections,asintherightmosttrellissectionofFig.13. trellis check nodes and will have received messages on
Thismodelisa“hidden”Markovmodelinwhichwecannot three oftheirfouredges, andso willbeina positiontocreate
observetheoutputsymbolsdirectly.AsdiscussedinExample5, anoutputmessagetosendtoaneighboringstatevariablenode.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

508 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
|     |     |     |     |     |     |     | The and         | messageshaveawell-definedprobabilisticinter- |                                           |                |                 |     |           |        |
| --- | --- | --- | --- | --- | --- | --- | --------------- | -------------------------------------------- | ----------------------------------------- | -------------- | --------------- | --- | --------- | ------ |
|     |     |     |     |     |     |     | pretation:      |                                              | isproportionaltotheconditionalprobability |                |                 |     |           |        |
|     |     |     |     |     |     |     | massfunctionfor |                                              |                                           | giventhe“past” |                 |     | ;i.e.,for |        |
|     |     |     |     |     |     |     | each state      |                                              |                                           | ,              | is proportional |     | to the    | condi- |
tionalprobabilitythatthetransmittedsequencepassedthrough
|     |     |     |     |     |     |     | state           | given       | the past. | Similarly, |             |             | is proportional   | to       |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----------- | --------- | ---------- | ----------- | ----------- | ----------------- | -------- |
|     |     |     |     |     |     |     | the conditional | probability |           | mass       | function    | for         | giventhe          | “fu-     |
|     |     |     |     |     |     |     | ture”           |             | , i.e.,   | the        | conditional | probability |                   | that the |
|     |     |     |     |     |     |     | transmitted     | sequence    | passed    | through    |             | state       | . The probability |          |
thatthetransmittedsequencepassedthroughaparticularedge
isthusgivenby
NotethatifwewereinterestedintheAPPsforthestatevari-
Fig.14. Adetailedviewofthemessagespassedduringtheoperationofthe
|     |     |     |     |     |     |     | ables or | the symbol |     | variables | ,   | these could | also be | com- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --------- | --- | ----------- | ------- | ---- |
forward/backwardalgorithm.
putedbytheforward/backwardalgorithm.
Again,sincethestatevariableshavedegreetwo,nocomputation
|     |     |     |     |     |     |     | B. TheMin-SumandMax-ProductSemiringsandtheViterbi |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
isperformed;atstatenodesmessagesreceivedononeedgeare
Algorithm
simplytransferredtotheotheredge.
Wemightinmanycasesbeinterestedindeterminingwhich
| In the literature | on  | the forward/backward |     |     | algorithm | (e.g., |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------------------- | --- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
[4]),themessage isdenotedas ,themessage valid configuration has largest APP, rather than determining
isdenotedas ,andthemessage the APPs for the individual symbols. When all codeword are
isdenotedas .Additionally,themessage will a priori equally likely, this amounts to maximum-likelihood
| bedenotedas | .   |     |     |     |     |     | sequencedetection(MLSD). |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
AsmentionedinSectionII(seealso[31],[2]),thecodomain
Theoperationofthesum-productalgorithmcreatestwonat-
uralrecursions:onetocompute asafunctionof oftheglobalfunction representedbyafactorgraphmayin
and and the other to compute as a function of general be any semiring with two operations “ ” and “” that
and . These two recursions are called the forward satisfythedistributivelaw
| and backward | recursions, | respectively, |     | according | to  | the direc- |     |     |     |     |     |     |     |     |
| ------------ | ----------- | ------------- | --- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
(14)
| tion of message | flow | in the trellis. | The | forward | and | backward |     |     |     |     |     |     |     |     |
| --------------- | ---- | --------------- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Inanysuchsemiring,aproductoflocalfunctionsiswellde-
recursionsdonotinteract,sotheycouldbecomputedinparallel.
Fig.14givesadetailedviewofthemessageflowforasingle fined, as is the notion of summation of values of . It follows
|                  |           |          |     |             |            |     | thatthe “not-sum” |     | or summaryoperationis |     |     |     | also well-defined. |     |
| ---------------- | --------- | -------- | --- | ----------- | ---------- | --- | ----------------- | --- | --------------------- | --- | --- | --- | ------------------ | --- |
| trellis section. | The local | function | in  | this figure | represents | the |                   |     |                       |     |     |     |                    |     |
trellischeck . Infact,ourobservationthatthestructureofacycle-freefactor
The Forward/Backward Recursions: Specializing the gen- graphencodesexpressions(i.e.,algorithms)forthecomputation
|     |     |     |     |     |     |     | of marginal | functions | essentially |     | follows | from | the distributive |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ----------- | --- | ------- | ---- | ---------------- | --- |
eralupdateequation(6)tothiscase,wefind
|     |     |     |     |     |     |     | law (14),  | and so      | applies | equally | well   | to the       | general semiring |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ------- | ------- | ------ | ------------ | ---------------- | --- |
|     |     |     |     |     |     |     | case. This | observation |         | is key  | to the | “generalized | distributive     |     |
law”of[2].
AsemiringofparticularinterestfortheMLSDproblemisthe
|     |     |     |     |     |     |     | “max-product” | semiring, |     | in which | real | summation | is replaced |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | -------- | ---- | --------- | ----------- | --- |
Termination: The algorithm terminates with the computa- withthe“max”operator.Fornonnegativereal-valuedquantities
| tionofthe | messages. |     |     |     |     |     | , ,and       | ,“”distributesover“max” |              |     |     |           |           |     |
| --------- | --------- | --- | --- | --- | --- | --- | ------------ | ----------------------- | ------------ | --- | --- | --------- | --------- | --- |
|           |           |     |     |     |     |     | Furthermore, | with                    | maximization |     | as  | a summary | operator, |     |
Thesesumscanbeviewedasbeingdefinedovervalidtrellis
|                      |                               |                                   |     |       |              |       | the maximum | value                            | of  | a nonnegative |     | real-valued | function |       |
| -------------------- | ----------------------------- | --------------------------------- | --- | ----- | ------------ | ----- | ----------- | -------------------------------- | --- | ------------- | --- | ----------- | -------- | ----- |
| edges                |                               | suchthat                          |     |       | .Foreachedge |       |             |                                  |     |               |     |             |          |       |
|                      |                               |                                   |     |       |              |       |             | isviewedasthe“completesummary”of |     |               |     |             |          | ;i.e. |
| , we let             |                               | ,                                 |     | , and |              |       | .           |                                  |     |               |     |             |          |       |
| Denotingby           | thesetofedgesincidentonastate |                                   |     |       |              | inthe |             |                                  |     |               |     |             |          |       |
| thtrellissection,the |                               | and updateequationsmayberewritten |     |       |              |       |             |                                  |     |               |     |             |          |       |
as
FortheMLSDproblem,weareinterestednotsomuchindeter-
miningthismaximumvalue,asinfindingavalidconfiguration
|     |     |     |     |     |     | (13) | thatachievesthismaximum. |      |     |            |         |     |                     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------------------------ | ---- | --- | ---------- | ------- | --- | ------------------- | --- |
|     |     |     |     |     |     |      | In practice,             | MLSD | is  | most often | carried |     | out in the negative |     |
The basic operations in the forward and backward recursions log-likelihooddomain.Here,the“product”operationbecomes
aretherefore“sumsofproducts.” a“sum”andthe“ ”operationbecomesa“ ”operation,
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

KSCHISCHANGetal.:FACTORGRAPHSANDTHESUM-PRODUCTALGORITHM 509
so that we deal with the “min-sum” semiring. For real-valued linear combinations of jointly Gaussian random variables are
quantities , , ,“ ”distributesover“min” Gaussian, it follows that the and sequences are jointly
Gaussian.
Weusethenotation
WeextendIverson’sconventiontothegeneralsemiringcase
by assuming that contains a multiplicative identity and a
nullelement suchthat and forall . to represent Gaussian density functions, where and rep-
When isapredicate,thenby wemeanthe -valued resentthemeanandvariance.Bycompletingthesquareinthe
functionthattakesvalue whenever istrueand otherwise. exponent,wefindthat
Inthe“min-sum”semiring,wherethe“product”isrealaddition, (16)
wetake and .Underthis extensionofIverson’s
where
convention,factorgraphsrepresentingcodesarenotaffectedby
thechoiceofsemiring.
Consider again the chain graph that represents a trellis, and
and
suppose that we apply the min-sum algorithm; i.e., the sum-
product algorithm in the min-sum semiring. Products of posi-
tivefunctions(intheregularfactorgraph)areconvertedtosums
Similarly,wefindthat
of functions (appropriate for the min-sum semiring) by taking
their negative logarithm. Indeed, such functions can be scaled
andshifted(e.g.,setting where
(17)
and are constants with ) in any manner that is con-
venient. In this way, for example, we may obtain squared Eu- AsinExample5,theMarkovstructureofthissystempermits
clideandistanceasa“branchmetric”inGaussianchannels,and ustowritetheconditionaljointprobabilitydensityfunctionof
Hammingdistanceasa“branchmetric”indiscretesymmetric thestatevariables given as
channels.
Applying the min-sum algorithm in this context yields the (18)
samemessageflowasintheforward/backwardalgorithm.Asin
theforward/backwardalgorithm,wemaywriteanupdateequa- where isaGaussiandensitywithmean
tion for the various messages. For example, the basic update and variance , and is a Gaussian density with
equationcorrespondingto(13)is mean andvariance .Again,theobservedvaluesofthe
outputvariablesareregardedasparameters,notasfunctionar-
(15)
guments.
so thatthe basicoperationis a “minimumof sums”insteadof Theconditionaldensityfunctionfor givenobservationsup
a “sum of products.” A similar recursion may be used in the totime isthemarginalfunction
backwarddirection,andfromtheresultsofthetworecursions
the most likely sequence may be determined. The result is a
“bidirectional”Viterbialgorithm.
The conventional Viterbi algorithm operates in the forward
where we have introduced an obvious generalization of the
directiononly;however,sincememoryofthebestpathismain-
“not-sum” notation to integrals. The mean of this conditional
tained and some sort of “traceback” is performed in making
density, is the minimum mean-
a decision, even the conventional Viterbi algorithm might be
squared-error (MMSE) estimate of given the observed
viewedasbeingbidirectional.
outputs. This conditional density function can be computed
C. KalmanFiltering via the sum-product algorithm, using integration (rather than
summation)asthesummaryoperation.
Inthissection,wederivetheKalmanfilter(see,e.g.,[3],[23])
A portion of the factor graph that describes (18) is shown
as an instance of the sum-product algorithm operating in the
in Fig. 15. Also shown in Fig. 15 are messages that are
factorgraphcorrespondingtoadiscrete-timelineardynamical
passed in the operation of the sum-product algorithm.
systemsimilartothatgivenby(11).Forsimplicity,wefocuson
We denote by the message passed to from
thecaseinwhichallvariablesarescalarssatisfying
. Up to scale, this message is always of the form
, and so may be represented by the
pair . We interpret as the MMSE
where , , , and are the time- state, output, input, predictionof giventhesetofobservationsuptotime .
and noise variables, respectively, and , , , and are Accordingtotheproductrule,applying(16),wehave
assumedtobeknowntime-varyingscalars.Generalizationtothe
caseofvectorvariablesisstandard,butwillnotbepursuedhere.
Weassumethattheinput andnoise areindependentwhite
Gaussiannoisesequenceswithzeromeanandunitvariance,and
that the state sequence is initialized by setting . Since
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore. Restrictions apply.

510 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
orLDPCcodes—arisepreciselyinsituationsinwhichtheun-
derlyingfactorgraphdoeshavecycles.Extensivesimulationre-
|     |     |     |     | sults(see, | e.g.,[5],[21],[22])show |     | thatwithverylongcodes |     |
| --- | --- | --- | --- | ---------- | ----------------------- | --- | --------------------- | --- |
suchdecodingalgorithmscanachieveastonishingperformance
(withinasmallfractionofadecibeloftheShannonlimitona
Gaussianchannel)eventhoughtheunderlyingfactorgraphhas
cycles.
Descriptionsofthewayinwhichthesum-productalgorithm
Fig.15. Aportionofthefactorgraphcorrespondingto(18).
maybeappliedtoavarietyof“compoundcodes”aregivenin
|     |     |     |     | [19]. In | this section, we | restrict ourselves | to three examples: |     |
| --- | --- | --- | --- | -------- | ---------------- | ------------------ | ------------------ | --- |
where
turbocodes[5],LDPCcodes[11],andrepeat–accumulate(RA)
codes[6].
A. Message-PassingSchedules
|     |     |     |     | Although | a clock may   | not be           | necessary in practice, | we   |
| --- | --- | --- | --- | -------- | ------------- | ---------------- | ---------------------- | ---- |
|     |     |     |     | assume   | that messages | are synchronized | with a global          | dis- |
and
|     |     |     |     | crete-time  | clock, with         | at most one | message passed  | on any  |
| --- | --- | --- | --- | ----------- | ------------------- | ----------- | --------------- | ------- |
|     |     |     |     | edge in     | any given direction | at one      | time. Any such  | message |
|     |     |     |     | effectively | replaces previous   | messages    | that might have | been    |
Likewise,applying(17),wehave
|     |     |     |     | sent on                                     | that edge in the                        | same direction. | A message | sent from |
| --- | --- | --- | --- | ------------------------------------------- | --------------------------------------- | --------------- | --------- | --------- |
|     |     |     |     | node attime                                 | willbeafunctiononlyofthelocalfunctionat |                 |           |           |
|     |     |     |     | (ifany)andthe(mostrecent)messagesreceivedat |                                         |                 |           | priorto   |
time .
|     |     |     |     | Sincethemessagesentbyanode |     |     | onanedgeingeneralde- |     |
| --- | --- | --- | --- | -------------------------- | --- | --- | -------------------- | --- |
where
pendsonthemessagesthathavebeenreceivedonotheredgesat
,andafactorgraphwithcyclesmayhavenonodesofdegree
|     |     |     | (19) | one,howismessagepassinginitiated?Wecircumventthisdiffi- |                    |             |               |       |
| --- | --- | --- | ---- | ------------------------------------------------------- | ------------------ | ----------- | ------------- | ----- |
| and |     |     |      | cultybyinitiallysupposingthataunitmessage(i.e.,amessage |                    |             |               |       |
|     |     |     |      | representing                                            | the unit function) | has arrived | on every edge | inci- |
dentonanygivenvertex.Withthisconvention,everynodeisin
apositiontosendamessageateverytimealongeveryedge.
Amessage-passingscheduleinafactorgraphisaspecifica-
In(19),thevalue tionofmessagestobepassedduringeachclocktick.Obviously
|     |     |     |     | a wide variety | of message-passing     | schedules | are possible.  | For    |
| --- | --- | --- | --- | -------------- | ---------------------- | --------- | -------------- | ------ |
|     |     |     |     | example,       | the so-called flooding | schedule  | [19] calls for | a mes- |
sagetopassineachdirectionovereachedgeateachclocktick.
iscalledthefiltergain.
|     |     |     |     | A schedule | in which at | most one message | is passed | anywhere |
| --- | --- | --- | --- | ---------- | ----------- | ---------------- | --------- | -------- |
TheseupdatesarethoseusedbyaKalmanfilter[3].Asmen-
inthegraphateachclocktickiscalledaserialschedule.
| tioned, generalization | to the vector | case is standard. | We note |                      |     |                            |     |     |
| ---------------------- | ------------- | ----------------- | ------- | -------------------- | --- | -------------------------- | --- | --- |
|                        |               |                   |         | Wewillsaythatavertex |     | hasamessagependingatanedge |     |     |
thatsimilarupdateswouldapplytoanycycle-freefactorgraph
|     |     |     |     | ifithasreceivedanymessagesonedgesotherthan |     |     |     | afterthe |
| --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | -------- |
inwhichalldistributions(factors)areGaussian.Theoperation
|     |     |     |     | transmission | of the most | previous message | on . Such | a mes- |
| --- | --- | --- | --- | ------------ | ----------- | ---------------- | --------- | ------ |
ofthesum-productalgorithminsuchagraphcan,therefore,be
sageispendingsincethemessagesmorerecentlyreceivedcan
regardedasageneralizedKalmanfilter,andinagraphwithcy-
|     |     |     |     | affectthemessagetobesenton |     | .Thereceiptofamessageat |     |     |
| --- | --- | --- | --- | -------------------------- | --- | ----------------------- | --- | --- |
clesasaniterativeapproximationtotheKalmanfilter.
|     |     |     |     | fromanedge | willcreatependingmessagesatallotheredges |          |                         |     |
| --- | --- | --- | --- | ---------- | ---------------------------------------- | -------- | ----------------------- | --- |
|     |     |     |     | incident   | on . Only pending                        | messages | need to be transmitted, |     |
V. ITERATIVEPROCESSING:THESUM-PRODUCTALGORITHM
sinceonlypendingmessagescanbedifferentfromtheprevious
INFACTORGRAPHSWITHCYCLES
messagesentonagivenedge.
Inaddition toitsapplication tocycle-freefactor graphs,the In a cycle-free factor graph, assuming a schedule in which
sum-product algorithm may also be applied to factor graphs onlypending messagesare transmitted, the sum-product algo-
with cycles simply by following the same message propaga- rithmwilleventuallyhaltinastatewithnomessagespending.
tion rules, since all updates are local. Because of the cycles Inafactorgraphwithcycles,however,itisimpossibletoreach
in the graph, an “iterative” algorithm with no natural termi- a state with no messages pending, since the transmission of a
nation will result, with messages passed multiple times on a message on any edge of a cycle from a node will trigger a
givenedge.Incontrastwiththecycle-freecase,theresultsofthe chainofpendingmessagesthatmustreturnto ,triggering to
sum-productalgorithm operatinginafactorgraphwithcycles sendanothermessageonthesameedge,andsoonindefinitely.
cannot in general be interpreted as exact function summaries. Inpractice,allschedulesarefinite.Forafiniteschedule,the
However, some of the most exciting applications of the sum- sum-product algorithm terminates by computing, for each ,
product algorithm—for example, the decoding of turbo codes the product of the most recent messages received at variable
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

| KSCHISCHANGetal.:FACTORGRAPHSANDTHESUM-PRODUCTALGORITHM |     |     |     |     |     |     |     |     |     |     |     |     | 511 |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.16. Turbocode.(a)Encoderblockdiagram.(b)Factorgraph.
| node .If                  | hasnomessagespending,thenthiscomputation |         |     |              |      |              |     |     |     |     |     |     |     |
| ------------------------- | ---------------------------------------- | ------- | --- | ------------ | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| is equivalent             | to the                                   | product | of  | the messages | sent | and received |     |     |     |     |     |     |     |
| onanysingleedgeincidenton |                                          |         |     | .            |      |              |     |     |     |     |     |     |     |
B. IterativeDecodingofTurboCodes
A“turbocode”(“parallelconcatenatedconvolutionalcode”)
| hastheencoderstructureshowninFig.16(a).Ablock |     |     |     |     |     | ofdata |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Fig.17. AfactorgraphforaLDPCcode.
| tobetransmittedentersasystematicencoderwhichproduces |            |      |               |     |                      |            | ,           |             |              |         |                         |        |         |
| ---------------------------------------------------- | ---------- | ---- | ------------- | --- | -------------------- | ---------- | ----------- | ----------- | ------------ | ------- | ----------------------- | ------ | ------- |
| andtwoparity-checksequences                          |            |      |               | and | atitsoutput.Thefirst |            |             |             |              |         |                         |        |         |
|                                                      |            |      |               |     |                      |            | LDPC        | codes, like | turbo codes, | are     | very effectivelydecoded |        |         |
| parity-check                                         | sequence   |      | is generated  |     | via a standard       | recursive  |             |             |              |         |                         |        |         |
|                                                      |            |      |               |     |                      |            | using the   | sum-product | algorithm;   | for     | example                 | MacKay | and     |
| convolutionalencoder;viewedtogether,                 |            |      |               |     | and wouldformthe     |            |             |             |              |         |                         |        |         |
|                                                      |            |      |               |     |                      |            | Neal report | excellent   | performance  | results | approaching             |        | that of |
| output of                                            | a standard | rate | convolutional |     | code.                | The second |             |             |              |         |                         |        |         |
parity-checksequence isgeneratedbyapplyingapermutation turbo codes using what amounts to a flooding schedule [21],
[22].
| to the                                                    | input stream, |          | and applying | the        | permuted | stream to | a          |     |     |     |     |     |     |
| --------------------------------------------------------- | ------------- | -------- | ------------ | ---------- | -------- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
| second convolutional                                      |               | encoder. |              | All output | streams  | , , and   |            |     |     |     |     |     |     |
| aretransmittedoverthechannel.Bothconstituentconvolutional |               |          |              |            |          |           | D. RACodes |     |     |     |     |     |     |
encodersaretypicallyterminatedinaknownendingstate. RAcodesareaspecial,low-complexityclassofturbocodes
Afactorgraphrepresentationfora(very)shortturbocodeis introducedbyDivsalar,McEliece,andothers,whoinitiallyde-
showninFig.16(b).Includedinthefigurearethestatevariables vised these codes because their ensemble weight distributions
forthetwoconstituentencoders,aswellasaterminatingtrellis are relatively easy to derive. An encoder for an RA code op-
sectioninwhichnodataisabsorbed,butoutputsaregenerated.
|     |     |     |     |     |     |     | erates on | input | bits | repeating |     | each bit | times, |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ---- | --------- | --- | -------- | ------ |
Exceptfortheinterleaver(andtheshortblocklength),thisgraph and permuting the result to arrive at a sequence .
is generic, i.e., all standard turbo codesmay be representedin Anoutputsequence isformedviaanaccumulator
| this way. |     |     |     |     |     |     | thatsatisfies |     | and |     | for |     | .   |
| --------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
Iterativedecodingofturbocodesisusuallyaccomplishedvia Two equivalent factor graphs for an RA code are shown in
| a message-passing |     | schedule | that | involves | a forward/backward |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | ---- | -------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.18.ThefactorgraphofFig.18(a)isastraightforwardrepre-
computationovertheportionofthegraphrepresentingonecon- sentationoftheencoderasdescribedinthepreviousparagraph.
stituentcode,followedbypropagationofmessagesbetweenen- Thechecksallenforcetheconditionthatincidentvariablessum
coders (resulting in the so-called extrinsic information in the tozeromodulo .(Thusa degree-twocheckenforcesequality
turbo-coding literature). This is then followed by another for- of the two incident variables.) The equivalent but slightly less
| ward/backward | computation |     | over | the | other constituent | code, |             |       |               |      |          |             |     |
| ------------- | ----------- | --- | ---- | --- | ----------------- | ----- | ----------- | ----- | ------------- | ---- | -------- | ----------- | --- |
|               |             |     |      |     |                   |       | complicated | graph | of Fig. 18(b) | uses | equality | constraints | to  |
and propagation of messages back to the first encoder. This represent the same code. Thus, e.g., , corre-
scheduleofmessagesisillustratedin[19,Fig.10];seealso[31]. spondingtoinputvariable andstatevariables , ,and
ofFig.18(a).
C. LDPCCodes
LDPC codes were introduced by Gallager [11] in the early E. SimplificationsforBinaryVariablesandParityChecks
1960s. LDPC codes are defined in terms of a regular bipartite For particular decoding applications, the generic updating
graph. In a LDPC code, left nodes, representing code- rules(5)and(6)canoftenbesimplifiedsubstantially.Wetreat
wordsymbols,allhavedegree ,whilerightnodes,representing here only the important case where all variables are binary
checks, all have degree . For example, Fig. 17 illustrates the (Bernoulli) and all functions except single-variable functions
factorgraphforashort LDPCcode.Thecheckenforces are parity checks or repetition (equality) constraints, as in
theconditionthattheadjacentsymbolsshouldhaveevenoverall Figs. 11,17, and 18. Thisincludes,inparticular, LDPCcodes
parity,muchasinExample2.AsinExample2,thisfactorgraph and RA codes. These simplifications are well known, some
isjusttheoriginalunadornedTannergraphforthecode. datingbacktotheworkofGallager[11].
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

512 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
Fig.18. EquivalentfactorgraphsforanRAcode.
The probability mass function for a binary random variable LikelihoodDifference(LD):
| mayberepresentedbythevector |                                         |          |     | ,where |      |          | . Definition: |     |     |     | .   |     |
| --------------------------- | --------------------------------------- | -------- | --- | ------ | ---- | -------- | ------------- | --- | --- | --- | --- | --- |
| According                   | to the generic                          | updating |     | rules, | when | messages |               |     |     |     |     |     |
|                             | and arriveatavariablenodeofdegreethree, |          |     |        |      |          |               |     |     |     |     |     |
theresulting(normalized)outputmessageshouldbe
|     |     |     |     |     |     | (20) | SignedLog-LikelihoodDifference(SLLD): |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------------------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |      | Definition:                           |     |     |     |     | .   |
Similarly,atachecknoderepresentingthefunction
if
| (where“ | ”representsmodulo- |     | addition),wehave |     |     |     |     |     |     |     |     |     |
| ------- | ------------------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(21)
Wenotethatatchecknoderepresentingthedual(repetitioncon-
| straint)         |           |            | ,wewouldhave |     |         |         |     |     |     | if  |     |     |
| ---------------- | --------- | ---------- | ------------ | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
| i.e., the update | rules for | repetition | constraints  |     | are the | same as |     |     |     |     |     |     |
IntheLLRdomain,weobservethatfor
| those for | variable nodes, | and these | may | be  | viewed as | duals | to  |     |     |     |     |     |
| --------- | --------------- | --------- | --- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- |
thoseforasimpleparity-checkconstraint.
|         |               |               |     |     |          |          | Thus,anapproximationtothe |     |     |     | function(22)is |     |
| ------- | ------------- | ------------- | --- | --- | -------- | -------- | ------------------------- | --- | --- | --- | -------------- | --- |
| We view | (20) and (21) | as specifying |     | the | behavior | of ideal |                           |     |     |     |                |     |
“probabilitygates”thatoperatemuchlikelogicgates,butwith
soft(“fuzzy”)values.
| Since | ,binaryprobabilitymassfunctionscanbe |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichturnsouttobepreciselythemin-sumupdaterule.
parametrizedbyasinglevalue.Dependingontheparametriza-
Byapplyingtheequivalencebetweenfactorgraphsillustrated
| tion, various  | probability       | gate | implementations |        | arise. | We give |         |                |           |       |          |                |
| -------------- | ----------------- | ---- | --------------- | ------ | ------ | ------- | ------- | -------------- | --------- | ----- | -------- | -------------- |
|                |                   |      |                 |        |        |         | in Fig. | 19, it is easy | to extend | these | formulas | to cases where |
| four different | parametrizations, |      | and             | derive | the    | and     |         |                |           |       |          |                |
variablenodesorchecknodeshavedegreelargerthanthree.In
functionsforeach. particular,wemayextendthe and functionstomore
| LikelihoodRatio(LR): |     |     |     |     |     |     | thantwoargumentsviatherelations |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- |
| Definition:          |     |     | .   |     |     |     |                                 |     |     |     |     |     |
(23)
Ofcourse,thereareotheralternatives,correspondingtothevar-
|     |     |     |     |     |     |     | iousbinarytreeswith |     | leafvertices.Forexample,when |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ---------------------------- | --- | --- | --- |
|     |     |     |     |     |     |     | wemaycompute        |     |                              |     | as  |     |
Log-LikelihoodRatio(LLR):
| Definition: |     |     |     | .   |     |     |       |                   |      |            |     |                      |
| ----------- | --- | --- | --- | --- | --- | --- | ----- | ----------------- | ---- | ---------- | --- | -------------------- |
|             |     |     |     |     |     |     | which | would have better | time | complexity |     | in a parallel imple- |
mentationthanacomputationbasedon(23).
VI. FACTOR-GRAPHTRANSFORMATIONS
Inthissectionwedescribeanumberofstraightforwardtrans-
|     |     |     |     |     |     | (22) | formations | that may | be applied |     | to a factor | graph in order to |
| --- | --- | --- | --- | --- | --- | ---- | ---------- | -------- | ---------- | --- | ----------- | ----------------- |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

| KSCHISCHANGetal.:FACTORGRAPHSANDTHESUM-PRODUCTALGORITHM |     |     |     |     |     |     |     |     |     |     |     |     |     | 513 |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
factorgraph.Alsonoticethattherearetwolocalfunctionscon-
|     |     |     |     |     |     |     |     | necting   | to        | .          |        |       |              |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---------- | ------ | ----- | ------------ | --- |
|     |     |     |     |     |     |     |     | The local | functions | in the new | factor | graph | retain their | de- |
pendencesfromtheoldfactorgraph.Forexample,although
|     |     |     |     |     |     |     |     | isconnectedto | andthepairofvariables |                  |          |             | ,itdoesnotac- |        |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------------------- | ---------------- | -------- | ----------- | ------------- | ------ |
|     |     |     |     |     |     |     |     | tually depend | on                    | . So, the global | function | represented |               | by the |
newfactorgraphis
Fig.19. Transformingvariableandchecknodesofhighdegreetomultiple
nodesofdegreethree.
modifyafactorgraphwithaninconvenientstructureintoamore
convenientform.Forexample,itisalwayspossibletotransform whichisidenticaltotheglobalfunctionrepresentedbytheold
factorgraph.
afactorgraphwithcyclesintoacycle-freefactorgraph,butat
theexpenseofincreasingthecomplexityofthelocalfunctions In Fig. 20(b), there is still one cycle; however, it can be re-
movedbyclusteringfunctionnodes.InFig.20(c),wehaveclus-
| and/or the | domains | of  | the variables. | Nevertheless, |     | such | trans- |                                       |     |     |     |     |      |     |
| ---------- | ------- | --- | -------------- | ------------- | --- | ---- | ------ | ------------------------------------- | --- | --- | --- | --- | ---- | --- |
|            |         |     |                |               |     |      |        | teredthelocalfunctionscorrespondingto |     |     |     | ,   | ,and |     |
formationscanbeusefulinsomecases;forexample,attheend
ofthissectionweapplythemtoderiveanFFTalgorithmfrom
(24)
| the factor | graph | representing | the | DFT | kernel. | Similar | general |     |     |     |     |     |     |     |
| ---------- | ----- | ------------ | --- | --- | ------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Thenewglobalfunctionis
| procedures | are | described | in [17], | [20], | and in | the construction |     |     |     |     |     |     |     |     |
| ---------- | --- | --------- | -------- | ----- | ------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ofjunctiontreesin[2].
A. Clustering
| It is        | always | possible | to cluster   | nodes         | of  | like type—i.e., |     |     |     |     |     |     |     |     |
| ------------ | ------ | -------- | ------------ | ------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| all variable | nodes  | or       | all function | nodes—without |     | changing        |     |     |     |     |     |     |     |     |
whichisidenticaltotheoriginalglobalfunction.
| the global | function | being | represented |     | by a factor | graph. | We  |     |     |     |     |     |     |     |
| ---------- | -------- | ----- | ----------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
consider the case of clustering two nodes, but this is easily Inthiscase,byclusteringvariableverticesandfunctionver-
|             |           |           |     |     |     |           |       | tices, we | have removed | the cycles | from | the factor | graph | frag- |
| ----------- | --------- | --------- | --- | --- | --- | --------- | ----- | --------- | ------------ | ---------- | ---- | ---------- | ----- | ----- |
| generalized | to larger | clusters. | If  | and | are | two nodes | being |           |              |            |      |            |       |       |
clustered, simply delete and and any incident edges from ment.Iftheremainderofthegraphiscycle-free,thenthesum-
the factor graph, introduce a new node representing the pair productalgorithmmaybeusedtocomputeexactmarginals.No-
ticethatthesizesofthemessagesinthisregionofthegraphhave
,andconnectthisnewnodetonodesthatwereneighbors
of or intheoriginalgraph. increased.Forexample, and havealphabetsofsize and
|             |         |          |                |         |     |        |       | , respectively,                             |     | and if functions | are | represented | by  | a list of |
| ----------- | ------- | -------- | -------------- | ------- | --- | ------ | ----- | ------------------------------------------- | --- | ---------------- | --- | ----------- | --- | --------- |
| When        | and     | are      | variables with | domains |     | and    | , re- |                                             |     |                  |     |             |     |           |
|             |         |          |                |         |     |        |       | theirvalues,thelengthofthemessagepassedfrom |     |                  |     |             | to  |           |
| spectively, | the new | variable | has            | domain  |     | . Note | that  |                                             |     |                  |     |             |     |           |
the size of this domain is the product of the original domain isequaltotheproduct .
sizes,whichcanimplyasubstantialcostincreaseincomputa-
B. StretchingVariableNodes
| tional complexity |     | of the | sum-product | algorithm. |     | Any function |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------ | ----------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
thathad or asanargumentintheoriginalgraphmustbe In the operation of the sum-product algorithm, in the mes-
converted into an equivalent function that has as an sagepassedonanedge ,localfunctionproductsaresum-
argument,butthiscanbeaccomplishedwithoutincreasingthe marized for the variable associated with the edge. Outside of
complexityofthelocalfunctions. thoseedgesincidentonaparticularvariablenode ,anyfunc-
When and arelocalfunctions,bythepair wemean tiondependencyon isrepresentedinsummaryform;i.e., is
| theproductofthelocalfunctions.If |     |     |     |     | and | denotethesets |     | marginalizedout. |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
ofargumentsof and ,respectively,then istheset Here we will introduce a factor graph transformation that
ofarguments ofthe product.Pairingfunctionsinthisway can willextendtheregioninthegraphoverwhich isrepresented
implyasubstantialcostincreaseincomputationalcomplexityof without being summarized. Let denote the set of nodes
thesum-productalgorithm;however,clusteringfunctionsdoes thatcanbereachedfrom byapathoflengthtwoin .Then
notincreasethecomplexityofthevariables. is a set of variable nodes, and for any , we
Clustering nodes may eliminate cycles in the graph so that can pair and , i.e., replace with the pair , much as
thesum-productalgorithminthenewgraphcomputesmarginal inaclusteringtransformation.Thefunctionnodesincidenton
functionsexactly.Forexample,clusteringthenodesassociated wouldhavetobemodifiedasinaclusteringtransformation,but,
with and inthefactorgraphfragmentofFig.20(a)andcon- asbefore,thismodificationdoesnotincreasetheircomplexity.
nectingtheneighborsofbothnodestothenewclusterednode, We call this a “stretching” transformation, since we imagine
we obtain the factor graph fragment shown in Fig. 20(b). No- node being“stretched”alongthepathfrom to .
tice that the local function node connecting and in the Moregenerally,wewillallowfurtherarbitrarystretchingof
originalfactorgraphappearswithjustasingleedgeinthenew .If isasetofnodestowhich hasbeenstretched,wewill
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

514 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
Fig.20. Clusteringtransformations.(a)Originalfactorgraphfragment.(b)Variablenodesyandzclustered.(c)Functionnodesf ,f ,andf clustered.
Fig.21. Stretchingtransformation.(a)Originalfactorgraph.(b)Nodex isstretchedtox andx .(c)Thenoderepresentingx aloneisnowredundantand
canberemoved.
allow tobestretchedtoanyelementof ,thesetofvari- whenevertheyariseastheresultofaseriesofstretchingtrans-
able nodes reachable from any node of by a path of length formations.
two. In stretching in this way, we retain the following basic Fig.12(b)illustratesanimportantmotivationforintroducing
property:thesetofnodestowhich hasbeenpaired(together thestretchingtransformation;itmaybepossibleforanedge,or
with the connecting function nodes) induces a connected sub- indeedavariablenode,tobecomeredundant.Let bealocal
graphofthefactorgraph.Thisconnectedsubgraphgeneratesa function, let be an edge incident on , and let be the set
well-defined set of edges over which is represented without ofvariables(fromtheoriginalfactorgraph)associatedwith .
being summarized in the operation of the sum-product algo- If is contained in the union of the variable sets associated
rithm.Thisstretchingleadstopreciselythesameconditionthat withtheedgesincidenton otherthan ,then isredundant.A
definejunctiontrees[2]:thesubgraphconsistingofthosever- redundantedgemaybedeletedfromafactorgraph.(Redundant
tices whose label includes a particular variable, together with edgesmustberemovedoneatatime,becauseitispossiblefor
theedgesconnectingthesevertices,isconnected. an edge to be redundant in the presence of another redundant
Fig. 21(a) shows a factor graph, and Fig. 21(b) shows an edge,andbecomerelevantoncethelatteredgeisremoved.)If
equivalent factor graph in which has been stretched to all alledgesincidentonavariablenodecanberemoved,thenthe
variablenodes. variablenodeitselfisredundantandmaybedeleted.
When a single variable is stretched in a factor graph, since For example, the node containing alone is redundant
allvariablenodesrepresentdistinctvariables,themodifiedvari- in Fig. 21(b) since each local function neighboring has a
ablesthatresultfromastretchingtransformationarealldistinct. neighbor(otherthan )towhich hasbeenstretched.Hence
However,ifwepermit morethan onevariable tobe stretched, thisnodeandtheedgesincidentonitcanberemoved,asshown
thismaynolongerholdtrue.Forexample,intheMarkovchain in Fig. 21(c). Note that we are not removing the variable
factorgraphofFig.12(c),ifboth and arestretchedtoall from the graph, but rather just a node representing . Here,
variables, the result will be a factor graph having two vertices unlike elsewhere in this paper, the distinction between nodes
representingthepair .Themeaningofsuchapeculiar andvariablesbecomesimportant.
“factorgraph”remainsclear,however,sincethelocalfunctions Let be a variable node involved in a cycle, i.e., for which
andhencealsotheglobalfunctionareessentiallyunaffectedby thereisanontrivialpath from toitself.Let
thestretchingtransformations.Allthatchangesisthebehavior bethelasttwoedgesin ,forsomevariablenode andsome
of the sum-product algorithm, since, in this example, neither functionnode .Letusstretch alongallofthevariablenodes
nor willeverbemarginalizedout.Hencewewillpermit involvedin .Thentheedge isredundantandhencecan
theappearanceofmultiplevariablenodesforasinglevariable bedeletedsinceboth and areincidenton .(Actually,
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore. Restrictions apply.

| KSCHISCHANGetal.:FACTORGRAPHSANDTHESUM-PRODUCTALGORITHM |     |     |     |     |     |     |     |     |     |     |     |     | 515 |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.22. TheDFT.(a)Factorgraph.(b)Aparticularspanningtree.(c)Spanningtreeafterclusteringandstretchingtransformation.
thereisalsoanotherredundantedge,correspondingtotraveling variablenodesappearingineachpathfrom toalocalfunction
in the opposite direction.) In this way, the cycle from to having asanargument.Intuitively, isnotmarginalizedout
| itselfisbroken. |     |     |     |     |     |     | intheregionof | inwhich |     | is“involved.” |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ------------- | ------- | --- | ------------- | --- | --- | --- |
Bysystematicallystretchingvariablesaroundcyclesandthen
| deletingaresultingredundantedgetobreakthecycle,itispos- |     |     |     |     |     |     | D. AnFFT |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
sibletousethestretchingtransformationtobreakallcyclesin AnimportantobservationduetoAjiandMcEliece[1],[2]is
thegraph,transforminganarbitraryfactorgraphintoanequiva- thatvariousfasttransformalgorithmsmaybedevelopedusing
lentcycle-freefactorgraphforwhichthesum-productalgorithm
|     |     |     |     |     |     |     | a graph-based | approach. | We  | now show | how we | may | use the |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | -------- | ------ | --- | ------- |
producesexactmarginals.Thiscanbedonewithoutincreasing factor-graphtransformationsofthissectiontoderiveanFFT.
thecomplexityofthelocalfunctions,butcomesattheexpense The DFT is a widely used tool for the analysis of dis-
ofan(oftenquitesubstantial)increaseinthecomplexityofthe crete-time signals. Let be a complex-
| variablealphabets. |      |                 |     |       |     |              | valued   | -tuple,andlet  |         |       | ,with  | ,beaprim-      |     |
| ------------------ | ---- | --------------- | --- | ----- | --- | ------------ | -------- | -------------- | ------- | ----- | ------ | -------------- | --- |
|                    |      |                 |     |       |     |              | itive th | root of unity. | The DFT | of    | is the | complex-valued |     |
| C. SpanningTrees   |      |                 |     |       |     |              | -tuple   |                |         | where |        |                |     |
| A spanning         | tree | for a connected |     | graph | is  | a connected, |          |                |         |       |        |                |     |
(25)
| cycle-freesubgraphof |     | havingthesamevertexsetas |     |     |     | .Let |     |     |     |     |     |     |     |
| -------------------- | --- | ------------------------ | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
beaconnectedfactorgraphwithaspanningtree andforevery Considernowthecasewhere isapoweroftwo,e.g.,
variablenode of ,let denotethesetoffunctionnodes for concreteness. We express variables and in (25) in
| having | as an argument. | Since |     | is a tree, | there | is a unique |              |            |        |     |     |     |         |
| ------ | --------------- | ----- | --- | ---------- | ----- | ----------- | ------------ | ---------- | ------ | --- | --- | --- | ------- |
|        |                 |       |     |            |       |             | binary; more | precisely, | we let |     |     |     | and let |
pathbetweenanytwonodesof ,andinparticularbetween ,where and takevaluesfrom .
and every element of . Now suppose is stretched to all WewritetheDFTkernel,whichwetakeasourglobalfunction,
variablenodesinvolvedineachpathfrom toeveryelementof intermsofthesevariablesas
| ,andlet                   | betheresultingtransformedfactorgraph.  |     |                             |     |                   |         |     |     |     |     |     |     |     |
| ------------------------- | -------------------------------------- | --- | --------------------------- | --- | ----------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| Itturnsoutthateveryedgeof |                                        |     | notin                       |     | isredundantandall |         |     |     |     |     |     |     |     |
| suchedgescanbedeletedfrom |                                        |     | .Indeed,if                  |     | isanedgeof        |         |     |     |     |     |     |     |     |
| notin                     | ,let bethesetofvariablesassociatedwith |     |                             |     |                   | ,andlet |     |     |     |     |     |     |     |
| bethelocalfunctiononwhich |                                        |     | isincident.Foreveryvariable |     |                   |         |     |     |     |     |     |     |     |
,thereisapathin from to ,and isstretchedtoall where and we have used the
variablenodesalongthispath,andinparticularisstretchedtoa
|     |     |     |     |     |     |     | relations |     | ,   |     | , and | .   | We see |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ----- | --- | ------ |
neighbor(in )of .Sinceeachelementof appearsinsome thattheDFTkernelfactorsintoaproductoflocalfunctionsas
| neighboringvariablenodenotinvolving |     |     |     | ,   | isredundant.The |     |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
expressedbythefactorgraphofFig.22(a).
removal of does not affect the redundant status of any other Weobservethat
| edgeof | notin | ,henceallsuchedgesmaybedeletedfrom |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ----- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
.
| Thisobservationimpliesthatthesum-productalgorithmcan |     |     |     |     |     |     |     |     |     |     |     |     | (26) |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
beusedtocomputemarginalfunctionsexactlyinanyspanning so that the DFT can be viewed as a marginal function, much
tree of ,providedthateachvariable isstretchedalongall like a probability mass function. When is composite, sim-
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

516 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
ilarprime-factor-baseddecompositionsof and willresultin Factor graphs afford great flexibility in modeling systems.
similarfactorgraphrepresentationsfortheDFTkernel. Both Willems’ behavioral approach to systems and the tradi-
The factor graph in Fig. 22(a) has cycles. We wish to carry tionalinput/outputorstate-spaceapproachesfitnaturallyinthe
out exact marginalization, so we form a spanning tree. There factor graph framework. The generality of allowing arbitrary
are many possible spanning trees, of which one is shown in functions (not just probability distributions or characteristic
Fig.22(b).(Differentchoicesforthespanningtreewillleadto functions) to be represented further enhances the flexibility of
| possiblydifferentDFTalgorithmswhenthesum-productalgo- |     |     |     |     |     |     | factorgraphs. |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
rithmisapplied.)Ifweclusterthelocalfunctionsasshownin Factorgraphs alsohavethe potentialtounifymodelingand
Fig.22(b),essentiallybydefining signalprocessingtasksthatareoftentreatedseparatelyincur-
rentsystems.Incommunicationsystems,forexample,channel
modelingandestimation,separationofmultipleusers,andde-
codingcanbetreatedinaunifiedwayusingasinglegraphical
modelthatrepresentstheinteractionsofthesevariouselements,
assuggestedbyWiberg[31].Webelievethatthefullpotentialof
thisapproachhasnotyetbeenrealized,andwesuggestthatfur-
thenwearriveatthespanningtreeshowninFig.22(c).Thevari-
ablesthatresultfromtherequiredstretchingtransformationare therexplorationofthemodelingpoweroffactorgraphsandap-
shown.Althoughtheyareredundant,wehaveincludedvariable plicationsofthesum-productalgorithmwillprovetobefruitful.
| nodes | and . | Observe | that each | message | sent | from left | to  |     |     |     |     |     |
| ----- | ----- | ------- | --------- | ------- | ---- | --------- | --- | --- | --- | --- | --- | --- |
rightisafunctionofthreebinaryvariables,whichcanberepre- APPENDIX A
sentedasalistofeightcomplexquantities.Alongthepathfrom FROMFACTORTREESTOEXPRESSIONTREES
| to    | first  |                                     | ,then | ,andthen | aremarginalized |     |     |     |               |     |          |           |
| ----- | ------ | ----------------------------------- | ----- | -------- | --------------- | --- | --- | --- | ------------- | --- | -------- | --------- |
|       |        |                                     |       |          |                 |     | Let |     | be a function |     | that can | be repre- |
| outas | , ,and | areaddedtotheargumentlistofthefunc- |       |          |                 |     |     |     |               |     |          |           |
sentedbyacycle-freeconnectedfactorgraph,i.e.,afactortree
| tions. In | three steps, | the | function | is  | converted | to the func- |     |     |     |     |     |     |
| --------- | ------------ | --- | -------- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- |
.Weareinterestedindevelopinganexpressionfor
tion .Clearly,wehaveobtainedanFFTasaninstanceofthe
sum-productalgorithm.
VII. CONCLUSION i.e.,thesummaryfor of .Weconsider tobetherootof ,
|        |                |     |           |           |             |        | sothatallotherverticesof |     | aredescendantsof |                    | .   |     |
| ------ | -------------- | --- | --------- | --------- | ----------- | ------ | ------------------------ | --- | ---------------- | ------------------ | --- | --- |
| Factor | graphs provide |     | a natural | graphical | description | of the |                          |     |                  |                    |     |     |
|        |                |     |           |           |             |        | Assumingthat             |     | has neighborsin  | ,thenwithoutlossof |     |     |
factorization of a global function into a product of local func- generality maybewrittenintheform
tions.Factorgraphscanbeappliedinawiderangeofapplication
areas,aswehaveillustratedwithalargenumberofexamples.
| A major | aim of | this paper | was | to demonstrate |     | that a single |     |     |     |     |     |     |
| ------- | ------ | ---------- | --- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
algorithm—thesum-productalgorithm—basedononlyasingle
conceptually simple computational rule, can encompass an where istheproductofalllocalfunctionsinthesub-
| enormous | variety | of practical | algorithms. |     | As we | have seen, |        |             |              |            |     |       |
| -------- | ------- | ------------ | ----------- | --- | ----- | ---------- | ------ | ----------- | ------------ | ---------- | --- | ----- |
|          |         |              |             |     |       |            | treeof | thathavethe | thneighborof | asroot,and |     | isthe |
these include the forward/backward algorithm, the Viterbi set of variables in that subtree. Since is a tree, for ,
| algorithm,     | Pearl’s    | belief | propagation | algorithm, |     | the iterative |     |                |     |     |        |         |
| -------------- | ---------- | ------ | ----------- | ---------- | --- | ------------- | --- | -------------- | --- | --- | ------ | ------- |
|                |            |        |             |            |     |               |     | and            |     |     |        | , i.e., |
| turbo decoding | algorithm, |        | the Kalman  | filter,    | and | even certain  |     |                |     |     |        |         |
|                |            |        |             |            |     |               |     | is a partition | of  |     | . This | decom-  |
FFT algorithms! Various extensions of these algorithms—for positionisrepresentedbythe genericfactortreeofFig.23,in
| example, | a Kalman | filter | operating |     | on a tree-structured |     |       |                        |     |     |     |     |
| -------- | -------- | ------ | --------- | --- | -------------------- | --- | ----- | ---------------------- | --- | --- | --- | --- |
|          |          |        |           |     |                      |     | which | isshowninexpandedform. |     |     |     |     |
system—althoughnottreatedhere,canbederivedinastraight- Now, by the distributive law, and using the fact that
forward manner by applying the principles enunciated in this arepairwisedisjoint,weobtain
paper.
| We have           | emphasized    |           | that the       | sum-product   | algorithm      | may          |     |     |     |     |     |     |
| ----------------- | ------------- | --------- | -------------- | ------------- | -------------- | ------------ | --- | --- | --- | --- | --- | --- |
| be applied        | to arbitrary  | factor    | graphs,        | cycle-free    | or             | not. In the  |     |     |     |     |     |     |
| cycle-free        | finitecase,we |           | haveshown      | thatthe       | sum-productal- |              |     |     |     |     |     |     |
| gorithm           | may be used   | to        | compute        | function      | summaries      | exactly.     |     |     |     |     |     |     |
| In some           | applications, | e.g.,     | in processing  |               | Markov         | chains and   |     |     |     |     |     |     |
| hidden Markov     | models,       |           | the underlying |               | factor graph   | is natu-     |     |     |     |     |     |     |
| rally cycle-free, | while         | in        | other          | applications, | e.g.,          | in decoding  |     |     |     |     |     |     |
| of LDPC           | codes and     | turbo     | codes,         | it is not.    | In the         | latter case, | a   |     |     |     |     |     |
| successful        | strategy      | has been  | simply         | to apply      | the            | sum-product  |     |     |     |     |     |     |
| algorithm         | without       | regard    | to the         | cycles.       | Nevertheless,  | in some      |     |     |     |     |     |     |
| cases it might    | be            | important | to obtain      | an            | equivalent     | cycle-free   |     |     |     |     |     |     |
representation,andwehavegivenanumberofgraphtransfor- i.e.,thesummaryfor of istheproductofthesummariesfor
mationsthatcanbeusedtoachievesuchrepresentations. ofthe functions.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

| KSCHISCHANGetal.:FACTORGRAPHSANDTHESUM-PRODUCTALGORITHM |     |     |     |     |     |     |     |              |                      |           |                    |               |        |              | 517    |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------------- | --------- | ------------------ | ------------- | ------ | ------------ | ------ |
|                                                         |     |     |     |     |     |     |     | The problem  | of computing         |           | the                | summary       | for    |              | of the |
|                                                         |     |     |     |     |     |     |     | product      | of the local subtree |           | descending         | from          |        | is a problem |        |
|                                                         |     |     |     |     |     |     |     | of the same  | general              | form with | which              | we            | began, | and          | so the |
|                                                         |     |     |     |     |     |     |     | same general | approach             | can       | be applied         | recursively.  |        | The          | result |
|                                                         |     |     |     |     |     |     |     | of this      | recursion justifies  |           | the transformation |               | of     | the          | factor |
|                                                         |     |     |     |     |     |     |     | tree for     | with root            | vertex    | into               | an expression |        | tree         | for    |
,asillustratedinFig.5.
APPENDIX B
OTHERGRAPHICALMODELSFORPROBABILITYDISTRIBUTIONS
Factorgraphsarebynomeansthefirstgraph-basedlanguage
|     |     |     |     |     |     |     |     | for describing | probability   | distributions. |     | In                 | the next | two     | exam- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------- | -------------- | --- | ------------------ | -------- | ------- | ----- |
|     |     |     |     |     |     |     |     | ples, we       | describe very | briefly        | the | close relationship |          | between |       |
factorgraphsandmodelsbasedonundirectedgraphs(Markov
|     |     |     |     |     |     |     |     | random | fields) and models |     | based | on directed | acyclic |     | graphs |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------------ | --- | ----- | ----------- | ------- | --- | ------ |
(Bayesiannetworks).
|     |     |     |     |     |     |     |     | A. MarkovRandomFields |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
AMarkovrandomfield(see,e.g.,[18])isagraphicalmodel
Fig.23. Agenericfactortree. basedonanundirectedgraph inwhicheachnode
|     |     |     |     |     |     |     |     | corresponds | to a random | variable. |     | The graph |     | is a Markov |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --------- | --- | --------- | --- | ----------- | --- |
Consider thecase .Tocompute thesummaryfor of randomfield (MRF) if the distribution satisfies
, observethat, withoutlossof generality, canbe thelocalMarkovproperty
written as
(27)
|     |     |     |     |     |     |     |     | where              | denotesthesetofneighborsof |                                    |     |     | .Inwords, |     | isan |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | -------------------------- | ---------------------------------- | --- | --- | --------- | --- | ---- |
|     |     |     |     |     |     |     |     | MRFifeveryvariable |                            | isindependentofnonneighboringvari- |     |     |           |     |      |
ablesinthegraph,giventhevaluesofitsimmediateneighbors.
| where, for | convenience, |     | we  | have | numbered | the | arguments |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | ---- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
MRFsarewelldevelopedinstatistics,andhavebeenusedina
| of so that |     |     |     | is  | the first | neighbor | of  | .   |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
varietyofapplications(see,e.g.,[18],[26],[16],[15]).
| This decomposition |     | is  | illustrated | in   | Fig.      | 23. We | note that |          |            |                 |     |             |     |       |         |
| ------------------ | --- | --- | ----------- | ---- | --------- | ------ | --------- | -------- | ---------- | --------------- | --- | ----------- | --- | ----- | ------- |
|                    |     |     |             |      |           |        |           | A clique | in a graph | is a collection |     | of vertices |     | which | are all |
|                    |     |     |             | is a | partition | of     | . Again,  |          |            |                 |     |             |     |       |         |
usingthefactthatthesesetsarepairwise-disjointandapplying pairwiseneighbors. Underfairly general conditions (e.g.,pos-
|     |     |     |     |     |     |     |     | itivity of | the joint probability |     | density | is sufficient), |     | the | joint |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------------------- | --- | ------- | --------------- | --- | --- | ----- |
thedistributivelaw,weobtain
probabilitymassfunctionofanMRFmaybeexpressedasthe
productofacollectionofGibbspotentialfunctions,definedon
|     |     |     |     |     |     |     |     | theset | ofcliquesintheMRF,i.e. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------------------- | --- | --- | --- | --- | --- | --- |
(28)
|     |     |     |     |     |     |     |     | where | is a normalizing |     | constant, | and | each |     | is a |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------------- | --- | --------- | --- | ---- | --- | ---- |
clique.Forexample(cf.Fig.1),theMRFinFig.24(a)maybe
usedtoexpressthefactorization
|     |     |     |     |     |     |     |     | Clearly, | (28) has precisely |     | the structure |     | needed | for a | factor |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | ------------- | --- | ------ | ----- | ------ |
graphrepresentation.Indeed,afactorgraphrepresentationmay
|                        |     |     |     |                             |     |               |     | be preferable  | to an MRF       | in  | expressing           | such | a    | factorization, |     |
| ---------------------- | --- | --- | --- | --------------------------- | --- | ------------- | --- | -------------- | --------------- | --- | -------------------- | ---- | ---- | -------------- | --- |
| Inwords,weseethatif    |     |     |     |                             |     | isaneighborof |     | ,              |                 |     |                      |      |      |                |     |
|                        |     |     |     |                             |     |               |     | since distinct | factorizations, |     | i.e., factorizations |      | with | different      |     |
| tocomputethesummaryfor |     |     |     | oftheproductofthelocalfunc- |     |               |     |                |                 |     |                      |      |      |                |     |
tionsinthesubtreeof descendingfrom ,weshoulddothe ’s in (28), may yield precisely the same underlying MRF
|     |     |     |     |     |     |     |     | graph, whereas | they | will always | yield | distinct | factor | graphs. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ----------- | ----- | -------- | ------ | ------- | --- |
following:
|             |          |     |     |        |      |            |     | (An example | in a coding | context |     | of this | MRF | ambiguity | is  |
| ----------- | -------- | --- | --- | ------ | ---- | ---------- | --- | ----------- | ----------- | ------- | --- | ------- | --- | --------- | --- |
| 1) for each | neighbor |     | of  | (other | than | ), compute | the |             |             |         |     |         |     |           |     |
givenin[19].)
| summary               | for |     | of the | product | of the | functions | in the |                     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ------ | ------- | ------ | --------- | ------ | ------------------- | --- | --- | --- | --- | --- | --- | --- |
| subtreedescendingfrom |     |     |        | ;       |        |           |        | B. BayesianNetworks |     |     |     |     |     |     |     |
2) form the product of these summaries with , summa- Bayesian networks (see, e.g., [25], [17], [10]) are graphical
rizingtheresultfor . models for a collection of random variables that are based on
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

518 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.47,NO.2,FEBRUARY2001
Fig.24. Graphicalprobabilitymodels.(a)AMarkovrandomfield.(b)ABayesiannetwork.(c)Afactorgraph.
directedacyclicgraphs(DAGs).Bayesiannetworks,combined
withPearl’s“beliefpropagationalgorithm”[25],havebecome
| an important | tool     | in          | expert | systems.    | The        | first | to connect   |     |     |     |     |     |     |
| ------------ | -------- | ----------- | ------ | ----------- | ---------- | ----- | ------------ | --- | --- | --- | --- | --- | --- |
| Bayesian     | networks | and         | belief | propagation |            | with  | applications |     |     |     |     |     |     |
| in coding    | theory   | were MacKay |        | and         | Neal [21]; | more  | recently,    |     |     |     |     |     |     |
[19],[24]developaviewofthe“turbodecoding”algorithm[5]
asaninstanceofprobabilitypropagationinaBayesiannetwork
modelofacode.
| Each node                 |          | in a Bayesian |       | network           | is  | associated | with     | a   |     |     |     |     |     |
| ------------------------- | -------- | ------------- | ----- | ----------------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
| randomvariable.Denotingby |          |               |       | thesetofparentsof |     |            | (i.e.,   |     |     |     |     |     |     |
| the set of                | vertices | from          | which | an edge           | is  | incident   | on ), by |     |     |     |     |     |     |
definition,thedistributionrepresentedbytheBayesiannetwork
maybewrittenas
Fig.25. Messagessentinbeliefpropagation.
(29)
|     |     |     |     |     |     |     |     | and isachildof       |     | .Messagessentbetweenvariablesarealways |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | -------------------------------------- | --- | --- | --- |
|     |     |     |     |     |     |     |     | functionsoftheparent |     | .In[25],amessagesentfrom               |     | to  | is  |
If (i.e., hasnoparents),wetake . denoted ,whileamessagesentfrom to isdenotedas
Forexample(cf.(2))Fig.24(b)showsaBayesiannetworkthat
,asshowninFig.25forthespecificBayesiannetworkof
| expressesthefactorization |                |     |         |             |          |              |              | Fig.24(c).                 |           |                    |                          |          |       |
| ------------------------- | -------------- | --- | ------- | ----------- | -------- | ------------ | ------------ | -------------------------- | --------- | ------------------ | ------------------------ | -------- | ----- |
|                           |                |     |         |             |          |              |              | Considerthecentralvariable |           |                    | inFig.25.Clearly,themes- |          |       |
|                           |                |     |         |             |          |              |              | sage sent                  | upwards   | by the sum-product | algorithm                | to the   | local |
|                           |                |     |         |             |          |              | (30)         | function                   | contained | in the ellipse     | is, from (5),            | given by | the   |
|                           |                |     |         |             |          |              |              | productoftheincoming       |           | messages,i.e.      |                          |          |       |
| Again, as                 | with Markov    |     | random  | fields,     | Bayesian | networks     | ex-          |                            |           |                    |                          |          |       |
| press a factorization     |                | of  | a joint | probability |          | distribution | that         | is                         |           |                    |                          |          |       |
| suitable for              | representation |     | by      | a factor    | graph.   | The          | factor graph |                            |           |                    |                          |          |       |
correspondingto(30)isshowninFig.24(c);cf.Fig.1. Themessagesentfrom to is,accordingto(6),theproduct
|         |                 |     |          |     |              |     |            | of withtheothermessagesreceivedat |     |     | summarizedfor |     | .   |
| ------- | --------------- | --- | -------- | --- | ------------ | --- | ---------- | --------------------------------- | --- | --- | ------------- | --- | --- |
| It is a | straightforward |     | exercise |     | to translate |     | the update |                                   |     |     |               |     |     |
rules that govern the operation of the sum-product algorithm Notethatthislocalfunctionistheconditionalprobabilitymass
to Pearl’s belief propagation rules [25], [17]. To convert a function ;hence
| Bayesian      | network | into    | a factor | graph:      | simply |         | introduce  | a   |     |     |     |     |     |
| ------------- | ------- | ------- | -------- | ----------- | ------ | ------- | ---------- | --- | --- | --- | --- | --- | --- |
| function node | for     | each    | factor   |             |        | in (29) | and draw   |     |     |     |     |     |     |
| edges from    | this    | node to | and      | its parents |        | .       | An example |     |     |     |     |     |     |
conversionfromaBayesiannetworktoafactorgraphisshown
inFig.24(c).
| Equations | similar | to  | Pearl’s | belief | updating |     | and bottom- |     |     |     |     |     |     |
| --------- | ------- | --- | ------- | ------ | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
up/top-down propagation rules [25, pp. 182–183] may be de- Similarly,themessage sentfrom totheellipsecon-
|     |     |     |     |     |     |     |     | taining | isgivenby |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | --- | --- | --- |
rivedfromthegeneralsum-productalgorithmupdateequations
(5)and(6)asfollows.
| In belief             | propagation, |     | messages   | are | sent     | between | “variable  |     |     |     |     |     |     |
| --------------------- | ------------ | --- | ---------- | --- | -------- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
| nodes,” corresponding |              | to  | the dashed |     | ellipses | for the | particular |     |     |     |     |     |     |
BayesiannetworkshowninFig.25.InaBayesiannetwork,ifan
| edgeisdirectedfromvertex |     |     |     | tovertex | ,then | isaparentof |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | -------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.

| KSCHISCHANGetal.:FACTORGRAPHSANDTHESUM-PRODUCTALGORITHM |     |     |     |     |     |     |     |     |     |     | 519 |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In general, let us denote the set of parents of a variable by [5] C. Berrou, A. Glavieux, and P. Thitimajshima, “Near Shannonlimit
, and the set of children of by . We will have, for error-correcting coding and decoding: Turbo codes,” in Proc. 1993
IEEEInt.Conf.Communications,Geneva,Switzerland,May1993,pp.
every
1064–1070.
|     |     |     |     |     |     | [6] D.Divsalar,H.Jin,andR.J.McEliece,“Codingtheoremsfor‘turbo- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- |
like’codes,”inProc.36thAllertonConf.Communications,Control,and
Computing,Urbana,IL,Sept.23–25,1998,pp.201–210.
|     |     |     |     |     |     | [7] G.D.ForneyJr.,“Oniterativedecodingandthetwo-wayalgorithm,”in |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- |
Proc.Int.Symp.TurboCodesandRelatedTopics,Brest,France,Sept.
|     |     |     |     |     | (31) | 1997.        |            |                       |     |             |         |
| --- | --- | --- | --- | --- | ---- | ------------ | ---------- | --------------------- | --- | ----------- | ------- |
|     |     |     |     |     |      | [8] , “Codes | on graphs: | Normal realizations,” |     | IEEE Trans. | Inform. |
and,forevery
Theory,vol.47,pp.520–548,Feb.2001.
|     |     |     |     |     |     | [9] B.J.FreyandF.R.Kschischang,“Probabilitypropagationanditerative |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- |
decoding,”inProc.34thAnnu.AllertonConf.Communication,Control,
andComputing,Monticello,IL,Oct.1–4,1996.
|     |     |     |     |     |     | [10] B.J.Frey,GraphicalModelsforMachineLearningandDigitalCom- |                             |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --------------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     | munication.                                                   | Cambridge,MA:MITPress,1998. |     |     |     |     |
(32)
|     |     |     |     |     |     | [11] R. G.Gallager, | Low-Density | Parity-Check | Codes. | Cambridge, | MA: |
| --- | --- | --- | --- | --- | --- | ------------------- | ----------- | ------------ | ------ | ---------- | --- |
MITPress,1963.
Theterminationconditionforcycle-freegraphs,calledthe“be-
|     |     |     |     |     |     | [12] R.Garello,G.Montorsi,S.Benedetto,andG.Cancellieri,“Interleaver |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- |
liefupdate”equationin[25],isgivenbytheproductofthemes-
|     |     |     |     |     |     | properties | and their applications | to the | trellis complexity |     | analysis of |
| --- | --- | --- | --- | --- | --- | ---------- | ---------------------- | ------ | ------------------ | --- | ----------- |
sagesreceivedby inthefactorgraph turbocodes,”IEEETrans.Commun.,tobepublished.
|     |     |     |     |     |      | [13] M.R.GareyandD.S.Johnson,ComputersandIntractability:AGuide |                                 |                        |            |              |        |
| --- | --- | --- | --- | --- | ---- | -------------------------------------------------------------- | ------------------------------- | ---------------------- | ---------- | ------------ | ------ |
|     |     |     |     |     |      | totheTheoryofNP-Completeness.                                  |                                 | NewYork:Freeman,1979.  |            |              |        |
|     |     |     |     |     |      | [14] R. L. Graham,                                             | D. E. Knuth,                    | and O.                 | Patashnik, | Concrete     | Mathe- |
| BEL |     |     |     |     |      | matics.                                                        | Reading,MA:Addison-Wesley,1989. |                        |            |              |        |
|     |     |     |     |     |      | [15] G.E.HintonandT.J.Sejnowski,“LearningandrelearninginBoltz- |                                 |                        |            |              |        |
|     |     |     |     |     | (33) | mann machines,”                                                | in Parallel                     | DistributedProcessing: |            | Explorations | in     |
theMicrostructureofCognition,D.E.RumelhartandJ.L.McClelland,
Pearlalsointroducesascalefactorin(32)and(33)sothatthe Eds. Cambridge,MA:MITPress,1986,pp.282–317.
resulting messages properly represent probability mass func- [16] V. Isham, “An introduction to spatial point processes and Markov
tions. Therelativecomplexityof(31)–(33)compared withthe randomfields,”Int.Stat.Rev.,vol.49,pp.21–43,1981.
|     |     |     |     |     |     | [17] F. V. Jensen, | An Introduction | to Bayesian | Networks. |     | New York: |
| --- | --- | --- | --- | --- | --- | ------------------ | --------------- | ----------- | --------- | --- | --------- |
simplicity of the sum-product update rule given in Section II Springer-Verlag,1996.
providesastrongpedagogicalincentivefortheintroductionof [18] R.KindermannandJ.L.Snell,MarkovRandomFieldsandTheirAp-
|     |     |     |     |     |     | plications. | Providence,RI:Amer.Math.Soc.,1980. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ---------------------------------- | --- | --- | --- | --- |
factorgraphs.
|     |     |     |     |     |     | [19] F.R.KschischangandB.J.Frey,“Iterativedecodingofcompoundcodes |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
byprobabilitypropagationingraphicalmodels,”IEEEJ.Select.Areas
Commun.,vol.16,pp.219–230,Feb.1998.
|     |     |     |     |     |     | [20] S.L.LauritzenandD.J.Spiegelhalter,“Localcomputationswithprob- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- |
ACKNOWLEDGMENT
abilitiesongraphicalstructuresandtheirapplicationtoexpertsystems,”
J.Roy.Statist.Soc.,ser.B,vol.50,pp.157–224,1988.
| The concept | of factor | graphs as | a generalization | of  | Tanner |                                                          |     |     |     |     |     |
| ----------- | --------- | --------- | ---------------- | --- | ------ | -------------------------------------------------------- | --- | --- | --- | --- | --- |
|             |           |           |                  |     |        | [21] D.J.C.MacKayandR.M.Neal,“Goodcodesbasedonverysparse |     |     |     |     |     |
graphs was devised by a group at ISIT ’97 in Ulm, Germany, matrices,”inCryptographyandCoding.5thIMAConference(Lecture
|     |     |     |     |     |     | NotesinComputerScience),C.Boyd,Ed. |     |     | Berlin,Germany:Springer, |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | ------------------------ | --- | --- |
thatincludedtheauthors,G.D.Forney,Jr.,R.Kötter,D.J.C.
1995,vol.1025,pp.100–111.
MacKay,R.J.McEliece,R.M.Tanner,andN.Wiberg.Theau-
|     |     |     |     |     |     | [22] D.J.C.MacKay,“Gooderror-correctingcodesbasedonverysparse |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- |
thorsbenefittedgreatlyfromthemanydiscussionsonthistopic matrices,”IEEETrans.Inform.Theory,vol.45,pp.399–431,Mar.1999.
|                 |              |      |          |               |      | [23] P. S. Maybeck, | Stochastic | Models, Estimation, |     | and Control. | New |
| --------------- | ------------ | ---- | -------- | ------------- | ---- | ------------------- | ---------- | ------------------- | --- | ------------ | --- |
| that took place | in Ulm. They | wish | to thank | G. D. Forney, | Jr., |                     |            |                     |     |              |     |
York:Academic,1979.
andtherefereesformanyhelpfulcommentsonearlierversions
|     |     |     |     |     |     | [24] R.J.McEliece,D.J.C.MacKay,andJ.-F.Cheng,“Turbodecodingas |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- |
ofthis paper. aninstanceofPearl’s‘beliefpropagation’algorithm,”IEEEJ.Select.
AreasCommun.,vol.16,pp.140–152,Feb.1998.
| The work   | of F. R. Kschischang       |     | took place | in part       | while on |                                                                |     |     |     |     |     |
| ---------- | -------------------------- | --- | ---------- | ------------- | -------- | -------------------------------------------------------------- | --- | --- | --- | --- | --- |
|            |                            |     |            |               |          | [25] J.Pearl,ProbabilisticReasoninginIntelligentSystems,2nded. |     |     |     |     | San |
| sabbatical | leave at the Massachusetts |     | Institute  | of Technology |          |                                                                |     |     |     |     |     |
Francisco,CA:Kaufmann,1988.
(MIT).Hegratefullyacknowledgesthesupportandhospitality [26] C.J.Preston,GibbsStatesonCountableSets. Cambridge,U.K.:Cam-
of Prof. G. W. Wornell of MIT. H.-A. Loeliger performed his bridgeUniv.Press,1974.
|     |     |     |     |     |     | [27] L.Rabiner,“AtutorialonhiddenMarkovmodelsandselectedappli- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- |
work while with Endora Tech AG, Basel, Switzerland. He cationsinspeechrecognition,”Proc.EEE,vol.77,pp.257–286,Feb.
| wishestoacknowledgethesupportofF.Tarköy. |     |     |     |     |     | 1989.                                                       |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                          |     |     |     |     |     | [28] K.H.Rosen,DiscreteMathematicsanditsApplications,4thed. |     |     |     |     | New |
York:WCB/McGraw-Hill,1999.
|     |     |     |     |     |     | [29] R.M.Tanner,“Arecursiveapproachtolowcomplexitycodes,”IEEE |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- |
REFERENCES Trans.Inform.Theory,vol.IT-27,pp.533–547,Sept.1981.
|     |     |     |     |     |     | [30] A.Vardy,“Trellisstructureofcodes,”inHandbookofCodingTheory, |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- |
[1] S.M.AjiandR.J.McEliece,“Ageneralalgorithmfordistributinginfor- V.S.PlessandW.C.Huffman,Eds. Amsterdam,TheNetherlands:
| mationonagraph,”inProc.1997IEEEInt.Symp.InformationTheory, |     |     |     |     |     | Elsevier,1998,vol.2. |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
Ulm,Germany,July1997,p.6. [31] N.Wiberg,“Codesanddecodingongeneralgraphs,”Ph.D.dissertation,
[2] ,“Thegeneralizeddistributivelaw,”IEEETrans.Inform.Theory, LinköpingUniv.,Linköping,Sweden,1996.
vol.46,pp.325–343,Mar.2000. [32] N. Wiberg, H.-A. Loeliger, and R. Kötter, “Codes and iterative de-
[3] B.D.O.AndersonandJ.B.Moore,OptimalFiltering. Englewood codingongeneralgraphs,”Eur.Trans.Telecomm.,vol.6,pp.513–525,
| Cliffs,NJ:Prentice-Hall,1979. |     |     |     |     |     | Sept./Oct.1995. |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
[4] L.R.Bahl,J.Cocke,F.Jelinek,andJ.Raviv,“Optimaldecodingoflinear [33] J.C.Willems,“ModelsforDynamics,”inDynamicsReported,Volume
codesforminimizingsymbolerrorrate,”IEEETrans.Inform.Theory, 2,U.KirchgraberandH.O.Walther,Eds. NewYork:Wiley,1989,pp.
| vol.IT-20,pp.284–287,Mar.1974. |     |     |     |     |     | 171–269. |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on September 17,2025 at 10:45:16 UTC from IEEE Xplore.  Restrictions apply.