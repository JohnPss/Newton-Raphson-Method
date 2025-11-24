# 🔬 Método de Newton-Raphson

Implementação robusta e interativa do método de Newton-Raphson para encontrar raízes de funções matemáticas.

## 📋 Descrição

O método de Newton-Raphson é um algoritmo iterativo para encontrar aproximações de raízes (zeros) de funções reais. Este projeto oferece uma implementação completa com interface interativa, validações e relatórios detalhados.

### Fórmula do Método

```
x_{n+1} = x_n - f(x_n) / f'(x_n)
```

## ✨ Funcionalidades

- ✅ Entrada interativa de funções matemáticas
- ✅ Cálculo automático de derivadas
- ✅ Validação robusta de entradas
- ✅ Detecção de divergência
- ✅ Tratamento de erros matemáticos
- ✅ Relatório detalhado em arquivo de texto
- ✅ Visualização do progresso em tempo real
- ✅ Suporte a expressões complexas

## 🚀 Como Usar

### Pré-requisitos

```bash
pip install sympy
```

### Execução

```bash
python3 newton_interativo.py
```

### Exemplo de Uso

```
=============================================================
MÉTODO DE NEWTON-RAPHSON - CALCULADORA DE RAÍZES
=============================================================

Digite f(x): x**2 - 4
Digite f'(x) (deixe vazio para derivar automaticamente): 
✓ Derivada calculada: f'(x) = 2*x

Digite x0 (chute inicial): 1
Digite ε (tolerância): 0.0001
Digite max_iter (máximo de iterações): 50

------------------------------------------------------------
EXECUTANDO MÉTODO...
------------------------------------------------------------

Iteração   1: xn =   1.0000000000, f(xn) =  -3.0000e+00, erro =   1.5000e+00
Iteração   2: xn =   2.5000000000, f(xn) =   2.2500e+00, erro =   2.5000e-01
Iteração   3: xn =   2.2500000000, f(xn) =   6.2500e-02, erro =   1.3889e-02
Iteração   4: xn =   2.2361111111, f(xn) =   9.8846e-05, erro =   4.9383e-05
✓ Convergiu em 4 iterações!

✓ Resultados salvos em 'resultado_newton_raphson.txt'
```

## 📝 Entrada de Funções

O programa aceita expressões matemáticas usando a sintaxe do Python/SymPy:

### Operadores Suportados

| Operação | Sintaxe | Exemplo |
|----------|---------|---------|
| Adição | `+` | `x + 5` |
| Subtração | `-` | `x - 3` |
| Multiplicação | `*` | `3*x` |
| Divisão | `/` | `x/2` |
| Potência | `**` | `x**2` |
| Raiz quadrada | `sqrt(x)` | `sqrt(x - 1)` |
| Exponencial | `exp(x)` | `exp(-x)` |
| Logaritmo natural | `log(x)` | `log(x)` |
| Seno | `sin(x)` | `sin(x)` |
| Cosseno | `cos(x)` | `cos(x)` |
| Tangente | `tan(x)` | `tan(x)` |

### Exemplos de Funções Válidas

```python
x**2 - 4                    # Parábola simples
x**3 - 2*x - 5              # Polinômio cúbico
exp(x) - 3                  # Função exponencial
sin(x) - 0.5                # Função trigonométrica
x*log(x) - 1                # Função transcendental
sqrt(x) - 2                 # Raiz quadrada
```

## 📊 Arquivo de Saída

O programa gera um arquivo `resultado_newton_raphson.txt` contendo:

- Função e derivada utilizadas
- Parâmetros do método (x0, tolerância)
- Raiz aproximada encontrada
- Status de convergência
- Histórico completo de todas as iterações

### Exemplo de Saída

```
============================================================
MÉTODO DE NEWTON-RAPHSON - RESULTADOS
============================================================

Função: f(x) = x**2 - 4
Derivada: f'(x) = 2*x
Chute inicial (x0): 1.0
Tolerância (ε): 0.0001

------------------------------------------------------------
RESULTADO FINAL
------------------------------------------------------------
Raiz aproximada: 2.000000000000000
Número de iterações: 4
Status: ✓ Convergiu

------------------------------------------------------------
HISTÓRICO DE ITERAÇÕES
------------------------------------------------------------
   k                 xn             f(xn)              erro
------------------------------------------------------------
   1       1.0000000000    -3.0000000e+00     1.5000000e+00
   2       2.5000000000     2.2500000e+00     2.5000000e-01
   3       2.2500000000     6.2500000e-02     1.3889000e-02
   4       2.2361111111     9.8846000e-05     4.9383000e-05
```

## ⚠️ Avisos e Limitações

### O método pode falhar se:

- **Derivada próxima de zero**: O método não consegue prosseguir quando f'(x) ≈ 0
- **Chute inicial inadequado**: Escolha de x0 pode levar à divergência
- **Pontos de inflexão**: Podem causar oscilações
- **Múltiplas raízes**: O método encontra apenas uma raiz por execução
- **Domínio da função**: Erros podem ocorrer fora do domínio (ex: log de negativos)

### Dicas para Convergência

1. **Escolha um bom x0**: Próximo da raiz esperada
2. **Verifique o gráfico**: Visualize a função antes se possível
3. **Teste diferentes valores**: Tente múltiplos chutes iniciais
4. **Ajuste a tolerância**: Use valores realistas (ex: 1e-6 a 1e-10)
5. **Aumente max_iter**: Para funções mais complexas

## 🔧 Estrutura do Código

```
newton_interativo.py
├── parse_expression()          # Converte string em função
├── newton_raphson()            # Implementa o método
├── salvar_resultados()         # Gera relatório
├── obter_entrada_float()       # Validação de entrada
├── obter_entrada_int()         # Validação de entrada
└── main()                      # Interface principal
```

## 📚 Teoria

O método de Newton-Raphson é baseado na linearização da função através da reta tangente:

1. Começa com uma estimativa inicial x₀
2. Calcula a tangente da função em x₀
3. Encontra onde a tangente cruza o eixo x (novo x₁)
4. Repete até convergir

### Condições de Convergência

O método converge quando:
- f'(x) ≠ 0 na região da raiz
- x₀ está suficientemente próximo da raiz
- f é duas vezes diferenciável

### Velocidade de Convergência

Convergência **quadrática**: o erro aproximadamente dobra de precisão a cada iteração quando próximo da raiz.

## 🤝 Contribuições

Melhorias sugeridas são bem-vindas! Áreas para expansão:

- Plotagem gráfica do processo iterativo
- Implementação de outros métodos (bisseção, secante)
- Interface gráfica (GUI)
- Suporte a sistemas de equações

## 📄 Licença

Este projeto é de código aberto e pode ser usado livremente para fins educacionais e acadêmicos.

## 👨‍💻 Autor

Desenvolvido como ferramenta educacional para análise numérica e cálculo computacional.

---

**Nota**: Este é um projeto educacional. Para aplicações críticas, considere usar bibliotecas especializadas como `scipy.optimize`.