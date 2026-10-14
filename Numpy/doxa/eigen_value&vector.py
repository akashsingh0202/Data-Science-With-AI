
import numpy as np

# Step 1: Matrix create karo
A = np.array([[3, 0],
              [0, 6]])

# Step 2: Eigenvalues aur eigenvectors calculate karo
values, vectors = np.linalg.eig(A)

# Step 3: Eigenvalues print karo
print("Eigenvalues:")
print(values)

# Step 4: Eigenvectors print karo
print("Eigenvectors:")
print(vectors)


# - np.linalg.eig(A) matrix ki eigenvalues aur eigenvectors calculate karta hai.
# - values mein eigenvalues store hoti hain: 3 aur 6.
# - vectors mein corresponding eigenvectors ke columns store hote hain.