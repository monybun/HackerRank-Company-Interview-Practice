'''
Three coordinations of a triangle (x1, y1, x2, y2, x3, y3) ---point 1,2,3
Check if point p(xp, yp) q(xq, yq) in the triangle:
  * both in : return 3
  * ONLY point p in: return 1
  * ONLY point q in: return 2
  * None of them in: return 4
'''

def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    # Write your code here
    # calculate area of the triangle
    Triangle_area = abs((x1*(y2-y3)+(x2*(y3-y1))+(x3*(y1-y2)))*0.5)
    if Triangle_area == 0:
        return 0
    else:
        #checking xp,yp
        A1 = abs((x1*(y2-yp)+(x2*(yp-y1))+(xp*(y1-y2)))*0.5)
        A2 = abs((x1*(yp-y3)+(xp*(y3-y1))+(x3*(y1-yp)))*0.5)
        A3 = abs((xp*(y2-y3)+(x2*(y3-yp))+(x3*(yp-y2)))*0.5)
        
        A4 = abs((x1*(y2-yq)+(x2*(yq-y1))+(xq*(y1-y2)))*0.5)
        A5 = abs((x1*(yq-y3)+(xq*(y3-y1))+(x3*(y1-yq)))*0.5)
        A6 = abs((xq*(y2-y3)+(x2*(y3-yq))+(x3*(yq-y2)))*0.5)
        
        Area_p = A1+A2+A3
        Area_q = A4+A5+A6
        
        if Area_p != Triangle_area and Area_q != Triangle_area:
            return 4
        elif Area_p == Triangle_area and Area_q != Triangle_area:
            return 1
        elif Area_p != Triangle_area and Area_q == Triangle_area:
            return 2
        elif Area_p == Triangle_area and Area_q == Triangle_area:
            return 3
        
## Try:  triangle a(2,2)  b(7,2)  c(5,4)     points: p(1,2)  q(5,3)
x1 = 2; y1 = 2
x2 = 7; y2 = 2
x3 = 5; y3 = 4
xp = 1; yp = 2
xq = 5; yq = 3
print(pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq))
#Output: 2 ---> ONLY point q in
