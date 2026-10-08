import numpy as np

def project(Pc, W, H, n, f, fx, fy, ox, oy):
    P = np.array([
        [2*fx/W, 0, 1-2*ox/W, 0],
        [0, 2*fy/H, 1-2*oy/H, 0],
        [0, 0, -(f+n)/(f-n), -2*f*n/(f-n)],
        [0, 0, -1, 0]
    ])

    clip = P @ np.array(Pc)
    ndc = clip[:3] / clip[3]

    u = (ndc[0] + 1) * W / 2
    v = (ndc[1] + 1) * H / 2

    return u, v

print(project(
    [0.3, -0.15, -6, 1],
    800, 600, 0.2, 20,
    800, 800, 400, 400
))
