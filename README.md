# 🧮 Surface Volume Integration using `scipy.integrate.dblquad`


> 📌 A Python script to **compute the volume under a 3D surface** defined by the equation  
> \[
z = x^2 + y^2
\]  
> over a rectangular region using **SciPy’s double integration** method.

---

## 📂 Project Description

This project performs **numerical double integration** to calculate the volume underneath the surface:

\[
z = x^2 + y^2
\]

within the region:
- \( x \in [0, 3] \)
- \( y \in [0, 1] \)

It uses the `dblquad()` function from SciPy’s `integrate` module.

---

## 📈 Mathematical Concept

We are evaluating the double integral:

\[
\text{Volume} = \int_{x=0}^{3} \int_{y=0}^{1} (x^2 + y^2) \, dy \, dx
\]

This computes the **volume under the 3D surface** defined by:

\[
z = x^2 + y^2
\]

within the region \( x \in [0, 3] \) and \( y \in [0, 1] \).

---

## ✅ Output

text
Volume under surface z = x^2 + y^2: 12.0


---
### 🛠️ Requirements
Make sure you have the required package installed:


pip install scipy
### 💡 How to Use
Clone the repo or copy the code into your Python script, then run:

python your_script_name.py
### ✅ You'll see the volume printed in your terminal.


### 📎 License
MIT License – free to use and modify.

### 🤝 Contribute
Pull requests and feedback are welcome!
Feel free to fork and experiment with more surface functions.

