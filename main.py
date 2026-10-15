"""Main module for running the election data processing and views."""

from packages.elections.src.elections import processed_data, use_cases, views


def main():
    """Main function to run the election data processing and views."""

    data = processed_data.run()
    views.run(data)

    print("""Para exportar os resultados como CSV, selecione uma opção:
    1. Amostragem dos dados
    2. Votos por Partido
    3. Prefeitos Eleitos
    4. Vereadores Eleitos
    5. Sair
    """)
    option = input("Selecione uma opção: ").strip()

    if option == "5":
        print("Saindo...")
        return

    exports = {
        "1": (
            lambda: use_cases.sample_data(data),
            "ex_amostragem_dos_dados.csv",
            "Amostragem dos dados exportada",
        ),
        "2": (
            lambda: use_cases.calculate_votes_per_party(data),
            "ex_votos_por_partido.csv",
            "Votos por partido exportados",
        ),
        "3": (
            lambda: use_cases.calculate_winners(data, position="Prefeito"),
            "ex_prefeitos_eleitos.csv",
            "Prefeitos eleitos exportados",
        ),
        "4": (
            lambda: use_cases.calculate_winners(data, position="Vereador"),
            "ex_vereadores_eleitos.csv",
            "Vereadores eleitos exportados",
        ),
    }

    if option not in exports:
        print("Opção inválida.")
        return

    build_data, file_name, success_text = exports[option]
    if not processed_data.save_to_csv(build_data(), file_name):
        print("Operação cancelada.")
        return

    print(f"{success_text} com sucesso em `data/{file_name}`")


if __name__ == "__main__":
    main()
