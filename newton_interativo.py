#!/usr/bin/env python3
import math
import sympy as sp

def parse_expression(expr_str):
    x = sp.symbols('x')
    sym_expr = sp.sympify(expr_str, evaluate=True)
    numeric = sp.lambdify(x, sym_expr, modules=["math"])
    return sym_expr, numeric

def newton_raphson(f, fp, x0, eps, max_iter):
    xn = x0
    iters = []
    for k in range(1, max_iter+1):
        fxn = f(xn)
        fpxn = fp(xn)
        if abs(fpxn) < 1e-15:
            iters.append((k, xn, fxn, float('nan')))
            print(f"Derivada muito próxima de zero na iteração {k}.")
            return xn, k, False, iters
        xn1 = xn - fxn/fpxn
        err = abs(xn1 - xn)
        iters.append((k, xn, fxn, err))
        print(f"Iter {k}: xn = {xn}, f(xn) = {fxn}, erro = {err}")
        if err < eps:
            return xn1, k, True, iters
        xn = xn1
    return xn, max_iter, False, iters

def main():
    print("=== Newton-Raphson Interativo ===")
    f_str = input("Digite f(x): ").strip()
    fp_str = input("Digite f'(x) (deixe vazio para derivar automaticamente): ").strip()
    x0 = float(input("Digite x0: "))
    eps = float(input("Digite epsilon: "))
    max_iter = int(input("Digite max_iter: "))

    sym_f, f_num = parse_expression(f_str)
    if fp_str.strip() == "":
        x = sp.symbols('x')
        sym_fp = sp.diff(sym_f, x)
        fp_num = sp.lambdify(x, sym_fp, modules=["math"])
        print(f"Derivada automática: {sym_fp}")
    else:
        _, fp_num = parse_expression(fp_str)

    root, niter, conv, its = newton_raphson(f_num, fp_num, x0, eps, max_iter)

    with open("resultado_interativo.txt", "w") as f:
        f.write(f"Raiz: {root}\nIterações: {niter}\nConvergiu: {conv}\n")
        for row in its:
            f.write(str(row) + "\n")

    print("Finalizado. Resultado salvo em resultado_interativo.txt.")

if __name__ == "__main__":
    main()
