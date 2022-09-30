import sympy as s

if __name__ == "__main__":
    while True:
        try:
            coefs_a = list(map(int, input("Введите вектор коэффициентов f: ").split()))
            coefs_b = list(map(int, input("Введите вектор коэффициентов модуля: ").split()))
        except:
            print("Произошла какая-то ошибка при считывании вектора. Повторите снова.")
        try:
            x = s.symbols('x')
            f = s.Poly(sum([x ** (len(coefs_a) - 1 - idx) if coefs_a[idx] == 1 else 0 for idx in range(len(coefs_a))]), modulus = 2)
            mod = s.Poly(sum([x ** (len(coefs_b) - 1 - idx) if coefs_b[idx] == 1 else 0 for idx in range(len(coefs_b))]), modulus = 2)
            inv = s.invert(f, mod)
            print(f"({f.as_expr()})^-1 mod ({mod.as_expr()}) = {inv.as_expr()}".replace("**", "^"))
            print("Вектор коэффициентов f^-1:", " ".join(map(str, inv.all_coeffs())))
        except s.NotInvertible:
            print("f не обратим по заданному модулю.")
        except:
            print("Произошла какая-то ошибка. Проверьте корректность введённых данных.")

        print()
