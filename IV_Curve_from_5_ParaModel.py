import numpy as np
import matplotlib.pyplot as plt                            # Used this library for plotting

def iv_curve(V, Iph, Isc, Rs, Rsh, a, n_cells):            # The parameters are defined in the function iv_curve
    q = 1.602e-19
    k = 1.381e-23
    T = 298.15
    V_cell = V / n_cells
    Id = Isc * (np.exp(q * V_cell / (a * k * T)) - 1)
    I = Iph - Id - Rs / Rsh
    return I

Iph = float(input("Enter Iph (in A): "))
Isc = float(input("Enter Isc (in A): "))
Rs = float(input("Enter Rs (in Ohm): "))
Rsh = float(input("Enter Rsh (in Ohm): "))
a = float(input("Ideality Factor: "))
n_cells = int(input("Enter number of cells: "))          

V = np.linspace(0, 15 * n_cells, 1000)       
I = iv_curve(V, Iph, Isc, Rs, Rsh, a, n_cells)      

P = V * I
idx_max = np.argmax(P)
Vmp = V[idx_max]
Imp = I[idx_max]
Pmax = Vmp * Imp

def find_zero_crossing(x, y):
    for i in range(len(y) - 1):
        if y[i] * y[i + 1] < 0:
            x_zero = x[i] - y[i] * (x[i + 1] - x[i]) / (y[i + 1] - y[i])
            return x_zero
    return None

Voc = find_zero_crossing(V, I)

ff = (Pmax) * 100 / (Iph * Voc)

print("Vmp: ", round(Vmp, 2), "V")
print("Imp: ", round(Imp, 2), "A")
print("Pmax: ", round(Pmax, 2), "W")
print("Voc: ", round(Voc, 2), "V")
print("Isc: ", round(Iph, 2), "A")
print("Fill Factor: ", round(ff, 2), "%")

# Plot the IV curve
plt.plot(V, I)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title(f'IV Curve of a Solar Panel with {n_cells} Cells')
plt.grid(True)

# Plot the maximum power point
plt.scatter(Vmp, Imp, color='red', marker='o', label='MPP')
plt.xlim(0, float(Voc) + 0.5)
plt.ylim(0, float(Iph) + 1)
plt.legend()
plt.show()
