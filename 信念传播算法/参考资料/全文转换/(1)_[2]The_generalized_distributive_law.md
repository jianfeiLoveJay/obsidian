IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.46,NO.2,MARCH2000 325
|     |     |     | The | Generalized |     |        |     | Distributive        |         |      | Law |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | ------ | --- | ------------------- | ------- | ---- | --- | --- | --- | --- | --- |
|     |     |     |     | Srinivas    |     | M. Aji | and | Robert J. McEliece, | Fellow, | IEEE |     |     |     |     |     |
Abstract—In this semitutorial paper we discuss a general (We summarize (1.1) by saying that is obtained by
message passing algorithm, which we call the generalized dis- “marginalizing out” the variables and from the function
tributivelaw(GDL).TheGDLisasynthesisoftheworkofmany
|     |     |     |     |     |     |     |     |     |     | .Similarly, |     | isobtainedbymarginalizing |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------------------- | --- | --- | --- |
authorsintheinformationtheory,digitalcommunications,signal
|             |             |       |                |            |              |              |     | out , ,and                              | fromthesamefunction.)Howmanyarithmetic |     |     |     |                    |     |     |
| ----------- | ----------- | ----- | -------------- | ---------- | ------------ | ------------ | --- | --------------------------------------- | -------------------------------------- | --- | --- | --- | ------------------ | --- | --- |
| processing, | statistics, |       | and artificial |            | intelligence | communities. |     | It                                      |                                        |     |     |     |                    |     |     |
|             |             |       |                |            |              |              |     | operations(additionsandmultiplications) |                                        |     |     |     | arerequiredforthis |     |     |
| includes    | as special  | cases | the            | Baum–Welch |              | algorithm,   | the | fast                                    |                                        |     |     |     |                    |     |     |
Fourier transform (FFT) on any finite Abelian group, the Gal- task?Ifweproceedintheobviousway,wenoticethatforeach
lager–Tanner–Wiberg decoding algorithm, Viterbi’s algorithm, ofthe valuesof thereare termsinthesumdefining
theBCJRalgorithm,Pearl’s“beliefpropagation”algorithm,the
,eachtermrequiringoneadditionandonemultiplica-
Shafer–Shenoyprobabilitypropagationalgorithm,andtheturbo
tion,sothatthetotalnumberofarithmeticoperationsrequired
decodingalgorithm.Althoughthisalgorithmisguaranteedtogive
|     |     |     |     |     |     |     |     | for the computation |     | of  |     | is  | . Similarly, | computing |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | ------------ | --------- | --- |
exactanswersonlyincertaincases(the“junctiontree”condition),
unfortunately not including the cases of GTW with cycles or requires operations, so computing both and
turbo decoding, there is much experimental evidence, and a few usingthedirectmethodrequires operations.
theorems,suggestingthatitoftenworksapproximatelyevenwhen
Ontheotherhand,becauseofthedistributivelaw,thesumin
itisnotsupposedto.
(1.1)factors
| Index | Terms—Belief |     | propagation, |     | distributive | law, | graphical |     |     |     |     |     |     |     |     |
| ----- | ------------ | --- | ------------ | --- | ------------ | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
models,junctiontrees,turbocodes.
(1.3)
|     |     |     | I. INTRODUCTION |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
THEhumbledistributivelaw,initssimplestform,statesthat Using this fact, we can simplify the computation of .
|     |     |     |     |     |     |     |     | First we | compute | tables | of the | functions |     | and |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------ | ------ | --------- | --- | --- | --- |
.Theleftsideofthisequationinvolves
| three arithmetic |     | operations | (one | addition |     | and two | multiplica- | definedby |     |     |     |     |     |     |     |
| ---------------- | --- | ---------- | ---- | -------- | --- | ------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
tions),whereastherightsideneedsonlytwo.Thusthedistribu-
| tivelawgivesusa“fastalgorithm”forcomputing |              |     |                |      |                     |                  |       | .The |     |     |     |     |     |     |     |
| ------------------------------------------ | ------------ | --- | -------------- | ---- | ------------------- | ---------------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
| object of                                  | this paper   | is  | to demonstrate |      | that                | the distributive |       | law  |     |     |     |     |     |     |     |
| can be vastly                              | generalized, |     | and            | that | this generalization |                  | leads | to   |     |     |     |     |     |     |     |
(1.4)
alargefamilyoffastalgorithms,includingViterbi’salgorithm
andthefastFouriertransform(FFT).Togiveabetterideaofthe
potentialpowerofthedistributivelawandtointroducetheview- which requires atotal of additions.Then wecompute
pointweshalltakeinthispaper,weofferthefollowingexample. the valuesof usingtheformula(cf.(1.3))
| Example                    | 1.1: | Let |      |                            | and  |                    | be  | given          |     |                  |     |      |               |     | (1.5) |
| -------------------------- | ---- | --- | ---- | -------------------------- | ---- | ------------------ | --- | -------------- | --- | ---------------- | --- | ---- | ------------- | --- | ----- |
| real-valuedfunctions,where |      |     |      | , ,                        | ,and | arevariablestaking |     |                |     |                  |     |      |               |     |       |
| valuesinafiniteset         |      |     | with | elements.Supposewearegiven |      |                    |     |                |     |                  |     |      |               |     |       |
|                            |      |     |      |                            |      |                    |     | which requires |     | multiplications. |     | Thus | by exploiting | the | dis-  |
thetaskofcomputingtablesofthevaluesof and , tributivelaw,wecanreducethetotalnumberofoperationsre-
definedasfollows:
|     |     |     |     |     |     |     |     | quiredtocompute |     |     | from | to  |     | .Similarly,the |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ---- | --- | --- | -------------- | --- |
distributivelawtellsusthat(1.2)canbewrittenas
(1.1)
(1.2)
(1.6)
ManuscriptreceivedJuly8,1998;revisedSeptember23,1999.Thiswork
| was supported      | by  | NSF under | Grant              | NCR-9505975, |     | AFOSR     | under         | Grant              |     |            |     |                             |       |            |     |
| ------------------ | --- | --------- | ------------------ | ------------ | --- | --------- | ------------- | ------------------ | --- | ---------- | --- | --------------------------- | ----- | ---------- | --- |
|                    |     |           |                    |              |     |           |               | where              | is  | as defined | in  | (1.4). Thus                 | if we | precompute | a   |
| 5F49620-97-1-0313, |     | anda      | GrantfromQualcomm. |              |     | A portion | of McEliece’s |                    |     |            |     |                             |       |            |     |
|                    |     |           |                    |              |     |           |               | tableofthevaluesof |     |            | (   | operations),andthenuse(1.6) |       |            |     |
contributionwasperformedattheSonyCorporationinTokyo,Japan,whilehe
| was aholder | of aSony | SabbaticalChair.Preliminaryversions |     |     |     |     | of this | paper                           |     |     |     |     |     |               |     |
| ----------- | -------- | ----------------------------------- | --- | --- | --- | --- | ------- | ------------------------------- | --- | --- | --- | --- | --- | ------------- | --- |
|             |          |                                     |     |     |     |     |         | ( furtheroperations),weonlyneed |     |     |     |     |     | operations(as |     |
werepresentedattheIEEEInternationalSymposiumonInformationTheory,
|     |     |     |     |     |     |     |     | compared | to  | for the | direct | method) | to compute | the values |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- | ------ | ------- | ---------- | ---------- | --- |
Ulm,Germany,June1997,andatISCTA1997,AmblesideU.K.,July1997.
|     |     |     |     |     |     |     |     | of . |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
TheauthorsarewiththeDepartmentofElectricalEngineering,California
InstituteofTechnology,Pasadena,CA91125USA(e-mail:{mas;rjm}@sys- Finally,weobservethattocomputeboth and
tems.caltech.edu).
|     |     |     |     |     |     |     |     | using the | simplifications |     | afforded | by  | (1.3) and | (1.6), we | only |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | --- | -------- | --- | --------- | --------- | ---- |
CommunicatedbyF.R.Kschischang,AssociateEditorforCodingTheory.
PublisherItemIdentifierS0018-9448(00)01679-5. needtocompute once,whichmeansthatwecancompute
0018–9448/00$10.00©2000IEEE
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

326 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.46,NO.2,MARCH2000
thevaluesof and withatotalofonly somerecenttheoreticalworkonGDL-likealgorithmsongraphs
operations,ascomparedto forthedirectmethod. withasinglecycle.
Although this paper is semitutorial, it contains a number of
The simplification in Example 1.1 was easy to accomplish,
things which have not appeared previously. Beside the gener-
and the gains were relatively modest. In more complicated
alityofourexposition,theseinclude:
cases, it can be much harderto see the best way to reorganize
• A de-emphasis of a priori graphical models, and an em-
thecalculations,butthecomputationalsavingscanbedramatic.
phasis on algorithms to construct graphical models to fit
Itis the objectofthis papertoshowthatproblemsofthe type
thegivenproblem.
described in Example 1.1 have a wide range of applicability,
• Anumberofnonprobabilisticapplications,includingthe
and to describea general procedure,which we called the gen-
FFT.
eralized distributive law (GDL), for solving them efficiently.
• A carefuldiscussion of message scheduling,and a proof
Roughly speaking, the GDL accomplishes its goal by passing
ofthecorrectnessofalargeclassofpossibleschedules.
messages in a communications network whose underlying
• Aprecisemeasureofthecomputationalcomplexityofthe
graphisatree.
GDL.
Important special cases of the GDL have appeared many
times previously. In this paper, for example, we will demon- Finally, we note that while this paper was being written,
stratethattheGDLincludesasspecialcasesthefastHadamard Kschischang, Frey, and Loeliger [41] were simultaneously
transform, Viterbi’s algorithm, the BCJR algorithm, the andindependently working outa similarsynthesis.And while
Gallager–Tanner–Wibergdecodingalgorithm(whentheunder- the final forms of the two papers have turned out to be quite
lyinggraphiscycle-free),andcertain“probabilitypropagation” different, anyone interested in the results of this paper should
algorithms known in the artificial intelligence community. havealookatthealternativeformulationin[41].
With alittle morework, wecouldhaveaddedthe FFTonany
finite Abelian group, the Baum–Welch “forward-backward” II. THEMPFPROBLEM
algorithm, and discrete-state Kalman filtering. Although this
The GDL can greatly reduce the number of additions and
paper contains relatively little that is essentially new (for
multiplications required in a certain class of computational
example, the 1990 paper of Shafer and Shenoy [33] describes
problems. It turns out that much of the power of the GDL is
an algorithm similar to the one we present in Section III), we
duetothefactthatitappliestosituationsinwhichthenotions
believe it is worthwhile to present a simply stated algorithm
ofadditionandmultiplicationarethemselvesgeneralized.The
of such wide applicability, which gives a unified treatment of
appropriateframeworkforthisgeneralizationisthecommuta-
a great manyalgorithms whose relationship to each other was
tivesemiring.
notfullyunderstood,ifsensedatall.
Hereisanoutlineofthepaper.InSectionII,wewillstatea Definition: Acommutativesemiringisaset ,togetherwith
generalcomputationalproblemwecalltheMPF(“marginalize twobinaryoperationscalled“ ”and“”,whichsatisfythefol-
a product function”) problem, and show by example that lowingthreeaxioms:
a number of classical problems are instances of it. These S1. Theoperation“ ”isassociativeandcommutative,and
problemsincludecomputingthediscreteHadamardtransform, thereisanadditiveidentityelementcalled“ ”suchthat
maximum-likelihood decoding of a linear code over a memo- forall .(Thisaxiommakes
ryless channel, probabilistic inference in Bayesian networks, acommutativemonoid.)
a “probabilistic state machine” problem, and matrix chain S2. Theoperation“”isalsoassociativeandcommutative,
multiplication.InSectionIII,weshallgiveanexactalgorithm andthereisamultiplicativeidentityelementcalled“ ”
for solving the MPF problem (the GDL) which often gives suchthat forall .(Thus isalso
acommutativemonoid.)
an efficient solution to the MPF problem. In Section IV we
S3. Thedistributivelawholds,i.e.,
will discuss the problem of finding junction trees (the formal
name for the GDL’s communication network), and “solve”
the example instances of the MPF problem given in Section
II, thereby deriving, among other things, the fast Hadamard
foralltriples from .
transformandViterbi’salgorithm.InSectionVwewilldiscuss
the computational complexity of the GDL. (A proof of the The difference between a semiring and a ring is that in a
correctnessoftheGDLisgivenintheAppendix.) semiring, additive inverses need not exist, i.e., is only
In Section VI, we give a brief history of the GDL. Finally, requiredtobeamonoid,notagroup.Thuseverycommutative
in Section VII, we speculate on the possible existence of an ringisautomaticallyacommutativesemiring.Forexample,the
efficientclassofapproximate,iterative,algorithmsforsolving setofrealorcomplexnumbers,withordinaryadditionandmul-
theMPFproblem,obtainedbyallowingthecommunicationnet- tiplication,formsacommutativesemiring.Similarly,thesetof
worktohavecycles.Thisspeculationisbasedpartlyonthefact polynomials in one or more indeterminates over any commu-
that two experimentally successful decoding algorithms, viz., tative ring forms a commutative semiring. However, there are
theGTWalgorithmforlow-densityparity-checkcodes,andthe manyothercommutativesemirings,someofwhicharesumma-
turbo decoding algorithm, can be viewed as an application of rizedinTable I.(Insemirings4–8,theset isanintervalof
the GDLmethodologyonnetworks withcycles,andpartlyon realnumberswiththepossibleadditionof .)
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore. Restrictions apply.

| AJIANDMCELIECE:THEGENERALIZEDDISTRIBUTIVELAW |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 327 |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TABLE I -marginalizationoftheglobalkernel ,whichisthefunction
A
|     | SOME | COMMUTATIVE | SEMIRINGS. |     | HERE |     |     |     | ,definedby |     |     |     |     |     |     |
| --- | ---- | ----------- | ---------- | --- | ---- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
DENOTESANARBITRARYCOMMUTATIVERING,SISANARBITRARYFINITE
SET,AND(cid:3)DENOTESANARBITRARYDISTRIBUTIVELATTICE
(2.2)
|     |     |     |     |     |     |     |     | In(2.2),   | denotesthecomplementoftheset |     |              |     |     | relativetothe |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------------------- | --- | ------------ | --- | --- | ------------- | --- |
|     |     |     |     |     |     |     |     | “universe” |                              | .   | For example, |     | if  | , and         | if  |
,then
|              |          |     |             |          |     |          |     | Wewillcallthefunction  |     |               |                            | definedin(2.2)the          |      |             | thobjec-  |
| ------------ | -------- | --- | ----------- | -------- | --- | -------- | --- | ---------------------- | --- | ------------- | -------------------------- | -------------------------- | ---- | ----------- | --------- |
|              |          |     |             |          |     |          |     | tive function,         | or  | the objective | function                   |                            | at . | We note     | that the  |
|              |          |     |             |          |     |          |     | computation            | of  | the th        | objective                  | function                   | in   | the obvious | way       |
|              |          |     |             |          |     |          |     | requires               |     | additionsand  |                            |                            |      |             | multipli- |
|              |          |     |             |          |     |          |     | cations,foratotalof    |     |               |                            | arithmeticoperations,where |      |             |           |
|              |          |     |             |          |     |          |     | denotesthesizeoftheset |     |               | .Weshallseebelow(SectionV) |                            |      |             |           |
| For example, | consider |     | the min-sum | semiring |     | in Table | I   |                        |     |               |                            |                            |      |             |           |
thatthealgorithmwecallthe“generalizeddistributivelaw”can
(entry 7). Here is the set of real numbers, plus the special oftenreducethisfiguredramatically.
| symbol“ | .”Theoperation“ |     | ”isdefinedastheoperationof |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Weconcludethissectionwithsomeillustrativeexamplesof
| takingtheminimum,withthesymbol |     |     |     | playingtheroleofthe |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theMPFproblem.
correspondingidentityelement,i.e.,wedefine
for all . The operation “” is defined to be ordinary Example 2.1: Let , , , and be variables taking
|          |             |          |        |     |         |          |     | values in | the | finite sets | ,   | ,   | , and | .   | Suppose |
| -------- | ----------- | -------- | ------ | --- | ------- | -------- | --- | --------- | --- | ----------- | --- | --- | ----- | --- | ------- |
| addition | [sic], with | the real | number |     | playing | the role | of  |           |     |             |     |     |       |     |         |
the identity, and for all . Oddly enough, this and aregivenfunctionsofthesevari-
combination forms a semiring, because the distributive law is ables, and that it is desired to compute tables of the functions
|     |     |     |     |     |     |     |     |     | and | definedby |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
equivalentto
| which is   | easily seen | to be    | true. We    | shall | get a glimpse |      | of the |     |     |     |     |     |     |     |     |
| ---------- | ----------- | -------- | ----------- | ----- | ------------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| importance | of this     | semiring | in Examples |       | 2.3 and       | 4.3, | below. |     |     |     |     |     |     |     |     |
(Infact,semirings5–8areallisomorphictoeachother;forex-
|                              |     |     |     |     |              |     |     | ptThis is | an instance | of  | the MPF | problem, | if  | we define | local |
| ---------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --------- | ----------- | --- | ------- | -------- | --- | --------- | ----- |
| ample,5becomes6viathemapping |     |     |     |     | ,and6becomes |     |     |           |             |     |         |          |     |           |       |
domainsandkernelsasfollows:
| 7underthemapping |     |     |     | .)  |     |     |     |     |     |             |     |             |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | --- | --- | --- |
|                  |     |     |     |     |     |     |     |     |     | localdomain |     | localkernel |     |     |     |
Havingbrieflydiscussedcommutativesemirings,wenowde-
| scribe the | “marginalize  | a       | product      | function” | problem, | which  | is     |     |     |     |     |     |     |     |     |
| ---------- | ------------- | ------- | ------------ | --------- | -------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| a general  | computational | problem |              | solved    | by the   | GDL.   | At the |     |     |     |     |     |     |     |     |
| end of the | section       | we will | give several | examples  |          | of the | MPF    |     |     |     |     |     |     |     |     |
problem,whichdemonstratehowitcanoccurinasurprisingly
widevarietyofsettings. Thedesiredfunction istheobjectivefunctionatlocal
Let be variables taking values in the finite domain , and is the objective function at local domain
sets , with for . If . This is just a slightly altered version of Example 1.1, and
is a subset of , we denote the we shall see in Section IV that when the GDL is applied, the
| product |     | by  | ,thevariablelist |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
“algorithm”ofExample1.1results.
| by ,andthecardinalityof |                                         |        | ,i.e., |             | ,by        | .Wedenote  |      |                     |          |               |              |            |       |                  |           |
| ----------------------- | --------------------------------------- | ------ | ------ | ----------- | ---------- | ---------- | ---- | ------------------- | -------- | ------------- | ------------ | ---------- | ----- | ---------------- | --------- |
|                         |                                         |        |        |             |            |            |      | Example             | 2.2:     | Let           | , ,          | , ,        | , and | be               | six vari- |
| the product             |                                         | simply | by     | , and       | the        | variable   | list |                     |          |               |              |            |       |                  |           |
|                         |                                         |        |        |             |            |            |      | ables, each         | assuming | values        | in           | the binary | set   |                  | , and let |
|                         | simplyby                                |        | .      |             |            |            |      |                     |          |               |              |            |       |                  |           |
|                         |                                         |        |        |             |            |            |      |                     | be       | a real-valued |              | function   | of    | the variables    | ,         |
| Now let                 |                                         |        | be     | subsets     | of         |            | .    |                     |          |               |              |            |       |                  |           |
|                         |                                         |        |        |             |            |            |      | , and               | . Now    | consider      | the MPF      | problem    |       | (the commutative |           |
| Suppose                 | that for each                           |        |        |             | , there is | a function |      |                     |          |               |              |            |       |                  |           |
|                         |                                         |        |        |             |            |            |      | semiring            | being    | the set of    | real numbers |            | with  | ordinary         | addition  |
|                         | , where                                 |        | is a   | commutative | semiring.  |            | The  |                     |          |               |              |            |       |                  |           |
|                         |                                         |        |        |             |            |            |      | and multiplication) |          | with          | the          | following  | local | domains          | and       |
| variablelists           | arecalledthelocaldomainsandthefunctions |        |        |             |            |            |      |                     |          |               |              |            |       |                  |           |
kernels:
| are called | the local | kernels. | We  | define | the global |     | kernel |     |     |     |     |     |     |     |     |
| ---------- | --------- | -------- | --- | ------ | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
asfollows:
|     |     |     |     |     |     |     |     |     |     | localdomain |     | localkernel |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | --- | --- | --- |
(2.1)
Withthissetup,theMPFproblemisthis:Foroneormoreof
| theindices |     | ,computeatableofthevaluesofthe |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

328 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.46,NO.2,MARCH2000
Heretheglobalkernel,i.e.,theproductofthelocalkernels,is
| andtheobjectivefunctionatthelocaldomain |              |                |              |           |              |          | is       |     |     |     |     |     |     |
| --------------------------------------- | ------------ | -------------- | ------------ | --------- | ------------ | -------- | -------- | --- | --- | --- | --- | --- | --- |
| which is                                | the          | Hadamard       | transform    | of        | the original |          | function |     |     |     |     |     |     |
|                                         | [17].        | Thus           | the problem  |           | of computing | the      | Hada-    |     |     |     |     |     |     |
| mard transform                          |              | is a           | special case | of        | the MPF      | problem. | (A       |     |     |     |     |     |     |
| straightforward                         |              | generalization | of           | this      | example      | shows    | that the |     |     |     |     |     |     |
| problem                                 | of computing |                | the Fourier  | transform |              | over any | finite   |     |     |     |     |     |     |
AbeliangroupisalsoaspecialcaseoftheMPFproblem.While
| the kernel | for the                                     | Hadamard | transform |       | is of diagonal |     | form,   | in                                     |     |     |     |     |     |
| ---------- | ------------------------------------------- | -------- | --------- | ----- | -------------- | --- | ------- | -------------------------------------- | --- | --- | --- | --- | --- |
| general,   | the kernel                                  | will     | only be   | lower | triangular.    | See | [1, Ch. |                                        |     |     |     |     |     |
| 3]forthe   | details.)WeshallseebelowinExample4.2thatthe |          |           |       |                |     |         |                                        |     |     |     |     |     |
|            |                                             |          |           |       |                |     |         | Fig.1. TheBayesiannetworkinExample2.4. |     |     |     |     |     |
GDLalgorithm,whenappliedtothissetoflocaldomainsand
kernels,yieldsthefastHadamardtransform.
Theglobalkernelisthen
| Example | 2.3: | (Wiberg | [39]). | Consider | the |     | binary |     |     |     |     |     |     |
| ------- | ---- | ------- | ------ | -------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
linearcodedefinedbytheparity-checkmatrix
if
isacodeword
if
| Supposethatanunknowncodeword |     |     |     |     |     |     | fromthis |     |     |     | isnotacodeword. |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --------------- | --- | --- |
codeistransmittedoveradiscretememorylesschannel,andthat
|                    |     |     |              |     |        |              |     | Thustheobjectivefunctionatthelocaldomain |     |     |     | is  |     |
| ------------------ | --- | --- | ------------ | --- | ------ | ------------ | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
| the vector         |     |     | is received. |     | The    | “likelihood” | of  | a                                        |     |     |     |     |     |
| particularcodeword |     |     |              |     | isthen |              |     |                                          |     |     |     |     |     |
allcodewordsforwhich
(2.3)
|           |     |                    |         |            |               |         |         | It follows    | that the value                        | of for    | which | is smallest | is  |
| --------- | --- | ------------------ | ------- | ---------- | ------------- | ------- | ------- | ------------- | ------------------------------------- | --------- | ----- | ----------- | --- |
|           |     |                    |         |            |               |         |         | thevalueofthe | thcomponentofamaximum-likelihoodcode- |           |       |             |     |
| where the |     | ’s                 | are the | transition | probabilities |         | of the  |               |                                       |           |       |             |     |
|           |     |                    |         |            |               |         |         | word, i.e.,   | a codeword                            | for which |       |             | is  |
| channel.  | The | maximum-likelihood |         | decoding   |               | problem | is that |               |                                       |           |       |             |     |
largest.Astraightforwardextensionofthisexampleshowsthat
| of finding | the      | codeword | that    | maximizes | the  | expression    |     | in          |                       |     |          |       |           |
| ---------- | -------- | -------- | ------- | --------- | ---- | ------------- | --- | ----------- | --------------------- | --- | -------- | ----- | --------- |
|            |          |          |         |           |      |               |     | the problem | of maximum-likelihood |     | decoding | of an | arbitrary |
| (2.3). Now | consider |          | the MPF | problem   | with | the following |     |             |                       |     |          |       |           |
linearblockcodeisaspecialcaseoftheMPFproblem.Weshall
domains and kernels, using the min-sum semiring (semiring seeinExample4.3thatwhenthe GDLis appliedtoproblems
| from Table | I). | There | is one local | domain | for | each codeword |     |               |                            |     |          |           |     |
| ---------- | --- | ----- | ------------ | ------ | --- | ------------- | --- | ------------- | -------------------------- | --- | -------- | --------- | --- |
|            |     |       |              |        |     |               |     | of this type, | the Gallager–Tanner–Wiberg |     | decoding | algorithm |     |
coordinateandoneforeachrowoftheparity-checkmatrix.
results.
localdomain localkernel Example2.4: Considerthedirectedacylicgraph(DAG) in
|     |     |     |     |     |     |     |     | Fig.1.1InaDAG,the“parents”ofavertex            |     |      | ,denoted         |     | ,are    |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | ---- | ---------------- | --- | ------- |
|     |     | .   | .   |     |     |     |     | thosevertices(ifany)whichlieimmediately“above” |     |      |                  |     | .Thusin |
|     |     | .   | .   |     |     |     |     |                                                |     |      |                  |     |         |
|     |     | .   | .   |     |     |     |     |                                                |     |      |                  |     |         |
|     |     |     |     |     |     |     |     | Fig.1,                                         |     | ,and | .Letusassociatea |     |         |
randomvariablewitheachofthevertices,andassumethateach
randomvariableisdependentonlyonits“parents,”i.e.,thejoint
densityfunctionfactorsasfollows:
| Here     | is a function |       | that indicates |          | whether   | a given | parity |     |     |     |     |     |     |
| -------- | ------------- | ----- | -------------- | -------- | --------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
| check is | satisfied,    | or    | not. For       | example, | at the    | local   | domain |     |     |     |     |     |     |
|          | ,             | which | corresponds    | to       | the first | row     | of the |     |     |     |     |     |     |
parity-checkmatrix,wehave
|     |     |     |     |     |     |     |     | 1Thisexampleistakenfrom[29],inwhichBstandsforburglary,E |     |     |     |     | isfor |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | ----- |
if
|     |     |     |     |     |     |     |     | earthquake,Aisforalarmsound,Risforradioreport,andW |     |     |     | isforWatson’s |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | ------------- | --- |
|     |     |     |     | if  |     |     |     | call.                                              |     |     |     |               |     |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

| AJIANDMCELIECE:THEGENERALIZEDDISTRIBUTIVELAW |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 329 |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.2. TheBayesiannetworkfortheprobabilisticstatemachineinExample2.5.
or,usingstreamlinednotation wheretheconstantofproportionality isgivenby
(2.4)
ADAG,togetherwithassociatedrandomvariableswhosejoint
densityfunctionfactorsaccordingtothestructureoftheDAG,
iscalledaBayesiannetwork[18]. Similarly, the computation of the conditional probabilities of
| Let us | assume | that the | two random | variables |     | and | are |     |        |              |     |            |     |               |     |
| ------ | ------ | -------- | ---------- | --------- | --- | --- | --- | --- | ------ | ------------ | --- | ---------- | --- | ------------- | --- |
|        |        |          |            |           |     |     |     | and | can be | accomplished | via | evaluation | of  | the objective |     |
observedtohavethevalues and ,respectively.Theprob- functions at the local domains and , respectively. Thus the
abilisticinferenceproblem,inthiscase,istocomputethecon- problem of probabilistic inference in Bayesian networks is a
| ditional | probabilities | of  | one or more | of  | the remaining | random |     |              |     |         |          |          |     |            |     |
| -------- | ------------- | --- | ----------- | --- | ------------- | ------ | --- | ------------ | --- | ------- | -------- | -------- | --- | ---------- | --- |
|          |               |     |             |     |               |        |     | special case | of  | the MPF | problem. | We shall | see | in Section | IV  |
variables,i.e., , ,and ,wheretheconditioningiswithre- thatwhentheGDLisappliedtoproblemsofthistype,there-
| specttothe“evidence” |     |     |     |     | .Nowconsiderthe |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sultisanalgorithmequivalenttothe“probabilitypropagation”
MPFproblemwiththefollowinglocaldomainsandkernels: algorithmsknownintheartificialintelligencecommunity.
|     |     |             |     |             |     |     |     | Example2.5: |     | Asamoreusefulinstanceoftheprobabilistic |     |     |     |     |     |
| --- | --- | ----------- | --- | ----------- | --- | --- | --- | ----------- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
|     |     | localdomain |     | localkernel |     |     |     |             |     |                                         |     |     |     |     |     |
inferenceproblem,weconsideraprobabilisticstatemachine.2
|             |              |          |      |            |          |          |        | Ateachtime                          |                             |                                     |                       | ,thePSMhasstate    |               |         | ,input |
| ----------- | ------------ | -------- | ---- | ---------- | -------- | -------- | ------ | ----------------------------------- | --------------------------- | ----------------------------------- | --------------------- | ------------------ | ------------- | ------- | ------ |
|             |              |          |      |            |          |          |        | and output                          |                             | . The                               | are probabilistically |                    | generated,    |         | inde-  |
|             |              |          |      |            |          |          |        | pendently,                          | with                        | probabilities                       |                       | . The output       |               | depends | on     |
|             |              |          |      |            |          |          |        | thestate                            | andinput                    | andisdescribedbytheconditionalprob- |                       |                    |               |         |        |
|             |              |          |      |            |          |          |        | abilitydistribution                 |                             |                                     | .Thestate             |                    | alsodependson |         |        |
|             |              |          |      |            |          |          |        | and                                 | ,withconditionalprobability |                                     |                       |                    |               | .Ifthea |        |
| Then by     | (2.4) (using | semiring |      | from Table | I,       | viz. the | set of |                                     |                             |                                     |                       |                    |               |         |        |
|             |              |          |      |            |          |          |        | prioridistributionoftheinitialstate |                             |                                     |                       | isknown,wecanwrite |               |         |        |
| nonnegative | real         | numbers  | with | ordinary   | addition | and      | mul-   |                                     |                             |                                     |                       |                    |               |         |        |
thejointprobabilityoftheinputs,states,andoutputsfromtime
| tiplication)  | the global |           | kernel          |     | is just           | the function |     | to  | as  |     |     |     |     |     |     |
| ------------- | ---------- | --------- | --------------- | --- | ----------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|               |            | ,so that, | for example,the |     | objectivefunction |              |     |     |     |     |     |     |     |     |     |
| atlocaldomain |            | is        |                 |     |                   |              |     |     |     |     |     |     |     |     |     |
(2.5)
ButbyBayes’rule
ThismeansthatthePSMisaBayesiannetwork,asdepictedin
Fig. 2.
|             |             |     |             |     |         |                |     | Suppose            | we         | observe   | the output | values,         | denoting       |             | these |
| ----------- | ----------- | --- | ----------- | --- | ------- | -------------- | --- | ------------------ | ---------- | --------- | ---------- | --------------- | -------------- | ----------- | ----- |
|             |             |     |             |     |         |                |     | observations       | by         |           | (“         | ” for           | evidence),     | and         | wish  |
|             |             |     |             |     |         |                |     | to infer           | the values | of the    | inputs     | based on        | this evidence. |             | This  |
| so that the | conditional |     | probability | of  | , given | the “evidence” |     |                    |            |           |            |                 |                |             |       |
|             |             |     |             |     |         |                |     | is a probabilistic |            | inference | problem    | of the          | type           | discussed   | in    |
|             | , is        |     |             |     |         |                |     |                    |            |           |            |                 |                |             |       |
|             |             |     |             |     |         |                |     | Example            | 2.4.       | We can    | compute    | the conditional |                | probability |       |
2Ourprobabilisticstatemachinesarecloselyrelatedtothe“hiddenMarkov
models”consideredintheliterature[32].
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

330 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.46,NO.2,MARCH2000
|                 |                 | by            | taking | the joint         | probability |             | in     |                                                              |     |     |     |     |
| --------------- | --------------- | ------------- | ------ | ----------------- | ----------- | ----------- | ------ | ------------------------------------------------------------ | --- | --- | --- | --- |
| (2.5) with      | the observed    | values        | of     | and marginalizing |             | out         | all    |                                                              |     |     |     |     |
| the ’s          | and all but one | of the        | ’s.    | This is           | an instance | of          | the    |                                                              |     |     |     |     |
| MPF problem,    | with            | the following | local  | domains           |             | and kernels |        |                                                              |     |     |     |     |
| (illustratedfor |                 | ):            |        |                   |             |             |        |                                                              |     |     |     |     |
|                 | localdomain     |               |        | localkernel       |             |             |        |                                                              |     |     |     |     |
|                 |                 |               |        |                   |             |             | Fig.3. | Thetrelliscorrespondingtothemultiplicationofthreematrices,of |     |     |     |     |
sizes2(cid:2)3,3(cid:2)3,and3(cid:2)2.The(i;j)thentryinthematrixproductisthe
|     |     |     |     |     |     |     | sumoftheweightsofallpathsfroma |     |                                          | tob | .   |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | ---------------------------------------- | --- | --- | --- |
|     |     |     |     |     |     |     | multiplying                    |     | matricescanbeformulatedasthefollowingMPF |     |     |     |
problem:
|           |                 |       |            |                   |               |       |     |     | localdomain |     | localkernel |     |
| --------- | --------------- | ----- | ---------- | ----------------- | ------------- | ----- | --- | --- | ----------- | --- | ----------- | --- |
| This      | model includes, | as    | a special  | case,             | convolutional |       |     |     |             |     |             |     |
| codes, as | follows. The    | state | transition | is deterministic, |               | which |     |     |             |     |             |     |
.
.
| means that |            |                      | when |          |           |            |     |     |     | .   |     |     |
| ---------- | ---------- | -------------------- | ---- | -------- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
| and        |            | otherwise.           |      | Assuming | a         | memoryless |     |     |     |     |     |     |
| channel,   | the output | is probabilistically |      |          | dependent | on         | ,   |     |     |     |     |     |
whichisadeterministicfunctionofthestateandinput,andso
|           |                 |             | . Marginalizing |                 | the | product | of  |         |              |               |             |              |
| --------- | --------------- | ----------- | --------------- | --------------- | --- | ------- | --- | ------- | ------------ | ------------- | ----------- | ------------ |
|           |                 |             |                 |                 |     |         | the | desired | result being | the objective | function at | local domain |
| functions | in (2.5) in the | sum-product |                 | and max-product |     | semir-  |     | .       |              |               |             |              |
ingswillthengiveusthemaximum-likelihoodinputsymbolsor Asanalternativeinterpretationof(2.7),consideratrellisof
inputblock,respectively.Asweshallseebelow(Example4.5), depth ,withvertexset ,andanedgeofweight
whentheGDLisappliedhere,wegetalgorithmsequivalentto connectingthevertices and .
theBCJRandViterbidecodingalgorithms.3 Ifwe definethe weightofa path as the sum ofthe weights of
|                          |          |      |     |                 |      |         | the        | component | edges,    | then               | as defined | in (2.7) rep- |
| ------------------------ | -------- | ---- | --- | --------------- | ---- | ------- | ---------- | --------- | --------- | ------------------ | ---------- | ------------- |
| Example                  | 2.6: Let | be a |     | matrix          | with | entries | in         |           |           |                    |            |               |
|                          |          |      |     |                 |      |         | resentsthe |           | sum ofthe | weights ofallpaths | from       | to . For      |
| acommutativesemiring,for |          |      |     | .Wedenotetheen- |      |         |            |           |           |                    |            |               |
example,Fig.3showsthetrelliscorrespondingtothemultipli-
| triesin                    | by  | ,wherefor |      |                    |     | ,   | isa                           |     |     |     |        |        |
| -------------------------- | --- | --------- | ---- | ------------------ | --- | --- | ----------------------------- | --- | --- | --- | ------ | ------ |
|                            |     |           |      |                    |     |     | cationofthreematrices,ofsizes |     |     |     | , ,and | .Ifthe |
| variabletakingvaluesinaset |     |           | with | elements.Supposewe |     |     |                               |     |     |     |        |        |
computationisdoneinthemin-sumsemiring,theinterpretation
wanttocomputetheproduct
|     |     |     |     |     |     |     | isthat |                             | istheweightofaminimum-weightpathfrom |     |          |              |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------------------------- | ------------------------------------ | --- | -------- | ------------ |
|     |     |     |     |     |     |     |        | to                          | .                                    |     |          |              |
|     |     |     |     |     |     |     |        | WeshallseeinSectionIVthatif |                                      |     | theGDLis | appliedtothe |
matrixmultiplicationproblem,anumberofdifferentalgorithms
result,correspondingtothedifferentwaysofparenthesizingthe
| Thenfor | wehavebydefinition |     |     |     |     |     |            |     |     |                          |     |     |
| ------- | ------------------ | --- | --- | --- | --- | --- | ---------- | --- | --- | ------------------------ | --- | --- |
|         |                    |     |     |     |     |     | expression |     |     | .Iftheparenthesizationis |     |     |
(2.6)
|     |     |     |     |     |     |     | (illustratedfor |     |     | ),andthecomputationisinthemin-sum |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --------------------------------- | --- | --- |
andaneasyinductionargumentgivesthegeneralization
semiring,Viterbi’salgorithmresults.
|     |     |     |     |     |     |     |     | III. THEGDL:ANALGORITHM |     |     | FORSOLVINGTHEMPF |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ---------------- | --- |
PROBLEM
(2.7)
(Note that (2.7) suggests that the number of arithmetic opera- If the elements of stand in a certain special relationship
tionsrequiredtomultiplythese matricesis .)Thus to each other, then an algorithm for solving the MPF problem
canbebasedonthenotionof“messagepassing.”Therequired
3ToobtainanalgorithmequivalenttoViterbi’s,itisnecessarytotaketheneg-
|     |     |     |     |     |     |     | relationship |     | is that the | local domains | can be organized | into a |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | ------------- | ---------------- | ------ |
ativelogarithmof(2.5)beforeperformingthemarginalizationinthemin-sum
semiring. junction tree [18]. What this means is that the elements of
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

| AJIANDMCELIECE:THEGENERALIZEDDISTRIBUTIVELAW |     |     |     |     |     |     |     |     |     |     |     |     | 331 |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.4. Ajunctiontree.
canbeattachedaslabelstotheverticesofagraph-theoretictree
| ,suchthatforanytwovertices    |     |     |     | and                    | ,theintersectionof |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | ---------------------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| thecorrespondinglabels,viz.   |     |     |     | ,isasubsetofthelabelon |                    |     |     |     |     |     |     |     |     |
| eachvertexontheuniquepathfrom |     |     |     | to                     | .Alternatively,the |     |     |     |     |     |     |     |     |
subgraphof consistingofthoseverticeswhoselabelincludes Fig.5. Ajunctiontreewhichincludesthelocaldomainsfx ;x g,fx ;x g,
|                 |                                               |     |     |     |     |     | fx ;x g,andfx | ;x           | g.      |     |             |     |           |
| --------------- | --------------------------------------------- | --- | --- | --- | --- | --- | ------------- | ------------ | ------- | --- | ----------- | --- | --------- |
| theelement      | ,togetherwiththeedgesconnectingthesevertices, |     |     |     |     |     |               |              |         |     |             |     |           |
| isconnected,for |                                               |     | .   |     |     |     |               |              |         |     |             |     |           |
|                 |                                               |     |     |     |     |     | and when      | a particular | message |     | is updated, | the | following |
Forexample,considerthefollowingfivelocaldomains:
ruleis used:
localdomain
(3.1)
|     |     |     |     |     |     |     | A good             | way to remember |          | (3.1) is | to think | of the junction | tree |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --------------- | -------- | -------- | -------- | --------------- | ---- |
|     |     |     |     |     |     |     | as a communication |                 | network, | in which | an       | edge from       | to   |
isatransmissionlinethat“filtersout”dependenceonallvari-
| These local | domains | can | be organized | into | a junction | tree, as |                       |     |     |     |                        |     |     |
| ----------- | ------- | --- | ------------ | ---- | ---------- | -------- | --------------------- | --- | --- | --- | ---------------------- | --- | --- |
|             |         |     |              |      |            |          | ablesbutthosecommonto |     |     | and | .(Thefilteringisdoneby |     |     |
showninFig.4.Forexample,theuniquepathfromvertex to marginalization.)Whenthevertex wishestosendamessage
vertex is ,and ,asrequired. to ,itformstheproductofitslocalkernelwithallmessagesit
| On the | other hand, | the | following | set of | four local | domains |                                      |     |     |     |     |                  |     |
| ------ | ----------- | --- | --------- | ------ | ---------- | ------- | ------------------------------------ | --- | --- | --- | --- | ---------------- | --- |
|        |             |     |           |        |            |         | hasreceivedfromitsneighborsotherthan |     |     |     |     | ,andtransmitsthe |     |
cannotbeorganized intoajunctiontree,ascanbeeasilyveri- productto overthe transmissionline.
fied.
|     |     |     |             |     |     |     | Similarly,                     | the | “state” of | a vertex | is defined | to          | be a table |
| --- | --- | --- | ----------- | --- | --- | --- | ------------------------------ | --- | ---------- | -------- | ---------- | ----------- | ---------- |
|     |     |     |             |     |     |     | containingthevaluesofafunction |     |            |          |            | .Initially, |            |
|     |     |     | localdomain |     |     |     | isdefinedtobethelocalkernel    |     |            |          | ,butwhen   |             | isupdated, |
thefollowingruleisused:
(3.2)
However,byadjoiningtwo“dummydomains”
|     |     |     |     |     |     |     | Inwords,thestateofavertex |     |     | istheproductofitslocalkernel |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | ---------------------------- | --- | --- | --- |
localdomain witheachofthemessagesithasreceivedfromitsneighbors.The
|     |     |     |     |     |     |     | basic idea | is that | after sufficiently           |     | many messages |     | have been  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ---------------------------- | --- | ------------- | --- | ---------- |
|     |     |     |     |     |     |     | passed,    |         | willbetheobjectivefunctionat |     |               |     | ,asdefined |
in (2.2).
|                    |     |        |        |            |       |          | The question                   |     | remains as | to the | scheduling            | of the | message |
| ------------------ | --- | ------ | ------ | ---------- | ----- | -------- | ------------------------------ | --- | ---------- | ------ | --------------------- | ------ | ------- |
| to the collection, |     | we can | devise | a junction | tree, | as shown | in                             |     |            |        |                       |        |         |
|                    |     |        |        |            |       |          | passingandthestatecomputation. |     |            |        | Hereweconsideronlytwo |        |         |
Fig. 5.
specialcases,thesingle-vertexproblem,inwhichthegoalisto
| (In Section | IV, | we give | a   | simple algorithm |     | for deciding |     |     |     |     |     |     |     |
| ----------- | --- | ------- | --- | ---------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
whether or not a given set of local domains can be organized compute the objective function at only one vertex , and the
all-verticesproblem,wherethegoalistocomputetheobjective
intoajunctiontree,forconstructingoneifitdoesexist,andfor
functionatallvertices.4
findingappropriatedummydomainsifitdoesnot.)
|                                    |              |       |              |       |              |             | For the  | single-vertex | problem, |              | the natural | (serial) | sched-     |
| ---------------------------------- | ------------ | ----- | ------------ | ----- | ------------ | ----------- | -------- | ------------- | -------- | ------------ | ----------- | -------- | ---------- |
| In the “junction                   |              | tree” | algorithm,   | which | is what      | we call the |          |               |          |              |             |          |            |
|                                    |              |       |              |       |              |             | uling of | the GDL       | begins   | by directing | each        | edge     | toward the |
| generalizeddistributivelaw(GDL),if |              |       |              | and   | areconnected |             |          |               |          |              |             |          |            |
| by an edge                         | (indicatedby |       | the notation |       | ), the       | (directed)  |          |               |          |              |             |          |            |
4Wedonotconsidertheproblemofevaluatingtheobjectivefunctionatkver-
| “message” | from | to  | is a table | containing | the | values of | a   |     |     |     |     |     |     |
| --------- | ---- | --- | ---------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
tices,where1<k<M.However,aswewillseeinSectionV,thecomplexity
| function |     |     | .Initially,allsuchfunctionsarede- |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
oftheM-vertexGDLisatmostfourtimesaslargeasthe1-vertexGDL,soitis
finedtobeidentically (thesemiring’smultiplicativeidentity); reasonablyefficienttosolvethek-vertexproblemusingtheM-vertexsolution.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

332 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.46,NO.2,MARCH2000
|     |     |     |     |     |     |     |     |     |     |     | TABLE | III |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
A“HYBRID”SCHEDULEFORTHEALL-VERTICESGDLFORTHE
JUNCTIONTREEOFFig.4
ThejunctiontreeofFig.4withtheedgesdirectedtowardsv
| Fig.6. |     |     |       |     |     |     | .   |     |     |     |     |     |     |     |
| ------ | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|        |     |     | TABLE | II  |     |     |     |     |     |     |     |     |     |     |
ASCHEDULEFORTHESINGLE-VERTEXGDLFORTHEJUNCTIONTREEOF
Fig.4,WITHTARGETVERTEXv
|     |     |     |     |     |     |     |     | at most | equal to the | diameter | of  | the tree, | at which | point the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | -------- | --- | --------- | -------- | --------- |
statesoftheverticeswillbeequaltothedesiredobjectivefunc-
tions,andthealgorithmterminates.Alternatively,theGDLcan
bescheduledfullyserially,inwhichcaseeachmessageissent
onlyonce,andeachstateiscomputedonlyonce.Inthiscase,a
vertexsendsamessagetoaneighborwhen,forthefirsttime,it
target vertex . Then messages are sent only in the direc- hasreceivedmessagesfromallofitsotherneighbors,andcom-
tion toward , and each directed message is sent only once. putesitsstatewhen,forthefirsttime,ithasreceivedmessages
| A vertex | sends | a message | to  | a neighbor, | when, | for | the first |          |                |     |             |       |          |          |
| -------- | ----- | --------- | --- | ----------- | ----- | --- | --------- | -------- | -------------- | --- | ----------- | ----- | -------- | -------- |
|          |       |           |     |             |       |     |           | from all | its neighbors. | In  | this serial | mode, | messages | begin at |
time, it has received messages from each of its other neigh- theleaves,andproceedinwardsintothetree,untilsomenodes
| bors. The | target | computes |     | its state | when | it has | received |     |     |     |     |     |     |     |
| --------- | ------ | -------- | --- | --------- | ---- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
havereceivedmessagesfromalltheirneighbors,atwhichpoint
| messages | from | each of | its neighbors. |     | With | this scheduling, |     |     |     |     |     |     |     |     |
| -------- | ---- | ------- | -------------- | --- | ---- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
messagespropagateoutwards,sothateachvertexeventuallyre-
messages begin at the leaves (vertices with degree ), and ceivesmessagesfromallofitsneighbors.5WewillseeinSec-
| proceed | toward | , until | has | received | messages |     | from all |         |                |        |              |     |          |         |
| ------- | ------ | ------- | --- | -------- | -------- | --- | -------- | ------- | -------------- | ------ | ------------ | --- | -------- | ------- |
|         |        |         |     |          |          |     |          | tion IV | that the fully | serial | all-vertices | GDL | requires | at most |
its neighbors, at which point computes its state and the arithmeticoperations.
| algorithm | terminates. |     |     |     |     |     |     |       |            |         |             |        |            |        |
| --------- | ----------- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ------- | ----------- | ------ | ---------- | ------ |
|           |             |     |     |     |     |     |     | There | are also a | variety | of possible | hybrid | schedules, | inter- |
Forexample,ifwewishtosolvethesingle-vertexproblemfor
|     |     |     |     |     |     |     |     | mediate | between fully | parallel | and | fully | serial. For | example, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | -------- | --- | ----- | ----------- | -------- |
thejunctiontreeofFig.4,andthetargetvertexis ,theedges TableIIIshowsahybridscheduleforthejunctiontreeofFig.4,
| shouldallbedirectedtowards |     |     |     | ,asshowninFig.6.Thenone |     |     |     |          |                 |     |              |      |      |             |
| -------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | -------- | --------------- | --- | ------------ | ---- | ---- | ----------- |
|                            |     |     |     |                         |     |     |     | in which | the computation |     | is organized | into | four | rounds. The |
possible sequence ofmessages and state computations runs as computationsineachroundmaybeperformedinanyorder,or
| showninTable |     | II. |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
evensimultaneously,buttheroundsmustbeperformedsequen-
ItwillbeshowninSectionVthatthisschedulingofthesingle
tially.
vertexGDLrequiresatmost ThatconcludesourinformaldiscussionofGDLscheduling.
Weendthissectionwithwhatwecallthe“schedulingtheorem”
|       |     |           |                      |     |              |     |          | forthe GDL.                                     |                              |     |        |        |         |               |
| ----- | --- | --------- | -------------------- | --- | ------------ | --- | -------- | ----------------------------------------------- | ---------------------------- | --- | ------ | ------ | ------- | ------------- |
|       |     |           | arithmeticoperations |     |              |     | (3.3)    |                                                 |                              |     |        |        |         |               |
|       |     |           |                      |     |              |     |          | Thuslet                                         | beajunctiontreewithvertexset |     |        |        |         | andedgeset    |
|       |     |           |                      |     |              |     |          | . In the                                        | GDL, messages                |     | can be | passed | in both | directions on |
|       |     |           |                      |     |              |     |          | eachedge,soitwillbeconvenienttoregardtheedgeset |                              |     |        |        |         | as            |
| where | is  | the label | of , and             |     | , the degree | of  | , is the |                                                 |                              |     |        |        |         |               |
number of vertices adjacent to . This should be compared to consistingoforderedpairsofvertices.Thusforexampleforthe
treeofFig.4,wehave
| the complexity                       |              | of the “obvious” |     | solution,                | which            | as           | we noted   |     |     |     |     |     |     |     |
| ------------------------------------ | ------------ | ---------------- | --- | ------------------------ | ---------------- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
| above is                             |              | operations.      |     | For example,             |                  | for the      | junction   |     |     |     |     |     |     |     |
| tree showninFig.6,thecomplexityofthe |              |                  |     |                          | single-vertexGDL |              |            |     |     |     |     |     |     |     |
| isby(3.3)atmost                      |              |                  |     |                          |                  |              | arithmetic |     |     |     |     |     |     |     |
| operations,versus                    |              |                  |     | forthedirectcomputation. |                  |              |            |     |     |     |     |     |     |     |
| For the                              | all-vertices | problem,         |     | the GDL                  | can              | be scheduled |            | in  |     |     |     |     |     |     |
several ways. For example, in a fully parallel implementation, A schedule for the GDL is defined to be a finite sequence
|             |            |              |       |                 |     |         |          | of subsets | of . | A typical | schedule |     | will be | denoted by |
| ----------- | ---------- | ------------ | ----- | --------------- | --- | ------- | -------- | ---------- | ---- | --------- | -------- | --- | ------- | ---------- |
| at every    | iteration, | every        | state | is updated,     | and | every   | message  |            |      |           |          |     |         |            |
| is computed | and        | transmitted, |       | simultaneously. |     | In this | case the |            |      |           |          |     |         |            |
5Wemightthereforecallthefullyserialall-verticesGDLan“inward–out-
| messages | and | states will | stabilize | after | a number | of  | iterations |     |     |     |     |     |     |     |
| -------- | --- | ----------- | --------- | ----- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
ward”algorithm.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

| AJIANDMCELIECE:THEGENERALIZEDDISTRIBUTIVELAW |     |     |     |     |                                                                    |                        |     |                    | 333 |
| -------------------------------------------- | --- | --- | --- | --- | ------------------------------------------------------------------ | ---------------------- | --- | ------------------ | --- |
|                                              |     |     |     |     | Fig.8. ThemessagetrellisforthejunctiontreeinFig.4,undertheschedule |                        |     |                    |     |
|                                              |     |     |     |     | ofTableIII,viz.,E                                                  | =f(3;1);(4;2);(5;2)g,E |     | =f(1;2);(2;1)g,and |     |
Fig.7. ThemessagetrellisforthejunctiontreeinFig.4undertheschedule
E =f(1;3);(2;4);(2;5)g.
| ofTableIIviz.,E | = f(3;1)g,E | = f(4;2)g,E |     | = f(5;2)g,E | =   |     |     |     |     |
| --------------- | ----------- | ----------- | --- | ----------- | --- | --- | --- | --- | --- |
f(2;1)g.
|                              | .Theideaisthat |                          | isthesetofmes- |     |     |     |     |     |     |
| ---------------------------- | -------------- | ------------------------ | -------------- | --- | --- | --- | --- | --- | --- |
| sagesthatareupdatedduringthe |                | throundofthealgorithm.In |                |     |     |     |     |     |     |
TablesIIandIII,forexample,thecorrespondingschedulesare
TableII
TableIII
| Givenaschedule      |                                    |       | ,thecorresponding    |            |     |     |     |     |     |
| ------------------- | ---------------------------------- | ----- | -------------------- | ---------- | --- | --- | --- | --- | --- |
| message trellis     | is a finite directed               | graph | with                 | vertex set |     |     |     |     |     |
|                     | ,inwhichatypicalelementisdenotedby |       |                      |            | ,   |     |     |     |     |
| for                 | .Theonlyallowededgesareoftheform   |       |                      |            |     |     |     |     |     |
|                     | ;and                               |       | isanedgeinthemes-    |            |     |     |     |     |     |
| sagetrellisifeither |                                    | or    | .Themessagetrellises |            |     |     |     |     |     |
forthejunctiontreeofFig.4,undertheschedulesofTablesII
| and III, are | shown inFigs. | 7and 8, respectively. |     | (In thesefig- |     |     |     |     |     |
| ------------ | ------------- | --------------------- | --- | ------------- | --- | --- | --- | --- | --- |
ures,theshadedboxesindicatewhichlocalkernelsareknown
towhichverticesatanytime.Forexample,inFig.7,wecansee
| thatknowledgeofthelocalkernels |           |              | , ,and      | hasreached |     |     |     |     |     |
| ------------------------------ | --------- | ------------ | ----------- | ---------- | --- | --- | --- | --- | --- |
| at time                        | . We will | elaborate on | this notion | of “knowl- |     |     |     |     |     |
edge”intheAppendix.)
| Theorem3.1(GDLScheduling): |     | Afterthecompletionofthe |     |     |     |     |     |     |     |
| -------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
messagepassingdescribedbytheschedule
|     |     |     |     |     | Fig. 9. (a) | The local domain graph | and (b) one | junction tree | for the local |
| --- | --- | --- | --- | --- | ----------- | ---------------------- | ----------- | ------------- | ------------- |
domainsandkernelsinExample2.1.
|                             |           |                             |     |             | the single-vertex | and all-vertices              | serial | GDL described | earlier |
| --------------------------- | --------- | --------------------------- | --- | ----------- | ----------------- | ----------------------------- | ------ | ------------- | ------- |
| thestateatvertex            | willbethe | thobjectiveasdefinedin(3.2) |     |             | inthis section.   |                               |        |               |         |
| ifandonlyifthereisapathfrom |           |                             | to  | inthecorre- |                   |                               |        |               |         |
| spondingmessagetrellis,for  |           |                             | .   |             |                   | IV. CONSTRUCTINGJUNCTIONTREES |        |               |         |
A proof ofTheorem 3.1 willbe foundin the Appendix, but InSectionIIIweshowedthatifwecanconstructajunction
Figs.7and8illustratetheidea.Forexample,inFig.8,wesee tree with the local domains as vertex labels, we can devise a
that there is a path from each of to , message-passingalgorithmtosolvetheMPFproblem.Butdoes
whichmeans(bytheschedulingtheorem)thataftertworounds suchajunctiontreeexist?Andifnot,whatcanbedone?Inthis
ofmessagepassing,thestateat willbethedesiredobjective sectionwewillanswerthesequestions.
function.Thisiswhy,inTable III,weareabletocompute Itiseasytodecidewhetherornotajunctiontreeexists.The
inround3.Theorem3.1immediatelyimpliesthecorrectnessof keyisthelocaldomaingraph ,whichisaweightedcom-
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

334 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.46,NO.2,MARCH2000
Constructingajunctiontreeforthelocaldomainsf1;2g,f2;3g,f3;4g,andf4;1gbytriangulatingthemoralgraph.
Fig.10.
pletegraphwith vertices ,oneforeachlocaldo- thatcaneasilybecheckeddirectly.IfweapplytheGDLtothis
main,withtheweightoftheedge definedby junctiontree,wegetthe“algorithm”describedinourintroduc-
|     |     |     |     |     |     |     |     | toryExample1.1 |     | (ifwe | usethe | schedule |     |      | ,   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | ------ | -------- | --- | ---- | --- |
|     |     |     |     |     |     |     |     | where          |     |       | ,      |          |     | ,and |     |
).
| If  | ,wewillsaythat |     |     | iscontainedin |     |     | .Denote |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | ------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
by theweightofamaximal-weightspanningtreeof .6 Ifnojunctiontreeexistswiththegivenvertexlabels ,allis
Finally,define notlost.Wecanalwaysfindajunctiontreewith verticessuch
|     |     |     |     |     |     |     |     | thateach         | isasubsetofthe |                  |     | thvertexlabel,sothateachlocal |            |              |         |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | -------------- | ---------------- | --- | ----------------------------- | ---------- | ------------ | ------- |
|     |     |     |     |     |     |     |     | kernel           | may be         | associated       |     | with the                      | th vertex, | by regarding |         |
|     |     |     |     |     |     |     |     | it as a function |                | of the variables |     | involved                      | in         | the label.   | The key |
tothisconstructionisthemoralgraph7whichistheundirected
|                |         |                  |                               |           |     |                |     | graphwithvertexsetequaltothesetofvariables |         |             |     |         |                       |              | ,   |
| -------------- | ------- | ---------------- | ----------------------------- | --------- | --- | -------------- | --- | ------------------------------------------ | ------- | ----------- | --- | ------- | --------------------- | ------------ | --- |
| Theorem4.1:    |         |                  | ,withequalityifandonlyifthere |           |     |                |     |                                            |         |             |     |         |                       |              |     |
|                |         |                  |                               |           |     |                |     | andhavinganedgebetween                     |         |             |     | and     | ifthereisalocaldomain |              |     |
| is a junction  | tree.   | If               |                               | , then    | any | maximal-weight |     |                                            |         |             |     |         |                       |              |     |
| spanningtreeof |         | isajunctiontree. |                               |           |     |                |     | whichcontainsboth                          |         |             | and | .       |                       |              |     |
|                |         |                  |                               |           |     |                |     | Given                                      | a cycle | in a graph, |     | a chord | is an                 | edge between | two |
| Proof:         | Foreach |                  |                               | ,denoteby |     | thenumber      |     |                                            |         |             |     |         |                       |              |     |
verticesonthecyclewhichdonotappearconsecutivelyinthe
| ofsets | whichcontainthevariable |     |     |     | .Notethat |     |     |          |          |              |     |          |        |              |     |
| ------ | ----------------------- | --- | --- | --- | --------- | --- | --- | -------- | -------- | ------------ | --- | -------- | ------ | ------------ | --- |
|        |                         |     |     |     |           |     |     | cycle. A | graph is | triangulated |     | if every | simple | cycle (i.e., | one |
withnorepeatedvertices)oflengthlargerthanthreehasachord.
In[18],itisshownthatthecliques(maximalcompletesub-
graphs)ofagraphcanbethevertexlabelsofajunctiontreeif
|        |              |     |         |     |           |        |     | and only | if the graph | is  | triangulated. |     | Thus | to form a | junction |
| ------ | ------------ | --- | ------- | --- | --------- | ------ | --- | -------- | ------------ | --- | ------------- | --- | ---- | --------- | -------- |
| Let be | any spanning |     | tree of |     | , and let | denote | the |          |              |     |               |     |      |           |          |
numberofedgesin whichcontain .Clearly tree with vertex labels such that each of the local domains is
|              |     |     |                   |     |     |     |         | contained         | in some   | vertexlabel, |      | we form  | the      | moral graph,     | add     |
| ------------ | --- | --- | ----------------- | --- | --- | --- | ------- | ----------------- | --------- | ------------ | ---- | -------- | -------- | ---------------- | ------- |
|              |     |     |                   |     |     |     |         | enough edgestothe |           | moralgraphso |      | thatthe  |          | resultinggraphis |         |
|              |     |     |                   |     |     |     |         | triangulated,     | and       | then form    | a    | junction | tree     | with the cliques | of      |
|              |     |     |                   |     |     |     |         | this graph        | as vertex | labels.      | Each | of the   | original | local            | domains |
| Furthermore, |     |     | ,sincethesubgraph |     |     | of  | induced |                   |           |              |      |          |          |                  |         |
willbeasubsetofatleastoneofthesecliques.Wecanthenat-
| bytheverticescontaining |     |     | hasnocycles,andequalityholds |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tachtheoriginallocaldomainsas“leaves”tothecliquejunction
| ifandonlyif | isconnected,i.e.,atree.Itfollowsthenthat |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tree,therebyobtainingajunctiontreefortheoriginalsetoflocal
domainsandkernels,plusextralocaldomainscorrespondingto
|                                     |     |     |     |     |     |                   |     | the cliques | in the  | moral    | graph.  | We can | then    | associate | one of  |
| ----------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- | ----------- | ------- | -------- | ------- | ------ | ------- | --------- | ------- |
|                                     |     |     |     |     |     |                   |     | the local   | kernels | attached | to each | of the | cliques | to that   | clique, |
| withequalityifandonlyifeachsubgraph |     |     |     |     |     | isconnected,i.e., |     |             |         |          |         |        |         |           |         |
anddeletethecorrespondingleaf.Inthiswaywewillhavecon-
if isajunctiontree. structedajunctiontreefortheoriginalsetoflocalkernels,with
Example4.1: HerewecontinueExample2.1.TheLDgraph some of the local domains enlarged to include extra variables.
However,thisconstructionisfarfromunique,andthechoices
| is shown | in Fig. 9(a). | Here |     |     |     |     |     | .   |     |     |     |     |     |     |     |
| -------- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AmaximalweightspanningtreeisshowninFig.9(b),andits thatmustbemade(whichedgestoaddtothemoralgraph,how
toassignlocalkernelstotheenlargedlocaldomains)makethe
| weight is | , so by | Theorem | 4.1, | this | is a junction | tree, | a fact |     |     |     |     |     |     |     |     |
| --------- | ------- | ------- | ---- | ---- | ------------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
proceduremoreofanartthanascience.
6Amaximal-weightspanningtreecaneasilybefoundwithPrim’s“greedy”
algorithm [27, Ch. 3], [9, Sec. 24.2]. In brief, Prim’s algorithm works by 7Thewhimsicalterm“moralgraph”originallyreferredtothegraphobtained
growingthetreeoneedgeatatime,alwayschoosinganewedgeofmaximal fromaDAGbydrawingedgesbetween—“marrying”—eachoftheparentsofa
| weight. |     |     |     |     |     |     |     | givenvertex[23]. |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

AJIANDMCELIECE:THEGENERALIZEDDISTRIBUTIVELAW 335
Fig.11. TheLDgraphforthelocaldomainsandkernelsinExample2.2.(All
edgeshaveweight1.)Thereisnojunctiontree.
Fig.13. ConstructingajunctiontreeforExample4.2.
| of them, | and viewing | the associated |     | local kernels | as functions |     |
| -------- | ----------- | -------------- | --- | ------------- | ------------ | --- |
ontheenlargedlocaldomains:
|     | localdomain |     | localkernel |     |     |     |
| --- | ----------- | --- | ----------- | --- | --- | --- |
Thedifficultyisthatwemustenlargethelocaldomainsenough
| so that they | will support | a junction | tree, | but | not so much | that |
| ------------ | ------------ | ---------- | ----- | --- | ----------- | ---- |
theresultingalgorithmwillbeunmanageablycomplex.Wewill
Fig.12. Themoralgraph(top)andatriangulatedmoralgraph(bottom)forthe
returntotheissueofjunctiontreecomplexityinSectionV.
localdomainsandkernelsinExample2.2.
Thenextexampleillustratesthisprocedureinamorepractical
setting.
Forexample,supposethelocaldomainsandlocalkernelsare
| Example4.2: | HerewecontinueExample2.2.Thelocaldo- |     |     |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- | --- | --- |
localdomain localkernel maingraphisshowninFig.11.Sincealledgeshaveweight ,
| any spanning          | tree will     | have       | weight      | , but             |              | .      |
| --------------------- | ------------- | ---------- | ----------- | ----------------- | ------------ | ------ |
| Thus by               | Theorem 4.1,  | the local  | domains     | cannot            | be organized |        |
| into a junction       | tree,         | so we need | to consider |                   | the moral    | graph, |
| which is              | shown in Fig. | 12(a).     | It is       | not triangulated  | (e.g.,       | the    |
| cycleformedbyvertices |               | ,          | , ,and      | hasnochord),butit |              |        |
Asweobservedabove,theselocaldomainscannotbeorganized canbetriangulatedbytheadditionofthreeadditionaledges,as
intoajunctiontree.Themoralgraphforthesedomainsisshown showninFig.12(b).Thereareexactlythreecliquesinthetrian-
inFig.10(a)(solidlines).Thisgraphisnottriangulated,butthe gulated moral graph, viz., , ,
additionoftheedge2–4(dashedline)makesitso.Thecliques and .Thesethreesetscanbeorganizedintoa
inthetriangulatedgraphare and ,andthese uniquejunctiontree,andeachoftheoriginalfivelocaldomains
setscanbemadethelabelsinajunctiontree(Fig.10(b)).Wecan isasubsetofexactlyoneofthese,asshowninFig.13(a).Ifwe
attachtheoriginalfourlocaldomainsasleavestothisjunction wantauniquelocaldomainforeachofthefivelocalkernels,we
tree, as shown in Fig. 10(c) (note that this graph is identical canretaintwooftheoriginallocaldomains,thusobtainingthe
to the junction tree in Fig. 5). Finally, we can assign the local junctiontreeshowninFig.13(b).Sincethisisa“single-vertex”
kernel at to the local domain , and the local problem, to apply the GDL, we first direct each of the edges
kernelat tothelocaldomain ,therebyobtaining towards the target vertex, which in this case is .
the junction tree shown in Fig. 10(d). What we have done, in It is now a straightforward exercise to show that the (serial,
effect,istomodifytheoriginallocaldomainsbyenlargingtwo one-vertex) GDL, when applied to this directed junction tree,
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

336 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.46,NO.2,MARCH2000
Fig.14. AjunctiontreeforExample4.3.
|     |     |     |     |     |     |     |     | Fig.15. AjunctiontreeforExample4.4.Thisfigureshouldbecomparedto |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Fig.1.
yieldstheusual“fast”Hadamardtransform.Moregenerally,by
extendingthemethodinthisexample,itispossibletoshowthat
theFFTonanyfiniteAbeliangroup,asdescribed,e.g.,in[8]or Example 4.6: Here we continue Example 2.6, the matrix
[31],canbederivedfromanapplicationoftheGDL.8 multiplicationproblem.Itiseasytoseethatfor ,thereis
|                     |          |             |               |         |               |          |            | no junction                                | tree for | the original |     | set of local      | domains, | because |
| ------------------- | -------- | ----------- | ------------- | ------- | ------------- | -------- | ---------- | ------------------------------------------ | -------- | ------------ | --- | ----------------- | -------- | ------- |
| Example             | 4.3:     | Here        | we continue   | Example |               | 2.3. In  | this case, |                                            |          |              |     |                   |          |         |
|                     |          |             |               |         |               |          |            | thecorrespondingmoralgraphisacycleoflength |          |              |     |                   |          | .Itis   |
| the local           | domains  | can         | be organized  |         | as a junction |          | tree. One  |                                            |          |              |     |                   |          |         |
|                     |          |             |               |         |               |          |            | possibletoshowthatfortheproductof          |          |              |     | matrices,thereare |          |         |
| such tree           | is shown | in          | Fig. 14.      | It can  | be shown      | that     | the GDL,   |                                            |          |              |     |                   |          |         |
| when applied        |          | to the      | junction tree | of      | Fig. 14,      | yields   | the Gal-   |                                            |          |              |     |                   |          |         |
| lager–Tanner–Wiberg |          |             | algorithm     | [15],   | [34],         | [39] for | decoding   |                                            |          |              |     |                   |          |         |
| linear codes        | defined  |             | by cycle-free |         | graphs.       | Indeed,  | Fig. 14    |                                            |          |              |     |                   |          |         |
| is identical        | to       | the “Tanner | graph”        | cited   | by            | Wiberg   | [39] for   |                                            |          |              |     |                   |          |         |
possibletriangulationsofthemoralgraph,whichareinone-to-
decodingthisparticularcode.
onecorrespondencewiththedifferentwaystoparenthesizethe
Example4.4: HerewecontinueExample2.4.Thelocaldo- expression .Forexample,theparenthesization
mainscanbearrangedintoajunctiontree,asshowninFig.15.
| (In general,    | the | junction     | tree has | the           | same       | topology   | as DAG, |     |     |     |     |     |     |     |
| --------------- | --- | ------------ | -------- | ------------- | ---------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| if the DAG      | is  | cycle-free.) | The      | GDL           | algorithm, | when       | applied |     |     |     |     |     |     |     |
| to the junction |     | tree of      | Fig. 15, | is equivalent |            | to certain | algo-   |     |     |     |     |     |     |     |
correspondstothetriangulationshowninFig.17.
| rithms which | are | known | in the | artificial | intelligence |     | commu- |     |     |     |     |     |     |     |
| ------------ | --- | ----- | ------ | ---------- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Thustheproblemoffindinganoptimaljunctiontreeisiden-
nityforsolvingtheprobabilisticinferenceproblemonBayesian ticaltotheproblemoffindinganoptimalparenthesization.For
networkswhoseassociatedDAG’sarecycle-free;inparticular,
|     |     |     |     |     |     |     |     | example,inthecase |     |     | ,illustratedinFig.18,therearetwo |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | -------------------------------- | --- | --- | --- |
Pearl’s“beliefpropagation”algorithm[29],andthe“probability differenttriangulationsofthemoralgraph,whichlead,viathe
propagation”algorithmofShaferandShenoy[33].
|     |     |     |     |     |     |     |     | techniques | described | in this | section, | to the | two junction | trees |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------- | -------- | ------ | ------------ | ----- |
Example 4.5: Here we continue Example 2.5, the proba- shown in the lower part of Fig. 18. With the top vertex as the
bilistic state machine. In this case the local domains can be target, the GDL applied to each of these trees computes the
organized into a junction tree, as illustrated in Fig. 16 for the product .Theleftjunctiontreecorrespondstoparen-
case .TheGDLalgorithm,appliedtothejunctiontreeof thesizing the product as and requires
arithmeticoperations,whereastherightjunc-
Fig.16,givesusessentiallytheBCJR[5]andViterbi[37][11]
algorithms, respectively. (For Viterbi’s algorithm, we take the tion tree corresponds to and requires
operations.Thuswhichtreeoneprefersdependsonthe
negativelogarithmoftheobjectivefunctionin(2.5),andusethe
min-sum semiring, with a single target vertex, preferably the relativesizeofthematrices.Forexample,if , ,
|        |                  |     |     |                       |     |     |     | ,and |     | ,theleftjunctiontreerequires15000oper- |     |     |     |     |
| ------ | ---------------- | --- | --- | --------------------- | --- | --- | --- | ---- | --- | -------------------------------------- | --- | --- | --- | --- |
| “last” | ,whichinFig.16is |     |     | .FortheBCJRalgorithm, |     |     |     |      |     |                                        |     |     |     |     |
ationsandtherightjunctiontreetakes150000.(Thisexample
| we use | the objective | function | in  | (2.5) | as it stands, | and | use the |     |     |     |     |     |     |     |
| ------ | ------------- | -------- | --- | ----- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
istakenfrom[9].)
| sum–product       | semiring, |     | and evaluate |     | the objective | function      |     | at         |            |            |           |                 |                |             |
| ----------------- | --------- | --- | ------------ | --- | ------------- | ------------- | --- | ---------- | ---------- | ---------- | --------- | --------------- | -------------- | ----------- |
|                   |           |     |              |     |               |               |     | As we      | discussed  | in Example |           | 2.6, the matrix | multiplication |             |
| eachofthevertices |           |     | ,for         |     |               | .Inbothcases, |     |            |            |            |           |                 |                |             |
|                   |           |     |              |     |               |               |     | problem is | equivalent | to         | a trellis | path problem.   | In             | particular, |
theappropriatescheduleisfullyserial.)
|     |     |     |     |     |     |     |     | if the computations |         | are in       | the min-sum | semiring,       | the | problem   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | ------- | ------------ | ----------- | --------------- | --- | --------- |
|     |     |     |     |     |     |     |     | is that of          | finding | the shortest | paths       | in the trellis. | If  | the moral |
8Forthis,see[1],whereitisobservedthatthemoralgraphfortheDFTover
graphistriangulatedasshowninFig.17,theresultingjunction
afiniteAbeliangroupGistriangulatedifandonlyifGisacyclicgroupof
|     |     |     |     |     |     |     |     | tree yields | an algorithm | identical |     | to Viterbi’s | algorithm. | Thus |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --------- | --- | ------------ | ---------- | ---- |
prime-powerorder.Inallothercases,itisnecessarytotriangulatethemoral
graph,aswehavedoneinthisexample. Viterbi’s algorithm can be viewed as an algorithm for multi-
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

| AJIANDMCELIECE:THEGENERALIZEDDISTRIBUTIVELAW |     |     |     |     |     |     |     |     |     |     |     |     | 337 |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.16. Ajunctiontreefortheprobabilisticstatemachine(illustratedforn=4).
Webeginbyrewritingthemessageandstatecomputationfor-
mulas(3.1)and(3.2),usingslightlydifferentnotation.Themes-
|     |     |     |     |     |     |     | sagefromvertex |     | tovertex | isdefinedas(cf.(3.1)) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --------------------- | --- | --- | --- |
(5.1)
|     |     |     |     |     |     |     | andthestateofvertex |     | isdefinedas(cf.(3.2)) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --------------------- | --- | --- | --- | --- |
(5.2)
| Fig. 17. | The triangulation     | of the moral          | graph | corresponding |     | to the |     |     |     |     |     |     |     |
| -------- | --------------------- | --------------------- | ----- | ------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|          | (cid:1)(cid:1)(cid:1) | (cid:1)(cid:1)(cid:1) |       |               |     |        |     |     |     |     |     |     |     |
parenthesization(( (M M ) )M )M . We first consider the single-vertex problem, supposing that
|     |     |     |     |     |     |     | is the              | target. For                                 | each                     | , there              | is exactly | one          | edge |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | ------------------------------------------- | ------------------------ | -------------------- | ---------- | ------------ | ---- |
|     |     |     |     |     |     |     | directedfrom        | toward                                      | .Wesupposethatthisedgeis |                      |            |              | .    |
|     |     |     |     |     |     |     | Tocomputethemessage |                                             |                          | asdefinedin(5.1)fora |            |              |      |
|     |     |     |     |     |     |     | particularvalueof   |                                             | requires9                |                      |            | additionsand |      |
|     |     |     |     |     |     |     |                     |                                             | multiplications,where    |                      |            | isthedegree  |      |
|     |     |     |     |     |     |     | ofthevertex         | .Usingsimplifiedbut(wehope)self-explanatory |                          |                      |            |              |      |
notationwerewritethisasfollows:
additions,and
multiplications.
But thereare
|     |     |     |     |     |     |     | possibilities | for | , so | the entire message |     |     | re- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---- | ------------------ | --- | --- | --- |
quires
additions,and
multiplications.
Thetotalnumberofarithmeticoperationsrequiredtosendmes-
|     |     |     |     |     |     |     | sagestoward | alongeachoftheedgesofthetreeisthus |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------------------------------- | --- | --- | --- | --- | --- |
Fig. 18. The moral graph for Example 4.6, triangulated in two ways, and additions
| the corresponding | junction trees. | The left  | junction | tree corresponds |             | to the |          |              |      |                  |     |              |     |
| ----------------- | --------------- | --------- | -------- | ---------------- | ----------- | ------ | -------- | ------------ | ---- | ---------------- | --- | ------------ | --- |
| parenthesization  | (M M )M         | , and the | one on   | the right        | corresponds | to     |          |              |      |                  |     |              |     |
| M (M M            | ).              |           |          |                  |             |        |          |              |      | multiplications. |     |              |     |
|                   |                 |           |          |                  |             |        | When all | the messages | have | been computed    | and | transmitted, |     |
plyingachainofmatricesinthemin-sumsemiring.(Thiscon-
|     |     |     |     |     |     |     | the algorithm | terminates | with | the computation |     | of the state | at  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | ---- | --------------- | --- | ------------ | --- |
nectionisexploredinmoredetailin[4].)
|     |     |     |     |     |     |     | , defined | by (5.2). | This | state computation | requires |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---- | ----------------- | -------- | --- | --- |
furthermultiplications,sothatthetotalis
V. COMPLEXITYOFTHEGDL
additions
| In this | section we will | providecomplexityestimates |     |     | for | the |     |     |     |     |     |     |     |
| ------- | --------------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
serial versions of the GDL discussed in Section III. Here by multiplications.
| complexity | we mean the | arithmetic | complexity, |     | i.e., the | total |     |     |     |     |     |     |     |
| ---------- | ----------- | ---------- | ----------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
numberof(semiring)additionsand/ormultiplicationsrequired
9Hereweareassumingthattheaddition(multiplication)ofNelementsofS
requiresN(cid:0)
tocomputethedesiredobjectivefunctions. 1binaryadditions(multiplications).
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

338 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.46,NO.2,MARCH2000
Thusthegrandtotalnumberofadditionsandmultiplicationsis asinthesingle-vertexcase,and,summedoverallmessages,re-
quire
(5.3)
| where | if  |     | is an | edge, its “size” |     | is defined | to be |     |     |     |     |     |     |     |     |
| ----- | --- | --- | ----- | ---------------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
.
Notethattheformulain(5.3)givestheupperbound
additions.Thusthetotalnumberofarithmeticoperationsisno
|     |     |     |     |     |     |     | (5.4) | more than        |     |     | , which  | shows   | that the | complexity | of      |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------------- | --- | --- | -------- | ------- | -------- | ---------- | ------- |
|     |     |     |     |     |     |     |       | the all-vertices | GDL | is  | at worst | a fixed | constant | times      | that of |
mentionedinSectionIII. thesingle-vertexGDL.Therefore,wefeeljustifiedindefining
|     |           |          |     |                 |     |                    |     | the complexity | of  | a junction | tree, | irrespective |     | of which | objec- |
| --- | --------- | -------- | --- | --------------- | --- | ------------------ | --- | -------------- | --- | ---------- | ----- | ------------ | --- | -------- | ------ |
| The | formulain | (5.3)can |     | be rewrittenina |     | useful alternative |     |                |     |            |       |              |     |          |        |
way,ifwedefinethe“complexity”oftheedge as tive functions are sought, by (5.3) or (5.6). (In [23], the com-
plexityofasimilar,butnotidentical,algorithmwasshowntobe
(5.5)
|     |     |     |     |     |     |     |     | upper-boundedby |     |     |     |     | .Thisboundisstrictly |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | -------------------- | --- | --- |
Withthisdefinition,theformulain(5.3)becomes
greaterthantheboundin(5.4).)
|     |     |     |     |     |     |     |     | InSectionIV,wesawthatinmanycases |     |     |     |     |     |     | andthe |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | ------ |
(5.6)
LDgraphhasmorethanonemaximal-weightspanningtree.In
Forexample,forthejunctiontreeofFig.4,therearefouredges view of the results in this section, in such cases it is desirable
| and |     |     |     |     |     |     |     | to find the | maximal-weight |     | spanning |     | tree with |     | as small |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | --- | -------- | --- | --------- | --- | -------- |
aspossible.ItiseasytomodifyPrim’salgorithmtodothis.In
|     |     |     |     |     |     |     |     | Prim’s algorithm, |         | the basic | step  | is to        | add to   | the growing | tree      |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | --------- | ----- | ------------ | -------- | ----------- | --------- |
|     |     |     |     |     |     |     |     | a maximal-weight  |         | edge      | which | does         | not form | a cycle.    | If there  |
|     |     |     |     |     |     |     |     | are several       | choices | with      | the   | same weight, | choose   |             | one whose |
complexity,asdefinedby(5.5),isassmallaspossible.Thetree
thatresultsisguaranteedtobeaminimum-complexityjunction
so that
tree[19].Infact,weusedthistechniquetofindminimum-com-
plexityjunctiontreesinExamples4.1,4.3,4.4,and4.5.
Weconcludethissectionwithtwoexampleswhichillustrate
Wenextbrieflyconsidertheall-verticesproblem.Hereames- the difficulty of finding the minimum-complexity junction
|      |         |           |      |          |                  |     |         | tree for a    | given | marginalization |     | problem. | Consider |     | first the  |
| ---- | ------- | --------- | ---- | -------- | ---------------- | --- | ------- | ------------- | ----- | --------------- | --- | -------- | -------- | --- | ---------- |
| sage | must be | sent over | each | edge, in | both directions, |     | and the |               |       |                 |     |          |          |     |            |
|      |         |           |      |          |                  |     |         | local domains |       | ,               | ,   | , and    |          |     | . There is |
statemustbecomputedateachvertex.Ifthisisdonefollowing
theideasaboveintheobviousway,theresultingcomplexityis a unique junction tree with these sets as vertex labels, shown
|     |     |     |     |     |     |     |     | in Fig. 19(a). | By  | (5.3), | the complexity |     | of this | junction | tree is |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | -------------- | --- | ------- | -------- | ------- |
.However,wemayreducethisbynoticingthat
.Nowsupposeweartificiallyenlargethelocaldomain
| if                                   |          | isasetof |     | numbers,itispossibletocompute |      |             |     |     |     |                                         |     |     |                    |     |     |
| ------------------------------------ | -------- | -------- | --- | ----------------------------- | ---- | ----------- | --- | --- | --- | --------------------------------------- | --- | --- | ------------------ | --- | --- |
|                                      |          |          |     |                               |      |             |     | to  |     | .Thenthemodifiedsetoflocaldomains,viz., |     |     |                    |     |     |
| all the                              | products | of       |     | of the ’s                     | with | at most     |     |     |     |                                         |     |     |                    |     |     |
|                                      |          |          |     |                               |      |             |     | ,   | ,   | ,and                                    |     |     | canbeorganizedinto |     |     |
| multiplications,ratherthantheobvious |          |          |     |                               |      | .Wedothisby |     |     |     |                                         |     |     |                    |     |     |
precomputing the quantities , , the junction tree shown in Fig. 19(b), whose complexity is
|          |             |                        |         |     |                   |       |     |                       | ,   | which | is less | than that          | of the               | original | tree as |
| -------- | ----------- | ---------------------- | ------- | --- | ----------------- | ----- | --- | --------------------- | --- | ----- | ------- | ------------------ | -------------------- | -------- | ------- |
| ,        |             |                        |         |     |                   | , and |     | ,                     |     |       |         |                    |                      |          |         |
|          |             |                        |         |     |                   |       |     | longas                | .   |       |         |                    |                      |          |         |
|          |             |                        |         | , , |                   |       |     | ,                     |     |       |         |                    |                      |          |         |
|          |             |                        |         |     |                   |       |     | Asthesecondexample,we |     |       |         | considerthedomains |                      |          | ,       |
| using    |             | multiplications.Thenif |         |     | denotestheproduct |       |     |                       |     |       |         |                    |                      |          |         |
|          |             |                        |         |     |                   |       |     | ,                     |     | ,and  |         |                    | ,whichcanbeorganized |          |         |
| ofallthe | ’sexceptfor |                        | ,wehave |     | ,                 |       | ,   | ,                     |     |       |         |                    |                      |          |         |
, , using a further multipli- intoauniquejunctiontree(Fig.20(a)).Ifweadjointhedomain
,however,wecanbuildajunctiontree(Fig.20(b))
| cations,foratotalof |     |     |     | .Withonefurthermultiplication |     |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whosecomplexityislowerthantheoriginalone,providedthat
| (   | ),wecancompute |     |     |     |     | .10 |     |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Returningnowtotheserialimplementationoftheall-vertex ismuchlargerthananyoftheother ’s.(Itisknownthatthe
problemoffindingthe“best”triangulationofagivengraphis
| GDL, | each vertex | must | pass | a message | to each | of  | its neigh- |     |     |     |     |     |     |     |     |
| ---- | ----------- | ---- | ---- | --------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
bors.Vertex willhave incomingmessages,and(priorto NP-complete[40],where“best”referstohavingtheminimum
maximumcliquesize.)
marginalization)eachoutgoingmessagewillbetheproductof
|                      | of these | messages |                          | with the | local kernel | at  | . For its |     |     |     |     |     |     |     |     |
| -------------------- | -------- | -------- | ------------------------ | -------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ownstatecomputation, |          |          | alsoneedstheproductofall |          |              |     | in-       |     |     |     |     |     |     |     |     |
VI. ABRIEFHISTORYOFTHEGDL
comingmessageswiththelocalkernel.Bytheaboveargument,
allthiscanbedonewithatmost multiplicationsforeach Importantalgorithmswhoseessential underlyingideaisthe
ofthe valuesofthevariablesinthelocaldomainat .Thus exploitation of the distributive law to simplify a marginaliza-
thenumberofmultiplicationsrequiredisatmost . tionproblemhavebeendiscoveredmanytimesinthepast.Most
Themarginalizationsduringthemessagecomputationsremain ofthesealgorithmsfall intoone ofthree broadcategories:de-
codingalgorithms,the“forward–backwardalgorithm,”andar-
10Oneoftherefereeshasnotedthatthetrickdescribedinthisparagraphis
tificialintelligencealgorithms.Inthissectionwewillsumma-
itselfanapplicationoftheGDL;ithasthesamestructureastheforward–back-
wardalgorithmappliedtoatrellisrepresentingarepetitioncodeoflengthd. rizethesethreeparallelthreads
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

AJIANDMCELIECE:THEGENERALIZEDDISTRIBUTIVELAW 339
sum-productandmin-sumsemirings,andspeculatedonthepos-
sibility of further generalizations to what he called “universal
algebras”(oursemirings).
In an independent series of developments, in 1967 Viterbi
[37]inventedhiscelebratedalgorithmformaximum-likelihood
decoding (minimizing sequence error probability) of convolu-
tionalcodes.Sevenyearslater(1974),Bahl,Cocke,Jelinek,and
Raviv[5]publisheda“forward–backward”decodingalgorithm
(seenextbullet)forminimizingthebit-errorprobabilityofcon-
volutionalcodes.Thecloserelationshipbetweenthesetwoal-
gorithmswasimmediatelyrecognizedbyForney[11].Although
these algorithms did not apparently lead anyone to discover a
class of algorithms of GDL-like generality, with hindsight we
canseethatalltheessentialideaswerepresent.
•TheForward–BackwardAlgorithm
Fig.19. Enlargingalocaldomaincanlowerthejunctiontreecomplexity. Theforward–backwardalgorithm(alsoknownasthe -step
intheBaum–Welchalgorithm)wasinventedin1962byLloyd
Welch,andseemstohavefirstappearedintheunclassifiedliter-
atureintwoindependent1966publications[6],[7].Itappeared
explicitly as an algorithm for tracking the states of a Markov
chain in the early 1970’s [5], [26] (see also the survey arti-
cles[30]and[32]).Asimilaralgorithm(inmin-sumform)ap-
pearedina1971paperonequalization[35].Thealgorithmwas
connected to the optimization literature in 1987 [36], where a
semiring-typegeneralizationwasgiven.
•ArtificialIntelligence
Therelevantresearchintheartificialintelligence(AI)com-
munity began relatively late, but it has evolved quickly. The
activity began in the 1980’s with the work of Kim and Pearl
[20] and Pearl [29]. Pearl’s“belief propagation” algorithm, as
it has come to be known, is a message-passing algorithm for
solvingtheprobabilisticinferenceproblemonaBayesiannet-
workwhoseDAGcontainsno(undirected)cycles.Soonafter-
Fig.20. Addinganextralocaldomaincanlowerthejunctiontreecomplexity. wards,LauritzenandSpiegelhalter[23]obtainedanequivalent
algorithm, and moreover generalized it to arbitrary DAG’s by
•DecodingAlgorithms introducingthetriangulationprocedure.Thenotionofjunction
trees(underthename“Markovtree”)wasexplicitlyintroduced
TheearliestoccurrenceofaGDL-likealgorithmthatweare
byShafer and Shenoy [33].A recent bookby Jensen [18]is a
aware of is Gallager’s 1962 algorithm for decoding low-den-
goodintroductiontomostofthismaterial.Arecentunification
sity parity-check codes [15] [16]. Gallager was aware that his
ofmanyoftheseconceptscalled“bucketelimination”appears
algorithm could be proved to be correct only when the under-
in[10],andarecentpaperbyLauritzenandJensen[22]abstracts
lying graphical structure had no cycles, but also noted that it
theMPFproblemstillfurther,sothatthemarginalizationisdone
gavegoodexperimentalresultsevenwhencycleswerepresent.
axiomatically,ratherthanbysummation.
Gallager’s work attracted little attention for 20 years, but in
In any case, by early 1996, the relevance of these AI algo-
1981Tanner[34],realizingtheimportanceofGallager’swork,
rithms had become apparent to researchers in the information
made an important generalization of low-density parity-check
theorycommunity[21][28].Conversely,theAIcommunityhas
codes,introducedthe“Tannergraph”viewpoint,andrecastGal-
becomeexcitedbythedevelopmentsintheinformationtheory
lager’s algorithm in explicit message-passing form. Tanner’s
community[14][38],whichdemonstratethatthesealgorithms
work itself went relatively unnoticed until the 1996 thesis of
can be successful on graphs with cycles. We discuss this is in
Wiberg [39], which showed that the message-passing Tanner
thenextsection.
graph decoding algorithm could be used not only to describe
Gallager’s algorithm, but also Viterbi’s and BCJR’s. Wiberg
VII. ITERATIVEANDAPPROXIMATEVERSIONSOFTHEGDL
too understood the importanceof the cycle-freecondition, but
neverthelessobservedthattheturbodecodingalgorithmwasan AlthoughtheGDLcanbeprovedtobecorrectonlywhenthe
instanceoftheGallager–Tanner–Wibergalgorithmonagraph- local domains can be organized into a junction tree, the com-
icalstructurewithcycles.Wibergexplicitlyconsideredboththe putations of the messages and states in (3.1) and (3.2) make
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore. Restrictions apply.

340 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.46,NO.2,MARCH2000
| sense | whenever |     | the local | domains | are | organized | as  | vertex la- |     |     |     |     |     |     |     |
| ----- | -------- | --- | --------- | ------- | --- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
belsonanykindofaconnectedgraph,whetheritisajunction
treeornot.Onsuchajunctiongraph,thereisnonotionof“ter-
mination,”sincemessagesmaytravelaroundthecyclesindefi-
|     |     |     |     |     |     |     |     |     | Fig.21. AjunctiontreeforLemmaA.1. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
nitely.Instead,onehopesthataftersufficientlymanymessages
havebeenpassed,thestatesoftheselectedverticeswillbeap-
proximatelyequaltothedesiredobjectivefunctions.Thishope
| is  | based | on a large | body | of experimental |     | evidence, |     | and some |     |     |     |     |     |     |     |
| --- | ----- | ---------- | ---- | --------------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
emergingtheory.
•ExperimentalEvidence
|     | It is now | known | that | an application |     | of the | GDL, | or one of |     |     |     |     |     |     |     |
| --- | --------- | ----- | ---- | -------------- | --- | ------ | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
itscloserelatives,toanappropriatejunctiongraphwithcycles,
givesboththeGallager–Tanner–Wibergalgorithmforlow-den- Fig.22. AjunctiontreeforLemmaA.2.
sityparity-checkcodes[24],[25],[28],[39],theturbodecoding
algorithm [21], [28], [39]. Both of these decoding algorithms . We denote by the function of the vari-
haveprovedtobeextraordinarilyeffectiveexperimentally,de- ablelist obtainedby“marginalizingout”thevariablesin
spitethefactthatthereareasyetnogeneraltheoremsthatex-
|     |     |     |     |     |     |     |     |     | whicharenotin | :   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
plaintheirbehavior.
•EmergingTheory:Single-CycleJunctionGraphs
|         |           |          |     |               |          |        |           |        | LemmaA.1: | If  | ,then |     |     |     |     |
| ------- | --------- | -------- | --- | ------------- | -------- | ------ | --------- | ------ | --------- | --- | ----- | --- | --- | --- | --- |
|         | Recently, | a number | of  | authors       | [1]–[3], | [12],  | [38],[39] | have   |           |     |       |     |     |     |     |
| studied | the       | behavior | of  | the iterative |          | GDL on | junction  | graphs |           |     |       |     |     |     |     |
whichhaveexactlyonecycle.Itseemsfairtosaythat,atleastfor
|     |     |     |     |     |     |     |     |     | Proof: | (NotefirstthatLemmaA.1isaspecialcaseofthe |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------------------------------------- | --- | --- | --- | --- | --- |
thesum-productandthemin-sumsemirings,theiterativeGDL single-vertex GDL, with the following local domains and ker-
isfairlywellunderstoodinthiscase,andtheresultsimply,for
nels.
example,thatiterativedecodingiseffectiveformosttail-biting
|     |     |     |     |     |     |     |     |     |     | localdomain |     | localkernel |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | --- | --- | --- |
codes.Althoughtheseresultsshednodirectlightontheproblem
ofthebehavioroftheGDLonmulticyclejunctiongraphs,like
thoseassociatedwithGallagercodesorturbocodes,thisisnev-
erthelessanencouragingstep.
TheappropriatejunctiontreeisshowninFig.21.)
|     |     |     |     |          |     |     |     |     | To see that                  | the assertion | is true, | note | that | the variables   | not |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | ---------------------------- | ------------- | -------- | ---- | ---- | --------------- | --- |
|     |     |     |     | APPENDIX | A   |     |     |     |                              |               |          |      |      |                 |     |
|     |     |     |     |          |     |     |     |     | marginalizedoutinthefunction |               |          |      |      | arethoseindexed |     |
PROOFOFTHESCHEDULINGTHEOREM by .Thevariablesnotmarginalizedoutin
|     |     |     |     |     |     |     |     |     | arethoseindexedby |     | .Butbythehypothesis |     |     |     | ,   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------------- | --- | --- | --- | --- |
Summary:Inthisappendix,wewillgiveaproofoftheSched-
thesetwosetsareequal.
ulingTheorem3.1,whichwillprovethecorrectnessoftheGDL.
|     |     |     |     |     |     |     |     |     | LemmaA.2: | Let | ,for |     |     | belocalkernels, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---- | --- | --- | --------------- | --- |
ThekeytotheproofisCorollaryA.4,whichtellsusthatatevery
stageofthealgorithm,thestateat agivenvertexis theappro- andconsidertheMPFproblemofcomputing
| priately | marginalized |     | product |     | of a subset | of  | the local | kernels. |     |     |     |     |     |     |     |
| -------- | ------------ | --- | ------- | --- | ----------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Informally, we say that at time , the state at vertex is the (A.1)
| marginalized |     | product | of  | the local | kernels | which | are | currently |     |     |     |     |     |     |     |
| ------------ | --- | ------- | --- | --------- | ------- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
“known”to .Giventhisresult,theremainingproblemistoun- Ifnovariablewhichismarginalizedoutin(A.1)occursinmore
derstandhowknowledgeofthelocalkernelsisdisseminatedto thanonelocalkernel,i.e.,if for ,then
theverticesofthejunctiontreeunderagivenschedule.Aswe
shallsee,this“knowledgedissemination”canbedescribedre-
cursivelyasfollows:
• Rule(1): Initially ,eachvertex knowsonlyits Proof: (Lemma A.2 is also a special case of the single-
ownlocalkernel . vertexGDL,withthefollowinglocaldomainsandkernels:
• Rule (2): If a directed edge is activated at time localdomain localkernel
|     | ,i.e.,if       |     |     | ,thenvertex |     |     | learnsallthelocal |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | ----------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | kernelsknownto |     |     | attime      |     | .   |                   |     |     | . . | . . |     | . . |     |     |
|     |                |     |     |             |     |     |                   |     |     | .   | .   |     | .   |     |     |
TheproofofTheorem3.1thenfollowsquicklyfromtheserules.
|     | Webeginbyintroducingsomenotation.Let |     |     |     |     |     |     | beafunc- |     |     |     |     |     |     |     |
| --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
tion ofthe variable list , and let be anarbitrary subsetof TheappropriatejunctiontreeisshowninFig.22.)
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

| AJIANDMCELIECE:THEGENERALIZEDDISTRIBUTIVELAW |     |     |     |     |     |     |     |     |     |     |     | 341 |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Inanycase,LemmaA.2isasimpleconsequenceofthedis-
| tributive | law: Since | each | variable | being | marginalized | out | in  |     |     |     |     |     |
| --------- | ---------- | ---- | -------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
(A.1)occursinatmostonelocalkernel,itisallowabletotake
| the other | local | kernels out | of the | sum by | distributivity. | As an |     |     |     |     |     |     |
| --------- | ----- | ----------- | ------ | ------ | --------------- | ----- | --- | --- | --- | --- | --- | --- |
example,wehave
|     |     |     |     |     |     |     | Fig.23. Deletingtheedgee |     | breaksthejunctiontreeintotwocomponents. |                |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --------------------------------------- | -------------- | --- | --- |
|     |     |     |     |     |     |     | theoremprovedfor         |     | ,weassume                               | isupdatedinthe |     | th  |
|     |     |     |     |     |     |     | round,andconsider        |     | :                                       |                |     |     |
NowwearereadytoconsiderthedynamicsoftheGDL.Con-
by(3.1)
| sider an                                  | edge: |     | . Removing |     | from | the junction |     |     |     |     |     |     |
| ----------------------------------------- | ----- | --- | ---------- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
| tree breaksitintotwocomponents,           |       |     |            |     | and  | (seeFig.23). |     |     |     |     |     |     |
| Forfuturereference,wedenotethevertexsetof |       |     |            |     |      | by ,and      |     |     |     |     |     |     |
| theedgesetby                              |       | .   |            |     |      |              |     |     |     |     |     |     |
byinduction.
| Since       | isontheuniquepathbetweenanyvertexin |                                           |     |     |     | and |     |     |     |     |     |     |
| ----------- | ----------------------------------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anyvertexin |                                     | ,itfollowsfromthejunctiontreepropertythat |     |     |     |     |     |     |     |     |     |     |
anyvariablewhichoccursinavertexinbothcomponentsmust
Anyvariablethatoccursintwodifferentmessages
| occurinboth |     | and .Thusthemessage |     |     | ,whichmaybe |     |     |     |     |     |     |     |
| ----------- | --- | ------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
viewed as a message from to , is a function of exactly and mustalso,bythejunctiontreeproperty,occur
in ,sowemayapplyLemmaA.2torewritethelastlineas
thosevariableswhichoccurinbothcomponents.
| Inwhatfollows,foreachindex |      |            |     |      |      | wedefine |     |     |     |     |     |     |
| -------------------------- | ---- | ---------- | --- | ---- | ---- | -------- | --- | --- | --- | --- | --- | --- |
| and for each               | pair | of indices |     | such | that | , we     |     |     |     |     |     |     |
define
|     |     |     |     |     |     |     | Since a variable                                     | that | occurs in one of                    | the kernels | in  | the above |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | ---- | ----------------------------------- | ----------- | --- | --------- |
|     |     |     |     |     |     |     | equationandalsoin                                    |      | must,bythejunctiontreeproperty,also |             |     |           |
|     |     |     |     |     |     |     | occurin ,itfollowsfromLemmaA.1thatthislastexpression |      |                                     |             |     |           |
canbesimplifiedto
| Inwords,   | representsthe(indicesof)theneighborsof |              |     |               |     | ,and       |     |     |     |     |     |     |
| ---------- | -------------------------------------- | ------------ | --- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| represents |                                        | the (indices | of) | the neighbors | of  | other than |     |     |     |     |     |     |
.
| Nowlet                                                 |     |              |     | beascheduleforajunction |     |           |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | ------------ | --- | ----------------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
| tree,asdefinedinSectionIII,i.e.,afinitelistofsubsetsof |     |              |     |                         |     |           | ,   |     |     |     |     |     |
| and let                                                |     | be the value | of  | the message             |     | after the | th  |     |     |     |     |     |
thelastequalitybecauseofthedefinition(A.3).
| round of            | .   |            |                                 |                       |     |     |               |        |           |     |             |     |
| ------------------- | --- | ---------- | ------------------------------- | --------------------- | --- | --- | ------------- | ------ | --------- | --- | ----------- | --- |
|                     |     |            |                                 |                       |     |     | CorollaryA.4: | Forall | ,thestate |     | hasthevalue |     |
| TheoremA.3:         |     | Themessage |                                 | istheproductofasubset |     |     |               |        |           |     |             |     |
| ofthelocalkernelsin |     |            | ,withthevariablesthatdonotoccur |                       |     |     |               |        |           |     |             |     |
in marginalizedout.Specifically,wehave
(A.4)
(A.2)
|       |             |     |     |                 |     |          | wheretheset | isdefinedby |     |     |     |       |
| ----- | ----------- | --- | --- | --------------- | --- | -------- | ----------- | ----------- | --- | --- | --- | ----- |
| where | isasubsetof |     |     | ,thevertexsetof |     | .Thesets |             |             |     |     |     | (A.5) |
aredefinedinductivelyasfollows:
|     |     |     |     |     |     |     | Proof: | Bydefinition(3.2) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------------- | --- | --- | --- | --- |
andfor
if
(A.3)
if
| Proof:                              | Weuseinductionon |     |     | ,thecase |              | beingsimply |     |     |     |     |     |     |
| ----------------------------------- | ---------------- | --- | --- | -------- | ------------ | ----------- | --- | --- | --- | --- | --- | --- |
| arestatementoftheinitializationrule |                  |     |     |          | .Assumingthe |             |     |     |     |     |     |     |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

342 IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.46,NO.2,MARCH2000
(Weknowthat ,sincethekernel isbydefinitiona (Inwords,knowledgeof mustpasssequentiallyto through
functiononlyofthevariablesinvolvedinthelocaldomain .) the vertices of the path .) In view of (A.6), we have the
| ByTheoremA.3,thiscanbewrittenas |     |     |     |     |     |     |     | following path        | from |     |     | to  |     |     | in  |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------- | ---- | --- | --- | --- | --- | --- | --- |
|                                 |     |     |     |     |     |     |     | themessagetrellisfrom |      |     | to  | :   |     |     |     |
(A.7)
| But by the | junction | tree | property, | any | variable | that | occurs | in          |         |       |      |           |     |     |     |
| ---------- | -------- | ---- | --------- | --- | -------- | ---- | ------ | ----------- | ------- | ----- | ---- | --------- | --- | --- | --- |
|            |          |      |           |     |          |      |        | Conversely, | suppose | there | is a | path from |     | to  | in  |
two of the bracketed terms must also occur in , so that by the message trellis. Then since apart from “pauses” at a given
LemmaA.2
vertex,thispathinthemessagetrellismustbetheuniquepath
|     |     |     |     |     |     |     |     | from            | to ,Rule2impliesthatknowledgeofthekernel |         |     |          |     |          |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---------------------------------------- | ------- | --- | -------- | --- | -------- | --- |
|     |     |     |     |     |     |     |     | sequentially    | passes                                   | through | the | vertices | on  | the path | ,   |
|     |     |     |     |     |     |     |     | finallyreaching |                                          | attime  | .   |          |     |          |     |
ThiscompletestheproofofTheorem3.1.
bythedefinition(A.5)
REFERENCES
Theorem A.3 tells us that at time , the message from to [1] S.M.Aji,“Graphicalmodelsanditerativedecoding,”Ph.D.dissertation,
Cal.Inst.Technol.,Pasadena,CA,1999.
istheappropriatelymarginalizedproductofasubsetofthe
[2] S.M.Aji,G.B.Horn,andR.J.McEliece,“Ontheconvergenceofit-
| local kernels, | viz., |     |     |     | ,   | and Corollary | A.4 |     |     |     |     |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
erativedecodingongraphswithasinglecycle,”inProc.32ndConf.
tells us that at time , the state of vertex is the appropri- InformationSciencesandSystems,Princeton,NJ,Mar.1998.
[3] S.M.Aji,G.B.Horn,R.J.McEliece,andM.Xu,“Iterativemin-sum
atelymarginalizedproductofasubsetofthelocalkernels,viz.,
decodingoftail-bitingcodes,”inProc.IEEEInformationTheoryWork-
,whichwethinkofasthesubsetoflocalker-
shop,Killarney,Ireland,June1998,pp.68–69.
nelswhichare“known”to attime .Giventheseresults,the [4] S.M.Aji,R.J.McEliece,andM.Xu,“Viterbi’salgorithmandmatrix
remainingproblemistounderstandhowknowledgeofthelocal multiplication,”inProc.33rdConf.InformationSciencesandSystems,
Baltimore,MD,Mar.1999.
kernelsisdisseminatedtotheverticesofthejunctiontreeunder
[5] L.R.Bahl,J.Cocke,F.Jelinek,andJ.Raviv,“Optimaldecodingoflinear
agivenschedule.Astudyof(A.5),whichgivestherelationship codesforminimizingsymbolerrorrate,”IEEETrans.Inform.Theory,
betweenwhatisknownat thevertex andwhatisknownby vol.IT-20,pp.284–287,Mar.1974.
|     |     |     |     |     |     |     |     | [6] L. E. | Baum and | T. Petrie, | “Statistical |     | inference | for probabilistic |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ---------- | ------------ | --- | --------- | ----------------- | --- |
theincomingedges,togetherwiththemessageupdaterulesin functionsoffinite-stateMarkovchains,”Ann.Math.Stat,vol.37,pp.
(A.3),providesanicerecursivedescriptionofexactlyhowthis 1559–1563,1966.
informationisdisseminated: [7] R.W.ChangandJ.C.Hancock,“Onreceiverstructuresforchannels
havingmemory,”IEEETrans.Inform.Theory,vol.IT-12,pp.463–468,
Oct.1966.
• Rule(1):Initially ,eachvertex knowsonlyits [8] J.W.CooleyandJ.W.Tukey,“Analgorithmforthemachinecalculation
ownlocalkernel . ofcomplexFourierseries,”Math.Comp.,vol.19,p.297,Apr.1965.
[9] T.H.Cormen,C.E.Leiserson,andR.L.Rivest,IntroductiontoAlgo-
| • Rule(2):Ifadirectededge |     |     |     |     | isactivatedattime |     |     | ,       |                                    |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | ------- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
|                           |     |     |     |     |                   |     |     | rithms. | Cambridge,MA:MIT–McGraw-Hill,1990. |     |     |     |     |     |     |
i.e., if , then vertex learns all the local [10] R.Dechter,“Bucketelimination:Aunifyingframeworkforprobabilistic
kernelspreviouslyknownto attime . inference,”ArtificialIntell.,vol.113,pp.41–85,1999.
|     |     |     |     |     |     |     |     | [11] G. D. | Forney Jr., | “The | Viterbi algorithm,” |     | Proc. IEEE, | vol. | 61, pp. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ---- | ------------------- | --- | ----------- | ---- | ------- |
268–278,Mar.1973.
WeshallnowusetheserulestoproveTheorem3.1.
[12] G.D.ForneyJr.,F.R.Kschischang,andB.Marcus,“Iterativedecoding
Theorem3.1assertsthat knowseachofthe localkernels of tail-biting trellises,” in IEEE Information Theory Workshop, San
Diego,CA,Feb.1998,pp.11–12.
|     | attime |     | ifandonlyifthereisapathinthe |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[13] B.J.Frey,“Bayesiannetworksforpatternclassification,datacompres-
| messagetrellisfrom |     |     | to  | ,forall |     |     |     | .   |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sion,andchannelcoding,”Ph.D.dissertation,Univ.Toronto,Toronto,
| We willnow | provethe |     | slightly | moregeneral |     | statement | that |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | -------- | ----------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
ON,Canada,1997.
[14] B.J.FreyandD.J.C.MacKay,“Arevolution:Beliefpropagationin
| knows | at time |     | if and | only | if there | is a path | in the |     |     |     |     |     |     |     |     |
| ----- | ------- | --- | ------ | ---- | -------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
graphswithcycles,”inAdvancesinNeuralInformationProcessingSys-
| messagetrellisfrom |          |          | to   | .       |       |     |     |                                              |     |     |     |     |     |               |     |
| ------------------ | -------- | -------- | ---- | ------- | ----- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- |
|                    |          |          |      |         |       |     |     | tems,M.I.Jordan,M.I.Kearns,andS.A.Solla,Eds. |     |     |     |     |     | Cambridge,MA: |     |
| To this            | end, let | us first | show | that if | knows |     | at  | ,                                            |     |     |     |     |     |               |     |
MITPress,1998,pp.470–485.
then there must be a path in the message trellis from to [15] R.G.Gallager,“Low-densityparity-checkcodes,”IRETrans.Inform.
Theory,vol.IT-8,pp.21–28,Jan.1962.
.Becauseweareinatree,thereisauniquepathfrom
|          |     |     |     |     |     |     |     | [16] ,Low-DensityParity-CheckCodes.                   |     |     |     | Cambridge,MA:MITPress, |     |     |          |
| -------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | ---------------------- | --- | --- | -------- |
| to , say |     |     |     |     |     |     |     | 1963.                                                 |     |     |     |                        |     |     |          |
|          |     |     |     |     |     |     |     | [17] R.C.GonzalezandR.E.Woods,DigitalImageProcessing. |     |     |     |                        |     |     | Reading, |
MA:Addison-Wesley,1992.
|     |     |     |     |     |     |     |     | [18] F. V. | Jensen, An | Introduction | to  | Bayesian | Networks. | New | York: |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ------------ | --- | -------- | --------- | --- | ----- |
Springer-Verlag,1996.
| where | and |     | . Denote |     | by  | the first | (smallest) |     |     |     |     |     |     |     |     |
| ----- | --- | --- | -------- | --- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
[19] F.V.JensenandF.Jensen,“Optimaljunctiontrees,”inProc.10thConf.
timeindexforwhich knows .ThenbyRule2andaneasy UncertaintyinArtificialIntelligence,R.L.deMantarasandD.Poole,
inductionargument,wehave Eds.SanFrancisco,CA,1994,pp.360–366.
[20] J.H.KimandJ.Pearl,“Acomputationalmodelforcausalanddiagnostic
reasoning,”inProc.8thInt.JointConf.ArtificialIntelligence,1983,pp.
|     |     |     |     |     |     |     | (A.6) | 190–193. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore.  Restrictions apply.

AJIANDMCELIECE:THEGENERALIZEDDISTRIBUTIVELAW 343
[21] F.R.KschischangandB.J.Frey,“Iterativedecodingofcompoundcodes [31] E.C.Posner,“Combinatorialstructuresinplanetaryreconnaissance,”in
byprobabilitypropagationingraphicalmodels,”IEEEJ.Select.Areas ErrorCorrectingCodes,H.B.Mann,Ed. NewYork:Wiley,1968.
Commun.,vol.16,pp.219–230,Feb.1998. [32] L.Rabiner,“AtutorialonhiddenMarkovmodelsandselectedapplica-
[22] S.L.LauritzenandF.V.Jensen,“Localcomputationwithvaluations tionsinspeechrecognition,”Proc.IEEE,vol.77,pp.257–285,1989.
from a commutative semigroup,” Ann. Math. AI, vol. 21, no. 1, pp. [33] G.R.ShaferandP.P.Shenoy,“Probabilitypropagation,”Ann.Math.
51–69,1997. Art.Intel.,vol.2,pp.327–352,1990.
[23] S.L.LauritzenandD.J.Spiegelhalter,“Localcomputationwithproba- [34] R.M.Tanner,“Arecursiveapproachtolowcomplexitycodes,”IEEE
bilitiesongraphicalstructuresandtheirapplicationtoexpertsystems,” Trans.Inform.Theory,vol.IT-27,pp.533–547,Sep.1981.
J.Roy.Statist.Soc.B,pp.157–224,1988. [35] G.Ungerboeck,“NonlinearequalizationofbinarysignalsinGaussian
[24] D.J.C.MacKayandR.M.Neal,“Goodcodesbasedonverysparsema- noise,”IEEETrans.Commun.Technol.,vol.COM-19,pp.1128–1137,
trices,”inCryptographyandCoding,5thIMAConf.,ser.SpringerLec- Dec.1971.
tureNotesinComputerScienceNo.1025. Berlin,Germany:Springer- [36] S.VerdúandV.Poor,“Abstractdynamicprogrammingmodelsunder
Verlag,1995,pp.100–111. commutativity conditions,” SIAM J. Contr. Optimiz., vol. 25, pp.
[25] , “Near Shannon limit performance of low density parity-check 990–1006,July1987.
codes,”Electron.Lett.,vol.33,pp.457–458,1996. [37] A.J.Viterbi,“Errorboundsforconvolutionalcodesandanasymptoti-
[26] P.L.McAdam,L.R.Welch,andC.L.Weber,“M.A.P.bitdecoding callyoptimumdecodingalgorithm,”IEEETrans.Inform.Theory,vol.
of convolutional codes,” in Proc. 1972 IEEE Int. Symp. Information IT-13,pp.260–269,Apr.1967.
Theory,Asilomar,CA,Jan.1972,p.91. [38] Y. Weiss, “Correctness of local probability propagation in graphical
[27] R.J.McEliece,R.B.Ash,andC.Ash,IntroductiontoDiscreteMathe- modelswithloops,”NeuralComput.,vol.12,pp.1–41,2000.
matics. NewYork:RandomHouse,1989. [39] N.Wiberg,“Codesanddecodingongeneralgraphs,”dissertationno.
[28] R.J.McEliece,D.J.C.MacKay,andJ.-F.Cheng,“Turbodecoding 440,LinkopingStudiesinScienceandTechnology,Linkoping,Sweden,
asaninstanceofPearl’sbeliefpropagationalgorithm,”IEEEJ.Select. 1996.
AreasComm.,vol.16,pp.140–152,Feb.1998. [40] M. Yannakakis, “Computing the minimum fill-in is NP-complete,”
[29] J.Pearl,ProbabilisticReasoninginIntelligentSystems. SanMateo, SIAMJ.Alg.Discr.Methods,vol.2,pp.77–79,1981.
CA:MorganKaufmann,1988. [41] F.R.Kschischang,B.J.Frey,andH.-A.Loeliger,“Factorgraphsand
[30] A.M.Poritz,“HiddenMarkovmodels:Aguidedtour,”inProc.1988 thesum-productalgorithm,”IEEETrans.Inform.Theory,submittedfor
IEEEConf.Acoustics,Speech,andSignalProcessing,vol.1,pp.7–13. publication.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on October 17,2025 at 12:05:34 UTC from IEEE Xplore. Restrictions apply.