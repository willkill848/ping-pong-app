
import streamlit as st
import random

st.title("🏓 Ping Pong Virtual")

# Nombre de los jugadores
jugador1 = st.text_input("Nombre del Jugador 1", "Will")
jugador2 = st.text_input("Nombre del Jugador 2", "Máquina")

if st.button("Empezar partido"):
    st.write("🎯 Sorteando quién saca primero...")
    saque = random.choice([jugador1, jugador2])
    st.success(f"Empieza sacando: {saque}")

    # Simular 5 puntos de ejemplo
    puntos = {jugador1: 0, jugador2: 0}
    for punto in range(1, 6):
        ganador = random.choice([jugador1, jugador2])
        puntos[ganador] += 1
        st.write(f"Punto {punto}: ganó {ganador}")

    # Mostrar resultado final
    st.write("🏁 Resultado Final:")
    st.write(f"{jugador1}: {puntos[jugador1]} puntos")
    st.write(f"{jugador2}: {puntos[jugador2]} puntos")

    if puntos[jugador1] > puntos[jugador2]:
        st.balloons()
        st.success(f"¡Ganador: {jugador1}!")
    elif puntos[jugador1] < puntos[jugador2]:
        st.success(f"¡Ganador: {jugador2}!")
    else:
        st.warning("Empate técnico 🎲")
