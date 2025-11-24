#!/usr/bin/env python3
"""
Implementação robusta do método de Newton-Raphson para encontrar raízes de funções.
Inclui validações, tratamento de erros e interface interativa.
"""
import math
import sympy as sp
from typing import Tuple, List, Callable, Optional


def parse_expression(expr_str: str) -> Tuple[sp.Expr, Callable]:
    """
    Converte uma string em expressão simbólica e função numérica.
    
    Args:
        expr_str: String contendo a expressão matemática
        
    Returns:
        Tupla com (expressão simbólica, função numérica)
        
    Raises:
        ValueError: Se a expressão for inválida
    """
    try:
        x = sp.symbols('x')
        sym_expr = sp.sympify(expr_str, evaluate=True)
        numeric = sp.lambdify(x, sym_expr, modules=["math"])
        return sym_expr, numeric
    except (sp.SympifyError, SyntaxError) as e:
        raise ValueError(f"Expressão inválida: {expr_str}") from e


def newton_raphson(f: Callable, fp: Callable, x0: float, eps: float, 
                   max_iter: int) -> Tuple[float, int, bool, List[Tuple]]:
    """
    Implementa o método de Newton-Raphson para encontrar raízes.
    
    Args:
        f: Função f(x)
        fp: Derivada f'(x)
        x0: Chute inicial
        eps: Tolerância do erro
        max_iter: Número máximo de iterações
        
    Returns:
        Tupla com (raiz aproximada, número de iterações, convergiu?, histórico)
    """
    xn = x0
    iters = []
    err_anterior = float('inf')

    for k in range(1, max_iter + 1):
        try:
            fxn = f(xn)
            fpxn = fp(xn)
        except (ValueError, ZeroDivisionError, OverflowError) as e:
            print(f"Erro ao calcular f(xn) ou f'(xn) na iteração {k}: {e}")
            iters.append((k, xn, float('nan'), float('nan')))
            return xn, k, False, iters

        # Verifica se a derivada é muito pequena
        if abs(fpxn) < 1e-15:
            print(f"Derivada muito próxima de zero na iteração {k}.")
            iters.append((k, xn, fxn, float('nan')))
            return xn, k, False, iters

        # Fórmula de Newton-Raphson
        xn1 = xn - fxn / fpxn
        err = abs(xn1 - xn)

        # Armazena dados da iteração
        iters.append((k, xn, fxn, err))

        # Exibe progresso
        print(f"Iteração {k:3d}: xn = {xn:15.10f}, f(xn) = {fxn:15.10e}, erro = {err:15.10e}")

        # Verifica convergência
        if err < eps:
            print(f"✓ Convergiu em {k} iterações!")
            return xn1, k, True, iters

        # Detecta possível divergência
        if err > err_anterior * 10 and k > 3:
            print(f"Possível divergência detectada (erro crescente).")
            return xn1, k, False, iters

        err_anterior = err
        xn = xn1

    print(f"Não convergiu em {max_iter} iterações.")
    return xn, max_iter, False, iters


def salvar_resultados(filename: str, f_str: str, fp_str: str, x0: float, 
                      eps: float, root: float, niter: int, conv: bool, 
                      iters: List[Tuple]):
    """Salva os resultados em arquivo texto formatado."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("MÉTODO DE NEWTON-RAPHSON - RESULTADOS\n")
        f.write("=" * 60 + "\n\n")
        
        f.write(f"Função: f(x) = {f_str}\n")
        f.write(f"Derivada: f'(x) = {fp_str}\n")
        f.write(f"Chute inicial (x0): {x0}\n")
        f.write(f"Tolerância (ε): {eps}\n\n")
        
        f.write("-" * 60 + "\n")
        f.write("RESULTADO FINAL\n")
        f.write("-" * 60 + "\n")
        f.write(f"Raiz aproximada: {root:.15f}\n")
        f.write(f"Número de iterações: {niter}\n")
        f.write(f"Status: {'✓ Convergiu' if conv else '✗ Não convergiu'}\n\n")
        
        f.write("-" * 60 + "\n")
        f.write("HISTÓRICO DE ITERAÇÕES\n")
        f.write("-" * 60 + "\n")
        f.write(f"{'k':>4} {'xn':>18} {'f(xn)':>18} {'erro':>18}\n")
        f.write("-" * 60 + "\n")
        
        for k, xn, fxn, err in iters:
            f.write(f"{k:4d} {xn:18.10f} {fxn:18.10e} {err:18.10e}\n")


def obter_entrada_float(prompt: str, validacao: Optional[Callable] = None) -> float:
    """Obtém entrada numérica do usuário com validação."""
    while True:
        try:
            valor = float(input(prompt).strip().replace(',', '.'))
            if validacao and not validacao(valor):
                print("Valor inválido. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def obter_entrada_int(prompt: str, validacao: Optional[Callable] = None) -> int:
    """Obtém entrada inteira do usuário com validação."""
    while True:
        try:
            valor = int(input(prompt).strip())
            if validacao and not validacao(valor):
                print("Valor inválido. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def main():
    """Função principal com interface interativa."""
    print("\n" + "=" * 60)
    print("MÉTODO DE NEWTON-RAPHSON - CALCULADORA DE RAÍZES")
    print("=" * 60 + "\n")

    # Entrada da função
    while True:
        f_str = input("Digite f(x): ").strip()
        try:
            sym_f, f_num = parse_expression(f_str)
            break
        except ValueError as e:
            print(f"{e}. Tente novamente.")

    # Entrada da derivada (opcional)
    fp_str = input("Digite f'(x) (deixe vazio para derivar automaticamente): ").strip()
    
    if not fp_str:
        x = sp.symbols('x')
        sym_fp = sp.diff(sym_f, x)
        fp_num = sp.lambdify(x, sym_fp, modules=["math"])
        fp_str = str(sym_fp)
        print(f"✓ Derivada calculada: f'(x) = {sym_fp}")
    else:
        try:
            _, fp_num = parse_expression(fp_str)
        except ValueError as e:
            print(f"{e}. Encerrando.")
            return

    # Entrada dos parâmetros
    print()
    x0 = obter_entrada_float("Digite x0 (chute inicial): ")
    eps = obter_entrada_float("Digite ε (tolerância): ", lambda x: x > 0)
    max_iter = obter_entrada_int("Digite max_iter (máximo de iterações): ", lambda x: x > 0)

    print("\n" + "-" * 60)
    print("EXECUTANDO MÉTODO...")
    print("-" * 60 + "\n")

    # Executa o método
    root, niter, conv, iters = newton_raphson(f_num, fp_num, x0, eps, max_iter)

    # Salva resultados
    filename = "resultado_newton_raphson.txt"
    salvar_resultados(filename, f_str, fp_str, x0, eps, root, niter, conv, iters)

    print(f"\n✓ Resultados salvos em '{filename}'")
    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExecução interrompida pelo usuário.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")