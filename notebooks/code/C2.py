import datetime


def make_meshgrid(X, Y, empty=False):
    if empty:
        return [[0 for i in range(len(X))] for j in range(len(Y))]

    return [[complex(re, im) for re in X] for im in Y]


def make_julia_set_1(Z, q, c, it):
    r = len(Z)

    for i in range(r):
        for j in range(r):
            for k in range(it):
                Z[i][j] = (Z[i][j] * Z[i][j]) + c
                if abs(Z[i][j]) > 2:
                    q[i][j] = k
                    break

    return Z, q


def basic_profiler(f, args=[], kwargs={}):
    timer = datetime.datetime.now()

    output = f(*args, **kwargs)

    timer = datetime.datetime.now() - timer
    print("{0:}".format(timer))

    return output


def main(f):
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
    z = make_meshgrid(x, y, empty=False)
    q = make_meshgrid(x, y, empty=True)

    # Crunching number and profiling
    z, q = basic_profiler(f, args=[z, q, c, max_it])

if __name__ == '__main__':
    main(make_julia_set_1)
