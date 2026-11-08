def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	return [[covariance(a,b) for b in vectors] for a in vectors]

def covariance(a, b):
	x = sum(a) / len(a)
	y = sum(b) / len(b)
	cov = 0
	for idx, _ in enumerate(a):
		cov += (a[idx] - x) * (b[idx] - y)
	return cov / (len(a) - 1)