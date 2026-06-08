from statistics import mean


def summarize_scores(scores: list[int]) -> dict[str, float]:
    return {
        "count": len(scores),
        "average": mean(scores),
        "highest": max(scores),
        "lowest": min(scores),
    }


if __name__ == "__main__":
    sample_scores = [88, 92, 79, 95, 90]
    summary = summarize_scores(sample_scores)
    print("Score summary:")
    for key, value in summary.items():
        print(f"- {key}: {value}")
