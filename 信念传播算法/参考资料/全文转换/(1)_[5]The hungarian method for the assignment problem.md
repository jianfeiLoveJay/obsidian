THE HUNGARIAN METHOD FOR THE ASSIGNMENT PROBLEM'
H. W. Kuhn
Bryn Yaw College
Assuming that numerical scores are available for the perform-
ance of each of n persons on each of n jobs, the "assignment problem"
is the quest for an assignment of persons to jobs so that the sum of the
n scores so obtained is as large as possible. It is shown that ideas latent
in the work of two Hungarian mathematicians may be exploited to yield
a new method of solving this problem.
1. INTRODUCTION
Stated informally, the problem of personnel-assignment asks for the best assignment of
a set of persons to a set of jobs, where the possible assignments are ranked by the total scores
or ratings of the workers in the jobs to which they are assigned. Variations of this problem,
both mathematical and non-mathematical, have a long history (see the Bibliography appended).
However, recent interest in the question, when posed in the terms of linear programming,
seems to stem from the independent work of Flood, J. Robinson, Votaw, and Orden. Flood's
work [ 121, begun in 1949, regards the problem as the most "degenerate" case of the transpor-
tation problem. Robinson regarded it as a relative of the travelling salesman problem; her
work is available only in the form of RAND Corporation memoranda. The problem was dis-
cussed from various points of view in the work of Votaw and Orden (see [ 91 ) presented to the
SCOOP Symposium on Linear Inequalities and Programming, June 14-16, 1951. The compu-
tational advantages to be gained by considering the problem in combination with the dual linear
program have been stressed by Dantzig, von Neumann and others (see [a], [lo], and [12]) . The
purpose of this paper is to develop a computational method that uses this duality in a particu-
larly effective manner. One interesting aspect of the algorithm is the fact that it is latent in
work of D. Kanig and E. Egervby that predates the birth of linear programming by more than
15 years (hence the name, the "Hungarian Method").
The theoretical basis of the algorithm is laid in Sections 2 and 3. Section 2 (which is
derived from the proof of Kbnig in "Theorie der Graphen" (1936) Chelsea, 1950, pp. 232-233)
treats the problem of assignment when there are but two ratings, 1 and 0, indicating that a
worker is qualified or not. Section 3 (which is derived from the work of Egervhry in [3]) shows
that the general problem of assignment can be reduced to this special case by a procedure that
is computationally trivial.
The algorithm is given an independent (and self-contained) statement in Section 4 and
Section 5 is devoted to a detailed example to illustrate its application.
2. THE SIMPLE ASSIGNMENT PROBLEM
The problem of Simple Assignment is illustrated by the following miniature example:
Four individuals (denoted by i = 1, 2, 3, 4) are available for four -jobs (denoted by j = 1,
2, 3, 4). They qualify as follows:
lThe preparation of this report was supported, in part, by the ONR Logistics Project,
Department of Mathematics, Princeton University.
a3

84 THE HUNGARIAN METHOD FOR THE ASSIGNMENT PROBLEM
1, 2, and 3
3 and 4
This information can be presented effectively by a qualification matrix
in which horizontal rows stand for individuals and vertical columns for jobs; a qualified individ-
ual is marked by a 1 and an unqualified individual by a 0. Then the Simple Assignment Prob-
lem asks:
What is the largest number of jobs that can be assigned to qualified
individuals (with not more than one job assigned to each individual)?
This may be stated abstractly in terms of the matrix Q:
What is the largest number of 1's that can be chosen from Q with
no two chosen from the same row or column?
It is clear that we can start an assignment by placing unassigned individuals in any unassigned
jobs for which they qualify. Thus, we might assign individuals 1 and 2 to jobs 3 and 4, respec-
tively; this information is entered in the matrix below by asterisks.
[a
1 1 l * O
i ; i.J
Since it is impossible to improve this assignment by placing an unassigned individual in an
unassigned job for which he qualifies, this assignment is said to be complete. If an assignment
is complete, it is natural to attempt an improvement by means of a tranefer. For instance, the
transfer:
Move individual 1 from job 3 to job 1
11 2 4 3 ,
" 'I
results in the following incomplete assignment:
'j
i ;*
[;*
0 0 0 1 .
Here we may assign either individual 3 or 4 to job 4 to complete the assignment. Either result,
say
:g
1 * 1 1 0
i 8';+
is optimal, since there all qualified pairs involve either individual 1 or job 3 or job 4, and
hence four assignments would involve one of these twice. Thus, although there is a transfer

H. W. KUHN 85
possible in this optimal assignment (move 1 from job 1 to job 2), it leads to a complete assign-
ment. The discussion to follow establishes that this situation holds in general, namely, that
one can always construct an optimal assignment by a successsion of transfers followed by
additional assignments until this is no longer possible.
Suppose n individuals (i = 1, . . . , n) are available for n -jobs ( 1 = 1, . . . , n) and that a
qualification matrix Q = (4. ) is given, where qil = 1 if individual i qualifies for job j and
11
9.. = 0 otherwise. If an assignment (not necessarily optimal) of certain qualified individuals to
13
jobs is given, then the easiest way to improve it is to assign any unassigned individual to an
unassigned job for which he qualifies. If this is possible, the given assignment is said to be
incomplete; otherwise, it is complete. If the assignment is complete, then it is reasonable to
attempt an improvement by means of a transfer. A transfer changes the assignment of r
distinct individuals il, . . . , ir employed in jobs j,, . . . , 1,. It moves il into an unassigned job
jo and ik into job jk-l for k = 2, . . . , r. All of the new assignments (ik to jk-l) are assumed to
. . . ,
be qualified for k = 1, r. It is convenient to call the result of leaving all assignments
unchanged a transfer also. A useful notation for transfers that change some assignment is
We shall call every (assigned) individual involved in such a transfer an essential individual and
every job assigned to an inessential individual an essential job. Thus:
LEMMA 1. For a given assignment, if an individual is assigned
to a job, then either the individual or the job is essential, and not both.
COROLLARY 1. For all assignments, the number of individuals
assigned to jobs equals the number of essential individuals and jobs.
The motivation of the definition of essentiality is partially explained by the next two lemmas.
LEMMA 2. For a given assignment, if an individual is assigned
to a job and qualifies for another, unassigned, job then the individual is
essential.
PROOF: The transfer of the individual to the unassigned job establishes him as
essential.
LEMMA 3. For a given assignment, if every transfer leaves a
job assigned then the job is essential.
PROOF. Assume the job j to be inessential. Then some individual ik is assigned to it
and involved in a transfer that moves il, i2, . . . , ik in order. Symbolically,
and j is unassigned. This proves the lemma.

86 THE HUNGARIAN METHOD FOR THE ASSIGNMENT PROBLEM
These lemmas, in combination, establish the key result:
THEOREM 1. For a given assignment, if every transfer leads to
a complete assignment then, for every individual qualified for a job, either
the individual or the job is essential, and possibly both.
PROOF. Let individual i be qualified for job j. If i is assigned to j then Lemma 1
asserts that one or the other is essential. If i is assigned to another job then j is unassigned
and Lemma 2 asserts that the individual i is essential. If i is unassigned then every transfer
leaves j assigned (otherwise the assignment is incomplete) and Lemma 3 asserts that j is
essential. This proves the theorem.
Starting with any assignment (say, of one individual to a job for which he is qualified),
either every transfer leads to a complete assignment or at least one more individual can be
assigned after some transfer. Since at most n individuals can be assigned, this proves:
THEOREM 2. There is an assignment which is complete after
every possible transfer.
The problem will now be viewed from another, dual, aspect. Consider a possible budget
to account for the value of an individual assigned to a job for which he is qualifed. Such a
budget will allot either one unit or nothing to each individual and to each job. A budget is said
to be adequate if, for every individual qualified for a job, either the individual or the job is
allotted one unit, and possibly both.
THEOREM 3. The total allotment of any adequate budget is not
less than the largest number of jobs that can be assigned to qualified
individuals.
PROOF. If the part of the adequate budget allotted to jobs assigned in an optimal assign-
ment is counted, it is seen to be not less than the number of jobs assigned because these jobs
are all assigned to qualified individuals. Since the total budget is not less than this amount, this
proves the theorem.
Consider any assignment that is complete after every possible transfer (by Theorem 2,
there are such) and consider the budget that allots one unit to each essential individual or job
and zero otherwise. Theorem 1 asserts that this budget is adequate. Taking account of Corol-
lary 1, we have proved:
THEOREM 4. There is an adequate budget and an assignment
such that the total allotment of the budget equals the number of jobs
assigned to qualified individuals.
Since Theorem 3 implies that the assignment of Theorem 4 is optimal, we have provided
the following answer to the Simple Assignment Problem:

H. W. KUHN 87
The largest number of jobs that can be assigned to qualified
individuals is equal to the smallest total allotment of any adequate
budget. Any assignment is optimal if and only if it is complete after
every possible transfer.
3. THE GENERAL ASSIGNMENT PROBLEM
Suppose n individuals (i = 1, . .. , n) are available for n jobs (I = 1, . . . , n) and that a
rating matrix R = (r ) is given, where the r are positive integers, for all i and j. An assign-
il ij
-ment c onsists of the choice of one job ji for each individual i such that no job is assigned to
two different men. Thus, all of the jobs are assigned and an assignment is a permutation
(:1 : : :
" )
2 ; jn
. . . ,
of the integers 1, 2, n. The General Assignment Problem asks:
For which assignments is the Bum
rljl + r2j2+ . . . + r
"4
of the ratings largest?
The dual problem considers adequate budgets, that is, allotments of non-negative
integral amounts of u. to each individual and v to each job in such a manner that the sum of
'ith
th
the allotments to the individual and the j job is not less than his rating in that job. In
symbols,
+
- -
(i, j = 1, ., n).
"J rij
The problem dual to the General Assignment Problem is then:
What is the smallest total allotment
ul+. . . + Un+V1 +. , . n'
+
possible for an adequate budget?
The following analogue of Theorem 3 is immediate.
THEOREM 5. The total allotment of any adequate budget is
not less than the rating sum of any assignment.
PROOF. Since each individual and job occurs exactly once in an assignment the sum of
the allotments to individuals and jobs in an assignment is exactly the total allotment. However,
the budget is adequate and therefore this is not less than the sum of the rating8 of the individ-
uals in their assigned jobs. In symbols,
.
ul+v 1 1 2 rljl,. . , un+v j n= > r "1,
by the condition that the budget is adequate. Adding these inequalities, we have

| 88  | THE HUNGARIAN METHOD FOR  |     | THE ASSIGNMENT PROBLEM  |     |     |     |
| --- | ------------------------- | --- | ----------------------- | --- | --- | --- |
-
|     |      | ...+     | +...+ v jn2 rljl +  | . . .  |     |     |
| --- | ---- | -------- | ------------------- | ------ | --- | --- |
|     | U1+  | U n+V 4  |                     | t      |     |     |
"In
. . . ,
| However, the integers jl,  |     | jn appearing in the assignment  |     |     |     |     |
| -------------------------- | --- | ------------------------------- | --- | --- | --- | --- |
. . . , n and the theorem is proved.
| are merely an arrangement of  |     | 1,  |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- |
It is an immediate consequence of  this theory that, if an adequate budget and an assign-
ment can be exhibited such that the total allotment equals the rating sum, then they must be
simultaneously a solution of the assignment problem and its dual.  We shall now show that this
is always possible and can be achieved by solving certain, related, Simple Assignment Problems.
Associate with each adequate budget for the rating matrix R = (r  ) a Simple Assignment
il
Problem by the following rule:
The individual i is qualified for the job j  if ui + v. = r.:  otherwise,
I  11,
he is not qualified.
We see immediately that:
THEOREM  6.  If  all n individuals can be assigned to jobs for which
they are qualified in the Simple Assignment Problem associated with an
adequate budget, then the assignment and the budget solve the given General
Assignment Problem and the rating sum equals the total allotment.
| PROCF.  | For the given budget and assignment, we have  |     |     |     |     |     |
| ------- | --------------------------------------------- | --- | --- | --- | --- | --- |
, . . . , un+v
|     |     | u1 + vjl= rljl  |     | = r   .  |     |     |
| --- | --- | --------------- | --- | -------- | --- | --- |
1,
njn
Adding these equations,
|     |     |                | . . + vn= rlil +  | . . .  |     |     |
| --- | --- | -------------- | ----------------- | ------ | --- | --- |
|     |     | u 1 + .  . .+  |                   | + r    |     |     |
Un+V1+.
"Jn
and t$is proves the theorem.
If  not all individuals can be assigned to jobs for which they are qualified in the Simple
Assignment Problem associated with an adequate budget, then the budget can be improved by a
simple procedure.  Before this procedure can be described, it must be noted that an adequate
budget must allot either a positive amount to every individual or a positive amount to every job
since otherwise it would not be enough for the positive rating of  some individual in some job.
We shall assume, without loss of  generality since rows and columns enter symmetrically, that
every individual is allotted a positive amount; in symbols
. . . ,
0
|     |     |     | Ui'  |     | (i= 1,  | n).  |
| --- | --- | --- | ---- | --- | ------- | ---- |
Assume that the largest number of individuals that can be assigned to jobs for which they are
. . ,r
qualified is m  n.  Choose an optimal assignment and let the essential individuals be i= 1,.

H. W. KUHN 89
and the essential jobs be j = 1, . . . , s (possibly renumbering individuals and jobs). Corollary
1 asserts that
r+ s = m .
Then the rule for changing the budget is:
Ui = ul, ...) u ; = ur, u;+1= Ur+l - 1, ..., U; = un - 1
vi =v1+ 1, ..., V;=V; + 1, V's +l= vs+l, . . ., v' n = v n '
(The u; are still non-negative because the ui were positive integers.) We must check that
(a) the new budget is adequate, and
(b) the total allotment has been decreased.
The adequacy is checked by inequalities (1) which can only fail where ui has been decreased and
v has been left unchanged. But this means that both the individual i and the job j are ines-
1
sential. Theorem 1 then asserts that individual i is not qualified for job j and hence
by the rule for constructing the associated Simple Assignment Problem. Since all the numbers
involved are integers,
u; + v; = (ui - 1) + vj = (ui + vl. ) - 12 rij
and the new budget is adequate.
The total allotment has been decreased by n - r and increased by 6, thus has been
decreased by n - (r + s) = n - m > 0. Summarizing:
THEOREM 7. If at most m < n individuals can be assigned to jobs
for which they are qualified in the Simple Assignment Problem associated
with an adequate budget, then the total allotment of the budget can be
decreased by a positive integral amount.
Starting with any adequate budget (say, that which allots to every individual his highest
rating and nothing to the jobs), either it is optimal, and Theorem 6 applies, or it can be de-
creased by Theorem 7. Since it can be improved at most a finite number of times, we have
provided the following answer to the General Assignment Problem:
The largest possible rating sum for any assignment is equal to
the smallest total allotment of any adequate budget. It can be found by
solving a finite sequence of associated Simple Assignment Problems.
4. THE HUNGARIAN METHOD
In this section we shall assemble the results of the two preceding sections, abstracted
from the context of actual assignments, and state explicitly the algorithm implicit in the

90 THE HUNGARIAN METHOD FOR THE ASSIGNMENT PROBLEM
arguments of those sections. In certain cases where it seems advisable to use a different
terminology, the discrepancy will be noted parenthetically.
As considered in this paper, the General Assignment Problems asks: Given an n by n
matrix R = (r ) of positive integers, find the permutation jl, . . . , jn of the integers 1, . . . , n
il
that maximizes the sum r + . . . + r . It is well known (see references [3] and [lo] in the
lj1 "jn
Bibliography) that the linear program dual to this problem can be stated: Find non-negative
integers ul, . . . , un and vl,. . . , vn subject to
(i, j = 1, . . . , n)
that minimize the sum u1 + . . . + un + v1 + , . . + vn. A set of non-negative integers satisfying
(1) will be called a cover (or an adequate budget) and the positions (i, j) in the matrix for which
equality holds are said to be marked (or qualified in the associated Simple Assignment Prob-
lem); otherwise (i, j) is said to be blank. A set of marks is called independent if no two marks
from the set lie in the same line (the term "line" is used here to denote either a row or column).
Then a fundamental result of Kdnig says: If the largest number of independent marks that can
be chosen is m then m lines can be chosen that contain all of the marked positions. (This is
precisely the conclusion of Section 1 with "jobs assigned to qualified individuals" playing the
r61e of "independent marks.")
The algorithm to be described in this report is based on these remarks in the following
manner. If a cover for R is given, a largest set of independent marks is found; if this set
contains n marks then obviously the marked (i, j) cgnstitute the desired assignment (Theorem
6). If the set contains less than n marks then a set of less than n lines containing all of the
marked (i, j) is used to improve the cover (Theorem 7).
The construction of an initial cover and an initial set of independent marks can be made
quite conveniently as follows:
Let ai = max r for i = 1, . . . , n and b = miax rij for j = 1, . . . , n. Further let
ij
1
a = C a and b = C b
i i 1 J'
. . ,
ui =ai for i = 1 ,. n
If a 2 b define
...,
vj=O for j = l , n .
c
ui =O for i =1 ,. . . , n
If a > b define . . ,
vj =bj for j = 1,. n .
At this stage, as at all subsequent stages, there is associated with the matrix R and the
cover {ui, v }a matrix Q = (q ) where
1 il
+
vf = rij
0 otherwise.
At each stage we shall also need a set of independent 1's from Q which will be distinguished
by asterisks. To provide such a set at the first stage, in the first case (a2 b) the rows are

H. W. KUHN 91
examined in order and the first 1 in each row without a 1* in its column is changed to a l*.In
the second case (a > b), the same instructions are followed with rows and columns exchanging
r6h.
The two basic routines of the algorithm will be called Routine I and Routine II. A
schematic description of the order of their repetition is given in Figure 1.
Prob 1e m
p lI q
7 4
Routine I
1Ia
Ib
RRoouuttiinnee II11
Solut ion
Figure 1
Overy occurrenc of Ia will increase the number of assignment (i.e., of asterisks in Q) by one
and every Occurrence of IIa will decrease the current covering sum (C ui + C v ) by at least
1
i 1
one. Since the number of assignments is bounded from above by n and the covering sums are
bounded from below by zero, this insures the termination of the combined algorithm.
Routine I
Routine I works with a fixed matrix Q associated with a fixed cover { ui, vj}* The input
also includes a certain set of asterisks marking 1's in Q.
The computation begins with the search of each column of Q in turn for a 1*. If a l*i s
found, we proceed to the next column (no columns left = Alternative Ib). If a 1* is -not found in
the column, then the column is called eligible and is searched for a 1. If a 1 is not found, we
proceed to the next column (no columns left = Alternative Ib). If a 1 is found in (il, jo), we
record il and jo and start a process that constructs a sequence of the following form:
. . . . . . . . .
The routine then divides into two cases according to the parity of the number of terms currently
in the sequence. In Case 1, we have just found a 1 in (ik, jk-1) and have recorded ik and jk-l.
We then search the row ik for a l*.If a 1* is not found then we change each 1 in the sequence
to 1* and each 1* in the sequence (if any) to a 1. This is Alternative Ia and means that we start

| 92  | THE HUNGARIAN  |     | METHOD FOR  |     | THE ASSIGNMENT PROBLEM  |     |     |     |
| --- | -------------- | --- | ----------- | --- | ----------------------- | --- | --- | --- |
Routine I again.  In Case 2, we have just found a 1* in (ik, jk).  We then search column  for a
j,
1.  If  a 1 is not found, then row ik is recorded as essential, ik and jk-l  are deleted from the
record and we go back to Case 2 with the last two terms of  the sequence deleted and searching
for a 1 in column jk-l  from row ik t 1 on.  Note that, if  k = 1, then we go back to our pre-
liminary search for a 1 in the eligible column jo from row il + 1 on.
Completing Case 2, if
| a 1 is found in (ik+  |     |                      |     |      |                       |     | . . . ,  | it is distinct  |
| --------------------- | --- | -------------------- | --- | ---- | --------------------- | --- | -------- | --------------- |
|                       |     | jk) we test whether  |     | ik+  | is distinct from il,  |     | ik.      |                 |
then we record ik+l and jk  and are back in Case 1.  If  it is not distinct, we go on searching
| for a 1 in column jk  |     | from row ik+l + 1 on.  |     |     |     |     |     |     |
| --------------------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
(This routine is connected with Section 2 in the following way. Given an assignment, we
enumerate all possible transfers.  Such a transfer starts at an eligible column.  If  there are no
eligible columns, there are no transfers and the given assignment is complete.  The occurrence
of  Alternative Ia means that we have found a transfer that frees a column that contains a 1 that
| is unassigned.  |     | In this event, we carry out the transfer:  |         |     |           |     |     |     |
| --------------- | --- | ------------------------------------------ | ------- | --- | --------- | --- | --- | --- |
|                 |     |                                            | J'1/'2  |     | ik-7ik-l  |     |     |     |
'  *  '
|     |     |     |  1, il  | . . .  |       |       |     |     |
| --- | --- | --- | ------- | ------ | ----- | ----- | --- | --- |
|     |     |     |         | j2     | jk-2  | jk-1  |     |     |
and assign (ik, jk-l).  If  a transfer is developed that cannot be continued and which yields a
complete assignment, the last row involved is recorded as essential, following which the
enumeration of the transfers is continued.  If the enumeration of the transfers is completed
without the occurrence of  Alternative Ia, this is Alternative Ib and we have an assignment in
which all transfers yield complete assignments.)
The output of  Routine I in Alternative Ib is an optimal assignment for Q and a set of
essential rows.  Every 1 lies either in an essential row or in the column of  a 1* in an essential
row (Theorem 1).
A tentative flow diagram for Routine I is given in Figure 2.  For this arrangement of  the
routine, we use the following notation:
|     |     | Symbol  |     |     | Use in Routine  |     |     |     |
| --- | --- | ------- | --- | --- | --------------- | --- | --- | --- |
Index of rows of
|     |     | i   |           |             | Q.  |     |     |     |
| --- | --- | --- | --------- | ----------- | --- | --- | --- | --- |
|     |     |     | Index of  | columns of  | Q.  |     |     |     |
j
|     |     |     | Tally of  | length of  | sequence of  | 1's and  | l*'s.  |     |
| --- | --- | --- | --------- | ---------- | ------------ | -------- | ------ | --- |
k
Tally to clear essential rows in Alternative Ia.
. . . ,
|     |          | 4   | Tally to test distinctness of  |                      |     | ik+ from il,   |     | ik  ,  |
| --- | -------- | --- | ------------------------------ | -------------------- | --- | -------------- | --- | ------ |
|     | '1, '2,  | in  | Record of                      | rows in sequence of  |     | 1's and 1*'s.  |     |        |
* * * 9
|     |     | 1,-1  | Record of columns in sequence of  |     |     |     | 1's and 1*'s.  |     |
| --- | --- | ----- | --------------------------------- | --- | --- | --- | -------------- | --- |
j0, j1,
* 9
|                                                  |          |             | Record of  | essential rows.  |                 |     |     |     |
| ------------------------------------------------ | -------- | ----------- | ---------- | ---------------- | --------------- | --- | --- | --- |
|                                                  | €1, €2,  | * * -9  'n  |            |                  |                 |     |     |     |
| The values of these quantities for the input of  |          |             |            |                  | Routine I are:  |     |     |     |
. .
|     |     | i=j = k=C= 1,  |     |           | for  |         | , n .   |     |
| --- | --- | -------------- | --- | --------- | ---- | ------- | ------- | --- |
|     |     |                |     | i  = EV=  | 0    | u= 1,.  |         |     |
U

H. W. KUHN  93
The values of these quantities for the output of Alternative Ib are:
| i = j = | k = 4 = 1 ,   | i  = j   =Ofor v=1,  | ...,  n .   |
| ------- | ------------- | -------------------- | ----------- |
v  u-1
and
1  essential
|     |     | if row i  is  |     |
| --- | --- | ------------- | --- |
inessential.
The symbol "A e~B"  is to be read "replace the value of  A by the value of  B".
Input
|     |     | 1 in (i, j)?  i < n?  |     |
| --- | --- | --------------------- | --- |
Figure 2

| 04  | THE HUNGARIAN  | METHOD FOR THE ASSIGNMENT  |     |     | PROBLEM  |
| --- | -------------- | -------------------------- | --- | --- | -------- |
Routine II
1
The input of Routine II consists of  a cover {u  v  and a set of  essential rows and col-
|     |     |     | i'  | 1   |     |
| --- | --- | --- | --- | --- | --- |
umns (a column is essential if it contains a I* in an inessential row).  We first compute d,
the minimum of  ui  + v  taken over all inessential rows i  and columns j.  If  there are no
1  -
rij
such  (i, j) then the set of  l* in Q constitutes a solution to the General Assignment Problem
('Theorem 6).  Otherwise,  d > 0 and there are two mutually exclusive cases to be considered.
Case 1.  For all inessential rows i, ui >  0.  Compute m, the minimum of  d and ui
| taken over all inessential i.  |     | Then  |     |     |     |
| ------------------------------ | --- | ----- | --- | --- | --- |
-
|     |     | ui  -+  ui  m  for all inessential rows i, and  |     |     |     |
| --- | --- | ----------------------------------------------- | --- | --- | --- |
v + m
|     |     | v  -+  for all essential columns j.  |     |     |     |
| --- | --- | ------------------------------------ | --- | --- | --- |
1  1
Case 2.  For some inessential row i, ui = 0.  Compute  m, the minimum of  d and v
1
| taken Over all inessential j.  |     | Then                                         |     |     |     |
| ------------------------------ | --- | -------------------------------------------- | --- | --- | --- |
|                                |     | ui  + ui + m  for all essential rows i, and  |     |     |     |
-
|     |     | v  ----, v  m  for all inessential columns j.  |     |     |     |
| --- | --- | ---------------------------------------------- | --- | --- | --- |
J  1
After these changes have been made in the cover, we are in Alternative LIa and should return to
Routine I.
5.  AN EXAMPLE
The foIlowing example, although small in size, illustrates all of  the possibilities of the
| routines (except Case 2 of  |     | Routine II):  |     |     |     |
| --------------------------- | --- | ------------- | --- | --- | --- |
; i]
|     |     |     | [ 8 i   7 9 | 9   |     |
| --- | --- | --- | ----------- | --- | --- |
J
R=
= 9 + 8 + 9 + 6 = 32.
Sum of row maxima
| Sum of column maxima = 8 + 7  |     | + 9 + 9 = 33.  |     |     |     |
| ----------------------------- | --- | -------------- | --- | --- | --- |
Hence, the initial cover is provided by the row maxima.  The next table shows the successive
covers obtained from the algorithm (reading out from the matrix):
|     |     | Stages:  |     | 1 0 2 | 3   |
| --- | --- | -------- | --- | ----- | --- |
|     |     |          |     | 0 0 1 | 2   |
|     |     |          |     | 0 0 1 | 1   |
|     |     |          |     | 0 0 0 | 0   |
|     |     |          |     | I     | I   |
~2  7  8
5  '6
|     |     | ~ 3 | 6 7 8 | 9   |     |
| --- | --- | --- | ----- | --- | --- |

H. W. KUHN 95
The following tables explain the construction of the successive covers and of the corresponding
assignments:
Stage 1. Remarks
This matrix marks (with 1) those positions for which ui + v1 = rij
in the first cover.
Assign in each row the first 1, if any, not in the column of a pre-
vious assignment. Assignments are marked by asterisks. No transfers are
possible and hence all assigned columns and no assigned rows are essential.
0 0
Thus, the algorithm decreases &lu i and increases v3 and v4 by
the minimum of ui +v on the part of the matrix shown at left. The
1 - ril
second cover is:
u1 = 8, u2 = 7, u3 = 8, u4 = 5 and v1 = v2 = 0, v3 = v4 = 1.
stage 2.
The change in the cover has introduced a new 1 at (1,l) and there is
one possible transfer, indicated by an arrow. Thus, row 1 and column 4
are essential.
0 0 1
Thus, the algorithm decreases u2, u3, and u4 and increases v4 by
-
the minimum of ui + v r on the part of the matrix shown at left. The
1 i1
third cover is:
~ ~ = 8 , ~ ~ = 6 , ~ ~ = 7 , u ~ = 4 a n d v ~ = ~ ~ = 0 , ~ ~ = 1 , ~ ~ = 2 .
Stage 3.
El
The change in the cover has introduced a new 1 at (2,3) and elimi-
nated the 1 at (1,4). The possible transfers are indicated by arrows.
The transfer 1 2 leads to an incomplete assignment (column 4
ld#4
is unassigned and (3,4) is qualified). The matrix at left completes it. All
assigned columns and no assigned rows are essential because there are no
transf ere.

96 THE HUNGARIAN METHOD FOR THE ASSIGNMENT PROBLEM
0
Thus, the algorithm decreases. all ui and increases vl, v3, and v4
by the minimum of ui +v on the part of the matrix shown at left.
1 - ril
The fourth cover is:
u1=7,u2=5,u3=6,u4=3 andvl=l,v2 --0 ,v3=2,v4=3.
Stage 4.
The change in the cover has introduced new 1's at (1,2) and (4,2).
Thus the assignment is incomplete and is completed by assigning (4,2).
El
The assignment shown is optimal.
ui + v 2 r for all i, j.
Check: f iI
rll + r23 + r34 + r42= 8 + 7 + 9 + 3 = 27.
u1+ . . . + ~4 + ~ 1 . + . . + ~4 = 7 + 5 + 6 + 3 + 1 + 0 + 2 + 3 = 27.
BIBLIOGRAPHY
Kdnig, D., "Uber Graphen und ihre Anwendung auf Determinantentheorie und
[ 11
Mengenlehre." Math. Ann. 77 (1916) 453-465.
[ 21 Frobenius, G., "Uber zerlegbare Determinanten," Sitzungsber., Preuss. Akad. Wiss.
(1917) 274-277.
Egervky, J., "Matrixok kombinatorius tulajdonsigairbl." Mat. Fiz. Lapok (1931) 16-28
[ 3 ]
(translated as "Combinatorial Properties of Matrices'' by H. W. Kuhn, ONR Logistics
Project, Princeton (1953), mimeographed).
(41 Hall, P., "On Representatives of Subsets," J. London Math. Soc. 10 (1935) 26-30.
[ 51 Easterfield, T. E., "A Combinatorial Algorithm," J. London Math. Soc. 21 (1946) 219-226.
61 Birkhoff, Garrett, "Tres Observaciones sobre el Algebra Lineal," Univ. Nac. Tucumin.
Revista A5 (1946) 147-151.
[ 71 Thorndike, R. L., "The Problem of Classification of Personnel," Psychometrika 15 (1950)
215-235.
[ 81 Dantzig, G. B., "Application of the Simplex Method to a Transportation Problem,"
Chapter XXIII in Activity Analysis of Production and Allocation, Cowles Commission
Monograph No. 13, ed. T. C. Koopmans, New York, 1951.
[ 91 Votaw, D. F. and Orden, A., "The Personnel Assignment Problem," Symposium on Linear
Inequalities and Programming, SCOOP 10, USAF (1952) 155-163.

H. W. KUHN 97
[lo] Neumann, J. von., "A Certain Zero-sum Two-Pereon Game Equivalent to the Optimal
Assignment Problem," Contribution8 to the Theory d Game8 U, Ann. Math. Study 28
(1953) 5-12.
(111 Dwyer, P. S., "Solution of the Personnel Classification Problem with the Method of Opti-
mal Regions," Psychometrika 19 (1954) 11-26.
[12] Flood, M. M., "On the Hitchcock Distribution Problem," Pacific J. Math. 3 (1953) 369-386.
[13] Motzkin, T. S., "The Assignment Problem" in Roc. of Sixth Symposium on Applied
Mathematics, to appear.
* * *