# salvar como simcred_dashboard.py

import streamlit as st

# Autenticação simples
senha = st.text_input("Digite a senha para acessar:", type="password")
if senha != "519901":
    st.warning("Acesso restrito.")
    st.stop()

# Logo
st.image("https://i.ibb.co/9kjcX1Kh/sim-cred-5.png", width=200)

st.title("📊 Simulador de Mensalidade")
st.markdown("Preencha os dados abaixo para simular os valores com base na produção e MDR.")

# Inputs
qtd_lojas = st.number_input("Quantidade de lojas", min_value=1, step=1)
producao_por_loja = st.number_input("Produção por loja (R$)", min_value=0.0, format="%.2f")
mdr_promo = st.text_input("MDR Promo (%)", value="9,10")

# Processamento ao clicar no botão
if st.button("Calcular"):
    try:
        mdr_promo_float = float(mdr_promo.replace(",", ".").replace("%", "")) / 100
        if not (0.0849 <= mdr_promo_float <= 0.0949):
            st.error("⚠️ O MDR Promo deve estar entre 8,49% e 9,49%.")
        else:
            producao_total = qtd_lojas * producao_por_loja

            # Cálculo da mensalidade
            if qtd_lojas == 1:
                mensalidade = 359
            elif qtd_lojas == 2:
                mensalidade = 259 * 2
            elif qtd_lojas == 3:
                mensalidade = 199 * 3
            elif qtd_lojas <= 5:
                mensalidade = 189 * qtd_lojas
            else:
                mensalidade = 0

            mdr_atual = 0.0949
            valor_mdr_atual = producao_total * mdr_atual
            valor_mdr_promo = producao_total * mdr_promo_float

            nova_mensalidade = mensalidade - (valor_mdr_atual - valor_mdr_promo)
            desconto = mensalidade - nova_mensalidade

            # Resultados
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Produção Total", f"R$ {producao_total:,.2f}")
                st.metric("Valor Mensalidade", f"R$ {mensalidade:,.2f}")
                st.metric("Nova Mensalidade", f"R$ {nova_mensalidade:,.2f}", delta=f"- R$ {desconto:,.2f}")

            with col2:
                st.metric("MDR Atual", "9,49%")
                st.metric("MDR Promo", f"{mdr_promo.replace('.', ',')}%")
                st.metric("Desconto Aplicado", f"R$ {desconto:,.2f}")
    except:
        st.error("❌ Preencha corretamente os campos.")
