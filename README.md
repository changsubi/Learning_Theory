Learning_Theory
======================
# Probability
Event : a subset of the sample space
probability is assigned to events   
Axioms :   
nonnegativity : P(A) $\geq$ 0   
normalization : P(S) = 1   
   
<img src="https://user-images.githubusercontent.com/100255173/226573523-4b1504ab-dc8d-4acb-ba9a-2b919706003b.png" width="450px" height="200px" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>
   
Def. Conditional Probability   
Probability of A, given that B occurred   
$P(A|B) = \frac{P(A \cap B)}{P(B)}$   
only when P(B)>0   
   
Partition of sample space into $A_1, A_2, A_3, ... $   
have $P(A_i)$, for every i   
have $P(B|A_i)$, for every i   
$P(B) = \sum_{i} P(A_i)P(B|A_i)$
   
Bayes' rule:   
$P(A_j|B) = \frac{P(A_j)P(B|A_j)}{\sum_{i} P(A_i)P(B|A_i)}$
   
The king comes from a family of two children. What is the probability that his sibling is female?
   
Independence of two events:   
$P(A \cap B) = P(A)P(B|A) = P(A)P(B)$   
Conditional independence:   
conditional independence, given C, is defined as independence under the probability law $P(\bullet|C)$
   
Counting:   
Number of license with 2 letters followed by 3 digits:   
$26 \times 26 \times 10 \times 10 \times 10$
but, if repetition is prohibited then, $26 \times 25 \times 10 \times 9 \times 8$   
Permutations :   
number of ways of ordering n elements : $n(n-1)(n-2)\cdots = n!$   
Combinations :   
number of k element subsets of a given n element set : $\frac{n!}{k!(n-k)!}$   
$(a+b)^n = \displaystyle\sum_{k=0}^{n} \frac{n!}{k!(n-k)!}a^{n-k}b^k$
   
# Information
Information theory is the scientific study of the quantification, storage, and communication of information.   
Something that reduces uncertainty about something
   
Uncertainty Measure   
Let X be a random variable taking values over a finite set $X = {x_1, x_2, x_3, \cdots, x_M}$ referred to as a "alphabet" in information theory.   
high uncertainty : hard to expect what is going to heppen   
low uncertainty : easy to expect what is going to heppen   
   
Entropy :   
$H(X) = -E_X[log (p(X))] = -\sum_{x \in X} p(x)log (p(x))$   
$H(X) \geq 0$ because $-log(p(x)) \geq 0$ always   
$H(X)  \leq log|X|$
   
Joint Entropy :   
Extend H(X) to a pair of random variables   
H(X,Y) of a pair discrete RVs (X,Y) with a joint pmf p(x,y) is   
$H(X,Y) = -\sum_{x \in X} \sum_{y \in Y} p(x,y)log(p(x,y))$   
that is the uncertainty in (X,Y)   
just consider Z:=(X,Y) as a new random variable. then it is no different from H(Z)   
$H(X,Y,Z) = -\sum_{x \in X} \sum_{y \in Y} \sum_{z \in Z} p(x,y,z)log(p(x,y,z))$
   
Conditional Entropy :   
Extend H(X) to a random variable given another   
If (X,Y) ~ p(x,y) then the conditional entropy H(Y|X) is   
$H(Y|X) = \sum_{x \in X} p(x)H(Y|X=x) = -\sum_{x \in X} p(x) \sum_{y \in Y} p(y|x)log(p(y|x)) = -\sum_{x \in X} \sum_{y \in Y} p(x,y)log(p(y|x))$   
Can be thought of as the remaining uncertainty in Y after observing X (X : dataset)
   
Chain Rule :   
For (X,Y) ~ p(x,y), H(X,Y) = H(X) + H(Y|X)   
proof >   
$H(X,Y) = -\sum_{x \in X} \sum_{y \in Y} p(x,y)log(p(x,y))$   
$= -\sum_{x \in X} \sum_{y \in Y} p(x,y)log(p(x)p(y|x))$   
$= -\sum_{x \in X} \sum_{y \in Y} p(x,y)log(p(x)) - \sum_{x \in X} \sum_{y \in Y} p(x,y)log(p(y|x))$   
$= -\sum_{x \in X} p(x)log(p(x)) -\sum_{x \in X} \sum_{y \in Y} p(x,y)log(p(y|x))$   
= H(X) + H(Y|X)
then, H(X,Y,Z) = H(X) + H(Y|X) + H(Z|X,Y)
   
<img src="https://user-images.githubusercontent.com/100255173/226596981-4a3df660-8fd2-4589-8065-c92249e9ae47.png" width="450px" height="200px" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>
   
Mutual Information :   
measure of the amount of common information(correlation) that one variable contains about the other random variable   
For (X,Y) ~ p(x,y), the mutual information I(X;Y) is   
$I(X;Y) = \sum_{x \in X} \sum_{y \in Y} p(x,y)log(\frac{p(x,y)}{p(x)p(y)}) = \sum_{x \in X} \sum_{y \in Y} p(x,y)log(\frac{p(x|y)}{p(x)})$   
$= -\sum_{x \in X} \sum_{y \in Y} p(x,y)p(x) + \sum_{x \in X} \sum_{y \in Y} p(x,y)log(p(x|y))$   
= H(X) - H(X|Y) = H(Y) - H(Y|X)   
   
<img src="https://user-images.githubusercontent.com/100255173/226598823-37bfb92a-a7d3-4443-b6fb-1a8874860e5d.png" width="300px" height="200px" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>
   







