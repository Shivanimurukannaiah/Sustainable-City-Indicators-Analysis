
def compute_scores(df):
    df['sustainability_score'] = (
        df['access_to_transport'] * 0.3 +
        (100 - df['air_quality_index']) / 100 * 0.2 +
        df['green_space_percentage'] / 100 * 0.2 +
        df['health_index'] * 0.2 +
        (1 - df['population_density'] / df['population_density'].max()) * 0.1
    )
    return df
