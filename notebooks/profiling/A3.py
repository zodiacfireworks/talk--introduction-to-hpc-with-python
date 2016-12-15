import datetime


def make_meshgrid(X, Y, empty=False):
    if empty:
        return [[0 for i in range(len(X))] for j in range(len(Y))]

    return [[complex(re, im) for re in X] for im in Y]


def make_julia_set_2(Z, q, c, it, verbose=False):
    r = len(Z)

    for i in range(r):
        for j in range(r):
            if verbose:
                p = i + j + i * (r - 1)

                if p % r == 0:
                    p = 100.0 * float(p) / float(r * r)
                    print("\rCompletado: {0:>7.3f}%".format(p), end="")
            z = Z[i][j]
            for k in range(it):
                z = (z * z) + c
                if abs(z) > 2:
                    q[i][j] = k
                    break

    if verbose:
        print("\rCompletado: 100.000%")

    return Z, q


def basic_profiler(f, args=[], kwargs={}):
    timer = datetime.datetime.now()

    output = f(*args, **kwargs)

    timer = datetime.datetime.now() - timer
    print("Tiempo total: {0:}".format(timer))

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

    print("Generando conjunto de Julia")
    print("Puntos: {}".format(len(x) * len(y)))

    # Crunching number and profiling
    z, q = basic_profiler(f, args=[z, q, c, max_it], kwargs={'verbose': True})


if __name__ == '__main__':
    main(make_julia_set_2)
