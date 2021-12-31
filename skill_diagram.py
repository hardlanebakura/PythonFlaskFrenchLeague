from teams import all_players
import plotly.express as px

def get_skill_diagram_for_player(player):

    theta = ["PAC", "SHO", "PHY", "PAS", "DEF", "DRI"]
    values = [player.pace, player.shooting, player.physic, player.passing, player.defending_sliding_tackle, player.dribbling]

    fig = px.line_polar(
                        r=values,
                        theta=theta,
                        line_close=True,
                        range_r = [0,100],
                        #title="PLAYER SKILL DIAGRAM",
    )

    fig.update_layout(
                          title_font_family="Times New Roman",
                          title_font_color="red",
                          legend_title_font_color="green",
                          font_size=24
                      )


    fig.write_image("static/images/charts/player_skill_diagram.png")

get_skill_diagram_for_player(all_players[104])