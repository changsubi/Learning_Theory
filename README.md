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
   1. 간결하다.
	2. 별도의 도구없이 작성가능하다.
	3. 다양한 형태로 변환이 가능하다.
	4. 텍스트(Text)로 저장되기 때문에 용량이 적어 보관이 용이하다.
	5. 텍스트파일이기 때문에 버전관리시스템을 이용하여 변경이력을 관리할 수 있다.
	6. 지원하는 프로그램과 플랫폼이 다양하다.
P(A|B) = P(A $\cap$ B) / P(B)   
only when P(B)>0
   
Partition of sample space into $A_1, A_2, A_3, ... $   
have $P(A_i)$, for every i   
have $P(B|A_i)$, for every i   
$P(B) = \sum_{i} P(A_i)P(B|A_i)$
