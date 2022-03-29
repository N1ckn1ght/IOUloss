def area(bbox):
    return (bbox[1] - bbox[0]) * (bbox[3] - bbox[2])
    

def iou(bbox1: list, bbox2: list) -> float:
    bbox3 = [max(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]), max(bbox1[2], bbox2[2]), min(bbox1[3], bbox2[3])]
    if (bbox3[0] > bbox3[1] or bbox3[2] > bbox3[3]):
        return 0
    union = area(bbox1) + area(bbox2) - area(bbox3)
    inter = area(bbox3)
    return inter / union


bbox1 = [0, 10, 0, 10]
bbox2 = [0, 10, 1, 10]
bbox3 = [20, 30, 20, 30]
bbox4 = [5, 15, 5, 15]

assert iou(bbox1, bbox1) == 1.0
print('1: OK')
assert iou(bbox1, bbox2) == 0.9
print('2: OK')
assert iou(bbox1, bbox3) == 0.0
print('3: OK')
assert round(iou(bbox1, bbox4), 2) == 0.14
print('4: OK')
