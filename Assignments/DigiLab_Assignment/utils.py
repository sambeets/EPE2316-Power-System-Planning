import pypsa 
import numpy as np 

def check_task_1_1(network: pypsa.Network):
    score = 0
    if (network.buses.v_mag_pu_set.values == np.array([1.02, 1.0, 1.02, 1.0, 1.02, 1.0])).all():
        score += 1
    else:
        print("Voltage set points are not correct")
    if np.isclose(network.lines.s_nom.values.round(3), 
                  np.array([228.6307066, 228.6307066, 160.04149462, 114.3153533, 228.6307066, 228.6307066]).round(3), 1e-6).all(): 
        score += 1
    else:
        print("Line ratings are not correct")
    if np.isclose(network.lines.x.values.round(3), 
                  np.array([2.,  2.,  4., 12.,  2.,  2.]).round(3), 1e-6).all():
        score += 1
    else:
        print("Line reactances are not correct")
    if np.isclose(network.lines.r.values.round(3), 
                  np.array([0.5, 0.5, 2. , 9. , 0.5, 0.5]).round(3), 1e-6).all():
        score += 1
    if (network.generators.control.values == np.array(["Slack", "PV", "PV"])).all(): 
        score += 1
    else:
        print("Generator controls are not correct (Slack, PV, PQ config)")
    if (network.generators.p_min_pu.values == np.array([0.01, 0.8, 0.6])).all():
        score += 1
    else:
        print("Generator minimum powers are not correct")
    if (network.generators.p_set.values == np.array([0, 300, 100])).all():
        score += 1
    else:
        print("Generator set points are not correct")
    if (network.loads_t.p_set.shape == (48, 3)): 
        score += 1
    else:
        print("Load time series is not correct")
    print("Task 1.1 score: ", score, "/ 8")

def check_task_1_2(network: pypsa.Network): 
    score = 0
    if network.buses_t.v_mag_pu.shape == (48, 6): 
        score += 6
    else:
        print("Power flow results are empty. ")
        try: 
            network.pf()
            score += 6
        except: 
            print("Power flow did not converge. ")
    print(f"Score: {score}/6")

def check_task_2_1(objective_function, opf_constraints): 
    score_obj = 0
    val_1 = objective_function(np.array([1.02, 1.02, 1.02, 300, 100]))
    val_2 = objective_function(np.array([1.02, 1.02, 1.02, 100, 0]))
    val_3 = objective_function(np.array([1.05, 1.05, 1.05, 0, 0]))
    if round(val_1, 5) == round(3.406988302301761, 5): 
        score_obj += 1
    if round(val_2, 5) == round(2.215011905075742, 5):
        score_obj += 1
    if round(val_3, 5) == round(3.264575038144324, 5): 
        score_obj += 1
    if not score_obj == 3:
        print("Objective function is not correct.") 
    score_const = 0
    val_1 = opf_constraints(np.array([1.02, 1.02, 1.02, 300, 100]))
    val_2 = opf_constraints(np.array([1.02, 1.02, 1.02, 100, 0]))
    val_3 = opf_constraints(np.array([1.05, 1.05, 1.05, 0, 0]))
    val_1_correct = np.array([1.01560636, 0.99853285, 1.01785734, -126.59301191,
                              90.46918336, 35.66519845, 18.7217287, 476.86671914,
                              829.24760879, 493.21855151, 109.07514599, 364.43641948,
                              190.74953421])
    val_2_correct = np.array([1.01573674, 0.99799356, 1.01786263, 172.21501184,
                              14.61501278, 87.77710336, 37.72808624, 407.67844952,
                              157.99903725, 458.14968215, 130.43571726, 164.41434368,
                              335.80856821])
    val_3_correct = np.array([1.04576196, 1.0280766, 1.04791489, 273.264575,
                              -8.2799852, 119.66762932, 32.41859638, 756.69560049,
                              416.53669437, 418.89209791, 172.82674275, 211.83175124,
                              382.14652633])
    if np.allclose(val_1, val_1_correct, rtol=1e-5): 
        score_const += 1
    if np.allclose(val_2, val_2_correct, rtol=1e-5):
        score_const += 1
    if np.allclose(val_3, val_3_correct, rtol=1e-5):
        score_const += 1
    if not score_const == 3:
        print("Constraints are not correct.")
    print(f"Task 2.1: {score_obj+score_const}/6")

def check_task_2_2(sol_OPF): 
    if not sol_OPF.success: 
        raise ValueError("The optimization was not successful. Score 0/6")
    sol = np.array([1.04932527, 1.05, 1.04850317, 154.15605287, 41.4629837])
    if np.allclose(sol_OPF.x, sol, atol=1e-5): 
        print("Success! Score 6/6")