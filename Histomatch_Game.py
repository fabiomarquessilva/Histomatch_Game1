
import streamlit as st

# Configuração inicial do aplicativo
st.set_page_config(page_title="Histomatch: Explore o Microcosmo", layout="centered")

# Cabeçalho do jogo
st.title("Histomatch: Explore o Microcosmo")
st.subheader("Teste seus conhecimentos em Histologia e divirta-se aprendendo!")

# Início do jogo
st.write("Responda às perguntas abaixo e descubra o quanto você sabe sobre tecidos e células.")

# Lista de perguntas
questions = [
    {
        "question": "Qual tipo de tecido possui células cilíndricas com microvilosidades e é encontrado no intestino?",
        "options": ["Tecido Epitelial de Revestimento", "Tecido Conjuntivo", "Tecido Muscular", "Tecido Nervoso"],
        "answer": "Tecido Epitelial de Revestimento",
    },
    {
        "question": "Qual corante é utilizado para evidenciar fibras colágenas em cortes histológicos?",
        "options": ["Hematoxilina", "Eosina", "Tricrômico de Masson", "Azul de Toluidina"],
        "answer": "Tricrômico de Masson",
    },
    {
        "question": "Qual tecido armazena lipídeos e fornece isolamento térmico?",
        "options": ["Tecido Muscular", "Tecido Adiposo", "Tecido Nervoso", "Tecido Conjuntivo Denso"],
        "answer": "Tecido Adiposo",
    },
]

# Variável para pontuação
score = 0

# Loop para exibir as perguntas
for i, q in enumerate(questions):
    st.write(f"### Pergunta {i+1}: {q['question']}")
    user_answer = st.radio("", q["options"], key=i)
    
    # Avaliação
    if st.button(f"Verificar resposta {i+1}", key=f"check_{i}"):
        if user_answer == q["answer"]:
            st.success("Resposta correta!")
            score += 1
        else:
            st.error(f"Resposta incorreta! A resposta correta é: {q['answer']}.")

# Exibir a pontuação final
if st.button("Finalizar jogo"):
    st.write(f"### Sua pontuação final: {score}/{len(questions)}")
    if score == len(questions):
        st.balloons()
        st.success("Parabéns! Você acertou todas as perguntas!")
    elif score > len(questions) // 2:
        st.info("Bom trabalho! Continue estudando para aprimorar ainda mais.")
    else:
        st.warning("Não se preocupe, pratique mais para melhorar seu desempenho.")
