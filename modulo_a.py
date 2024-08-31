# modulo_a.py

from modulo_b import func_b


def func_a():
    print("Função A")


def call_b():
    func_b()


if __name__ == "__main__":
    func_a()
    call_b()
