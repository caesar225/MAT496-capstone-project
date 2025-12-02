def generate_report(state):
    report = "# Bias Analysis Report\n\n"

    for cluster_id, analysis in state.analysis_results.items():
        report += f"## {cluster_id}\n"
        report += f"```\n{analysis}\n```\n\n"

    report += "## Cross-Source Comparison\n"
    report += state.comparison_results

    state.final_report = report
    return state

node_report = generate_report
