# Lista de médicos que já possuem credenciamento

medicos = [
    {"nome": "Carlos", "crm": "12345"},
    {"nome": "Mariana", "crm": "67890"},
    {"nome": "Pedro", "crm": "54321"}
]
# Solicita o nome e o CRM do médico

nome = input("Digite seu nome: ")
crm = input("Digite seu CRM: ")

# Inicialmente, considera o médico não autorizado
autorizado = False

# Percorre a lista de médicos cadastrados
for medico in medicos:

    if medico["nome"] == nome and medico["crm"] == crm:
        autorizado = True

# Verifica se o médico foi autorizado
if autorizado:

    # Permite a emissão da receita
    print("Médico credenciado! Receita autorizada.")

else:

    # Bloqueia a emissão caso não seja credenciado
    print("Médico não credenciado! Emissão bloqueada.")
