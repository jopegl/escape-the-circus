import math

def calcular_mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def rsa_interativo():
    print("--- Configuração do RSA Passo a Passo ---")
    
    # 1. Entrada de p e q
    p = int(input("Digite o valor de p (primo): "))
    q = int(input("Digite o valor de q (primo): "))
    n = p * q
    phi = (p - 1) * (q - 1)
    
    print(f"-> n (p*q) = {n}")
    print(f"-> Euler de n (phi) = {phi}")
    print("-" * 30)

    # 2. Entrada de e com validação
    while True:
        e = int(input(f"Digite o valor de e (tal que mdc(e, {phi}) = 1): "))
        if calcular_mdc(e, phi) == 1:
            print(f"Sucesso! mdc({e}, {phi}) = 1")
            break
        else:
            print(f"Erro: mdc({e}, {phi}) é {calcular_mdc(e, phi)}. Tente outro 'e'.")

    # 3. Cálculo da Chave Privada d
    # d.e ≡ 1 (mod phi)
    d = pow(e, -1, phi)
    print(f"-> Chave Pública: (n={n}, e={e})")
    print(f"-> Chave Privada calculada (d): {d}")
    print("-" * 30)

    # 4. Entrada da Mensagem
    msg_texto = input("Digite a mensagem para codificar (letras e espaços): ").upper()
    
    # Conversão para o alfabeto numérico (A=10...Z=35, Espaço=99)
    msg_numerica = ""
    for char in msg_texto:
        if char == " ":
            msg_numerica += "99"
        elif 'A' <= char <= 'Z':
            msg_numerica += str(ord(char) - ord('A') + 10)
    
    print(f"Mensagem convertida: {msg_numerica}")

    # 5. Blocagem (Garantindo que o bloco seja < n e não comece com 0)
    # Vamos usar blocos de 2 dígitos por padrão para manter o valor < n com segurança
    # mas você pode ajustar o tamanho conforme o tamanho de n.
    tamanho_bloco = 2
    blocos = [int(msg_numerica[i:i+tamanho_bloco]) for i in range(0, len(msg_numerica), tamanho_bloco)]
    print(f"Blocos para cifragem: {blocos}")

    # 6. Cifragem
    print("\n--- Cifrando ---")
    blocos_cifrados = []
    for m in blocos:
        c = pow(m, e, n)
        print(f"Bloco {m}^{e} mod {n} = {c}")
        blocos_cifrados.append(c)
    print(f"Mensagem Cifrada: {blocos_cifrados}")

    # 7. Decifragem
    print("\n--- Decifrando ---")
    blocos_decifrados = []
    for c in blocos_cifrados:
        m_dec = pow(c, d, n)
        print(f"Bloco {c}^{d} mod {n} = {m_dec}")
        blocos_decifrados.append(m_dec)

    # 8. Reconstrução do Texto
    texto_final = ""
    for num in blocos_decifrados:
        if num == 99:
            texto_final += " "
        else:
            texto_final += chr(num - 10 + ord('A'))
    
    print("-" * 30)
    print(f"Resultado Final: {texto_final}")

if __name__ == "__main__":
    rsa_interativo()