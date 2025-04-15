
import plotly.express as px

def show_city_scores(df):
    fig = px.bar(df, x='city', y='sustainability_score', color='sustainability_score',
                 title='City Sustainability Scores', text_auto='.2f')
    return fig
