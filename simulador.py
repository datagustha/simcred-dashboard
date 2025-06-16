import streamlit as st

# --- Estilo CSS personalizado atualizado com animações extras ---
st.markdown("""
    <style>
        body {
            background-color: #F9FAFB;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .logo-container {
            text-align: center;
            margin-bottom: 10px;
            animation: fadeInDown 1s ease forwards;
        }
        .header-box {
            background-color: #F2EBF5;
            padding: 20px;
            border-radius: 16px;
            margin-bottom: 20px;
            animation: slideDown 1s ease forwards;
            box-shadow: 0 4px 12px rgba(126, 62, 154, 0.2);
        }
        .header-box h1 {
            color: #7E3E9A;
            text-align: center;
            font-size: 28px;
            font-weight: 700;
            letter-spacing: 1.2px;
        }
        .highlight-box {
            background-color: #7E3E9A;
            color: white;
            padding: 30px;
            border-radius: 16px;
            text-align: center;
            margin-top: 30px;
            animation: fadeInUp 1s ease forwards;
            box-shadow: 0 6px 20px rgba(126, 62, 154, 0.3);
            position: relative;
            overflow: hidden;
        }
        .highlight-box .label {
            color: #A1CC4C;
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .highlight-box .value {
            font-size: 48px;
            font-weight: 900;
            margin-bottom: 15px;
            animation: pulse 2s infinite;
        }
        .highlight-box .percent-reduction {
            font-size: 20px;
            color: #A1CC4C;
            font-weight: 700;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            animation: bounceArrow 2s infinite;
        }
        .desconto-box {
            background-color: #fff;
            color: #4CAF50;
            padding: 20px;
            border-radius: 16px;
            text-align: center;
            border: 2px dashed #A1CC4C;
            margin-top: 20px;
            animation: fadeIn 1.5s ease forwards;
            box-shadow: 0 4px 15px rgba(161, 204, 76, 0.3);
        }
        .desconto-box .label {
            font-weight: 600;
            font-size: 16px;
        }
        .desconto-box .value {
            font-size: 26px;
        }
        input, .stNumberInput > div > input {
            background-color: #F2EBF5 !important;
            border-radius: 8px;
            border: 1px solid #ddd;
            padding: 10px;
            font-size: 16px;
            transition: border-color 0.3s ease;
        }
        input:focus, .stNumberInput > div > input:focus {
            border-color: #7E3E9A !important;
            outline: none;
            box-shadow: 0 0 8px #7E3E9A;
        }
        button[kind="primary"] {
            background-color: #7E3E9A !important;
            color: white !important;
            border-radius: 8px !important;
            border: none;
            transition: all 0.3s ease-in-out;
            padding: 12px 24px;
            font-weight: 700;
            font-size: 18px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(126, 62, 154, 0.5);
        }
        button[kind="primary"]:hover {
            background-color: #5b2a75 !important;
            transform: scale(1.05);
            box-shadow: 0 6px 18px rgba(91, 42, 117, 0.7);
        }

        /* Animações */
        @keyframes slideDown {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
        @keyframes bounceArrow {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }
    </style>
""", unsafe_allow_html=True)

# --- Autenticação ---
senha = st.text_input("Digite a senha para acessar:", type="password")
if senha != "519901":
    st.warning("Acesso restrito.")
    st.stop()

# --- Logo ---
st.markdown('<div class="logo-container"><img src="https://i.ibb.co/9kjcX1Kh/sim-cred-5.png" width="200"></div>',
            unsafe_allow_html=True)

# --- Título com fundo roxo claro ---
st.markdown("""
    <div class="header-box">
        <h1>📊 Simulador de Mensalidade</h1>
        <p style='text-align:center;'>Preencha os dados abaixo para simular os valores com base na produção e MDR.</p>
    </div>
""", unsafe_allow_html=True)

# --- Inputs ---
qtd_lojas = st.number_input("Quantidade de lojas", min_value=1, max_value=10, step=1)
producao_por_loja = st.number_input("Produção por loja (R$)", min_value=0.0, format="%.2f")
mdr_promo = st.text_input("MDR Promo (%)", value="9,10")

# --- Cálculo ---
if st.button("Calcular"):
    try:
        mdr_promo_float = float(mdr_promo.replace(",", ".").replace("%", "")) / 100
        if not (0.0849 <= mdr_promo_float <= 0.0949):
            st.error("⚠️ O MDR Promo deve estar entre 8,49% e 9,49%.")
        else:
            if qtd_lojas > 5:
                st.error("❌ A quantidade de lojas não pode ser maior que 5. Por favor, insira um valor válido.")
            else:
                producao_total = qtd_lojas * producao_por_loja

                # Mensalidade padrão
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

                desconto_percentual = (desconto / mensalidade) * 100 if mensalidade > 0 else 0

                # Usar setas curvas Unicode com cor
                if desconto_percentual > 0:
                    seta = "⇣"
                    cor_seta = "#A1CC4C"  # verde
                else:
                    seta = "⇡"
                    cor_seta = "#FF5C5C"  # vermelho claro (se quiser)

                # --- Destaque: Nova Mensalidade com percentual e seta colorida ---
                st.markdown(f"""
                    <div class="highlight-box">
                        <div class="label">Nova Mensalidade 💸</div>
                        <div class="value">R$ {nova_mensalidade:,.2f}</div>
                        <div class="percent-reduction" style="color: {cor_seta}; font-weight: 700; display: flex; justify-content: center; align-items: center; gap: 10px; animation: bounceArrow 2s infinite;">
                            <span style="font-size: 24px;">{seta}</span> Redução de {desconto_percentual:.2f}% em relação ao valor original
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                # --- Destaque: Desconto em valor ---
                st.markdown(f"""
                    <div class="desconto-box">
                        <div class="label">Desconto Aplicado ✅</div>
                        <div class="value">R$ {desconto:,.2f}</div>
                    </div>
                """, unsafe_allow_html=True)

                # --- Informações Adicionais ---
                st.write("### Detalhes da Simulação")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Produção Total", f"R$ {producao_total:,.2f}")
                    st.metric("Valor Mensalidade", f"R$ {mensalidade:,.2f}")
                with col2:
                    st.metric("MDR Atual", "9,49%")
                    st.metric("MDR Promo", f"{mdr_promo.replace('.', ',')}%")

    except:
        st.error("❌ Preencha corretamente os campos.")
