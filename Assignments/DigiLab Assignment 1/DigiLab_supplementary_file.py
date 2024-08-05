import numpy as np 

Y_bus = np.array([[ 0.23543242-0.65826j, -0.19890411+0.53041095j, -0.0365283 +0.12784906j],
                  [-0.19890411+0.53041095j,  0.48360997-1.6692345j, -0.28470588+1.1388235j],
                  [-0.0365283 +0.12784906j, -0.28470588+1.1388235j, 0.32123417-1.2666726j ]])

def score_task_1(network): 
    P_calc = network.buses_t.p.values[0].round(3)
    Q_calc = network.buses_t.q.values[0].round(3)
    V_calc = network.buses_t.v_mag_pu.values[0].round(5)
    th_calc = (network.buses_t.v_ang.values[0]).round(6)
    

    P_sol = np.array([-0.488, -1.5, 2.0])
    Q_sol = np.array([-0.639, -0.5, 1.182])
    V_sol = np.array([1.0, 1.00867, 1.02 ])
    th_sol = np.array([0.0, 0.001282, 0.013395])

    score = 0
    if np.allclose(P_calc, P_sol, rtol=1e-3):
        score += 1
    else: 
        print(f"Expected P: {P_sol} but got {P_calc}")
    if np.allclose(Q_calc, Q_sol, rtol=1e-3):
        score += 1
    else:
        print(f"Expected Q: {Q_sol} but got {Q_calc}")
    if np.allclose(V_calc, V_sol, rtol=1e-5):
        score += 1
    else:
        print(f"Expected V: {V_sol} but got {V_calc}")
    if np.allclose(th_calc, th_sol, rtol=1e-6):
        score += 1
    else:
        print(f"Expected theta: {th_sol} but got {th_calc}")
    print(f"Score: {score}/4")

def score_task_2(sol): 
    if not sol.success: 
        print("Score: 0/4. The power flow equations were not solved.")

    th1 = round(sol.x[0], 5)
    th2 = round(sol.x[1], 5)
    V1 = round(sol.x[2], 5)

    th1_sol = 0.00128
    th2_sol = 0.01340
    v1_sol = 1.00867

    score = 0
    if round(th1, 5) == th1_sol:
        score += 1
    else: 
        print(f"Expected theta_1: {th1_sol} but got {th1} rad")
    if round(th2, 5) == th2_sol:
        score += 1
    else: 
        print(f"Expected theta_2: {th2_sol} but got {th2} rad")
    if round(V1, 5) == v1_sol:
        score += 1
    else: 
        print(f"Expected V_1: {v1_sol} but got {V1} pu")
    print(f"Score: {score}/3")

def score_task_3(Q3_vals: list[float]): 
    try: 
        Q3_calc = [round(Q, 5) for Q in Q3_vals]
    except: 
        print("The input is not a list of floats")
        print("Score: 0/3")
        return 
    Q3_sols = [-2.47271, 0.08099, 2.91929]
    score = 0
    for i in range(len(Q3_sols)): 
        if np.isclose(Q3_calc[i], Q3_sols[i], rtol=1e-3): 
            score += 1
    print(f"Score: {score}/3")