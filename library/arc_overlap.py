import math

def arc_overlap( arc1, arc2 ):
    arc1_wraps = arc1[0] > arc1[1]
    arc2_wraps = arc2[0] > arc2[1]

    if not arc1_wraps and not arc2_wraps:
        # Easy case - order and check
        if arc1[0] > arc2[0]:
            arc1, arc2 = arc2, arc1
        return arc1[1] > arc2[0]
    elif arc1_wraps and not arc2_wraps or not arc1_wraps and arc2_wraps:
        # Normalise to the wrap
        if arc1[0] > arc2[0]:
            arc1, arc2 = arc2, arc1   
        return arc1[1] > arc2[0] or arc2[1] > arc1[0]           
    elif arc1_wraps and arc2_wraps:
        # They both wrap so the MUST overlap!
        return True

    return None

def main():
    arc2 = (359.5, 0.5)
    arc1 = (1,359)

    if arc_overlap(arc1, arc2):
        print("Overlap")
    else:
        print("No overlap")

if __name__ == "__main__":
    main()

