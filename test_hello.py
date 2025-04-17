# test_hello.py
from hello import hello, soma  # Importa as funções que você quer testar

def test_hello():
    assert hello() == "Hello, World!"  # Testa se a função hello retorna a mensagem correta

def test_soma():
    assert soma(1, 1) == 2  # Testa se a soma de 1 + 1 é igual a 2
    assert soma(-1, 1) == 0  # Testa se a soma de -1 + 1 é igual a 0
    assert soma(0, 0) == 0  # Testa se a soma de 0 + 0 é igual a 0
