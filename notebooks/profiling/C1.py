import datetime

# Limites de la region a estudiar
xL, xU, yL, yU = -2, +2, -2, +2

# resolucion de la imagen
r = 2000

# numero maximo de iteraciones
max_it = 200

# Grillado de la region a estudiar
x = [xL + i * (float(xU) - float(xL)) / (float(r)) for i in range(r + 1)]
y = [yL + i * (float(yU) - float(yL)) / (float(r)) for i in range(r + 1)]

# Constantes a emplearse como c en
# z_n+1 = z_n*z_n + c
c = complex(-0.8350000, -0.23210000)

# Preparecion del mallado en el plano complejo
z = [[complex(re, im) for re in x] for im in y]
q = [[0 for i in range(r + 1)] for j in range(r + 1)]

# "Crunching number"
timer = datetime.datetime.now()

for i in range(len(x)):
    for j in range(len(y)):
        for k in range(max_it):
            z[i][j] = (z[i][j] * z[i][j]) + c
            if abs(z[i][j]) > 2:
                q[i][j] = k
                break

timer = datetime.datetime.now() - timer
print("{0:}".format(timer))
