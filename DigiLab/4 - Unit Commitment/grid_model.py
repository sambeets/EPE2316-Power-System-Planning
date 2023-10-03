import pypsa
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Insert your python code here 

# Task 1.1
V_base = 22.0 # kV 
S_base = 100 # MVA

def get_network(p_set_load, cost_g1, cost_g2):
    network = pypsa.Network(snapshots=range(len(p_set_load)))
    network.add("Bus", "Bus 1", v_nom=V_base)
    network.add("Bus", "Bus 2", v_nom=V_base)
    network.add("Bus", "Bus 3", v_nom=V_base)
    network.add("Line", "Line 12", bus0="Bus 1", bus1="Bus 2", r=3.0 , x=8.0, s_nom=100)
    network.add("Line", "Line 23", bus0="Bus 2", bus1="Bus 3", r=1.0 , x=4.0, s_nom=100)
    network.add("Line", "Line 13", bus0="Bus 1", bus1="Bus 3", r=10.0, x=35.0, s_nom=100)

    network.add("Generator", "Hydro 1", bus="Bus 1", committable=True, p_min_pu=0.1, p_nom=6, marginal_cost=cost_g1)
    network.add("Generator", "Hydro 2", bus="Bus 3", committable=True, p_min_pu=0.1, p_nom=3, marginal_cost=cost_g2)

    network.add("Load", "Load 1", bus="Bus 2", p_set=p_set_load)
    return network