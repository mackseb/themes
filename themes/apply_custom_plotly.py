import plotly.graph_objects as go
import plotly.io as pio


# Usage
"""
import httpimport
with httpimport.github_repo('mackseb', 'themes', branch = 'master'):
    from themes.apply_custom_plotly import set_template

set_template()
"""

def set_template():

    my_layout = {
        'annotationdefaults': {'arrowcolor': '#2a3f5f', 'arrowhead': 0, 'arrowwidth': 1},
        'autotypenumbers': 'strict',
        'coloraxis': {'colorbar': {'outlinewidth': 0, 'ticks': ''}},
        'colorscale': {'diverging': [[0, '#8e0152'], [0.1, '#c51b7d'], [0.2,
                                                                        '#de77ae'], [0.3, '#f1b6da'], [0.4, '#fde0ef'],
                                     [0.5, '#f7f7f7'], [0.6, '#e6f5d0'], [0.7,
                                                                          '#b8e186'], [0.8, '#7fbc41'], [0.9, '#4d9221'],
                                     [1, '#276419']],
                       'sequential': [[0.0, '#0d0887'], [0.1111111111111111,
                                                         '#46039f'], [0.2222222222222222, '#7201a8'],
                                      [0.3333333333333333, '#9c179e'],
                                      [0.4444444444444444, '#bd3786'],
                                      [0.5555555555555556, '#d8576b'],
                                      [0.6666666666666666, '#ed7953'],
                                      [0.7777777777777778, '#fb9f3a'],
                                      [0.8888888888888888, '#fdca26'], [1.0,
                                                                        '#f0f921']],
                       'sequentialminus': [[0.0, '#0d0887'], [0.1111111111111111,
                                                              '#46039f'], [0.2222222222222222, '#7201a8'],
                                           [0.3333333333333333, '#9c179e'],
                                           [0.4444444444444444, '#bd3786'],
                                           [0.5555555555555556, '#d8576b'],
                                           [0.6666666666666666, '#ed7953'],
                                           [0.7777777777777778, '#fb9f3a'],
                                           [0.8888888888888888, '#fdca26'], [1.0,
                                                                             '#f0f921']]},
        'colorway': ['#ff2d55', '#5856d6', '#ff9500', '#ffcc00', '#ff3b30', '#5ac8fa', '#007aff', '#4cd964'],
        'font': {'color': '#6e6e6e',
                 'family': 'helvetica neue', 'size': 11},
        'geo': {'bgcolor': 'white',
                'lakecolor': 'white',
                'landcolor': 'white',
                'showlakes': True,
                'showland': True,
                'subunitcolor': '#C8D4E3'},
        'hoverlabel': {'align': 'left'},
        'hovermode': 'closest',
        'mapbox': {'style': 'light'},
        'paper_bgcolor': 'yellow',
        'plot_bgcolor': 'white',
        'polar': {'angularaxis': {'gridcolor': '#EBF0F8', 'linecolor': '#EBF0F8', 'ticks': ''},
                  'bgcolor': 'white',
                  'radialaxis': {'gridcolor': '#EBF0F8', 'linecolor': '#EBF0F8', 'ticks': ''}},
        'scene': {'xaxis': {'backgroundcolor': 'white',
                            'gridcolor': '#DFE8F3',
                            'gridwidth': 2,
                            'linecolor': '#EBF0F8',
                            'showbackground': True,
                            'ticks': '',
                            'zerolinecolor': '#EBF0F8'},
                  'yaxis': {'backgroundcolor': 'white',
                            'gridcolor': '#DFE8F3',
                            'gridwidth': 2,
                            'linecolor': '#EBF0F8',
                            'showbackground': True,
                            'ticks': '',
                            'zerolinecolor': '#EBF0F8'},
                  'zaxis': {'backgroundcolor': 'white',
                            'gridcolor': '#DFE8F3',
                            'gridwidth': 2,
                            'linecolor': '#EBF0F8',
                            'showbackground': True,
                            'ticks': '',
                            'zerolinecolor': '#EBF0F8'}},
        'shapedefaults': {'line': {'color': '#2a3f5f'}},
        'ternary': {'aaxis': {'gridcolor': '#DFE8F3', 'linecolor': '#A2B1C6', 'ticks': ''},
                    'baxis': {'gridcolor': '#DFE8F3', 'linecolor': '#A2B1C6', 'ticks': ''},
                    'bgcolor': 'white',
                    'caxis': {'gridcolor': '#DFE8F3', 'linecolor': '#A2B1C6', 'ticks': ''}},
        'title': {'x': 0.05},
        'xaxis': {'automargin': True,
                  'gridcolor': '#ECECED',
                  'linecolor': '#ECECED',
                  'ticks': '',
                  'title': {'standoff': 15},
                  'zerolinecolor': 'black',
                  'zerolinewidth': 0.5},
        'yaxis': {'automargin': True,
                  'gridcolor': '#ECECED',
                  'linecolor': '#ECECED',
                  'ticks': '',
                  'title': {'standoff': 15},
                  'zerolinecolor': 'black',
                  'zerolinewidth': 0.5}
    }

    pio.templates["my_template"] = go.layout.Template(dict(layout=my_layout))
    pio.templates.default = "my_template"