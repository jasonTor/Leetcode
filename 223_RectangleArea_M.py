#223. Rectangle Area
#Retourne l'air de l'union de 2 rectangles

def is_inter(self,a,b):
    c = max(min(a),min(b))
    if c in a:
        if c<=max(b) and c>=min(b):
            return True
    elif c in b:
        if c<=max(a) and c>=min(a):
            return True
    return False

def computeArea(self,ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    L1 = [ax1,ax2]
    L1.sort()
    L2 = [bx1,bx2]
    L2.sort()
    l1 = [ay1,ay2]
    l1.sort()
    l2 = [by1,by2]
    l2.sort()

    if is_inter(L1,L2):
        if is_inter(l1,l2):
            air_inter = abs(max(min(L1),min(L2))-min(max(L1),max(L2))) * abs(max(min(l1),min(l2))-min(max(l1),max(l2)))
            return abs(ax1-ax2)*abs(ay1-ay2) + abs(bx1-bx2)*abs(by1-by2) - air_inter
    return abs(ax1-ax2)*abs(ay1-ay2) + abs(bx1-bx2)*abs(by1-by2)