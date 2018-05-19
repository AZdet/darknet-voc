import os
#AllClass = ['ball', 'goal', 'robot', 'goalpost', 'line', 'concealed ball']
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def getClsID(real_type):
    if real_type == "goal" or real_type == "goalpost":  # should we seperate goal and goalpost?
        return 0
    else:
        raise AssertionError("invalid type")

dataset_id = '368'
fin = open('export_'+dataset_id+'.txt', 'r')
#fout = open('out_'+dataset_id+'.txt', 'w')
#fout2 = open('train_list_'+dataset_id+'.txt', 'w')
name = 0
w = 1
h = 2
dataset = 3
ty = 4
minx = 5
miny = 6
maxx = 7
maxy = 8
homepath = "/home/alex/Desktop/darknet/pic/"
with open('train_list_'+dataset_id+'.txt', 'w') as fout2:
    for line in fin:
        items = line.split()
        if len(items) < 9 or (items[ty] != "goal" and items[ty] != "goalpost"):  # this line does not contain label
            # cls_id = getClsID("")
            # fout.write(str(cls_id) + " "  + '\n')
            # fout2.write(items[name] + '\n')
            continue
        # name W H dataset type minx miny maxx maxy
        #   0  1 2   3      4    5    6    7    8  
        assert(len(items) == 9)
        size = (int(items[w]), int(items[h]))
        b = [int(items[x]) for x in [minx, maxx, miny, maxy]]
        bb = convert(size, b)
        cls_id = getClsID(items[ty])
        annotation_name = homepath + items[name][:-3] + "txt"
        with open(annotation_name, "a") as fout:
            fout.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        fout2.write(homepath + items[name] + '\n')  # only name of pic should be saved
print('done')
