from project_updated.KinematicChain import *

def get_qdot_from_qlast(qlast,Chain,pd,Rd,vd,wd,dt):

    (p, R, Jv, Jw) = Chain.fkin(qlast)

    J = np.vstack((Jv,Jw))

    error = np.vstack((ep(pd,p),eR(Rd,R)))
    v = np.vstack((vd,wd))

    qdot = np.linalg.pinv(J) @ (v + 20*(error))
    q = qlast + dt*qdot

    return (q,qdot)



def get_indv_chain_q_from_full_q(q):

    q_pelvis_leftfoot = q[0:6].reshape(-1,1)
    q_pelvis_rightfoot = q[6:12].reshape(-1,1)
    q_pelvis_uppertorso = q[12:15].reshape(-1,1)
    q_uppertorso_head = q[15:16].reshape(-1,1)
    q_uppertorso_lefthand = q[16:23].reshape(-1,1)
    q_uppertorso_righthand = q[23:30].reshape(-1,1)

    return(q_pelvis_leftfoot,q_pelvis_rightfoot,q_pelvis_uppertorso,q_uppertorso_head,q_uppertorso_lefthand,q_uppertorso_righthand)
