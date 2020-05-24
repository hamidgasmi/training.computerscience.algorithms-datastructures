import sys
import global_alignment

def align_naive(m,mu,sigma,s,t):
    
    alignment = global_alignment.Alignment(m, mu, sigma)
    alignment.built_global_alignment_matrix(s, t)
    max_sub_global_align_score = alignment.global_alignment_score
    print("max_sub_global_align_score, i: ", 0, max_sub_global_align_score)
    sub_s_start = 0
    for i in range(1, len(s), 1):
               
        A = alignment.built_global_alignment_matrix(s[i:], t)

        print("global_alignment_score, i: ", i, alignment.global_alignment_score)
        if alignment.global_alignment_score > max_sub_global_align_score:
            max_sub_global_align_score = alignment.global_alignment_score
            sub_s_start = i
            print("max_sub_global_align_score, i: ", i, alignment.global_alignment_score)

    if sub_s_start == 0:
        alignment.global_alignment(s, t)
    else:
        alignment.global_alignment(s[sub_s_start:], t)
    
    print(alignment.global_alignment_score)
    print(alignment.aligned_seq_1)
    print(alignment.aligned_seq_2)

    #return ""

if __name__ == "__main__":
    m,mu,sigma = map(int,sys.stdin.readline().strip().split())
    s,t = [sys.stdin.readline().strip() for _ in range(2)]

    align_naive(m, mu, sigma, s, t)

    #print(align(m,mu,sigma,s,t))
