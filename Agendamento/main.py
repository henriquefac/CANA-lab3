def greedy_project_selection_with_print(projects):
    projects.sort(key=lambda x: x[2] / (x[1] - x[0]), reverse=True)

    selected_projects = []
    current_end = float('-inf')

    for project in projects:
        start, end, profit = project
        if start >= current_end:
            selected_projects.append(project)
            current_end = end
            print(f"Projeto selecionado - Data de Início: {start}, Data de Conclusão: {end}, Lucro: {profit}")

    return selected_projects


projects = [(1, 3, 5), (2, 5, 8), (4, 6, 3), (6, 8, 2)]
result = greedy_project_selection_with_print(projects)
