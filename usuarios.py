# usuarios.py


def validar_email(email):
    # Deve ser string e não pode ser None
    if not isinstance(email, str):
        return False

    # Não pode conter espaços comuns
    if " " in email:
        return False

    # Deve conter exatamente um @
    if email.count("@") != 1:
        return False

    usuario, dominio = email.split("@")

    # Parte anterior ao @ não pode ser vazia
    if not usuario:
        return False

    # Não pode terminar com ponto
    if dominio.endswith("."):
        return False

    # O domínio deve ter exatamente duas partes não vazias
    partes_dominio = dominio.split(".")
    if len(partes_dominio) != 2:
        return False

    if not partes_dominio[0] or not partes_dominio[1]:
        return False

    return True