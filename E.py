# def is_cros(a, b) -> bool:
#     ax1, ay1, ax2, ay2 = a[0], a[1], a[2], a[3]
#     bx1, by1, bx2, by2 = b[0], b[1], b[2], b[3]
#     s1 = (ax1 > bx1 and ax1 < bx2) or (ax2 > bx1 and ax2 < bx2)
#     s2 = (ay1 > by1 and ay1 < by2) or (ay2 > by1 and ay2 < by2)
#     s3 = (bx1 > ax1 and bx1 < ax2) or (bx2 > ax1 and bx2 < ax2)
#     s4 = (by1 > ay1 and by1 < ay2) or (by2 > ay1 and by2 < ay2)

#     if ax1 == bx1 and ax2 == bx2 and ay1 == by1 and ay2 == by2 : return True

#     return (s1 and s2) or (s3 and s4) or (s1 and s4) or (s3 and s2)

def is_cros_2(a, b) -> bool:
    return not ( b[3] <= a[1] or b[2] <= a[0] or b[0] >= a[2] or b[1] >= a[3] )

def count_cros(rectangle:list, all_recs:list[list]) -> int:
    res = 0
    for item in all_recs:
        if is_cros_2(rectangle,item): res += 1
    return res

def input_rectangle() -> list:
    return [int(i) for i in input().split()]


n = int(input())
rectangles = []
# rectangles.append([-2, -4, 2, 2])
# rectangles.append([-2, -4, 0, -1])
# rectangles.append([-2,-1 ,0 ,2 ])
# rectangles.append([0, -4,2 ,-1 ])
# rectangles.append([0, -1, 2, 2])
# rectangles.append([-1,-2 ,1 ,0 ])
for _ in range(n):
    rectangles.append(input_rectangle())

res = []
for rec in rectangles:
    res.append( str(count_cros(rec,rectangles)-1) )

print(' '.join(res))
