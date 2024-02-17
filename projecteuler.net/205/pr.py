from tqdm import tqdm


def num(b, z=None):
    pass

def prob(x, y):
    return num(4, x) / num(4) * num(6, y) / num(6)

x_gt_y_pr = 0
for x in tqdm(range(9, 9*4+1)):
    for y in range(6, min(6*6+1, x - 1)):
        x_gt_y_pr += prob(x, y)



