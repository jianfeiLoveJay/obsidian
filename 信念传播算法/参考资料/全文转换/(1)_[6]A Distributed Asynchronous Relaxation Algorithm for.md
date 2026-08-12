-
|     |     |     |     |     |     |     |     |     |     | FA10  |     |     | 10:30  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ------ | --- |
Proceedings of 24th  Conference
on Decision  and  Co.n trol
| Ft. Lauderdale, FL  |     | December 1985  |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A  DISTRIBUTED ASYSCHRONOURS  ELAXATION  ALGORITHlrI FOR  THE ASSIGhXEST PROBLEN
|     |     |     |     |                                      |     | Dimitri P.  | Bertsekas         |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------ | --- | ----------- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | MassachusettsI  nstituteo  fT        |     |             | echnology         |     |     |     |     |     |     |     |
|     |     |     |     | Laboratoryf  orI  nformationa  ndD   |     |             | ecisionS  ystems  |     |     |     |     |     |     |     |
|     |     |     |     | Cambridge,Y  assachusetts            |     |             | 02139 U.S.A.      |     |     |     |     |     |     |     |
Abstract  whilet  hep  ricesp  .a  nd"  profitm   argins"  i~~  given by
I
Relaxationn  ethodsf  oro  ptimaln  etworkf  lowp  rob-  (1) solvet  hed  ualp  roblem
|     |     |     |     |     |     |     |     | N   | N   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lems resemblec  lassicalc  oordinated  escent,J  acobi,  1  1
|     |     |     |     |     |     |     | minimize  |     |     | p.  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
andG   auss-Seidelm   ethodsf  ors  olvingu  nconstrainedn  on-  yi  t
|     |     |     |     |     |     |     |     | i=l  | j=1  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- |
linearo  ptimizationp  roblems  or systemso  fn  onlinear  J
| equations.I  nt  heirp  uref  ormt  heym   |     |                                              |                                | odifyt  hed  ual             |     |      |               |     |                                           |     |     |     |     |     |
| ------------------------------------------ | --- | -------------------------------------------- | ------------------------------ | ---------------------------- | --- | ---- | ------------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- |
| variables(  nodep  rices)o  nea  t         |     |                                              |                                | a  timeu  singo  nlyl  ocal  |     |      |               |     |                                           |     |     |     |     |     |
| nodei  nformationw                         |     | hilea  imingt  oi  mprovet  hed  ualc  ost.  |                                |                              |     |      |               |     |                                           |     |     |     |     |     |
| They are  particularly                     |     |                                              | well suited  for  distributed  |                              |     | im-  |               |     |                                           |     |     |     |     |     |
|                                            |     |                                              |                                |                              |     |      | Consider now  |     | thef  ollowingp  rocessf  ora  uctioning  |     |     |     |     |     |
plementation  on massivelyp  arallelm   achine.F  orp  rob-  theo  bjects.  arbitraryi  nitialp  rice  p. is given
An
lems withs  trictlyc  onvexa  rcc  ostst  heyc  anb  e  shown  I
toe  acho  bject.F  urthermorei  nitiallye  ithern  oo  b-
| toc  onvergee  ven        |     | if relaxationa  te  achn  ode  |                                       |     | is carried  |     |                                      |     |                            |             |       |                      |             |     |
| ------------------------- | --- | ------------------------------ | ------------------------------------- | --- | ----------- | --- | ------------------------------------ | --- | -------------------------- | ----------- | ----- | -------------------- | ----------- | --- |
|                           |     |                                |                                       |     |             |     | jectsa  rea  ssigned,                |     | or else fore  achp  erson  |             |       |                      | i assigned  |     |
| Outa  synchronouslyw      |     |                                | itho  ut-of-datep  ricei  nformation  |     |             |     |                                      |     |                            |             |       |                      |             |     |
|                           |     |                                |                                       |     |             |     | toa  no  bject                       | j   | equation                   | (1) holds.  |       | Thep  rocessp  ro-   |             |     |
| fromn  eighboringn  odes  |     |                                | [I].                                  |     |             |     |                                      | i   |                            |             |       |                      |             |     |
|                           |     |                                |                                       |     |             |     | ceedsi  terativelya  ndt  erminates  |     |                            |             | when  | therea  ren  oo  b-  |             |     |
Forp  roblemsw   ithl  ineara  rcc  ostsr  elaxation  jectsl  eftu  nassigned.  At theb  eginningo  fe  ach  iter-
methodsh  aveo  utperformedb  y  a substantialm   argint  he  atione  achp  erson  knows  thep  ricep  .o  fe  acho  bject
classicalp  rimals  implexa  ndp  rimal-dualm   ethods  on  I
|                                |     |     |     |             |          |            | andw  hetherh  e  |     | is assignedt  oa  no  bject.T  herea  re  |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ----------- | -------- | ---------- | ----------------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- |
| standardb  enchmarkp  roblems  |     |     |     | [2],  [3].  | However  | int  hese  |                   |     |                                           |     |     |     |     |     |
twop  hasesi  ne  achi  teration;t  heb  iddingp  hase,a  nd
| particularm   | ethods  |     | it is necessaryt  oc  hanges  ometimes  |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | ------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thea  ssignmentp  hased  escribedb  elow:
| thep  riceso  fs  everaln  odesa  s                  |     |     |     | a groupi  na  dditiont  o  |           |       |                                            |     |     |     |     |                  |     |     |
| ---------------------------------------------------- | --- | --- | --- | -------------------------- | --------- | ----- | ------------------------------------------ | --- | --- | --- | --- | ---------------- | --- | --- |
| carryingo  utp  urer  elaxations  teps.              |     |     |     | As                         | a result  |       |                                            |     |     |     |     |                  |     |     |
|                                                      |     |     |     |                            |           |       | BiddingP  hase:E  achu  nassignedp  erson  |     |     |     |     | i computest  he  |     |     |
| globaln  odep  ricei  nformation                     |     |     |     | is neededo  ccasionally,   |           |       |                                            |     |     |     |     |                  |     |     |
|                                                      |     |     |     |                            |           |       | "currentc  ost"o  fo  bject                |     |     | j   |     |                  |     |     |
| andd  istributedi  mplementatimmb  ecomess  omewhat  |     |     |     |                            |           | com-  |                                            |     |     |     |     |                  |     |     |
plicated.
|     |             |       |                                        |     |     |     | c..  =  | p.-a.,  |     |     |     |     |     | (3)  |
| --- | ----------- | ----- | -------------------------------------- | --- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- | ---- |
|     |             |       |                                        |     |     |     | 11      | 2  11'  |     |     |     |     |     |      |
|     | Int  hisp   | aper  | we  descrije a distributeda  lgorithm  |     |     |     |         |         |     |     |     |     |     |      |
fors  olvingt  hec  lassicall  inearc  osta  ssignmentp  rob-  andf  inds  a  "best"o  bjectj  *h  aving  minimum cost
lem.  It employse  xclusivelyp  urer  elaxations  teps
wherebyt  hep  riceso  fs  ourcesa  nds  inksa  rec  hanged  c. .  =  min  c. .,
|                  |     |                                          |     |     |     |     | 13*   | 11  |     |     |     |     |     |     |
| ---------------- | --- | ---------------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
| individually on  |     | theb  asiso  fo  nlyl  ocal(  neighbor)  |     |     |     |     |       | j   |     |     |     |     |     |     |
nodep  ricei  nformation.  The algorithmc  anb  ei  mple-  7
mented  ina  na  synchronous(  chaotic)m   anner,a  nds  eems  and a  "secondb  est"o  bject  satisfying
| quitee  fficientf  orp  roblemsw   |                                          |     |     | ith  a small arcc  ost  |        |     |       |             |      |     |     |     |     |     |
| ---------------------------------- | ---------------------------------------- | --- | --- | ----------------------- | ------ | --- | ----- | ----------- | ---- | --- | --- | --- | --- | --- |
|                                    |                                          |     |     |                         |        |     | c.:   | m in   c .  | . .  |     |     |     |     |     |
| range.                             | It hasa  ni  nterestingi  nterpretation  |     |     |                         | as an  |     | =     |             |      |     |     |     |     |     |
|                                    |                                          |     |     |                         |        |     | 1 J   | j+ j *  1   | 1    |     |     |     |     |     |
auctionw   heree  conomica  gentsc  ompetef  orr  esources
bym   akings  uccessivelyh  igherb  ids.
|     |     |     |     |     |     |     | Person i thenb  ids  |     | up  | thep   riceo   | f   | j* bya  ni  ncrement  |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | -------------- | --- | --------------------- | --- | --- |
 -
|     |                       |                 |     |                         |        |        | ri between             | E and  | (c . 7                                 | cij*)  | t E,  | where E  | is a  | pos-  |
| --- | --------------------- | --------------- | --- | ----------------------- | ------ | ------ | ---------------------- | ------ | -------------------------------------- | ------ | ----- | -------- | ----- | ----- |
|     | 1.                    | Assignmenbt  y  |     | Means  of  anA  uction  |        |        |                        |        | 1 3                                    |        |       |          |       |       |
|     |                       |                 |     |                         |        |        | itivec  onstantt  hat  |        | is fixedt  hroughoutt  hea  lgorithm.  |        |       |          |       |       |
|     | Consider N personsw   |                 |     | ishlngt  od   ivide     | among  | them-  |                        |        |                                        |        |       |          |       |       |
The bid
| selves N objects bym        |      |                 | eanso  fa  na  uction-likep  rocess.  |                                 |     |     |     |     |     |     |     |     |     |     |
| --------------------------- | ---- | --------------- | ------------------------------------- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Int  hee  nde  acho  bject  |      |                 | j                                     | wili bea  ssignedt  oe  xactly  |     |     |     |     |     |     |     |     |     |     |
| onep  erson                 | who  | will thenp  ay  |                                       | a pricep   .(  yett  ob         | e   |     |     |     |     |     |     |     |     |     |
I
determined)  for thato  bject.T  here  is a fixedv  alue  is communicated  toa  na  uctioneer.(  Thisc  hoice  of r
a..t  hatp   erson  i associatesw   itho  bject  j  ande  ach  guarantees  that,  if theb  id  is accepted,o  bject  j*  i
1 1
pe r s on i wishest  om   aximizet  heb  enefita  .-  p.f  rom  uill  be  at  most  within  E  ofb   eingb   est.)
l j   J
beinga  ssignedt  oo  bject  j.  Basedo  n  thisf  act  a  For eacho  bjectj  :  If there was
|     |     |     |     |     |     |     | AssignmenPt  hase:  |     |     |     |     |     |     | a   |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
satisfactorya  ssignment  will result if the  final  prices  bidf  oro   bject  j  its price is raisedt  ot  heh   ighest
| pj,a  nd,t  heo  bject  |     |     | j. assignedt  op  erson  |     | i, are such  |     | bid  |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ------------------------ | --- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
that for all i
andt  he  new price is anounced toa  llp  ersons.F  urther-
|                                         |                             |     |     |                             |     |     | more a person i* that made  |     |        | theh        | ighestb                       | id  | is assigned  |     |
| --------------------------------------- | --------------------------- | --- | --- | --------------------------- | --- | --- | --------------------------- | --- | ------ | ----------- | ----------------------------- | --- | ------------ | --- |
| By  usingl  inearp  rogrammingt  heory  |                             |     |     | it is possiblet  o          |     |     |                             |     |        |             |                               |     |              |     |
|                                         |                             |     |     |                             |     |     | tot  heo  bject.P  erson    |     |        | i* as well  | ast  hep  ersonp  re-         |     |              |     |
| show                                    | thats  ucha  na  ssignment  |     |     | is optimali  nt  hes  ense  |     |     |                             |     |        |             |                               |     |              |     |
|                                         |                             |     |     |                             |     |     | viouslya  ssignedt  oo      |     | bject  | j           | (ifa  ny)a  rei  nformedo  f  |     |              |     |
N
|            |      |                   |     |                            |     |     | the new assignment.            |     |     | If there was  | nob  idf  oro  bject  |     |     | j   |
| ---------- | ---- | ----------------- | --- | -------------------------- | --- | --- | ------------------------------ | --- | --- | ------------- | --------------------- | --- | --- | --- |
| thaat  ..  |      | is maximao lv er  |     | all possiblae s signments  |     |     |                                |     |     |               |                       |     |     |     |
| i=l        | 'Ji  |                   |     |                            |     |     | its price is leftu  nchanged.  |     |     |               |                       |     |     |     |
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on July 23,2026 at 10:28:13 UTC from IEEE Xplore.  Restrictions apply.
|     |     |     |     |     |     |     | 1703  |     | CH2245-9/85/0000-1703 $1.00 C 1985 IEEE  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |

a)  unassigned person will  bid for some object
|     | 2.  Properties of the  Algorithm  |     |     | An  |
| --- | --------------------------------- | --- | --- | --- |
within finite time, and  cannot  bid twice (i.e.  cannot
bid for a second object while ,waiting  for a reply
A  more detailed analysis of the  algorithm  mayb e
regardin g the  disposition of an earlier bid for another
| found  in  the  unpublished report [4].  |     |     | The following may  | .   |
| ---------------------------------------- | --- | --- | ------------------ | --- |
| be shown:                                |     |     | object)            |     |
a)  The  algorithm  terminates with an  assignment which  b)  Whenever one or more  bids are received that raise
is within (N-~)E of being optimal.  Therefore if  v*-   the price of an object then, within finite time, that
|                | x                                        |     | price must be updated, and its value must be communi-    |     |
| -------------- | ---------------------------------------- | --- | -------------------------------------------------------- | --- |
|                | 1                                        |     | cated (not necessarily simultaneously)  to all persons.  |     |
| is  the value  | a..  ofa n  optimal  assignment  and  v  |     |                                                          |     |
i=l  '1  Furthermore the new bidder assigned to the object must
be informed of this fact simultaneously with receiving
is  the value of the best nonoptimal assignment, the
the new price.
algorithm  terminates with an optimal  assignment pro-
vided
 ..
References
-v*-v
O < E <
N-1  (8)  [l]  Bertsekas, D.  P.  and El Baz, D., "Distributed
*
are integer a value E < -1    Asynchronous Relaxation Methods for Convex Net-
In particular, if all a.
Ij  N- 1  work Flow Problems",  LIDS  Report P-1417, M.I.T.,
suffices  to  guarantee that an  optimal assignment will  Oct. 1984.
| be found.    | The proof of termination  is  based on con-  |     |     |     |
| ------------ | -------------------------------------------- | --- | --- | --- |
| tradiction.  | If the  algorithm were to  continue indef-   |     |     |     |
[2]  Bertsekas, D.  P., "A  Unified  Framework for Primal-
initely, then  the prices of some of the objects would
Dual Methods in Minimum Cost  Network Flow Problems",
be  increased  to  infinity  throughs uccessive bidding.
blath. Progr., Vol. 32, 1985, pp. 125-145.
Meanwhile all  unassigned objects would  still be at
their starting price and  therefore at some point would  [x]  Bertsekas, D. P., and Tseng, P., "Relaxation
become more attractive than  the  objects  being  bidded  Methods for Minimum Cost Network Flow Problems",
on.  The proof of the bound (8) is  based on the fact  LIDS Report P-1339, M.I.T., Oct. 1983.
that  at  termination  the  prices  p  and  thep rofit
| margins  |     | j   |     |     |
| -------- | --- | --- | --- | --- |
[4]  Bertsekas, D.P  .,  Distributed Algorithm for
the Assignment Problem'', Unpublished  LIDS Report,
Ti  =  max {a. .-p.}
|     | 11  1  |     |     | M.I.T., March 1979.  |
| --- | ------ | --- | --- | -------------------- |
j
[SI  Bertsekas, D.  P., "Distributed Asvnchronous Com-
satisfy  complementary slackness within E.  This can be  putation of  Fixed  Points",  Math.b rogr., Vol. 27,
translated  after some calculation into the  bound (8).  1983, pp. 107-120.
| b)  The total number of arithmetic  operations needed  |     |     | -   |     |
| ------------------------------------------------------ | --- | --- | --- | --- |
Note:  This research  was  supported  by  the  National
|     |     | 1 .   | 3   |     |
| --- | --- | ----- | --- | --- |
for  termination  with E =  1 s  bounded  by O(bN  )  where  Science Foundation under Grant NSF-ECS-8217668.
| b  =  max a.  | - min a        | a   | . integer.  |     |
| ------------- | -------------- | --- | ----------- | --- |
|               | lj  i,j  ij '  | ij  |             |     |
| i,j           |                |     | '           |     |
The  algorithm  isn ot polynomial, since  examples
can  be  constructed showing that  the  bound O(bN3)  is
sharp.  However if b is small as for example in the
| pure matching problem (a.  |     | =  1 or a  | =  0) the com-  |     |
| -------------------------- | --- | ---------- | --------------- | --- |
1j  ij
plexity is satisfactory. Limited  computational exper-
imentation shows that  the  algorithm  performs  very  well
for small values of  b,b ut can also work  very poorly
when  b  is  large. There is no theoretical or experi-
mental estimate of the  potential speedup of the algo-
| rithm through parallelism.  |     | It is also  unclear whether  |     |     |
| --------------------------- | --- | ---------------------------- | --- | --- |
the  algorithm  will  compare  favorablwyi th distributed
versions of the Hungarian method or the relaxation
method  for  the  assignmentp roblem.
3.  Asynchronous Implementation
The auction algorithm given in Section 1 may be
described  as  synchronous since communication of all
relevant information follows all updating that takes
place in either the  bidding or the  assignment phases.
Furthermore bidding  and  assignment  are  carried  out
simultaneously for all persons and objects respective-
| ly.  asynchroRous  algorithm  (see  |     |     | [5] for a  general  |     |
| ----------------------------------- | --- | --- | ------------------- | --- |
An
model) results if each unassigned person makes  a  bid
at arbitrary  times on the  basis of object price infor-
mation that may be out dated  (because of additional
bidding of which the person is not informed).  Further-
more assignment of objects may be decided even if some
| potential bidders have not been  heard from.  |     |     | We can  |     |
| --------------------------------------------- | --- | --- | ------- | --- |
similarly show the  same termination properties as  for
the synchronous version of the  algorithm subject to
two  conditions.
Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on July 23,2026 at 10:28:13 UTC from IEEE Xplore.  Restrictions apply.
1704