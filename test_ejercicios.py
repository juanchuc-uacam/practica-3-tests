import pytest
import importlib

def try_import(module_name, func_name):
    """
    Intenta importar un módulo y obtener la función especificada.
    Si falla, el test se marcará como SKIPPED en lugar de romper toda la ejecución.
    """
    try:
        module = importlib.import_module(module_name)
        return getattr(module, func_name)
    except (ModuleNotFoundError, AttributeError):
        pytest.skip(f"Módulo o función no encontrada: {module_name}.{func_name}")


# -------------------------
# Ejercicios originales (1-5)
# -------------------------

def test_arreglo_basico():
    func = try_import("arreglo_basico", "arreglo_basico")
    assert func() == 30  # Debe devolver el tercer elemento


def test_modificar_arreglo():
    func = try_import("modificar_arreglo", "modificar_arreglo")
    assert func() == [5, 100, 25, 35]  # Segundo elemento modificado a 100


def test_matriz_basica():
    func = try_import("matriz_basica", "matriz_basica")
    assert func() == 6  # Elemento fila 1, columna 2


def test_suma_matriz():
    func = try_import("suma_matriz", "suma_matriz")
    assert func() == 10 + 60  # Primer elemento + último elemento


def test_matriz_cadenas():
    func = try_import("matriz_cadenas", "matriz_cadenas")
    assert func() == "María"  # Elemento fila 1, columna 0


# -------------------------
# Ejercicios de retroalimentación (6-10)
# -------------------------

def test_promedio_arreglo():
    func = try_import("promedio_arreglo", "promedio_arreglo")
    assert func() == (8 + 12 + 20) / 3


def test_producto_matriz():
    func = try_import("producto_matriz", "producto_matriz")
    assert func() == 3 * 4  # matriz[0][1] * matriz[1][0]


def test_concatenar_cadenas_arreglo():
    func = try_import("concatenar_cadenas_arreglo", "concatenar_cadenas_arreglo")
    assert func() == "Hola Mundo"


def test_suma_columna_matriz():
    func = try_import("suma_columna_matriz", "suma_columna_matriz")
    assert func() == 2 + 5  # segunda columna de la matriz


@pytest.mark.parametrize("nums, esperado", [
    ([1, 2, 3], [1, 2, 3]),
    ([10, 20, 30], [10, 20, 30]),
    ([5, 5, 5], [5, 5, 5]),
])
def test_arreglo_usuario(monkeypatch, nums, esperado):
    func = try_import("arreglo_usuario", "arreglo_usuario")
    # Simula entradas del usuario
    inputs = "\n".join(str(n) for n in nums)
    monkeypatch.setattr("builtins.input", lambda _: next(iter(inputs.split("\n"))))
    # Necesitamos iterador para consumir entradas
    iterator = iter(inputs.split("\n"))
    monkeypatch.setattr("builtins.input", lambda _: next(iterator))
    assert func() == esperado
