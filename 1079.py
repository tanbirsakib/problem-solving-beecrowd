# n = int(input())
# w1, w2, w3 = 2, 3, 5
# for i in range(1, n+1):
#     q1, q2, q3 = map(float, input().split())
#     r1, r2, r3 = map(float, input().split())
#     t1, t2, t3 = map(float, input().split())
#     avg1 = ((q1*w1) + (q2*w2) + (q3*w3)) / (w1 + w2 + w3)
#     avg2 = ((r1*w1) + (r2*w2) + (r3*w3)) / (w1 + w2 + w3)
#     avg3 = ((t1*w1) + (t2*w2) + (t3*w3)) / (w1 + w2 + w3)
#     print("%0.1f"%avg1)
#     print("%0.1f"%avg2)
#     print("%0.1f"%avg3)

n=int(input())
for i in range(n):
    a,b,c=list(map(float,input().split()))
    total=(a*2+b*3+c*5)/10
    print("%0.1f"%total)