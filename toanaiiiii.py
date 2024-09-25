import numpy as np

# Tải nội dung từ URL
url = '/Users/vuthu/Documents/Zalo Received Files/x.csv'
data = np.genfromtxt(url, delimiter=',', names=True,invalid_raise=False)

# Trích xuất TV và Sales
x = data['TV']
y = data['sales']

# Tính toán
cov_xy = np.cov(x, y)[0][1]
var_x = np.var(x)
var_y = np.var(y)
correlation = np.corrcoef(x, y)[0][1]
theta_rad = np.arccos(correlation)  
theta_deg = np.degrees(theta_rad)  
# In kết quả
print(f"Hiệp phương sai giữa TV và Sales: {cov_xy}")
print(f"Phương sai của TV: {var_x}")
print(f"Phương sai của Sales: {var_y}")
print(f"Hệ số tương quan Pearson giữa TV và Sales: {correlation}")
print(f"Góc θ (radian): {theta_rad}")
print(f"Góc θ (độ): {theta_deg}")
