Codes and Iterative Decoding on  General  Graphs

Niclas W i b e r g ,  H a n s - A n d r e a  i o e l i g e r .  a n d  Ralph K o t t e r
ISY, LinkbDing Un:vemty,  5-58183 hnkoping, Sweden

Keywords:

turbo  ( d e - ) c o d i n g ,   l o w - d e n s i t y   p a r i t y -
check  codes,  Tanner  graphs,  M a r k o v   random  fields,
“trellises”  w i t h  a g e n e r a l i z e d  “ t i m e ”   a x i s ,  g e n e r a l i z e d
V i t e r b i  and BCJR d e c o d i n g .

Tanner graph, there  is, in general, no unique minimal trellis.
(The simplest example are tail-biting trellises.)  Nevertheless,
bounds on the  “size” of  t h e  realization may be obtained from
the  (“abstract”) state spaces of  the code.

I. INTRODUCTION
Until  recently,  most  known decoding procedures for  error-
correcting codes were based either on algebraically  calculating
the error pattern or on some sort of  tree or trellis search.  With
the advent of  turbo coding [l], a third decoding principle has
finally  had its breakthrough:  iterative decoding.

(Iterative  decoding  is  not  a  new  idea,  though:

most  of
the key ideas were already present in Gallager’s work  on  low-
density parity-check  codes  [2] .)

With respect t o  Viterbi decoding, a code is  most naturally
described by  means  of  a trellis  diagram.  T h e  main  thesis  of
the present  paper is  t h a t ,  with  respect  t o  iterative decoding,
the natural way  of  describing a code is  by  means of  a Tanner
graph  [ 3 ] ,  which may be viewed as a generalized  trellis,  More
precisely,  it  is  t h e   “time axis”  of  a trellis  t h a t  is  generalized
t o  a Tanner graph.

Trellises  yield  Tanner  graphs  of  the  type shown  in  Fig.  1;

in  particular,  the  graph  has  no  cycles.  T h e   complexity  re-
duction  in  turbo  codes  (and  low-density  parity-check  codes:
and  many new  codes  t o   be  discovered)  comes  from  allowing
Tanner graphs with cycles,  cf.  Fig.  2.

11. DECODING
Both  Viterbi  decoding  and  BCJR  decoding  i4] are  easily
generalized  to arbitrary Tanner  graphs  without  cycles,  where
these  algorithms  are  still  optimal  (in  the  same  sense  as  for
trellises).  T h e  basic  idea  of  iterative  decoding  is  simpiy  t o
apply  these  algorithms  even  t o   Tanner  graphs  with  cycles,
ignoring  t h e  fact  t h a t  the  algorithms  are  no  longer  optimal.
T h e   empirical  success  of  turbo  coding  (as  well  as  our  own
experiments with other types of  codes)  confirm the validity  of
this approach.

Of  course, analytical understanding  of  the  decoder opera-
tion  is  also  desirable.  O u r  main  result  here  applies  t o   “cy-
cle  codes”  ( a  subclass of  low-density  parity-check  codes):  we
give a complete algebraic characterization of  all error patterns
t h a t  are corrected by  t h e  generalized  Viterbi  algorithm after
infinitely  many iterations.

111. REALIZATION THEORY O N   GENERAL GRAPHS
Much recent work was devoted t o  finding, and bounding the
size of, the %mallest” trellis for a given code.  This problem is
significantly generalized by considering general Tanner graphs.
In the traditional  setting, t h e  only degree of  freedom  (for
a given  code)  was  t h e   ordering  of  the  “time  axis”.  For  a
given  ordering,  every  linear  code  has  a  well-defined  unique
minimal trellis,  and every other trellis  for the same code  may
be  collapsed t o  t h e  minimal trellis  by  state merging.

In our more general setting, t h e  “time axis” need not be or-
dered, but may be an arbitrary Tanner graph. Even for a fixed

IV. A  PRIORI PROBABILITIES

Our  careful  derivation of  the  two basic  iterative decoding
aigorithms  clarifies, in particular,  what  a priori  distributions
are  admissible  and  how  they  are  properly  dealt  with.  As  it
turns  out, these  distributions  are  closely  related  t o   Markov
Random fields.

REFERENCES

Il]  C. Berrou, A .  Glavieux, and P. Thitimajshima, “Near Shannon

limit  error-correcting coding  and  decoding:  Turbo codes  (l),”
PTOC. ICC’93, Geneva, Switzerland, 1993, pp.  1064-1070.

[2]  R. G.  Gallager, “Low-density parity-check  codes,” IRE  Trans.

7nform. Theory, vol.  8, pp.  21-28,  Jan. 1962.

[3]  R. M. Tanner, “A recursive approach to low-complexity codes,”
IEEE  Trans. Inform. Theory, vol.  27, pp. 533-547,  Sept. 1981.
[4]  L.  R.  Bahl,  J. Cocke, F.  Jelinek,  and  J. Raviv,  “Optimal de-
coding of  linear codes for minimizing symbol error rate,”  IEEE
Trans. Inform.  Theory, vol.  20, pp.  284-287,  March  1974.

k y i

0

i

0

1

1

1

0

0

0

0

0

0

F i g u r e  1: A  trellis  ( t o p )  a n d  its T a n n e r  g r a p h   ( b o t t o m ) .

. . .

, ,

. .

interleaver

Figwe 2 :  The T a n n e r  graph of  t u r b o  coding  [I].

Authorized licensed use limited to: SHANDONG UNIVERSITY. Downloaded on July 23,2026 at 10:31:44 UTC from IEEE Xplore.  Restrictions apply.

468

