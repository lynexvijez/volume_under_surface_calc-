# volume_under_surface_calc-
🧮 Project Overview
This Python script calculates the volume under the surface defined by the equation:
z=x**2+y**2
over the square region:
0≤𝑥≤1
0≤y≤1
It uses double integration via scipy.integrate.dblquad.
![image](https://github.com/user-attachments/assets/1d5c3a43-7aac-4490-bb8c-c81161cbbba5)

🧰 Requirements
Python 3.x
NumPy
SciPy
Install dependencies with:

pip install numpy scipy

📎 Notes
The dblquad function performs double integration.

It returns both the computed volume and an estimate of the numerical error.

The integrand(y, x) function follows the order expected by dblquad (note y comes first).
