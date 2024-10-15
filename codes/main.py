from pymonntorch import Network, NeuronGroup, Recorder, EventRecorder, SynapseGroup
from lif import LIF , ELIF, AELIF
from dt import TimeResolution
from syn import SynFun, InpSyn
from current import SetCurrent, StepFunction, StepFunction1, StepFunction2
import torch

from matplotlib import pyplot as plt




current_value = -0.5
frequencies = []
currents = []
iteration_numbers = 1000
dt = 0.1
for i in range(41):
    current_value+=0.5
    net = Network(behavior={1: TimeResolution()}, dtype=torch.float64)
    ng1 = NeuronGroup(
        1,
        net=net,
        behavior={
            2: SetCurrent(value=current_value, s_current=0, e_current=100),
            # 3: StepFunction(value=20, t0=5, t1=10, t2=20, t3=50, t4=70),
            # 3: StepFunction1(value=5, t0=20, t1=40),
            # 3: StepFunction2(value=220, t0=20, t1=40),
            # 4: InpSyn(),
            # 5: LIF(
            #     tau=10,
            #     u_rest=-65,
            #     # u_reset=20,
            #     u_back=-73.42,
            #     threshold=-20,
            #     R=10,
            #     v_init="normal(-40, 10)",
            #     refractory_T=0
            # ),
            # 5: ELIF(
            #     tau=10,
            #     u_rest=-65,
            #     u_reset=20,
            #     u_back=-73.42,
            #     threshold=-20,
            #     R=10,
            #     v_init="normal(-60, 0)",
            #     delta_T=10,
            #     refractory_T=0
            # ),

            5: AELIF(
                tau=10,
                u_rest=-65,
                u_reset=20,
                u_back=-73.42,
                threshold=-20,
                R=10,
                # v_init="normal(-40, 10)",
                v_init=-65,
                delta_T=0.1,
                refractory_T=2,
                a=0.01,
                b=50,
                tau_w=10
            ),


            # 9: Recorder(variables=["v","w", "I", "first_term","second_term", "third_term"], tag="ng1_rec, ng1_recorder"),
            9: Recorder(variables=["v","I"], tag="ng1_rec, ng1_recorder"),
            10: EventRecorder("spike", tag="ng1_evrec"),
        },
        tag="NG1",
    )
    #
    # SynapseGroup(net=net, src=ng1, dst=ng1, behavior={
    #                  3: SynFun(),
    #              })

    net.initialize()


    net.simulate_iterations(iteration_numbers)
    spike_count = net["spike", 0][:,0]
    frequency = len(spike_count) / (iteration_numbers * dt)
    frequencies.append(frequency)
    currents.append(current_value)

# print(net["ng1_rec", 0]["v", 0])
# print(net["ng1_evrec", 0]["spike", 0])

font1 = {'size':17}



plt.figure(figsize=(18,6))
plt.plot(currents, frequencies)
plt.title("frequency-current relation", fontdict=font1)
plt.xlabel("I(t)", fontdict=font1)
plt.ylabel("f = 1/T", fontdict=font1)
plt.show()


plt.figure(figsize=(18,6))
plt.plot(net["v", 0])
plt.title("Membrane Potential", fontdict=font1)
plt.xlabel("Time", fontdict=font1)
plt.ylabel("u(t)", fontdict=font1)
plt.show()
plt.figure(figsize=(18,6))
plt.plot(net["I", 0])
plt.title("Current", fontdict=font1)
plt.xlabel("Time", fontdict=font1)
plt.ylabel("I(t)", fontdict=font1)
plt.show()

plt.scatter(net["spike", 0][:,0], net["spike", 0][:,1])
plt.title("Spike", fontdict=font1)
plt.xlabel("Time", fontdict=font1)
plt.ylabel("Neuron", fontdict=font1)
plt.show()

#
# plt.figure(figsize=(18,6))
# plt.plot(net["first_term", 0])
# plt.title("first_term", fontdict=font1)
# plt.xlabel("Time", fontdict=font1)
# plt.ylabel("I(t)", fontdict=font1)
# plt.show()
#
#
#
#
# plt.figure(figsize=(18,6))
# plt.plot(net["w", 0], label="W")
# plt.plot(net["first_term", 0], label="first_term")
# plt.title("W", fontdict=font1)
# # plt.title("v", fontdict=font1)
# plt.xlabel("Time", fontdict=font1)
# # plt.ylabel("I(t)", fontdict=font1)
# plt.legend()
# plt.show()
#
# plt.figure(figsize=(18,6))
# plt.plot(net["w", 0], label="W")
# plt.plot(net["v", 0], label="V")
# plt.title("W", fontdict=font1)
# # plt.title("v", fontdict=font1)
# plt.xlabel("Time", fontdict=font1)
# # plt.ylabel("I(t)", fontdict=font1)
# plt.legend()
# plt.show()
#
# plt.figure(figsize=(18,6))
# plt.plot(net["third_term", 0])
# plt.title("third_term", fontdict=font1)
# plt.xlabel("Time", fontdict=font1)
# plt.ylabel("I(t)", fontdict=font1)
# plt.show()